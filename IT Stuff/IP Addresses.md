[[IT Stuff]] 


## What is an IP Address?

An IP address represents an Internet Protocol address. A unique address that identifies the device over the network. It is almost like a set of rules governing the structure of data sent over the Internet or through a local network. An IP address helps the Internet to distinguish between different routers, computers, and websites. It serves as a specific machine identifier in a specific network and helps to improve visual communication between source and destination.

IP addresses play a crucial role in the transfer of data across networks, such as the Internet. However, they themselves do not transfer data. Instead, they function as unique identifiers that enable devices to locate and communicate with each other in a network.

IP address is divided into two parts: X1. X2. X3. X4  
1. [X1. X2. X3] is the Network ID  
2. [X4] is the Host ID  
  
Example IP Address****: 192.168.1.15****  
Here’s how the parts are divided based on your format:  
  
1. ****Network ID****: `192.168.1` (This corresponds to `[X1.X2.X3]`)  
****2. Host ID****: `15` (This corresponds to `[X4]`)

1. ****Network ID:**** The left-hand IP address part identifies the specific network where the device is located. In a normal home network, where the device has an IP address of 192.168.1.32, the 192.168.1 part of the address will be the network ID. Filling in the last part that is not zero is customary, so the device’s network ID is 192.168.1.0.
2. ****Hosting ID:**** The host ID is part of the IP address that was not taken by the network ID. Identifies a specific device (in the [TCP / IP](https://www.geeksforgeeks.org/tcp-ip-model/) world, we call devices “host”) in that network. Continuing with our example of the IP address 192.168.1.32, the host ID will be 32- the unique host ID on the 192.168.1.0 network.

### ****The version of The IP Address****

Currently, there are 2 versions of IP addresses in use i.e IPV4 and IPV6

1. [****IPV4****](https://www.geeksforgeeks.org/what-is-ipv4/) ****(Internet Protocol Version 4):**** It is the first version of the Internet Protocol address. The address size of IPV4 is a 32-bit number. In this version, Internet Protocol Security ([IPSec](https://www.geeksforgeeks.org/ip-security-ipsec/)) for network security is optional. It has 4,294,967,296 addresses, but we are still seeing a shortage in network addresses as the use of network and virtual devices is increasing rapidly.
2. [****IPV6****](https://www.geeksforgeeks.org/internet-protocol-version-6-ipv6/) ****(Internet Protocol Version 6):**** It is the recent version of the Internet Protocol address. The address size of IPV6 is 128-bit number. In this Internet Protocol Security (IPSec) with respect to network security is mandatory. It allows 3.4 x 10^38 unique IP addresses which seems to be more than sufficient to support trillions of internet devices present now or coming in future.

## ****Types of IP Addresses****

There are 4 types of IP Addresses- Public, Private, Fixed, and Dynamic. Among them, public and private addresses are derived from their local network location, which should be used within the network while public IP is used offline.

- ****Public IP address:**** A [public IP address](https://www.geeksforgeeks.org/what-is-public-ip-address/) is an Internet Protocol address, encrypted by various servers/devices. That’s when you connect these devices with your internet connection. This is the same IP address we show on our homepage. So why the second page, well, not all people speak the IP language. We want to make it as easy as possible for everyone to get the information they need. Some even call this their external IP address. A public Internet Protocol address is an Internet Protocol address accessed over the Internet. Like the postal address used to deliver mail to your home, the public Internet Protocol address is a different international Internet Protocol address assigned to a computer device. The web server, email server, and any server device that has direct access to the Internet are those who will enter the public Internet Protocol address. Internet Address Protocol is unique worldwide and is only supplied with a unique device.

- ****Private IP address:**** Everything that connects to your Internet network has a [private IP address](https://www.geeksforgeeks.org/private-ip-addresses-in-networking/). This includes computers, smartphones, tablets and Bluetooth-enabled devices such as speakers, printers, or smart TVs. With the growth in IoT devices, the number of private IP addresses we have at home is also increasing. Routers need a way to identify these problem separately, and most things need a way to know each other. Therefore, ****routers generates private IP addresses that are unique identifiers for each device that separates the network****.

![Types-of-IP-Addresses](https://media.geeksforgeeks.org/wp-content/uploads/20241111150516907732/Types-of-IP-Address.png)

Types of IP Addresses

- ****Static IP Address:**** A [static IP address](https://www.geeksforgeeks.org/advantages-and-disadvantages-of-static-ip/) is an invalid IP address. Conversely, a dynamic IP address will be provided by the [Dynamic Host Configuration Protocol](https://www.geeksforgeeks.org/dynamic-host-configuration-protocol-dhcp/) (DHCP) server, which can change. The Static IP address does not change but can be changed as part of normal network management.  
    Static IP addresses are incompatible, given once, remain the same over the years. This type of IP also helps you get more information about the device.

- ****Dynamic IP address:**** It means constant change. A [dynamic IP address](https://www.geeksforgeeks.org/what-is-a-dynamic-ip-address/) changes from time to time and is not always the same. If you have a live cable or DSL service, you may have a strong IP address. Internet Service Providers provide customers with dynamic IP addresses because they are too expensive. Instead of one permanent IP address, your IP address is taken out of the address pool and assigned to you. After a few days, weeks, or sometimes even months, that number is returned to the lake and given a new number. Most ISPs will not provide a static IP address to customers who live there and when they do, they are usually more expensive. Dynamic IP addresses are annoying, but with the right software, you can navigate easily and for free.