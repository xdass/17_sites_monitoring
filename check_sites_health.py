import requests
# whois server url - https://www.nic.ru/whois/?query=


def load_urls4check(filepath):
    try:
        with open(filepath) as file:
            sites_url = file.read()
            return sites_url.split()
    except FileNotFoundError:
        return None


def is_server_respond_with_200(url):
    response = requests.get('http://e1.ru')
    if response.status_code == 200:
        return True
    else:
        return False


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    print(load_urls4check('sites_url.txt'))
    print(is_server_respond_with_200('http://e1.ru'))