import requests

def test_order_process():
    #1.登录获取token
    login_resp = requests.post("https://httpbin.org/post", json={"user":"xiaoyu","password":"777"})
    token = "Bearer " + login_resp.json()['json']['user'] + login_resp.json()['json']['password']

    #2.下单，携带token
    headers = {"Authorization": token}
    order_resp = requests.post("https://httpbin.org/post", headers=headers, json={"item":"iPhone17","count":1})

    #3.断言
    assert order_resp.status_code == 200
    assert order_resp.json()["headers"]["Authorization"] == token
    print("✅ 订单流程测试通过！")

if __name__ == "__main__":
    print(f"🌐 测试开始...\n")
    test_order_process()