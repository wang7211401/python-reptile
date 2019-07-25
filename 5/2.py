import csv

with open('data.csv','a',encoding='utf-8') as csvfile:
    # writer = csv.writer(csvfile)
    # writer.writerow(['id','name','age'])
    # writer.writerows([['10001','Mike',20],['10002','Bob',22],['10003','Jordan',22]])
    # writer.writerow(['10002','Bob',22])
    # writer.writerow(['10003','Jordan',22])

    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    # writer.writeheader()
    # writer.writerow({'id':'10001','name':'Mike','age':20})
    # writer.writerow({'id':'10002','name':'Bob','age':22})
    # writer.writerow({'id':'10003','name':'Jordan','age':21})
    # writer.writerow({'id':'10004','name':'Durant','age':22})
    writer.writerow({'id':'10005','name':'王伟','age':22})