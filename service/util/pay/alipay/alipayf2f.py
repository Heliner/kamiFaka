from alipay import AliPay
from alipay.utils import AliPayConfig

# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

class AlipayF2F:

    def __init__(self):
        from service.util.pay.pay_config import get_config
        config = get_config('支付宝当面付')
        self.APPID = config['APPID']
        self.web_url = get_config('web_url')
        self.app_private_key_string = '-----BEGIN RSA PRIVATE KEY-----\n'+config['app_private_key']+'\n-----END RSA PRIVATE KEY-----'
        self.alipay_public_key_string = '-----BEGIN PUBLIC KEY-----\n'+config['alipay_public_key']+'\n-----END PUBLIC KEY-----'   
        self.alipay = AliPay(
            appid=self.APPID,
            app_notify_url=self.web_url + '/notify/alipay',  # 默认回调url
            app_private_key_string=self.app_private_key_string,
            alipay_public_key_string=self.alipay_public_key_string,
            sign_type="RSA2", # RSA 或者 RSA2
            debug=False,  # True后为开发环境，所有走dev接口，正式环境用False
            config=AliPayConfig(timeout=15)  # 可选, 请求超时时间
        )
    def create_order(self,name,out_order_id,total_price):
        # 注意加上开头结尾
        ali_order = self.alipay.api_alipay_trade_precreate(
            subject=name,
            out_trade_no=out_order_id,
            total_amount=total_price,
            notify_url=self.web_url + '/notify/alipay'
        )
        try:
            if ali_order['code'] == '10000' and ali_order['msg'] == 'Success':        
                return ali_order
        except Exception as e:
            print(e)
            pass
        return False

    def check(self,out_order_id):     #这里是上一步主动生成的订单，单独调用
        try:
            res = self.alipay.api_alipay_trade_query(out_trade_no=out_order_id)
            # print(res)
            if res.get("trade_status", "") == "TRADE_SUCCESS":
                return True
        except Exception as e:
            print(e)
            return False
        return False

    def verify(self,data):     #异步通知    这里data=request.from
        try:
            signature = data['sign']
            data.pop('sign')
            return self.alipay.verify(data,signature)   # 结果为一个布尔值
        except Exception as e:
            print(e)
            return False

    def cancle(self,out_order_id):
        try:
            self.alipay.api_alipay_trade_cancel(out_trade_no=out_order_id)
            return True
        except:
            return False
