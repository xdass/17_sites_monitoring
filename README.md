# Sites Monitoring Utility
This script check the site status if it's OK return HTTP status 200 
also it check if this one paid for at least one month.


# How to install
```bash
$python pip install -r requirements.txt
```

# How to run
Note: 
* Your site name should startswith http:// or https://
* The site address must be a new line in file

```bash
$python check_sites_health.py <filename>
От http://google.ru получен HTTP статус с кодом 200
Домменное имя http://google.ru, проплачено минимум на 1 месяц
От http://e1.ru получен HTTP статус с кодом 200
Домменное имя http://e1.ru, проплачено минимум на 1 месяц 
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
