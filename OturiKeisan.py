#config:utf-8

while True:
    ManNow = input('現在の10000円札の枚数は？：')
    if len(ManNow) == 0:
        break
    ManNow = int(ManNow)
    GosenNow = input('現在の5000万円札の枚数は？：')
    SenNow = input('現在の1000円札の枚数は？：')
    GohyakuNow = input('現在の500円玉の枚数は？：')
    HyakuNow = input('現在の100円玉の枚数は？：')
    GojyuNow = input('現在の50円玉の枚数は？：')
    JyuNow = input('現在の10円玉の枚数は？：')
    GoNow = input('現在の5円玉の枚数は？：')
    ItiNow = input('現在の1円玉の枚数は？：')
    GosenNow = int(GosenNow)
    SenNow = int(SenNow)
    GohyakuNow = int(GohyakuNow)
    HyakuNow = int(HyakuNow)
    GojyuNow = int(GojyuNow)
    JyuNow = int(JyuNow)
    GoNow = int(GoNow)
    ItiNow = int(ItiNow)
    NowMoney = ManNow * 10000 + GosenNow * 5000 + SenNow * 1000 + HyakuNow * 100 + GohyakuNow * 500 + GojyuNow * 50 + JyuNow * 10 + ItiNow + GoNow * 5
    print("合計{0}円" .format(NowMoney))
    Pay = input('お支払い金額は？：')
    Pay = int(Pay)
    Zan = NowMoney - Pay
    if Zan < 0 :
        print("お支払い限度を超えています")
    mankura = int(Pay / 10000)
    senkura = int((Pay - mankura *10000)  / 1000)
    hyakura = int((Pay - (mankura *10000 + senkura *1000 ))/100)
    jyukura = int((Pay - (mankura * 10000 + senkura *1000 + hyakura * 100)) / 10)
    itikura = int((Pay - (mankura * 10000 + senkura *1000 + hyakura * 100 + jyukura * 10)))
    Paymai = [mankura,senkura,hyakura,jyukura,itikura]
    count=0
    for z in Paymai:
        if z < 0:
            count++
            
