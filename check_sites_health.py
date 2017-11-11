import requests
import whois
import datetime
import sys


def load_urls4check(filepath):
    try:
        with open(filepath) as file:
            sites_url = file.read()
            return sites_url.split()
    except FileNotFoundError:
        return None


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        if response.ok:
            return True
        else:
            return False
    except requests.ConnectionError as err:
        print(err.args[0])


def get_domain_expiration_date(site_url):
    whois_info = whois.whois(site_url)
    if type(whois_info.expiration_date) == list:
        return whois_info.expiration_date[0]
    else:
        return whois_info.expiration_date


def check_expiration_date(site_expiration_date):
    today = datetime.datetime.now()
    days_in_month = datetime.timedelta(days=30)
    return site_expiration_date - today > days_in_month


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url_file_path = sys.argv[1]
        sites_url_list = load_urls4check(url_file_path)
        for site_url in iter(sites_url_list):
            if is_server_respond_with_200(site_url):
                print('От {} получен HTTP статус с кодом 200'.format(site_url))
                expiration_date = get_domain_expiration_date(site_url)
                if check_expiration_date(expiration_date):
                    print('Домменное имя {}, проплачено минимум на 1 месяц'.format(site_url))
                else:
                    print('Срок регистрации {}, заканчивается меньше чем через месяц'.format(site_url))
    else:
        print('Укажите имя файла: $python check_sites_health.py <filename>')
