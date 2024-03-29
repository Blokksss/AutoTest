import requests
import json
from common.Log import logger
import readExcel

logger = logger
class RunMain():

    def send_post(self,url,data):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self,url,data):
        result = requests.get(url=url, data=data)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self,method,url=None,data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url,data)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url,data)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证请求是否正
    rde = readExcel('userCase.xlsx', '登录')


    #result=RunMain().run_main('post','http://jydnew.dev.jinr.com',{"data":'{"method":"user.login","v":"1.0.0","platform":"4","appid":"app_key","timestamp":"1552012801","mobile":"15872896008","login_type":"pwd","code":"123456","user_role":"2"}'})
    #print(result)
    #print(type(result))