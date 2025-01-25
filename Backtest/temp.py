import requests

cookies = {
    '_gcl_au': '1.1.188627639.1713816164',
    '_ym_uid': '1713823413364728021',
    '_ym_d': '1713823413',
    'CBONDSSESSID': '3960abddd070509bbf9f136662fae2b3',
    '_gid': 'GA1.2.970274722.1714160430',
    '_clck': '7xyiv7%7C2%7Cfl9%7C0%7C1573',
    'reg_banner': 'true',
    '_ga_C7H1FKN29G': 'GS1.1.1714168446.5.1.1714172724.0.0.0',
    '_ga': 'GA1.2.118106074.1713816164',
    '_gat_UA-125462478-1': '1',
    '_ga_72QC8WS6GW': 'GS1.2.1714168461.4.1.1714172726.0.0.0',
    '_clsk': 'dxmrks%7C1714172726965%7C25%7C1%7Cx.clarity.ms%2Fcollect',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '_gcl_au=1.1.188627639.1713816164; _ym_uid=1713823413364728021; _ym_d=1713823413; CBONDSSESSID=3960abddd070509bbf9f136662fae2b3; _gid=GA1.2.970274722.1714160430; _clck=7xyiv7%7C2%7Cfl9%7C0%7C1573; reg_banner=true; _ga_C7H1FKN29G=GS1.1.1714168446.5.1.1714172724.0.0.0; _ga=GA1.2.118106074.1713816164; _gat_UA-125462478-1=1; _ga_72QC8WS6GW=GS1.2.1714168461.4.1.1714172726.0.0.0; _clsk=dxmrks%7C1714172726965%7C25%7C1%7Cx.clarity.ms%2Fcollect',
    'origin': 'https://cbonds.com',
    'priority': 'u=1, i',
    'referer': 'https://cbonds.com/bonds/210201/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

json_data = {
    'items': [
        {
            'id': 210201,
            'tgId': 20,
            'model': 'bonds',
        },
        {
            'id': None,
            'tgId': None,
            'model': 'index',
        },
    ],
    'startDate': '2021-04-26',
    'endDate': '2024-04-26',
    'chartType': 'price',
    'userChangePeriod': False,
    'getChartIteration': 2,
}

response = requests.post('https://cbonds.com/api/chart/get_tradings/', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"items":[{"id":210201,"tgId":20,"model":"bonds"},{"id":null,"tgId":null,"model":"index"}],"startDate":"2021-04-26","endDate":"2024-04-26","chartType":"price","userChangePeriod":false,"getChartIteration":2}'
#response = requests.post('https://cbonds.com/api/chart/get_tradings/', cookies=cookies, headers=headers, data=data)