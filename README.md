# **Cisco-DNA-Inventory**

## 1. Introduction
Cisco DNA Inventory prints the inventory of a Cisco DNA controller to a table within a CLI. Tested for Cisco DNA 2.2.2.0.

## 2. Usage

### 2.1 Additional installation
```
pip install requests
pip install prettytable
```

### 2.2 How to use within the CLI
```
python extract_cisco_dna.py -n "<cisco DNA Controller IP or DNS>" -u "<username>" -p "<strong_pw>"
```

## 3. Output
The script generates the following output:
```
venv) C:\Users\tom\PycharmProjects\DNA-Controller>python extract_cisco_dna.py -n "<cisco_dna_Controller>" -u "<username>" -p "<strong_pw>"
Script is created by Remote Syslog
Running from directory:  C:\Users\tom\PycharmProjects\DNA-Controller
Started session on: dnac.remotesyslog.com
Started session with user: tom
+--------------------+--------------------------+---------------+------------------+------------------------+--------------------------+--------------------+
|      Hostname      |       Platform Id        | Software Type | Software Version |        Up Time         |        Serial Nu         |      MGMT IP       |
+--------------------+--------------------------+---------------+------------------+------------------------+--------------------------+--------------------+
|     12345TEST      |    AIR-CAP3702I-E-K9     |      None     |    17.3.3.26     | 38 days, 12:16:57.040  |       FCZ1767P1F0        |     10.172.0.1     |
|  AP075000-RS3000   |        C9120AXI-E        |      None     |    17.3.3.26     | 35 days, 22:03:33.040  |       FVC2452P2T4        |     10.172.0.2     |
+--------------------+--------------------------+---------------+------------------+------------------------+--------------------------+--------------------+
```

## 4. Donation

Crypto:

```
XRP/Ripple: rHdkpJr3qYqBYY3y3S9ZMr4cFGpgP1eM6B
BTC/Bitcoin: 1JVmexqGBQyGv9fVkSynHapi2U6ZCyjTUJ
LTC/Litecoin Segwit: MAH8ATCK6X7biiTQrW7jUZ6L9eg1YBo5qS
ETH/Ethereum: 0xd617391076F9bEa628f657606DEAB7a189199AF5
```
PayPal:

[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KQKRPDQYHYR7W&currency_code=EUR&source=url)

## 5. Help

To improve the code and functions we like to have you help. Send your idea or code to: info@remotesyslog.com or create a pull request. We will review it and add it to this project.

## 6. License
"Cisco DNA Inventory" is a free application what can be used to control the Cisco DNA Controller and extract device information.

Copyright (C) 2021 Tom Slenter

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

For more information contact the author:

Name author: Tom Slenter

E-mail: info@remotesyslog.com

## 7. Used resources
https://blogs.cisco.com/developer/python-scripting-apis
