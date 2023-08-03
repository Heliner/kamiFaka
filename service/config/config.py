from service.database.models import *
from service.api.db import db

# 经验：先用true或false

def init_db(update=False):
    # 管理员信息
    db.session.add(AdminUser(
        'hfl3035@163.com', '$2b$12$BKSXKYuCgeXjr8IEbK02re0VhkFoAz7f3aHF3kYAMLzYaEiObqPYm'))
    # 邮箱配置
    # db.session.add(Smtp('demo@qq.com','卡密发卡网','smtp.qq.com','465','xxxxxxxxx',True))
    # 支付渠道
    db.session.add(Payment('支付宝当面付', '支付宝', "{'APPID':'2021004101685214',\
                           'alipay_public_key':'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiP+YAsj+G2hKfUMU+XWG7Tik6J1N7NvCAe9ECy/Mli/VW/BSWQ2+CJNUlfSErZEMa6544pZHJik0WSeWNzPFQ0isIrE08sS0uDAcv11JXg/ahYp92JP/ikQTEdLzsVD4Cf/C68w79bWb42zIXcZP2esrJRG/TN+18MC80fmY79iWlkS4XlcYPafX25guIGn4eJyReiqgJvOUehedMdSnjJPuH2NEfSYC2vVRNkxz4X3NkASdC8LvZwhiIcNnypqkwT6r83Xq7nUCWqYscQpkYzZTh551p+dwpajxj7xdndwijrh8RJOhN4xaWsyI2g04xGdP4tzTJXAtxo3fUDSZLwIDAQAB',\
                          'app_private_key':'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCT78anoNglBr9ub/zdJvdsKJrh5bz7IEMgjTs6tcMVT3UHPzeqjKGr6A7Zg9uWy4IXPv4xpZOqv3YNzD/oTdVBaqFUDg0JS43OJ1CNFY9FqCFM5LsIjaxNFtdM5FRlQSPvYpQoDpW3TR3Y7wZnCTDfXkYfR2Kzof0MFaB/JTKHNEIdlDrTYNMcpCtifhnm6Q3n/RWk6tlq3Wjck7M1FlKenTCh/FihTm5B3w03JXENhlHFWPoAorj/TCPASCVCr7MKJorDJu+NV/tL0k3PYUmf4C+hA/z7ZhFGcfec2JmLvETMY8/5pbUEIUjMwWEuO2Ty5pZ2RwApNFNUVAg7ko9/AgMBAAECggEAHBAQDxxj5CIzji+QOCN8K/hH6TI7dyfXlAU2hxyTtSctfAJx/NhQktuidYCd1y0jsGUysxhFus43BscIGHkrSw1/LQK9VlYOwFyU2y6LzxrltkBtemHlnXoHvX5SxCJnPrHkiPS7Udo/Hze4bzM/IiAwDR7tikXgSrqPh4721s64A8Pe0dFdZqmc4snJfp0mqoo7IktcV/Ed6lzJ9gO1snEdq4LWw3Zznu02mpVFIN717kcSU4/63Aaq5APGZEPNNMwOcD20wYyAaZs6pH2DkT8NFAy1u9gEy1uIMZkt2OLCnoB7RQxJ8rIVKiMoxWxDdJJTcnbVlKFCWiaTLCf1gQKBgQDn41KMDylq9ijh6NKtaji61nxvIxEX7cqUeV/ySxvpeIE7tU6jI6yfRfVSQeO85Azh8pmHPeiiW6Nlf/US+CN0nRpi0azQdnHdeluYBBGKWNaOHmuOjTAoMqlY2FX7q1bqUXtjqY8YoqyfkNt9JlZvf+x8dfpwgLKic0B+n5ThCwKBgQCjUbvdGt0lwtYl92QBPE4IcwIEJh+hyo1F0a83d16onD/d7lDAO8uBcoGAz3PKHDYVmsydX4IcUpPYD0K2iEdalWHAkLEKWRjQmI4D4ok9KVTI+6PC7cM9rqECqCW3iGoPAUTNuQjLL8mAyWZTNzwWDLizb8dJ50uDgazMG0R73QKBgQDd0lNQr+BK9Zc+I94FDaue7zaxibX8UfiL91+VA8x7lk7psxK6dJHY+q8mNOmJ9A1uxweem9ZCGa9AlRr3Pm+MSgzHoxPRhrx9xWKBFMNCuKDl6quw/danXW8qEiiOSuUl2TRTrgu44USIj6WnHllo59JtbN5ZaIN5aw6zEiz06QKBgGKw+nhjSm4OLgBlXb5NZc4/SWGedBD96J7fViWLcd0sBoAjChMQTyrbOhzPv+XLZHdrwuf6lhJtaD/xANxyv8Oib57BEOry6kbrWS5Jz6rw9fY58jzSFuCITW3glGIzAfwtRRmYDhNSvk6f5cC1qQ6eA2MTUfd72KsQSo5Qj/LVAoGASbRPM+F/hNHRrDw70zonaD8MQ40DTbV+VGb1cW2FAw4C8cOvoqCRayCc3pe5AyIk8Vuus6KOiiNlSaLha7VAE27AaMuwcnmStZ9OxsAiR8cuknvsjNrB69uXW8t5QZ72jIwZrBSRd5ut+dg8pMeXuRd/7PVT+LJ7dSfYVPLuWn0=='\
                              }",                       'alipay.com 官方接口0.38~0.6%', True))

    # 商品分类
    db.session.add(ProdCag('ChatGPT账号', '虚拟账号类商品', '100'))
    # db.session.add(ProdCag('激活码', '单独激活类商品', '1000'))
    # db.session.add(ProdCag('第三分类', '单独激活类商品', '1000'))
    # 商品设置
    db.session.add(ProdInfo('ChatGPT账号', 'ChatGPT账号', 'ChatGPT账号(支持邮箱密码登陆，账号余额5美元，三个月有效期)', 'images/null.png', '100', '示例：卡密格式：账号------密码-----',
                            0.01, None, True, 0, '请填写邮箱', True))
    # db.session.add(ProdInfo('ChatGPT账号','批发商品演示','商品简述信息演示XXXX','images/null.png','100','演示：我是商品描述信息',\
    #                             9.99,'9#9.9,8.8', True,0,0,True))
    # db.session.add(ProdInfo('ChatGPT账号', '批发商品演示', '商品简述信息演示XXXX', 'images/null.png', '100', '示例：卡密格式：账号------密码-----',
                            # 9.99, '9,100#9.9,8.82,7.7', True, 0, '请填写邮箱', True))
    # db.session.add(ProdInfo('ChatGPT账号', '普通商品DD', '商品简述信息演示XXXX', 'images/null.png', '100', '示例：卡密格式：账号------密码-----',
                            # 9.99, None, False, 0, '请填写邮箱', False))
    # db.session.add(ProdInfo('激活码', '重复卡密演示', '商品简述信息演示XXXX', 'images/null.png', '100', '示例：卡密格式：账号------密码-----',
                            # 9.99, None, True, 0, '请填写邮箱', True))
    # db.session.add(ProdInfo('激活码', '普通商品CC', '商品简述信息演示XXXX', 'images/null.png', '100', '示例：卡密格式：账号------密码-----',
                            # 9.99, None, True, 0, '请填写邮箱', True))
    # db.session.add(ProdInfo('激活码', '普通商品BB', '商品简述信息演示XXXX', 'images/null.png', '100', '示例：卡密格式：账号------密码-----',
                            # 9.99, None, True, 0, '请填写邮箱', False))
    # 卡密设置
    db.session.add(Card('ChatGPT账号', '454545454454545454', False, False))
    # db.session.add(Card('批发商品演示', '555555555555555555', False, False))
    # db.session.add(Card('批发商品演示', '666666666666666666', False, False))
    # db.session.add(Card('重复卡密演示', '666666666666666666', True, False))
    # 系统配置
    db.session.add(Config('web_name', '飞鱼云商城', '网站名称', True))
    db.session.add(Config('web_keyword', '飞鱼云商城,ChatGpt账号,QQ会员账号,视频会员账号,视频VIP', '网站关键词', True))
    db.session.add(Config('description', '飞鱼云商城支持购买各种账号、VIP,支持在线支付，一键式发卡，无需等待', '网站描述', True))
    # fixme
    db.session.add(
        Config('web_url', 'http://127.0.0.1:5000', '必填，网站实际地址', True))
    db.session.add(Config(
        'web_bg_url', 'https://cdn.jsdelivr.net/gh/Baiyuetribe/yyycode@dev/colorfull.jpg', '网站背景图片', True))
    db.session.add(
        Config('contact_us', '<p>客户支持: h303567649@gmail</p>', '首页-联系我们', True))
    db.session.add(Config(
        'web_footer', '<a style="color: #fafafa;" href="https://github.com/Heliner/kamiFaka"></a>', '可填写备案信息', True))
    db.session.add(Config('top_notice', '稳定版演示站点，公告信息可在后台设置', '首页公告', False))
    db.session.add(
        Config('toast_notice', '稳定版演示站点，公告信息可在后台设置', '首页滑动消息设置', False))
    # db.session.add(Config('top_notice','开发版演示站点，公告信息可在后台设置','首页公告',True))
    # db.session.add(Config('toast_notice','这里是开发板，每天更新好几次那种','首页滑动消息设置',True))
    # db.session.add(Config('modal_notice','【计划中】','全局弹窗信息',True))
    db.session.add(Config('contact_option', '0', '是否启用联系方式查询[0启用，1关闭]', True))
    db.session.add(Config('theme', 'list', '主题', False))
    db.session.add(Config(
        'kamiFaka', 'https://github.com/Heliner/kamiFaka', 'Github项目地址，用于手动检测新版', False))
    db.session.add(Config('kamiFaka_v', '1.88', 'Github项目地址，用于手动检测新版', False))

    # 通知渠道 ：名称；对管理员开关；对用户开关；对管理员需要管理员账号；用户无；名称+config+管理员+admin_switch+user_switch
    db.session.add(Notice(
        '邮箱通知', "{'sendname':'no_replay','sendmail':'303567469@qq.com','smtp_address':'smtp.qq.com','smtp_port':'465','smtp_pwd':'dxyjwwcivrntbhab'}", 'hfl3035@163.com', True, True))
    # db.session.add(Notice(
        # '微信通知', "{'token':'AT_nvlYDjev89gV96hBAvUX5HR3idWQwLlA'}", 'xxxxxxxxxxxxxxxx', False, False))
    # db.session.add(Notice(
        # 'TG通知', "{'TG_TOKEN':'1290570937:AAHaXA2uOvDoGKbGeY4xVIi5kR7K55saXhs'}", '445545444', False, False))
    # db.session.add(Notice(
        # '短信通知', "{'username':'XXXXXX','password':'YYYYY','tokenYZM':'必填','templateid':'必填'}", '15347875415', False, False))
    # db.session.add(
        # Notice('QQ通知', "{'Key':'null'}", '格式：您的KEY@已添加的QQ号,示例：abc@123', False, False))

    # 订单信息【测试环境】
    # db.session.add(Order('演示订单可删除', 'ChatGPT账号', '支付宝当面付', '472835979',
    #                '请求尽快发货', 9.99, 1, 0.9, '账号：xxxxx；密码：xxxx', None, None))

    # 插件配置信息
    # db.session.add(Plugin('TG发卡', "{'TG_TOKEN':'1488086653:AAHihuO0JuvmiDNZtsYcDBpUhL1rTDO6o1C'}",
                #    '### 示例 \n请在管理后台--》Telegram里设置，支持HTML格式', False))

    # 临时订单
    # db.session.add(TempOrder('id44454','重复卡密演示','alipay','154311','',10,False,None))
    # db.session.add(TempOrder('id44454','批发商品演示','alipay','154311','',22,False,None))
    db.session.commit()
