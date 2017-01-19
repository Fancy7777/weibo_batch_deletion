
import requests
import re
headers={'Referer':'your own referer','Cookie':'your own cookie'}
while 1==1:
    t=requests.get('your own referer',headers=headers).text
    idx=re.findall('<a name=(.*?) ',t,re.S)
    for x in idx:
		print x
		datax={'mid':x}
		html=requests.post('your own referer',data=datax,headers=headers).text
		print html
