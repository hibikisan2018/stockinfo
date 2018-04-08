#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 01:35:35 2018

Send LINE message with LINE notify
@author: hibikisan
"""
import logging
import argparse
import time

import requests
import bs4

def readtokenfile(filename):
    with open(filename, 'r') as f:
        token = f.read()
    return token

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="define log level")
parser.add_argument("tokenfile", help="the token of LINE notify")
args = parser.parse_args()

if args.log == None:
    logging.basicConfig()
    logging.disable(logging.CRITICAL)

else:
    loglevel = args.log
    numeric_level = getattr(logging, loglevel.upper(), None)
    logging.basicConfig(filename = 'sendLineMessage2logging.txt', level=numeric_level, format='%(asctime)s - %(levelname)s -%(message)s')
    
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level:{}'.format(loglevel))
    logging.critical('\nStart program...')
    
#TOKEN = args.token
TOKEN = readtokenfile(args.tokenfile)

def get_data_from_website(url, css_selector, n):
    '''Get data from website from 'url' with CSS selector 
    Input:
        url: URL of website
        css_selector: CSS selector
        n: element number of Tag object from select() method
    Output
        strings
    '''
    logging.debug('--get_data_from_website()')
    logging.debug('URL:{}'.format(url))
    logging.debug('CSS selector:{}'.format(css_selector))

    # check download of web site 5 times in every 5 minutes
    for i in range(10):
        # URLで指定したサイトのデータを取得（Responseオブジェクト）
        res = requests.get(url)
        # ダウンロードが正常にできたかチェック
        try:
            res.raise_for_status()
            break
        except Exception as exc:
            logging.debug('Found problem: {}'.format(exc))
            time.sleep(300)
    
    # (1)BeautifuleSoupオブジェクトを生成    
    bs = bs4.BeautifulSoup(res.text, 'lxml')
    
    # (2)select()メソッドを使って目的の要素を抽出
    # 　ここではclass属性：'dataHeader'の要素をTagオブジェクトとして返却
    elems = bs.select(css_selector)
    logging.debug('Element:{}'.format(elems))
    logging.debug('Element[{}]:{}'.format(n, elems[n]))
    logging.debug('--end get_data_from_website()')
    
    # (3)TagオブジェクトのgetText()メソッドから目的のデータを取り出す
    return elems[n].getText()

def sendmessage(message):
    logging.debug('--start sendmessage()')

    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization" : "Bearer "+ TOKEN}
    
    payload = {"message" :  message}
    #files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。
    
    r = requests.post(url ,headers = headers ,params=payload)
    logging.debug('Response:{}'.format(r.text))
    logging.debug('Response Header:{}'.format(r.headers))
    logging.debug('--end sendmessage()')


def main():

    #N225
    # URLの指定
    url1 = 'https://www.nikkei.com/markets/worldidx/chart/nk225/'

    for i in range(5):
        #get the current stock price of N225
        N225name = get_data_from_website(url1, '.m-headline_text_large', 0)
        N225price = get_data_from_website(url1, '.economic_value_now.a-fs26', 0)
        N225def = get_data_from_website(url1, '.economic_balance_value.a-fs18', 0)
        N225lastupdate = get_data_from_website(url1, '.economic_value_time.a-fs14', 0)
    
        if N225price == '--':
            time.sleep(600)
            continue
        else:
            break  
   
    # Create the message 
    N225message = '{0}:\n{1}yen({2})\n{3}'.format(N225name, N225price, N225def, N225lastupdate)

    #JPNUSD
    url2 = 'https://www.nikkei.com/markets/kawase/'
    JPNUSDname = get_data_from_website(url2, '.m-headline_text', 6)
    JPNUSDprice = get_data_from_website(url2, '.mkc-stock_prices', 0)

    try:
        JPNUSDdef = get_data_from_website(url2, 'div.cmn-minus', 0)
    except:
        JPNUSDdef = get_data_from_website(url2, 'div.cmn-plus', 0)

    JPNUSDlastupdate = get_data_from_website(url2, '.mkc-date', 0)
    
    JPNUSDmessage = '{0}:\n{1}yen\n{2}\n{3}'.format(JPNUSDname, JPNUSDprice, JPNUSDdef, JPNUSDlastupdate[:-6])

    # Send the message via LINE
    sendmessage(N225message)
    sendmessage(JPNUSDmessage)

    # output messages to stdout
    #print(N225message) 
    #print(JPNUSDmessage)
     
    
if __name__ == '__main__':
    main()
