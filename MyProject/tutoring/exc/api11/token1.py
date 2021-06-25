import requests

URL = 'https://api.iamport.kr/users/getToken'
data = {'imp_key': 'imp_apikey',
        'imp_secret': 'ekKoeW8RyKuT0zgaZsUtXXTLQ4AhPFW3ZGseDA6bkA5lamv9OqDMnxyeB9wqOsuO9W3Mx9YSJ4dTqJ3f'}
res = requests.post(URL, data=data)


print(res)
result_data = res.json()
print(result_data)
print(result_data['response']['access_token'])


URL1 = 'https://api.iamport.kr/subscribe/payments/onetime'
body = {'merchant_uid': 'qwerqq', 'amount': 100, 'card_number': '5365-1008-3760-0382', 'expiry': '2024-05',
           'birth': '980421', 'pwd_2digit': '20'}
headers = {'Authorization': result_data['response']['access_token']}

res1 = requests.post(URL1, data=body, headers=headers)

print(res1)
result_data = res1.json()
print(result_data)