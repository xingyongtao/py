#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2, json
import smtplib
from datetime import timedelta, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "yongtaoxing@yunrang.com"
#toaddrs = "yongtaoxing@yunrang.com".split("; ")
toaddrs = "yongtaoxing@yunrang.com; quj@yunrang.com; peilv@yunrang.com".split("; ")
date = datetime.today().strftime("%Y%m%d %H:%M")

auth_handler = urllib2.HTTPBasicAuthHandler()
#auth_handler.add_password(realm='RabbitMQ Management', uri = 'http://10.21.126.35:15672', user='guest', passwd='guest')
auth_handler.add_password(realm='RabbitMQ Management', uri = 'http://10.21.126.35:15672', user='yrservice', passwd='1101110_!@#')
opener = urllib2.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib2.install_opener(opener)
yrads_log_all = 'http://10.21.126.35:15672/api/queues/ads_servicelog_host/yrads_log_all'
f=urllib2.urlopen(yrads_log_all)
str_data = f.read()
json_data = json.loads(str_data)
msg = date + '\n' + yrads_log_all
msg += '\n\tmessages_ready: %d' % json_data['messages_ready']
msg += '\n\tmessages_unacknowledged: %d' % json_data['messages_unacknowledged']
msg += '\n\ttotal: %d' % json_data['messages']
ads_log_realtime = 'http://10.21.126.35:15672/api/queues/ads_servicelog_host/yrads_log_realtime'
f=urllib2.urlopen(ads_log_realtime)
str_data = f.read()
json_data = json.loads(str_data)
msg += '\n' + ads_log_realtime
msg += '\n\tmessages_ready: %d' % json_data['messages_ready']
msg += '\n\tmessages_unacknowledged: %d' % json_data['messages_unacknowledged']
msg += '\n\ttotal: %d' % json_data['messages']
print msg

content = MIMEText(msg)
content['Subject'] = "MQ消息数量监控邮件 " + date
content['From'] = fromaddr
content['To'] = ";".join(toaddrs)
server = smtplib.SMTP('10.21.130.11')
#server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, content.as_string())
server.quit()
