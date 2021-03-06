import os
import re
import socket
import queue
import itertools
import threading
import argparse
import time
import sys

sys.stdout.flush()
sys.stderr.flush()


class Context:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses

        ports = tuple(range(1, 1025))
        tasks = itertools.product(self.ip_addresses.keys(), ports)
        self.q = queue.Queue()
        for task in tasks:
            self.q.put(task)

    output_address = ''


class PingTest(threading.Thread):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def run(self):
        print(f'启动线程：{threading.current_thread().getName()}')
        sys.stdout.flush()
        self.scheduler()
        print(f'结束线程：{threading.current_thread().getName()}')
        sys.stdout.flush()

    # 模拟任务调度
    def scheduler(self):
        while not context.q.empty():
            ip_address, port = context.q.get()
            if self.context.ip_addresses[ip_address] is None:
                if context.f == 'ping':
                    ret = self.ping_test(ip_address)
                    if ret:  # ping success
                        self.context.ip_addresses[ip_address] = 1
                    else:
                        self.context.ip_addresses[ip_address] = 0

            if self.context.ip_addresses[ip_address] == 1:
                self.scan_port(ip_address, port)
                if context.output_address:  # output relative info
                    pass

    def ping_test(self, ip):
        ret_ping = os.popen(f'ping {ip}')
        result = re.search('TTL', ret_ping.read())
        if result:
            sys.stdout.flush()
            return ip

    def scan_port(self, ip, port, t_elapse=15):
        sys.stdout.flush()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(t_elapse)
        ret = s.connect_ex((ip, port))
        if ret == 0:
            print(f'{ip} {port} is opened')
            sys.stdout.flush()


if __name__ == '__main__':
    start_time = time.perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', dest='Number', type=int, required=True,
                        default='1', help='target Number')
    parser.add_argument('-f', '--function', dest='Function', type=str, required=True,
                        default='', help='target Function')
    parser.add_argument('-ip', '--ip', dest='ip', type=str, required=True,
                        default='', help='target ip')
    parser.add_argument('-w', '--write', dest='OutputAddress',
                        default='', type=str, help='target Write to File')
    args = parser.parse_args()
    ip_addresses = dict.fromkeys(args.ip.split('-'))
    context = Context(ip_addresses)
    context.n = args.Number
    context.f = args.Function
    context.output_address = args.OutputAddress

    threads = []
    for _ in range(context.n):
        thread = PingTest(context)  # 创建线程
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    time_cost = time.perf_counter() - start_time
    print(f'mission done, total time cost: {time_cost}')
