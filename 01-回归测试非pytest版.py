import requests

def baidu_home():
    resp = requests.get("https://www.baidu.com")
    assert resp.status_code == 200
    assert "baidu" in resp.text
    print("✅ 百度访问成功！")

def test_httpbin_get():
    payload = {"name":"xiaoyu","age":25}
    resp = requests.get("https://httpbin.org/get", params=payload)
    assert resp.status_code == 200
    assert resp.json()['args']['name'] == "xiaoyu"
    assert resp.json()['args']['age'] == "25"
    print("✅ httpbin GET 请求测试通过！")

if __name__ == "__main__":
    print(f"🌐 测试开始...\n")
    baidu_home()
    test_httpbin_get()