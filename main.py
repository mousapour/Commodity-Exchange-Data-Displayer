from bs4 import BeautifulSoup
import requests
from PIL import Image
import csv

payload = {'LoginModel.Username': 'your-username', 'LoginModel.Password': 'your-password'}

captcha_image_address = "/Users/Reza/Desktop/captcha.jpg"
login_url = 'https://rahavard365.com/login?returnurl=%2f'

request_urls_1min = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7091%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7127%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7176%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7537%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7795%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7838%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A14861%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']

request_urls_1day = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7091%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7127%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7176%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7537%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7795%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7838%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A14861%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']

request_url_names = ['9908_negin_talayesorkh', 'negin_day98', 'negin_esfand98', 'negin_ordibehesht99',
                     'negin_tir99', 'negin_shahrivar99', 'negin_aban99']

request_urls_1day = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16041%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A15823%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16054%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16428%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16445%3Areal_close&resolution=1200&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']

request_urls_1min = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16041%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A15823%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16054%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16428%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16445%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']

request_url_names = ['9908_negin_talayesorkh', 'negin_dey99', 'negin_esfand99', 'negin_ordibehesht1400', 'negin_tir1400']



request_urls_1min = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7085%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7087%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7088%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7091%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7093%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7428%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']

request_url_names = ['zarin', 'roosta', 'novin', 'talaye_sorkh', 'saharkhiz', 'birjand']

request_urls_1min = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7041%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7205%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7520%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7794%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A7837%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A15219%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A15827%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16027%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16425%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A16708%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true',
                     'https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A6896%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']

request_url_names = ['peste_azar98', 'peste_bahman98', 'peste_farvardin99', 'peste_khordad99', 'peste_mordad99', 'peste_mahr99', 'peste_azar99', 'peste_bahman99', 'peste_farvardin00', 'peste_khordad00', 'peste_sabzdane']

request_urls_1min = ['https://rahavard365.com/api/chart/bars?ticker=exchange.asset%3A6896%3Areal_close&resolution=1&startDateTime=1&endDateTime=1650000000&firstDataRequest=true']
request_url_names = ['peste_sabzdane']

s = requests.Session()
r = s.get(login_url)
# print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# print(soup.find(alt="CAPTCHA")['src'])
captcha_url = 'https://rahavard365.com' + soup.find(alt="CAPTCHA")['src']
# print(captcha_url)

cap_req = s.get(captcha_url)
with open(captcha_image_address, 'wb') as f:
    f.write(cap_req.content)
img = Image.open(captcha_image_address)
img.show()
captcha_code = input('CAPTCHA: ')
payload['captcha'] = captcha_code

# print(captcha_code)

__RequestVerificationToken = soup.find(id='loginForm').find('input')['value']
payload['__RequestVerificationToken'] = __RequestVerificationToken

# payload['captcha'] = captcha_code

payload['LoginModel.RememberMe'] = 'false'

guid = soup.find(id='loginForm').find_all('input')[4]['value']
payload['captcha-guid'] = guid

print(payload)

login = s.post(login_url, payload)
print(login.status_code)


def get_data(s, request_url, filename):
    data_location_temp = s.get(request_url)
    data_location = BeautifulSoup(data_location_temp.text, 'html.parser').text
    # print(data_location)

    temp = data_location.split(',')
    # print(*temp[:7], sep='\n')
    headers = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    # headers = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

    with open('/Users/Reza/Desktop/' + filename + '.csv', 'w', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        counter = 0
        row_data = {}
        for el in temp:
            if counter == 7:
                writer.writerow(row_data)
                print(row_data)
                counter = 0
                row_data = {}
            if counter == 6:
                row_data[headers[counter - 1]] = el.split(':')[1][:-1]
            # if counter == 0:
            #     continue
            else:
                row_data[headers[counter - 1]] = el.split(':')[1]
            counter += 1


for i in range(len(request_url_names)):
    get_data(s, request_urls_1min[i], request_url_names[i])
    print(request_url_names[i] + '.csv is saved.')







