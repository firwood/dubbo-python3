import json
import logging
import threading
import unittest

from dubbo.codec.encoder import Object
from dubbo.common.loggers import init_log
from dubbo.common.exceptions import DubboException
from dubbo.client import DubboClient, ZkRegister
from kazoo.client import KazooClient

logger = logging.getLogger('python-dubbo')

def run5():
    zk = ZkRegister('127.0.0.1:2181', auth_data=[('digest', 'username:password')])
    dubbo_cli = DubboClient('com.xxx.aaaService', zk_register=zk, group="xxx",
                            version="1.0.0")

    reqVo = Object('com.xxx.ReqVo', values={
        'userId': 600335433,
        'page': 1,
        'pageSize': 10,
    })
    result = dubbo_cli.call('getList', reqVo)
    print(result)

def main():
    run5()
    pass


if __name__=="__main__":
    main()