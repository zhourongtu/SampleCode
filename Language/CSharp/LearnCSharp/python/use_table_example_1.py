class MsgType(object):
    NAME = 1
    EMAIL = 2
    EMAIL_2 = 3


# 服务端
type_2_deal_dict = {
    MsgType.NAME: func_1,
    MsgType.EMAIL: func_2,
    MsgType.EMAIL_2: func_3,
}


def func_1(msg):
    pass


def func_2(msg):
    pass


def receive_a_msg(type, msg):
    deal_func = type_2_deal_dict.get(type, None)
    deal_func(msg)


# 客户端
def send_a_msg(type, msg):
    pass


send_a_msg(MsgType.NAME, "周荣图")
send_a_msg(MsgType.EMAIL, "zhourongtu@qq.com")
send_a_msg(MsgType.EMAIL_2, "zhourongtu@qq.com")