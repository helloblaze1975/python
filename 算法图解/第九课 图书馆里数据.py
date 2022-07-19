# coding=utf8
# Happy
# Huan Zhang
# Day day up!
# 22/05/04  20:31
bids={}
more=False
high_bid=0
while not more:
    key=raw_input("what is your name")
    value=int(raw_input("what is your bid?"))
    bids[key]=value
    print(bids)
    more_put=input("continue type 1 or not type 2")
    if more_put==2:
        more = True
        for k,v in bids.items():#数据组里怎么搞循环
            if v > high_bid:
                high_bid = v
                winner = k
        print("winner is "+winner +"with a bid",high_bid),#用+打印出来没有引号，但是没法和数据链接。
    else:
        more = False









