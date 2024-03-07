import requests
import json
import os
url = "https://proportionate-patient-seed.discover.quiknode.pro/d4ca034a23a3644dd5dbfe9326fa0f5ecc445496/"

Transaction = []
payload = json.dumps({
  "method": "eth_getBlockTransactionCountByHash",
  "params": [
    "0x29b29068575d939ed1168dce20a0e3538e00b21a779c9458f2be12d4aacf8736"
  ],
  "id": 1,
  "jsonrpc": "2.0"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
start = response.text.find("result")
end = response.text.rfind("}")
Trans_Number = response.text[start+9:end-1]
print(Trans_Number)

for i in range(int(Trans_Number,16)):
    payload = json.dumps({
        "method": "eth_getTransactionByBlockHashAndIndex",
        "params": [
        "0x29b29068575d939ed1168dce20a0e3538e00b21a779c9458f2be12d4aacf8736",
        hex(i)
        ],
        "id": 1,
        "jsonrpc": "2.0"
        })
    headers = {
        'Content-Type': 'application/json'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    Transaction.append(response.text)
    print(i)

A = open('rollup.txt','w')
for i in Transaction:
    A.write(i)
A.close()