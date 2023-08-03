from alipayf2f import AlipayF2F, AliPay, AliPayConfig


def test_alipay():
    a = AlipayF2F()
    print((a.create_order('test', 1001, 0.02)))
    exit(-1)

    # #本地开发环境测试
    app_private_key_string = '-----BEGIN RSA PRIVATE KEY-----\n' + 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCT78anoNglBr9ub/zdJvdsKJrh5bz7IEMgjTs6tcMVT3UHPzeqjKGr6A7Zg9uWy4IXPv4xpZOqv3YNzD/oTdVBaqFUDg0JS43OJ1CNFY9FqCFM5LsIjaxNFtdM5FRlQSPvYpQoDpW3TR3Y7wZnCTDfXkYfR2Kzof0MFaB/JTKHNEIdlDrTYNMcpCtifhnm6Q3n/RWk6tlq3Wjck7M1FlKenTCh/FihTm5B3w03JXENhlHFWPoAorj/TCPASCVCr7MKJorDJu+NV/tL0k3PYUmf4C+hA/z7ZhFGcfec2JmLvETMY8/5pbUEIUjMwWEuO2Ty5pZ2RwApNFNUVAg7ko9/AgMBAAECggEAHBAQDxxj5CIzji+QOCN8K/hH6TI7dyfXlAU2hxyTtSctfAJx/NhQktuidYCd1y0jsGUysxhFus43BscIGHkrSw1/LQK9VlYOwFyU2y6LzxrltkBtemHlnXoHvX5SxCJnPrHkiPS7Udo/Hze4bzM/IiAwDR7tikXgSrqPh4721s64A8Pe0dFdZqmc4snJfp0mqoo7IktcV/Ed6lzJ9gO1snEdq4LWw3Zznu02mpVFIN717kcSU4/63Aaq5APGZEPNNMwOcD20wYyAaZs6pH2DkT8NFAy1u9gEy1uIMZkt2OLCnoB7RQxJ8rIVKiMoxWxDdJJTcnbVlKFCWiaTLCf1gQKBgQDn41KMDylq9ijh6NKtaji61nxvIxEX7cqUeV/ySxvpeIE7tU6jI6yfRfVSQeO85Azh8pmHPeiiW6Nlf/US+CN0nRpi0azQdnHdeluYBBGKWNaOHmuOjTAoMqlY2FX7q1bqUXtjqY8YoqyfkNt9JlZvf+x8dfpwgLKic0B+n5ThCwKBgQCjUbvdGt0lwtYl92QBPE4IcwIEJh+hyo1F0a83d16onD/d7lDAO8uBcoGAz3PKHDYVmsydX4IcUpPYD0K2iEdalWHAkLEKWRjQmI4D4ok9KVTI+6PC7cM9rqECqCW3iGoPAUTNuQjLL8mAyWZTNzwWDLizb8dJ50uDgazMG0R73QKBgQDd0lNQr+BK9Zc+I94FDaue7zaxibX8UfiL91+VA8x7lk7psxK6dJHY+q8mNOmJ9A1uxweem9ZCGa9AlRr3Pm+MSgzHoxPRhrx9xWKBFMNCuKDl6quw/danXW8qEiiOSuUl2TRTrgu44USIj6WnHllo59JtbN5ZaIN5aw6zEiz06QKBgGKw+nhjSm4OLgBlXb5NZc4/SWGedBD96J7fViWLcd0sBoAjChMQTyrbOhzPv+XLZHdrwuf6lhJtaD/xANxyv8Oib57BEOry6kbrWS5Jz6rw9fY58jzSFuCITW3glGIzAfwtRRmYDhNSvk6f5cC1qQ6eA2MTUfd72KsQSo5Qj/LVAoGASbRPM+F/hNHRrDw70zonaD8MQ40DTbV+VGb1cW2FAw4C8cOvoqCRayCc3pe5AyIk8Vuus6KOiiNlSaLha7VAE27AaMuwcnmStZ9OxsAiR8cuknvsjNrB69uXW8t5QZ72jIwZrBSRd5ut+dg8pMeXuRd/7PVT+LJ7dSfYVPLuWn0==' + '\n-----END RSA PRIVATE KEY-----'

    alipay_public_key_string = '-----BEGIN PUBLIC KEY-----\n' + 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiP+YAsj+G2hKfUMU+XWG7Tik6J1N7NvCAe9ECy/Mli/VW/BSWQ2+CJNUlfSErZEMa6544pZHJik0WSeWNzPFQ0isIrE08sS0uDAcv11JXg/ahYp92JP/ikQTEdLzsVD4Cf/C68w79bWb42zIXcZP2esrJRG/TN+18MC80fmY79iWlkS4XlcYPafX25guIGn4eJyReiqgJvOUehedMdSnjJPuH2NEfSYC2vVRNkxz4X3NkASdC8LvZwhiIcNnypqkwT6r83Xq7nUCWqYscQpkYzZTh551p+dwpajxj7xdndwijrh8RJOhN4xaWsyI2g04xGdP4tzTJXAtxo3fUDSZLwIDAQAB' + '\n-----END PUBLIC KEY-----'

    # # 注意加上开头结尾

    alipay = AliPay(
        appid="2021004101685214",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # True后为开发环境，所有走dev接口，正式环境用False
        config=AliPayConfig(timeout=15)  # 可选, 请求超时时间
    )

    print(alipay.api_alipay_trade_precreate('test', 1001, 0.2))


if __name__ == '__main__':
    test_alipay()
