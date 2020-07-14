from ping3 import ping
import socket


def ping_host(ip):
    result = ping(ip, timeout=1)
    print(result)
    return type(result) == float and result > 0.0


def main():
    ip = '192.168.0.130'
    # ping_host(ip)
    print(ping_host(ip))


if __name__ == "__main__":
    main()
