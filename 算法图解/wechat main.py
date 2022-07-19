import itchat
import csvs
def get_data():
    core.loginInfo['wxsid'] = core.loginInfo['BaseRequest']['Sid'] = cookies["wxsid"]
    friends=itchat.get_friends(update=True)
    friends[0]
    fp=open('friend.cvs','w',newline='',encoding='utf-8')
    writer = csvs.writer(fp)

    writer.writerow(['nickname','sex','province','city','signature'])
    for friend in friends[1:]:
        writer.writerow([friend['nickname'],friend['sex'],friend['province'],friend['city'],friend['signature']])
    return friends

print(get_data())