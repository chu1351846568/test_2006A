import random

import allure
import requests

from tools.api import request_tool


'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_aaa(pub_data):
    print(pub_data)


def test_login(pub_data):

    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
            {
          "pwd": "19DYhSac",
          "userName": "sunyj97"
        }
            '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)
    pub_data["token"] = r.json()["data"]["token"]

def test_addOrder(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token":"${token}",'Host': 'qa.yansl.com:8084', 'Connection': 'keep-alive', 'Accept': '*/*', 'Origin': 'http://qa.yansl.com:8084', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 'Content-Type': 'application/json', 'Referer': 'http://qa.yansl.com:8084/swagger-ui.html', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "ordeerPrice": 0,
  "orderLineList": [
    {
      "qty": 0,
      "skuCode": "自动生成 字符串 2,5 数字字母 xuepl"
    }
  ],
  "receiver": "string",
  "receiverPhone": "string",
  "receivingAddress": "string",
  "sign": "string",
  "userName": "string"
}'''

    # --------------------


#4、充值


def test_chang_post_chongzhi(pub_data,db):
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL ;")
    pub_data["account_name"]=random.choice(res)[0]
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${account_name}",
  "changeMoney": 500000
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
def test_chang_post_chongzhi(pub_data,db):
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL ;")
    pub_data["account_name"]=random.choice(res)[0]
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${account_name}",
  "changeMoney": 500000
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)











#2、扣款
from config.conf import API_URL

@allure.feature("用户管理")#一级分类
@allure.story("充值提现模块")#二级分类
@allure.title("扣款接口-账户余额不足")#二级分类

def test_recharge(db):
    # 执行查询sql语句
    with allure.step("第一步、执行SQL语句"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account`WHERE STATUS=0 AND account_name IS NOT NULL;")
    # 从查询结果中随机获取一条，取第一个数据
    with allure.step("第二步、从结果中随机获取一条，取第一条数据"):
        account_name = random.choice(res)[0]
    # 准备请求数据
    with allure.step("第三步、准备请求数据"):
     data = {
        "accountName":account_name,
        "changeMoney": 3000
    }
    # 使用 requests框架发送http请求
    with allure.step("第四步、发送请求"):
        r = requests.post(API_URL + "/acc/charge",json=data)
    with allure.step("第五步、获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)
    with allure.step("第六步、获取请求内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响头正文",allure.attachment_type.TEXT)
    with allure.step("第七步、断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("账户余额不足","预期结果",allure.attachment_type.TEXT)
        assert "账户余额不足" in r.text


