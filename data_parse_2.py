#(Network IP, country code)로 이뤄진 csv파일을 읽어와서
#(country code, country name) csv 파일과 비교하여
#(Network IP, country name) csv 파일을 생성

import csv

#(Network IP, country code)로 이뤄진 csv파일
ip_locationID = open('GeoLite2-Country-Blocks-IPv4.csv','r')

#(country code, country name)로 이뤄진 csv 파일
locationID_code = open('GeoLite2-Country-Locations-en.csv','r')

ip_locationID_r = csv.reader(ip_locationID)
locationID_code_r = csv.reader(locationID_code)

ip_locationID_list = list()
locationID_code_list = list()

f_1 = open('networkIP_countryName.csv','w', newline='')
wr_1 = csv.writer(f_1)

for data in ip_locationID_r:
    ip_locationID_list.append(data)

for data in locationID_code_r:
    locationID_code_list.append(data)

for line in ip_locationID_list:
        for code in locationID_code_list:
            if(code[0] == line[1]):
                tmp = [line[0],code[1]]
                wr_1.writerow(tmp)
                break
        print("I'm working hard...")
