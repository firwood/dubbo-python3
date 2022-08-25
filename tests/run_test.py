# -*- coding: utf-8 -*-
"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

import json
import threading
import unittest

import time

from dubbo.client import DubboClient, ZkRegister
from dubbo.codec.encoder import Object
from dubbo.common.loggers import init_log


class TestDubbo(unittest.TestCase):
    def setUp(self):
        init_log()  # 初始化日志配置，调用端需要自己配置日志属性

    def test_run_default(self):
        zk = ZkRegister('172.19.71.7:2181')
        dubbo_cli = DubboClient('com.qianmi.pc.es.api.EsGoodsQueryProvider', zk_register=zk)

        goods_query_request = Object('com.qianmi.pc.es.api.request.EsGoodsQueryRequest', values={
            'chainMasterId': 'A859315',
            'fromSys': 2,
            'pageNum': 1
        })
        result = dubbo_cli.call('query', goods_query_request)
        pretty_print(result)

    @unittest.skip('skip not important test')
    def test_run(self):
        zk = ZkRegister('zook-ha-test.dns.guazi.com:2181')
        dubbo_cli = DubboClient('me.hourui.echo.provider.Echo', zk_register=zk)
        for i in range(4):
            thread = threading.Thread(target=run, args=(dubbo_cli,))
            thread.start()

    @unittest.skip('skip not important test')
    def test_run2(self):
        zk = ZkRegister('zook-ha-test.dns.guazi.com:2181')
        dubbo_cli = DubboClient('com.guazi.ctob.valuation.service.ActivityDService', zk_register=zk)
        eventTime = 1661396792
        result = dubbo_cli.call('queryAllVaildActivities', eventTime)
        print(result)

    @unittest.skip('skip not important test')
    def test_33(self):
        a=1
        b=2
        print(a+b)


def pretty_print(value):
    print(json.dumps(value, ensure_ascii=False, indent=4, sort_keys=True))


def run(_dubbo):
    for j in range(1000):
        _dubbo.call('echo18')


if __name__ == '__main__':
    unittest.main()
