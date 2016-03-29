# -*- coding: utf-8 -*-
import itertools
money_type = (10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1)

def smart_pay(saifu,kakaku):
    bestPttern=None
    patterns=[]
    for mtype in money_type:
        pattern=[]
        for c in range(saifu[mtype]+1):
            pattern.append([mtype,c])
        if len(pattern)>1:
            patterns.append(pattern)
    for p in itertools.product(*patterns):
        ptn={x[0]:x[1] for x in p}
        if coins2price(ptn)>=kakaku:
            if  bestPttern is None:
                bestPttern=ptn
            else:
                if count_coins(price2coins(coins2price(bestPttern)-kakaku)) > count_coins(price2coins(coins2price(ptn)-kakaku)):
                    bestPttern=ptn
    return bestPttern

def price2coins(price):
    coins = {}
    for mt in money_type:
        coins[mt], price = divmod(price, mt)
    return coins

def coins2price(coins):
    return sum(key * val for key,val in coins.items())

def count_coins(coins):
    return sum(val for key,val in coins.items())

if __name__ == "__main__":
    saifu={}
    print("まずお財布の中身をお聞きします...")
    for mtype in money_type:
        saifu[mtype]= int(raw_input(str(mtype)+ "円は何枚？\n>"))
    kakaku=int(raw_input("いくらの商品を買いますか？\n>"))
    print("最適な支払い方法は.\n.\n.\n")
    bestPttern=smart_pay(saifu,kakaku)
    if bestPttern is None:
        print("おかねたりないです。。。")
    else:
        for key,val in bestPttern.items():
            print(str(key)+"円を"+str(val)+"枚")
        print("です！")
