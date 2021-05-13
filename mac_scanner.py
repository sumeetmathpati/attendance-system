import arpreq

mac_list = []
for i in range(1, 255):
    request_mac = arpreq.arpreq(f'192.168.0.{i}')
    # print(f'192.168.0.{i} ' + str(request_mac))
    if request_mac:
        mac_list.append(f'192.168.0.{i} ' + str(request_mac))
