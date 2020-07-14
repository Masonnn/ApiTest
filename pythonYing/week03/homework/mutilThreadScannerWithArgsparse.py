#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import threading
import argparse
from ping3 import ping
import os
import sys

lock = threading.Lock()
openNum = 0
threads = []


def pingHost(host):
    result = ping(host, timeout=1)
    return type(result) == float and result > 0.0


# 连续 IP 地址支持 192.168.0.1-192.168.0.100 写法
def parseHosts(string1):
    hosts = []
    ips = string1.split('-')
    firstIPsplit = ips[0].split('.')
    lastIPsplit = ips[-1].split('.')
    # print(ips)
    cnt = int(lastIPsplit[-1]) - int(firstIPsplit[-1]) + 1

    for i in range(cnt):
        fourth = int(firstIPsplit[-1]) + i
        host = firstIPsplit[0] + "." + firstIPsplit[1] + "." + firstIPsplit[2] + "." + str(fourth)
        hosts.append(host)

    return hosts


def portScanner(host, port):
    global openNum
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()  # 上锁
        openNum += 1
        print('[+] %d open' % port)
        lock.release()  # 释放锁
        s.close()
    except:
        pass


# def commond():


def main():
    # 传入参数解析
    p = argparse.ArgumentParser(description='How to use Port scanner!.')
    p.add_argument('-ip', dest='hosts', type=str)
    p.add_argument('-n', dest='concurrent counts', type=int)
    p.add_argument('-f', dest='ping | tcp', type=str)
    p.add_argument('-w', dest='save result', type=str)
    args = p.parse_args()
    hostList = parseHosts(args.hosts)

    setdefaulttimeout(1)
    for host in hostList:
        try:
            pingHost(host)
            print('Scanning the host:%s......' % (host))
            for port in range(8070, 8090):
                t = threading.Thread(target=portScanner, args=(host, port))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()
        except:
            print("主机 %s ping不通，可能已经down了" % host)

        print('[*] The host:%s scan is complete!' % host)
        print('[*] A total of %d open port ' % openNum)


if __name__ == '__main__':
    main()
