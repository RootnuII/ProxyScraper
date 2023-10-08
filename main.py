## this script has made in 24 hours :skull:
import requests, os
from time import sleep
from pystyle import *

black = '\033[0;90m'
red = '\033[0;91m'
green = '\033[0;92m'
yellow = '\033[0;93m'
blue = '\033[0;94m'
purple = '\033[0;95m'
cyan = '\033[0;96m'
white = '\033[0;97m'
off = '\033[0m'
fgreen = '\033[42;97m'
fred = '\033[41;97m'

def clear():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")

def getproxy(url, cc):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        lines = content.split("\n")
        ee_proxies = [line.split()[0] for line in lines if f"{cc}" in line]
        if ee_proxies is not None:
            for proxy in ee_proxies:
                print(proxy)
        else:
            pass
    else:
        print(f"{red}[ERROR]{off}: {response.status_code}")
    return ee_proxies

def getproxys(url, cc):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        lines = content.split("\n")
        br_proxies = [line.split()[0] for line in lines if f"{cc}" and "-S" in line]
        if br_proxies is not None:
            for proxy in br_proxies:
                print(proxy)
        else:
            pass
    else:
        print(f"[ERROR]: {response.status_code}")
    return br_proxies

def getallproxies(url, cc):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        lines = content.split("\n")
        all_proxies = [line.split()[0] for line in lines if f"{cc}" and ("-S" in line or "-H" in line)]
        if all_proxies is not None:
            for proxy in all_proxies:
                with open("allcountries.txt", 'a') as a:
                    a.write(f"{proxy}\n")
        else:
            pass
    else:
        print(f"[ERROR]: {response.status_code}")

banner="""
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
"""
credits=f"{purple}[https://github.com/Detrew]{off}"
menu=f"""
[{green}1{off}] {green}Socks5 Proxy{off}
[{green}2{off}] {green}HTTP Proxy{off}
[{green}3{off}] {green}HTTPS Proxy{off}
[{green}4{off}] {green}All Proxies (HTTP and HTTPS){off}

[{green}00{off}] {green}Exit{off}
"""

country_codes = {
    '1': 'US',
    '2': 'ID',
    '3': 'FR',
    '4': 'DE',
    '5': 'RU',
    '6': 'SG',
    '7': 'BR',
    '8': 'BD',
    '9': 'TR',
    '10': 'EC',
}

ccav=f"""
[{green}1{off}] United States ({green}US{off})
[{green}2{off}] Indonesia ({green}ID{off})
[{green}3{off}] France ({green}FR{off})
[{green}4{off}] Germany ({green}DE{off})
[{green}5{off}] Russia ({green}RU{off})
[{green}6{off}] Singapore ({green}SG{off})
[{green}7{off}] Brazil ({green}BR{off})
[{green}8{off}] Bangladesh ({green}BD{off})
[{green}9{off}] Turkey ({green}TR{off})
[{green}10{off}] Ecuador ({green}EC{off})
"""

def socksproxy():
    url="https://spys.me/socks.txt"
    clear()
    print(Center.XCenter(f"[{green}Choose Your Country{off}]"))
    print(ccav)
    sel = input(f"[{yellow}?{off}]: ")
    country_code = country_codes.get(sel)
    if country_code is not None:
        clear()
        print(Center.XCenter(f"[{blue}*{off}] Searching Proxy..."))
        bproxy = getproxy(url,country_code)
        proxy_count = len(bproxy)
        for proxy in bproxy:
            with open(f"socks5_{country_code}.txt", 'a') as a:
                a.write(f"{proxy}\n")
        print(Center.XCenter(f"[{green}*{off}] {proxy_count} Proxies Saved on socks5_{country_code}.txt"))
        sleep(4)
        main()
    else:
        print(Center.XCenter(f"[{red}Invalid Option{off}]"))
        sleep(1)
        main()

def httpsproxy():
    url="https://spys.me/proxy.txt"
    clear()
    print(Center.XCenter(f"[{green}Choose Your Country{off}]"))
    print(ccav)
    sel = input(f"[{yellow}?{off}]: ")
    country_code = country_codes.get(sel)
    if country_code is not None:
        clear()
        print(Center.XCenter(f"[{blue}*{off}] Searching Proxy..."))
        proxy_list = getproxys(url,country_code)
        proxy_count = len(proxy_list)
        for proxy in proxy_list:
            with open(f"https_{country_code}.txt", 'a') as a:
                a.write(f"{proxy}\n")
        print(Center.XCenter(f"[{green}*{off}] {proxy_count} Proxies Saved on https_{country_code}.txt"))
        sleep(4)
        main()
    else:
        print(Center.XCenter(f"[{red}Invalid Option{off}]"))
        sleep(1)
        main()

def httpproxy():
    url = "https://spys.me/proxy.txt"
    clear()
    print(Center.XCenter(f"[{green}Choose Your Country{off}]"))
    print(ccav)
    sel = input(f"[{yellow}?{off}]: ")
    country_code = country_codes.get(sel)
    if country_code is not None:
        clear()
        print(Center.XCenter(f"[{blue}*{off}] Searching Proxy..."))
        proxy_list = getproxy(url, country_code)
        proxy_count = len(proxy_list)
        if proxy_list is not None:
            for proxy in proxy_list:
                with open(f"http_{country_code}.txt", 'a') as a:
                    a.write(f"{proxy}\n")
            print(Center.XCenter(f"[{green}*{off}] {proxy_count} Proxies Saved on http_{country_code}.txt"))
            sleep(4)
            main()
        else:
            print(f"[{red}ERROR{off}]: No proxy list found for the selected country.")
            sleep(1)
            main()
    else:
        print(Center.XCenter(f"[{red}Invalid Option{off}]"))
        sleep(1)
        main()

def allproxies():
    url = "https://spys.me/proxy.txt"
    clear()
    print(Center.XCenter(f"[{green}Choose Your Country or All Countries{off}]"))
    print(ccav)
    print(f"[{green}11{off}] All Countries")
    sel = input(f"[{yellow}?{off}]: ")
    if sel == '11':
        clear()
        print(Center.XCenter(f"[{blue}*{off}] Searching Proxies for All Countries..."))
        for country_code in country_codes.values():
            getallproxies(url, country_code)
        print(Center.XCenter(f"[{green}*{off}] All Proxies Saved on allcountries.txt"))
        sleep(4)
        main()
    elif sel in country_codes:
        country_code = country_codes.get(sel)
        clear()
        print(Center.XCenter(f"[{blue}*{off}] Searching Proxies for {country_code}..."))
        getallproxies(url, country_code)
        print(Center.XCenter(f"[{green}*{off}] All Proxies Saved on allcountries.txt"))
        sleep(4)
        main()
    else:
        print(Center.XCenter(f"[{red}Invalid Option{off}]"))
        sleep(1)
        main()

menuop = {
    '1':socksproxy,
    '2':httpproxy,
    '3':httpsproxy,
    '4':allproxies,
    '00':exit,
}

# main \o\
def main():
    clear()
    print(Center.XCenter(banner))
    print(Center.XCenter(credits))
    print(Center.XCenter(menu))
    sel = input(f"[{yellow}?{off}]: ")
    selected_option = menuop.get(sel)
    if selected_option is not None:
        selected_option()
    else:
        print(Center.XCenter(f"[{red}Invalid Option{off}]"))
        sleep(1)
        main()

try:
    main()
except KeyboardInterrupt:
    clear()
    exit()
