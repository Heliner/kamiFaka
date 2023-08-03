from enum import auto
from os import name
from service.database.models import TempOrder
from service.api.db import db

# 调用支付接口
from service.util.pay.alipay.alipayf2f import AlipayF2F  # 支付宝接口
from service.util.pay.wechat.weixin import Wechat   # 微信官方
from service.util.pay.qq.qqpay import QQpay   # 微信官方

# 日志记录
from service.util.log import log
from service.util.order.handle import make_order, notify_success
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(8)


def make_tmp_order(out_order_id, name, payment, contact, contact_txt, num):
    try:
        with db.auto_commit_db():
            db.session.add(TempOrder(out_order_id, name, payment,
                           contact, contact_txt, num, status=False, endtime=None))
        return make_pay_url(out_order_id)
    except Exception as e:
        log(e)
        return False


def make_pay_url(out_order_id):
    order = TempOrder.query.filter_by(out_order_id=out_order_id).first()
    if order:
        res = order.to_json()
        # print(res)
        # if res['status'] == False:
        #     return False
        payment = res['payment']
        name = res['name']
        total_price = res['total_price']
        if total_price == 0:
            return False
        r = pay_url(payment, name, out_order_id, total_price)
        if r:
            return r
    return False


def pay_url(payment, name, out_order_id, total_price):
    name = name.replace('=', '_')  # 防止k，v冲突
    try:
        if payment == '支付宝当面付':
            r = AlipayF2F().create_order(name, out_order_id, total_price)
        elif payment in ['微信官方接口']:
            r = Wechat().create_order(name, out_order_id, total_price)
        elif payment in ['QQ钱包']:
            r = QQpay().create_order(name, out_order_id, total_price)
        else:
            return None
        return r
    except Exception as e:
        log(e)
        return False


def alipay_check(out_order_id):
    r = AlipayF2F().check(out_order_id)
    if r:
        executor.submit(notify_success, out_order_id)
        return True
    return False
