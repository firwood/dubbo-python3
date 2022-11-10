import json
import logging
import threading
import unittest

from dubbo.codec.encoder import Object
from dubbo.common.loggers import init_log
from dubbo.common.exceptions import DubboException
from dubbo.client import DubboClient, ZkRegister
from kazoo.client import KazooClient

from dubbo.codec.encoder import Request
from dubbo.codec.encoder import List_Integer
from dubbo.codec.encoder import Integer

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

def run6():
    #  call com.xxx.aaaService#doJob(List<Integer> ids, Integer type)
    dubbo_cli = DubboClient('com.xxx.aaaService', host='127.0.0.1:2121', group="xxx", version="1.0.0")

    ids = List_Integer('java.util.List', values=[701846657])
    type = Integer('java.lang.Integer', values=1)
    args = (ids, type)
    resp = dubbo_cli.call('doJob', args=args, timeout=2)
    print(resp)
    pass


def main():
    run6()
    pass


if __name__=="__main__":
    main()