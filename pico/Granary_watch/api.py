import urequests
import utime

url = 'http://192.168.1.205:8000/submit'
data = {'device': 'esp01',
        'temperature': 9,
       }
response = urequests.post(url, json=data)
print("response code {}".format(response.status_code))