#(Network IP, country name) csv 파일을 가져와서
#ipaddress 모듈의 함수를 통해 
#Network IP를 host IP로 변환

import ipaddress
import csv

networkIP_countryName = open('networkIP_countryName.csv','r')

networkIP_countryName_r = csv.reader(networkIP_countryName)


networkIP_countryName_list = list()

f_1 = open('IP_countryName.csv','w', newline='')
wr_1 = csv.writer(f_1)

IP_countryName = list()

for data in networkIP_countryName_r:
    networkIP_countryName_list.append(data)

####################

for line in networkIP_countryName_list:
    try:
        ipList = list(ipaddress.ip_network(line[0]).hosts())
        for ip in ipList:
            tmp = [ip.compressed,line[1]]
            wr_1.writerow(tmp)

    except:
        print("error")
