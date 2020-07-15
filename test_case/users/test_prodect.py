from test_case.conftest import pub_data
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

#1、登录

def test_denglu(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=0ecb72339dd649bbbd6710089d5c8f8f; StuID=507; sidebarStatus=0'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "pwd": "aaa123",
  "userName": "aaa123"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
    pub_data["token"] = r.json()["data"]["token"]







#2、创建产品
def test_addProdcjsp(pub_data):
    pub_data["productCode"]="自动生成 字符串 3,5 数字"

    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    headers={"token":pub_data["token"]
             }

    json_data='''{
  "brand": "耐克",
  "colors": [
    "粉色","玫瑰金"
  ],
  "price": 2,
  "productCode": "${productCode}",
  "productName": "人本",
  "sizes": [
    "38"
  ],
  "type": "服装"
}'''
    json_path=[{"skuCode":"$.data[0].skuCode"}]


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data,json_path=json_path)

#3、查询单个产品

def test_getSKU_cxcp(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    headers={"token":pub_data["token"]
     }
    params={'SKU':'${skuCode}'}


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


#4、修改商品价格
def test_changePrice_xgjg(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    headers={"token":pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'SKU': '${skuCode}', 'price': '39800'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)


#5、查询商品价格是否已修改

def test_getSKU_qrcpjg(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    headers={"token":pub_data["token"]
             }
    params={'SKU':'${skuCode}'}


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

#6、根据产品编码批量修改商品价格

def test_changePriceByProdCode_xgjg(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers={"token":pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'price': '69800', 'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

#7、全量调整单个商品库存
def test_post_data_xgkc(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '锁定用户'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"qty":'2000',"skuCode":"${skuCode}"}
    headers={"token":pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

#8、#增量调整单个商品库存
def test_post_data_xgkc(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '锁定用户'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"qty":'5800',"skuCode":"${skuCode}"}
    headers={"token":pub_data["token"]
    }
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
