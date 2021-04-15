import lxml
import requests
from bs4 import BeautifulSoup
import json

# for t, p in enumerate(card, start=1):
#     Ttitle = p.find('h3', class_='card-title').text.strip()
#     Pprice = p.find('h4').text
#     img = p.find(class_='card-img-top img-fluid')
#     img = img.get('src')
#
#     print(f'Название товара: {Ttitle} , Цена: {Pprice} , Ссылка на фото: https://scrapingclub.com{img}')
# card_url_list=[]
# for i in range(1,8):
#
#     url = f'https://scrapingclub.com/exercise/list_basic/?page={1}'
#
#     q = requests.get(url)
#     result=q.content
#     soup=BeautifulSoup(result,'lxml')
#     cards=soup.find_all('div',class_='col-lg-4 col-md-6 mb-4')
#     # print(cards)
#
#
#     for card in cards:
#         urls=card.find('a')
#         card_page_url=urls.get('href')
#         card_url_list.append(card_page_url)
#
# with open('card_url_list.txt','a') as file:
#     for line in card_url_list:
#         file.write(f'https://scrapingclub.com{line}\n')

with open('card_url_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    data_dict=[]
    count=0
    for line in lines:
        q = requests.get(line)
        result=q.content

        soup = BeautifulSoup(result, 'lxml')
        card = soup.find(class_='card mt-4 my-4')
        card_img = soup.find(class_='card-img-top img-fluid')
        card_img = card_img.get('src')
        card_title = soup.find('h3').text
        card_price = soup.find(class_='card-body').find('h4').text
    # print(f'Название товара: {card_title}\nЦена: {card_price}\nСсылка на фото: https://scrapingclub.com{card_img}')

        data = {
            'Name product ': card_title,
            'Price ': card_price,
            'Image ': f'https://scrapingclub.com{card_img}'
        }

        count+=1
        print(f'#{count}:{line} is done!')
        data_dict.append(data)
        with open('data.json','w') as json_file:
            json.dump(data_dict,json_file,indent=4)
















