import requests
import multiprocessing

from bs4 import BeautifulSoup
from lxml import html

def myip(prox):

    print(f'MyIp prox prox {prox}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    url_today = 'https://2ip.ru'
    url_ica = "http://icanhazip.com"

    respica = requests.get(url=url_ica, headers=headers, proxies=prox)
    html_txt = respica.text
    tree = html.fromstring(html_txt)

    path_id = '//pre/text()'

    print(f'XML {html_txt}')
    # Id_Xpath=tree.xpath(path_id)
    # print(Id_Xpath)
    # for item in tree.xpath(path_item):  # .getall():
    #     print(item)

    response2 = requests.get(url=url_ica, headers=headers, proxies=prox)
    soup = BeautifulSoup(response2.text, 'lxml')
    # #print(soup)
    #
    #ip = soup.find('div', class_='ip').text.strip()
    ip = soup.find('pre').text.strip()

    # location = soup.find('div', class_='value-country').text.strip()
    #
    print(f'IP_soup xml: {ip}\n') #Location: {location}')


def handler(proxy):
    link = "http://icanhazip.com"


    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }

    # proxies = {
    #     'http': f'http://{proxy}',
    #     'https': f'https://{proxy}',
    # }
    # proxies = {
    #     'https': f'https://{proxy}',
    #     }

    # proxies = {
    # 'http': 'http://104.21.83.215:80',
    # 'https': 'https://104.21.83.215:80',
    # }
    proxies = {
        'http': 'http://202.43.190.10:53128',
        'https': 'https://202.43.190.10:53128',
    }

    #РАБОТАЕТ! ТИП HTPS https://hidemy.name/ru/proxy-list/?start=64#list

    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}',
    }



    url_today = 'https://2ip.ru'
    htmdoc = "HTML"
    # try:
    #     response = requests.get(link, proxies=proxies, timeout=5).text
    #     if htmdoc in response.upper():
    #         print("ПППОООППАААДДДОООССС")
    #     else:
    #         print(f'IP: {response.strip()}\n " ПРОКСИ СРАБОТАЛ " {proxies}')
    #         myip(proxies)
    # except:
    #     print(f'Прокси не валидный! {proxies} \n {proxies}')

    try:
        response2 = requests.get(url=url_today, proxies=proxies, timeout=5)
        soup = BeautifulSoup(response2.text, 'lxml')

        ip = soup.find('div', class_='ip').text.strip()
        location = soup.find('div', class_='value-country').text.strip()
        print(f'IP_Today: {ip}\nLocation: {location}')
        myip(proxies)

    except:
        print(f'TODAY Прокси не валидный! {proxies} \n {proxies}')


    #url_today = 'https://2ip.ru'
    #response2 = requests.get(url=url_today, headers=headers, proxies=proxies)
    # soup = BeautifulSoup(response.text, 'lxml')
    #
    # ip = soup.find('div', class_='ip').text.strip()
    # location = soup.find('div', class_='value-country').text.strip()
    #
    # print(f'IP_Today: {ip}\nLocation: {location}')


# with open('proxy') as file:
with open('proxies.txt') as file:
    proxy_base = "".join(file.readlines()).strip().split('\n')
    print(f'PROXY base {proxy_base}')
    #PROXY https://hideip.me/ru/proxy/socks5list

#with multiprocessing.Poll(multiprocessing.cpu_count()) as process: #Запускайте не через Pool, а через Process
    #Подскажие как сделать запросы асинхрнонными? Используйте aiohttp
    # И ещё asyncio. Создаёшь контекст менеджер для тасков и запускаешь в многопотоке асинхронные функции asyncio.
    #мультипроцессинг нужно вызывать через сравнение name == main, иначе он уйдет в рекурсию.
    #мне помогло только это:
    # def main():
    #     with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    #         process.map(handler, proxy_base)
    #
    # if _name_ == '__main__':
    #     main()
#    process.map(handler, proxy_base)

def main():
        with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
            process.map(handler, proxy_base)

if __name__ == '__main__':
        main()

