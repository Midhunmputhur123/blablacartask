# -*- coding: utf-8 -*-

# Scrapy settings for blablacar project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'blablacar'

SPIDER_MODULES = ['blablacar.spiders']
NEWSPIDER_MODULE = 'blablacar.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'blablacar (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12 Version/12.16',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML like Gecko) Chrome/26.0.1410.64 Safari/537.31',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.125 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/30.0.1599.101 Safari/537.36',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/27.0.1453.110 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.103 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/33.0.1750.154 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/38.0.2125.111 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.103 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.114 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.77.4 (KHTML like Gecko) Version/7.0.5 Safari/537.77.4',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.78.2 (KHTML like Gecko) Version/7.0.6 Safari/537.78.2',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML like Gecko) Chrome/21.0.1180.89 Safari/537.1',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.57 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.124 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.103 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:16.0) Gecko/20100101 Firefox/16.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML like Gecko) Chrome/26.0.1410.64 Safari/537.31',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML like Gecko) Chrome/26.0.1410.64 Safari/537.31',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.94 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x8664; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x8664; rv:32.0) Gecko/20100101 Firefox/32.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.125 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/32.0.1700.107 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
'Mozilla/5.0 (X11; Linux x8664) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Mozilla/5.0 (X11; Linux x8664) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.94 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/28.0.1500.95 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:26.0) Gecko/20100101 Firefox/26.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1010) AppleWebKit/600.1.8 (KHTML like Gecko) Version/8.0 Safari/600.1.8',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
'Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20100101 Firefox/12.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/34.0.1847.116 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/30.0.1599.101 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.97 Safari/537.11',
'Mozilla/5.0 (Windows NT 5.1; rv:27.0) Gecko/20100101 Firefox/27.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/27.0.1453.116 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0',
'Mozilla/5.0 (Windows NT 5.1; rv:22.0) Gecko/20100101 Firefox/22.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
'Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0',
'Mozilla/5.0 (Windows NT 5.1; rv:19.0) Gecko/20100101 Firefox/19.0',
'Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/30.0.1599.101 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/34.0.1847.131 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/28.0.1500.72 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/33.0.1750.154 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0',
'Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0',
'Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.114 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/29.0.1547.66 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0',
'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/29.0.1547.76 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0',
'Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.94 Safari/537.4',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
'Mozilla/5.0 (Windows NT 6.1; rv:16.0) Gecko/20100101 Firefox/16.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.97 Safari/537.11',
'Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/30.0.1599.69 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/29.0.1547.76 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML like Gecko) Chrome/25.0.1364.172 Safari/537.22',
'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/29.0.1547.76 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20100101 Firefox/22.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.57 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/27.0.1453.116 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:28.0) Gecko/20100101 Firefox/28.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/39.0.2171.71 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/28.0.1500.72 Safari/537.36',
'Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/33.0.1750.146 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:23.0) Gecko/20100101 Firefox/23.0']

