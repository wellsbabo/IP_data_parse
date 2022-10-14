import ipaddress
import csv

original_ASN_info_file = open('GeoLite2-ASN-Blocks-IPv4.csv','r')
original_ASN_info_data = csv.reader(original_ASN_info_file)

f = open('test.csv','w', newline='')
wr = csv.writer(f)

#test = list(ipaddress.ip_network('1.0.0.0/24').hosts())

for line in original_ASN_info_data:
    try:
        ip = line[0]
        ASN = line[1]
        #wr.writerow(ip)
        ipList = list(ipaddress.ip_network(ip).hosts())
        for ip in ipList:
            #print(ASN)
            tmp = [ip.compressed,ASN]
            print(tmp)
    except:
        print("error")

#print(test)
