import requests,json
from bs4 import BeautifulSoup

url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_1424766684?csrf_token='
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
'referer':'https://music.163.com/song?id=1424766684'}
data = {'params': 'mDIswkY7J+vBRuINKIO96huHNNhdXn+GQfPbLSJM++jF0Q6pXsLyEQaX+mcEuYvFZVokSKAnWmEqCcDjq4+8LsKCBQ4N19KxHA5cm2A9h1XYBIx+GmRY9WuZM1dKmF3yHkxg5e5TEgoBjLW42bomgc+qpwYhhm8ueU/WsUftsMLyciE7mkH2ecUMyjacZOkV',
'encSecKey': '5efc456f86b53af7055ce9c55d30ebd1db95fe8e713475dfb35100b12c68ddb08c8b6080049f3c5e30828b52222c22af9d03147c0e733650dad1ca61762d5b3aa9af662eb84243ad8eca55bf97e7221e6fe67c66849b976cdf9b3dc628cd5084b31cd002ed061fbbe8503845cb11e6d0b2425653d68975edf4348817c117b5cf'}

r = requests.post(url,headers = headers,data = data)

comment_json = json.loads(r.text)
hot_comments = comment_json["hotComments"]


with open('dianke.txt','w',encoding = 'utf-8') as file:
    for each in hot_comments:
        file.write(each['user']["nickname"]+':\n')
        file.write(each['content']+'\n')
        file.write('------------------------------------------------------------------------------------------------------------------\n')