PROXY_LIST = ['190.194.220.213:8080',
'209.97.164.113:8000',
'186.155.241.150:65301',
'185.61.183.113:8080',
'106.104.12.222:80',
'185.114.246.63:53281',
'109.233.23.178:8080',
'51.38.114.104:3128',
'185.213.165.136:8080',
'201.32.25.10:8080',
'77.68.91.22:3128',
'181.112.221.182:53281',
'200.187.87.138:20183',
'187.110.227.154:3130',
'36.66.55.181:8080',
'129.146.70.253:80',
'54.39.46.86:3128',
'77.55.217.220:3128',
'212.72.150.51:8081',
'187.102.68.145:20183',
'186.211.4.135:20183',
'89.23.18.29:53281',
'190.52.169.233:8080',
'177.47.225.157:20183',
'2.177.234.190:3128',
'189.76.93.53:20183',
'90.45.26.244:80',
'185.139.92.16:8080',
'41.164.168.174:8080',
'144.217.165.155:3128',
'168.253.201.19:53281',
'200.115.28.129:8080',
'195.88.208.115:3128',
'36.67.252.18:8080',
'213.6.198.2:8080',
'45.125.221.242:8080',
'80.211.225.28:8888',
'192.241.134.221:3128',
'216.198.170.70:8080',
'54.36.65.224:3128',
'163.172.122.68:80',
'167.99.5.127:8080',
'138.94.161.120:20183',
'5.152.158.4:8080',
'37.233.59.6:8080',
'209.222.86.48:8080',
'13.127.94.56:80',
'103.255.123.38:8080',
'37.187.99.146:3128',
'195.239.103.238:3128',
'167.114.211.122:3128',
'150.95.175.44:11014',
'213.138.103.117:8080',
'167.99.71.183:3128',
'117.74.125.192:8088',
'187.21.238.185:8080',
'187.110.93.120:20183',
'142.44.247.60:80',
'201.236.161.171:8080',
'128.70.172.67:8080',
'203.177.36.84:55555',
'180.183.67.200:8080',
'217.61.4.19:8080',
'89.42.228.10:8080',
'67.63.33.7:80',
'123.57.217.208:3128',
'212.237.51.47:3128',
'195.190.100.90:8090',
'89.37.0.68:8080',
'139.162.44.190:33228',
'52.203.60.247:80',
'34.225.249.169:80',
'202.131.233.202:53281',
'5.160.246.164:3128',
'18.221.232.80:3128',
'217.61.97.116:8080',
'123.231.236.147:8080',
'103.206.185.66:8080',
'155.93.108.170:8080',
'91.234.125.208:53281',
'82.112.202.202:8080',
'223.206.167.107:8080',
'103.228.117.244:8080',
'198.245.63.15:80',
'178.216.201.214:80',
'92.222.83.160:80',
'78.57.227.227:53281',
'201.150.255.185:3128',
'177.75.163.51:20183',
'124.108.17.21:8080',
'186.226.188.134:20183',
'201.76.180.174:20183',
'34.220.212.155:8080',
'31.173.188.162:3128',
'117.20.54.20:3128',
'171.25.245.126:53281',
'60.248.222.206:8080',
'173.212.209.59:80',
'80.122.84.246:8080',
'41.65.99.149:8080',
'41.90.98.246:8080',
'49.49.212.123:8080',
'212.116.103.82:8081',
'84.0.203.122:8080',
'165.16.32.1:8080',
'23.88.111.26:3128',
'77.82.237.248:8081',
'144.202.124.213:3128',
'186.93.226.242:8080',
'81.100.72.192:80',
'175.100.176.58:3128',
'39.104.75.54:8080',
'51.255.138.248:3128',
'1.179.174.2:8080',
'81.30.158.50:80',
'150.95.151.68:8181',
'121.41.171.223:3128',
'201.49.120.118:20183',
'202.173.214.39:8080',
'125.209.74.106:80',
'187.33.236.146:20183',
'72.222.130.57:53281',
'88.119.139.237:53281',
'159.255.163.178:80',
'36.78.27.51:8080',
'34.201.72.254:80',
'39.104.64.5:8080',
'43.228.182.227:3128',
'193.106.25.27:53281',
'177.22.107.86:8080',
'88.211.126.138:8080',
'187.95.98.162:3128',
'51.254.132.238:80',
'52.37.235.219:8080',
'187.114.185.224:20183',
'113.53.60.59:8080',
'78.46.194.98:3128',
'195.234.87.211:53281',
'167.99.235.248:3128',
'91.67.222.183:80',
'77.68.91.36:3128',
'194.169.206.141:8080',
'178.217.33.134:53281',
'45.120.88.200:8080',
'180.183.18.84:8080',
'51.15.227.220:3128',
'88.205.156.3:53281',
'194.182.72.223:3128',
'54.38.156.250:8080',
'144.217.105.153:80',
'165.227.191.45:80',
'220.229.67.58:3128',
'111.67.74.54:80',
'151.80.58.175:80',
'187.18.113.159:20183',
'206.189.38.152:3128',
'176.9.196.29:3128',
'177.64.53.21:3128',
'93.126.28.20:53281',
'94.177.233.135:3128',
'52.37.106.31:8080',
'5.235.84.59:8080',
'117.102.224.10:8080',
'139.255.69.148:3128',
'180.183.99.189:8080',
'216.158.241.244:8080',
'31.220.183.217:53281',
'208.65.66.155:8080',
'179.106.52.42:8080',
'111.251.26.134:3128',
'178.60.28.98:9999',
'177.43.41.140:20183',
'162.213.3.155:4444',
'217.61.7.172:80',
'177.154.56.45:8080',
'173.249.53.29:3128',
'45.115.55.104:8080',
'114.199.125.242:80',
'109.196.34.51:8080',
'62.213.87.171:8080',
'187.44.255.234:20183',
'91.225.190.38:53281',
'206.189.211.197:8080',
'69.164.205.111:10000',
'36.231.112.45:8080',
'113.53.57.27:8080',
'84.22.61.46:53281',
'47.74.9.208:3128',
'52.58.193.142:8080',
'185.6.197.82:3128',
'201.48.254.162:20183',
'210.212.210.99:8888',
'91.237.240.14:8080',
'51.15.147.94:80',
'51.38.233.169:80',
'202.74.243.112:8080',
'31.25.141.148:8080',
'93.90.178.97:80',
'223.27.151.100:8080',
'37.59.115.136:3128',
'103.16.61.134:8080',
'176.120.213.193:53281',
'202.94.164.94:8080',
'180.250.76.61:8080',
'103.248.248.235:53281',
'79.137.85.204:80',
'200.24.159.133:8080',
'177.22.127.82:8080',
'189.51.126.12:20183',
'41.77.128.18:53005',
'193.70.81.83:3128',
'103.105.228.102:8080',
'77.236.251.234:8080',
'177.21.102.55:20183',
'188.233.187.195:8080',
'187.45.123.167:3128',
'159.203.174.2:3128',
'24.245.100.212:48678',
'168.205.87.12:8080',
'187.95.236.240:20183',
'188.235.211.202:8080',
'183.89.89.14:8080',
'167.99.73.241:3128',
'167.114.185.238:3128',
'187.72.194.145:20183',
'182.253.35.239:8080',
'200.132.54.1:3128',
'14.143.47.178:3128',
'1.20.169.90:8080',
'173.249.38.68:3128',
'83.18.150.53:3128',
'163.172.181.29:80',
'103.254.94.70:8080',
'92.241.15.86:8080',
'46.73.33.253:8080',
'79.143.85.36:8888',
'186.194.64.162:20183',
'39.104.81.203:8080',
'110.232.76.247:8080',
'94.130.92.40:3128',
'61.136.163.244:3128',
'14.192.144.99:8080',
'103.230.6.10:8080',
'125.25.150.47:8080',
'80.229.84.33:80',
'86.105.51.105:3128',
'188.232.183.166:53281',
'213.87.101.187:8080',
'52.67.32.10:80',
'200.53.18.229:20183',
'14.207.127.237:8080',
'94.232.57.117:8080',
'178.239.168.57:8080',
'20.190.62.68:80',
'148.153.1.78:3128',
'45.123.43.138:8080',
'118.172.131.245:8080',
'178.162.203.97:3128',
'13.92.196.150:8080',
'81.14.205.231:8000',
'46.42.63.209:53281',
'14.207.69.84:8080',
'1.0.191.26:8080',
'62.176.1.191:8080',
'103.48.59.206:8080',
'35.182.167.62:3130',
'104.167.2.206:80',
'47.91.223.245:80',
'125.164.90.128:80',
'176.227.188.66:53281',
'35.188.79.43:80',
'39.104.79.89:8080',
'149.28.236.29:8080',
'83.238.100.226:3128',
'62.33.79.1:3129',
'54.39.20.167:3128',
'194.60.238.6:53281',
'91.194.42.51:80',
'85.15.179.5:8080',
'37.235.54.184:80',
'200.195.26.234:8080',
'82.209.219.118:3128',
'1.0.134.163:8080',
'185.156.214.34:80',
'170.254.251.121:8080',
'39.104.48.39:8080',
'217.91.90.46:53281',
'186.236.237.143:20183',
'109.167.215.233:3128',
'118.174.93.111:8080',
'189.8.89.250:20183',
'202.154.190.234:8080',
'46.98.144.125:53281',
'78.186.217.197:8080',
'183.89.40.130:8080',
'204.13.232.124:5836',
'76.190.78.10:3128',
'42.61.52.115:3128',
'159.253.80.242:8080',
'51.15.121.195:3128'
]

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.blablacar.in',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'blablacar.middlewares.BlablacarSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'blablacar.middlewares.BlablacarDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'blablacar.pipelines.BlablacarPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
RETRY_HTTP_CODES = [403,429]
RETRY_TIMES = 20