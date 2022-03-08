import random
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("**************************************************************")
print(BASE_DIR)

sys.path.append(BASE_DIR)
# print(os.path.join(BASE_DIR, 'apps'))

from ronglian_sms_sdk import SmsSDK




# accId = '容联云通讯分配的主账号ID'
accId = '8a216da87f63aaf1017f686b761200ee'

# accToken = '容联云通讯分配的主账号TOKEN'
accToken='c815492049a34e75912af6c78d40d829'

# appId = '容联云通讯分配的应用ID'

appId = '8a216da87f63aaf1017f686b773a00f5'


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    # tid = '容联云通讯创建的模板'
    # tid = "%06d" % random.randint(0, 999999)
    # print(tid)
    """"
    .免费开发测试使用的模板ID为1，具体内容：【云通讯】您的验证码是{1}，请于{2}分钟内正确输入。其中{1}和{2}为短信模板参数。
    """
    tid=1

    # mobile = '手机号1,手机号2'
    mobile = '15707974821'
    # datas = ('变量1', '变量2')
    datas = ('5','2')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

send_message()
