from __future__ import annotations

from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUX9kvHEjir5fniTg3GRQ8wO7zOvAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDczMTAyMDgxNVoXDTMyMDcy
ODAyMDgxNVowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAykxn/RsW32xbKhz4CFSnngEwji+mbyOREJihRy/2ydPI
dQ1vgMJdgatf3GUr49imIYu4r1PfvvLTHCCXLjbW4zk8K+Tf+gGfnm/rjvGvwO7I
J7qZj2slknkZAqq0jhVKkt+xkM4A3fbk6cy2DC+2w2se20fKvPa8Nwgt1GzBGpN4
ditUWZwhVz3Q+4QMnZTEiKkfkKBYlJntheIiLPTReDiHUlMIfl1kBqYZqLmX3lsS
J29o73BMyjNhQBMKe5F6TIcYeIME5H/DAKCfS6JR3HGMj1aqeunqVZ+Wacs+HOtD
hHLrSsCwMa1XVzPPNV1on7JekgSpEXTd9DEtpHO5TQIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQAk7pLuj7tqbztCXhLMD5TqIfml
HB3K1nOKwNEIJ29J8Xc6lKUMB/z3UFVmPPuuHW3FBXsrf1ZcZLaTNZuY2304yURV
uzpH5GAivGwSbXmccOee1HV8Rrvii/Gd8c2qdxBsypaiMaNAOCOUHqfGAQCWRefO
/8rn8TmXWikNFL2YygcR+XI5jWTAF6LoXCxV0y48X4Kg7G7s5QHDqnHYhakfAtyO
9KpUPODd3UIZoW5k8A0vn0xwrvyqwNhCTHOkt178jCiqCR1b3jnvmVHTw1rIOnXE
rhdGfc4ywMBp+Rv8hFZM0RPmt+aDy+O2XvdPqFCky6R4+l8RtlYP242urN8q
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAykxn/RsW32xbKhz4CFSnngEwji+mbyOREJihRy/2ydPIdQ1v
gMJdgatf3GUr49imIYu4r1PfvvLTHCCXLjbW4zk8K+Tf+gGfnm/rjvGvwO7IJ7qZ
j2slknkZAqq0jhVKkt+xkM4A3fbk6cy2DC+2w2se20fKvPa8Nwgt1GzBGpN4ditU
WZwhVz3Q+4QMnZTEiKkfkKBYlJntheIiLPTReDiHUlMIfl1kBqYZqLmX3lsSJ29o
73BMyjNhQBMKe5F6TIcYeIME5H/DAKCfS6JR3HGMj1aqeunqVZ+Wacs+HOtDhHLr
SsCwMa1XVzPPNV1on7JekgSpEXTd9DEtpHO5TQIDAQABAoIBAF6z1hqPC+4b87GL
TjHYL3+wXuKxO+DbbZWvXhDNS2LAWh8x4vkMBGonqACs/Bb13Q/nMNYjFaN2WY3Z
U+y2j3Jf4ONLie6nw+mPy15nljdjkR/IIwsYxcYEGsk80LmTDg4j2iRHy/AdHJy2
0KJz08M36oIM4cQEXagFlC7VmrCtc4fYktJQwxD1IzS7+9l+bgjYeZe6ItZS6AEo
CM/mDZxrjcPJRIRM6F5oeEqwGOpxnDQJB0H6QsA9dgF8rIzuJf8mWr2pk9RfS/E6
2KRDyW3Hpk4O1Cd5urKA/yuc5UBdWyhhozh03snG74M2rMrNPwmq4a9cMrWOBDhy
fzlOFKECgYEA7CipWGKjp/haF9rsxeSpsfE8g6d61geJ9Sbsl3MbvIO+9Wi9eigo
O/kWmlUG/rFE5g/rjmgXldGkVoMdVb+oeLVbvp2JSntIFJBKUWHgLGk7jJVx9EAI
3ocYWxqelJL5xPGU52cRX/0ETOwo59w8UWjUeeQwScT10kNf7sP573cCgYEA20t4
jLqphsYWwUFwwSthspsbru8OdWWQJqn9ZwNrfkWBBzQ5CHMIhq6QLP5RCpG63Vef
INylG65kzTM5i0RD5nHAQzFAeXoUf+g8lq6T58G0Q3uvsOdjVLusRBUQnljbkeJl
ww3fUMBC1Iex687urSblir5ExJ26tWQg0ZHLtlsCgYEAtIHb9ufmaaRF0MgQhK5k
GtPmSkdAd8npZA3td1GPmMcmtdPqSC3bmwOoiCyHnTOIE0WF6iKcLHLCZzHuwTUu
o50T1B3764dRsA4eEBh8zdVdo/Yy1NwBK34dWr19CtlQun1hMIKyYCk4GUfFeHv5
SsyS49xMIIbA0oeXExyOtL8CgYBGJsWAl3IF2DaNSgbs9JjDTxUzB+xjJ8NOaxDS
NGjdsxRMnqskBdCTbSJYEl8Qd4AEsLQKCiuTSF2cuydMYuEpxffQRuAuPBx0snE3
bs+H0xJ8iAOzHsJK5+J6wRZY4WoUKA2PsU9gALEgVexX2BHIOGoz0RwknaSNxGMv
R2mYgwKBgQC33VmlG+adWfH5yaOj5twnrETUqs+ehc0O8qoNmn+Ueop+AHgI7lY6
tkkf+ZKkyT4nJz0VRZuVL+jYFq1UeaY2m+fO7mg2AOWl2zWH2UaY+vlh2mAYpXiC
26qkyxUI5VRyVyQ7g7NtbSJGlzMXDVxzHI6jliR8YKuLOEsiRECQDg==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUJxG4nRreZqpC8YFg4bfgBgnjp8gwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQD7zuyb/gcsWCWbuLrEJSjVJWSOAP3YYVEnUIR949nIE+xS
32Z01a2/y4lcUf1DoB2ADYv4LqSrHnBasgznXJHYWPNRQX5hOGeJzC0Gb8B4MEWF
7gPC+v6//GXytGl2fg5GyGHDbKT33f6c1TaJXY4P2iummoFNoOX13EzyYEWXeBC1
L9p8+fkpSC1C1eCwRQdzrghqagP06kt4gpO2OSJ0xtBX5fz8NY4pZ2CP33nyG8S+
yTJLZweWMFnueUL3b9JJgticr8RteyrKOGoVhcFnymw3GnsbGZURUxp/yXM67ovN
Ud487CNHHOJl3gDK69LcALOMZAHS5Q0ZQECpPWSxAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCOzjCPbMEDx1Q1XJyJDF8l
c2z0Tk3xhlGY1PnaARt4xNHh5gFodCeFTb+f9Ywoy0cYQ67PRZyLgDyuRKp8T4+z
wgWmG4NmvMKO+9h4F76+VGqYX7Oc5QADPF+hJrAWUNNEN+NbUpDp+W8E1aUzkIBE
HK2aNM7PAapereWXyR+U/mUXrOtiecBD72g0zS4hp++Uxn3uEaQobBc1EaT/GS/x
HWy2tmWaczUf5TydC44lF8NZCuMm89ldF+Qmz8b30ON2OsFzr/2WVVaj+k+j0MsQ
+Urzepx4+8NnlBGwgAyzlA1nEoDIsKMqUyBQlqv7cSFh2m05q7UrAUk/nFw+tNOP
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA+87sm/4HLFglm7i6xCUo1SVkjgD92GFRJ1CEfePZyBPsUt9m
dNWtv8uJXFH9Q6AdgA2L+C6kqx5wWrIM51yR2FjzUUF+YThnicwtBm/AeDBFhe4D
wvr+v/xl8rRpdn4ORshhw2yk993+nNU2iV2OD9orppqBTaDl9dxM8mBFl3gQtS/a
fPn5KUgtQtXgsEUHc64IamoD9OpLeIKTtjkidMbQV+X8/DWOKWdgj9958hvEvsky
S2cHljBZ7nlC92/SSYLYnK/EbXsqyjhqFYXBZ8psNxp7GxmVEVMaf8lzOu6LzVHe
POwjRxziZd4AyuvS3ACzjGQB0uUNGUBAqT1ksQIDAQABAoIBABnN7rldouaMce4v
VBRdqn2NQ2y59UmDT4mz2p/8BYlXYVRsyFcYvqF0/jKTxFx1wBArUzivrvhKOkFR
Fblv5xJAq06cY5Ma8KFSZxrNwO+QIs/CwGfuyMRr3RauHlCiQlxGlJ4uOAmemkUA
JIKXL8O4G9kK5E1MO8SiOtBrxTXsR+BztpMUEw/gltjSd/h8AflnkmLjGVG/G4/z
XMALCeZqhR9G9lCsTJtAStLA5z8Atho6R/VSj2WwfOxm8y1GfyWYRP0QZgAR9QDm
wbarjp4QCgGHS7KAaFbW2yyrvDFwZgUzLirI1Qr3JGqGMeaaGnwQ1aWXEGn6tY6t
H8U3oEECgYEA/iAdgpaCYSKAtv0fLlSGxyjpFLbf1GRXt3Mb75/zLxMEHBpvU9b2
cMB+TDlCJNFZwv0glSJN4S6iPBf3VWb4KMd+2BMBRkcynKSS9DD58C478qrxsyGW
BtpBVjg/reJ853VW30CdfRHk87vAMDeicnLVAGs9Gj2xxVkO9wVXzwUCgYEA/apu
7kiO1ybPvn132SBHr9j3bZXATi3oN6i9N9rRPFxBbPeg1a5fFc2o9lZ499Gga8PH
VHJXVL8UCiKYgoVF8LVrvKMXbdE0sWlaWEJEkFzUJtkbnzI6t95cjbZtOcoDRecb
CgqGdeHPNTIFjjhCx2YlsCPejn/jQBMI8R4Mtr0CgYEApGPsEx0ADIwATd+iexsM
8OsDFHZUhxW+NJsPGE0VSH95qiBjog2t8DRlvzNPGXggI+YRXMgLLz82jb9HLYTl
xaN/55ErwuWt1O0Vb0f7dybBevKgVivE3Hv1xiuu7fJUsHoUj2lCN7UKsazj340t
1fF43sOAjGgahrpc1ukq620CgYAHlhlLNxBOjvKXl9kFvVlngO2lcV0W+XiAcaN3
ECxByeCLCbzdpyFg3Y24EE39218Y2foUJHdIKY7H3tEA1kuJL2PReG8y8ZbJ14TE
Lvct+hi+MLAKys3GwfeypUoO+GOwq4C7hCURUXeI974Cytv0arGl2uzFBj4dpHQY
AfYPYQKBgQDpeXIsbEfBF5h0KjLmU+4lk8OK1MsiB+UWUR61g/hl90tEWvsGNMCQ
T87fzHmiVuDrU4B0KUFgH1kfQtqPu8VMAO2mrsBoNjFRfIkkUjkgpKQ3zTPgBWUN
xzIOwhFaj7sqSxlJKhp70ENopk1jv3uGSnYw+B+7qyuPePo7gcLwsw==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUH+vOBpWm7GZBImUetpmvvngiuUQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDSMjjzEEqoICoK7gBXrUhkhzVLmNnPxTpod32QWSpnSR9/
R81bPlxoaWixzYfNnAntIOr6txh82sd3lPqT45zT/Ji7iTkcbmh10Kw2YMPb1+cM
GAy3x/K+ASUMP911J/4E+4jFqodY7EccfxbnZir/U7IktqllciPZoDC5Dvf5YtJZ
ZJLITRaAnoA66OC/cUWjxbzOGGPt9bJNbQXlgHGmJx6D9vaUE3hnIm03HpO+74S0
S54b4TI0R3H+fuU1jxgMuCHACcQTKpZRi5h4QT8QQJXoL/70dDG0DNFsI5RIEgf4
KS6wowbJLdqpZpeW4Sh513/xQYeEsIWgFnV6ZM3hAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAJKLQAkQBXoI8LJ0GRpLT+
wwdqXt1xdrLwyRI2Vf5hrxkRtYuvmXUjHrI/HxlIvapVUns2W9g9b2Eim/mb7FNJ
jztgEEP4V2OjbTOJOiqZakFA2te6FIlV4otaj6GOMwuCt8q2L+0m/KfHzLQYqn3X
YGUi9TQMMvJjVHmuZfEbVEKiNjjrT1DVE6YOQQBZKCCyTQccMXQSGwogtJOf3EH7
ruOiBExxyAFdntsE3VjSCD7U/jA2pnXD1KutI2o0g0bO1twuz7EzVLZFJNey0BUB
HtXDTP5TCJpf3lybcssjdiDnfARXUMTN2ka5WXgvebDwb1pqmuDlrVrA8UmqTYcy
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA0jI48xBKqCAqCu4AV61IZIc1S5jZz8U6aHd9kFkqZ0kff0fN
Wz5caGlosc2HzZwJ7SDq+rcYfNrHd5T6k+Oc0/yYu4k5HG5oddCsNmDD29fnDBgM
t8fyvgElDD/ddSf+BPuIxaqHWOxHHH8W52Yq/1OyJLasXIYj2aAwuQ73+WLSWWSS
yE0WgJ6AOujgv3FFo8W8zhhj7fWyTW0F5YBxpiceg/b2lBN4ZyJtNx6Tvu+EtEue
G+EyNEdx/n7lNY8YDLghwAnEEyqWUYuYeEE/EECV6C/+9HQxtAzRbCOUSBIH+Cku
sKMGyS3aqWaXluEoedd/8UGHhLCFoBZ1emTN4QIDAQABAoIBAFHwmhrG4xOfVkRk
e2Wye2IVA0WxFFfWfupyilRXLhyNeOXZS8iiCsv5K4MEqEgS6Bu0lWWfMsCZWODZ
BsXYGS7abX/OAqF+uOIUss2P80okZEFmrq6GF67SK2sXCnG9YVz34V2NGK4ljaMi
N/+E6IYYTn3ZaF+5Owh/Vf8OQsTIeGcFqLd+kpozQz8luM9623LEq/YZlHqsaBNy
rF8RxnSjbYNzUPqsAFCxN+apEHfjuJiIM+dUIu2ZWH4FauwRZ/FbOaz2Cue2/gAk
zL0XhspQfP69cB7YppO6fu7Y6WcsM6rqXEoJMt3XIdWw9iAmaWnjRo0BONJnYIIB
5h+t+EECgYEA7YGMaaX8wRO5OGKKXx2y+UZzXO8H7dJ84Kf84M/NVt3pl7Icuw3S
NaVcIQgXk7AiIH7bMkwZ3De2HiD+aTA4SGfFOhLYYbsj2Ke3VpnCCUiHqpf9/5lX
StuLGXJgwfQ2hrG2NKB9CPTfR2tsaI1FngqJRNWnmWLsiRXs/1m2n6UCgYEA4pBH
RNvbmHlNW4qFd0dc84cgIAixhdESbGbscGuc2BpEo7rMHpsWYkEEib/9/ZpxrigL
QFP3fbrfGsuvxWUhYenv8tt9YT55t56oj0mXgCcfkxoPnnntguD+Q9inw53pbMMp
g/qwn8STMqM8KNqWMbtLBR2HCJbhqFrXfl5dYI0CgYBNiu9iCuyDyUG+1AVjWpn1
YvgFTpFjJ0bYPmCEsbPT+a3rdh6FP9Ty6OM0caTo9ieePmyodko3KQVPvuvxQeoO
UbsF4+M7vVLNyKxGHPtJ9qE8pFUsX08txJIco8hNasNmpJzdf8xy4SgI9Fy3ofAp
0jzQ+YS3wqGBfGQdVpgWdQKBgDKxpcC6kQAk5DI/ZG20AhBbg8ynJVGT3lNzFCRz
b7zK4+Dewx12BiQl+CX6V5KPJDCbtSjHoPD5B0KvoLzCTB3kglQM2JkRqZp0XbLx
/HwoROBdTHFhRsuqHDqCF8elZb14TanCRhL5oRYLgEKD5mdqSPb0DGrXl9ZbvSwB
YVNhAoGAYuY7HJRgnfwqAhdDagbPlJxL74f4VGG1MrWQ3LNQAK18vC7qem3MWoNN
ShcbfVoevcC66HBfqvKVLlRpf8n67zs5uOetxBRtA52888s1P456JsVaihTKo7Lr
DSmPIkttRAJAZAr/T+aLncA/x80bUaDskUbhDUVu3r3bxPieU68=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUHVa/b7E1IfWxhidTznNrmWBa8rEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDLKM3aHoUk41DT3hOcg4HMYIdu+p6iIchg/LxlzQW2QLAD
ALcqP/u+c+a2ogqpWUC5Ub2o20UgboUJ67XdfqdiC3fBZ4hFpd9fuy0RYYtbPtYX
3DQkqY7U2eauRW78qTKP3AtTuGy25PmwtrEEMHpWTeeg2D3AdG6MGiiSzQHkPW/S
5t9y7UzNIKKsr5sCKNmEmxde1g9z0Aa7oJPXRLr93Y2YkQcsszX6DC6Q69VnhgC9
4CFfqp6kRk7DUxunJfNh0cUN2vHIP+0ICCr4o3FUslldpJrFvCpq9oyBxY1Gonpx
KaPhxkPJRmGNTxoubffDqwW0IjfxTMgGdjb2ZkytAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBXWejEkaLjR2YNUnUddqq4
Y49FDEmprs8tBY6bmpaJpKMCwLbBYBSnxRODlV2Q8MITeZUNSOwLhi96vsYFKRdD
yvYRXkk/aBl5soFCT8ihDFvx4mGKRNux0ouHEVveVJ5RJcMFyGAbI4J/L7XHgbXW
PSuY1Zdtnn/Tg0mkPvl9z+TPluxgLUBIvdzQIzcYNsCVL+iNZzjnbfz9qtvWGNXs
63AWYpgl9TdIOUsa3biOl1ou9QS9t35LdNrKg1SMUHOcHyW6gFJI1d4l7XC9vwVN
z8YBWFgUNLUjSaW2N0Cv54XUQS7pAxo74x3R6t7u5QeIIc4JcsxO229bzGfYVGKD
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAyyjN2h6FJONQ094TnIOBzGCHbvqeoiHIYPy8Zc0FtkCwAwC3
Kj/7vnPmtqIKqVlAuVG9qNtFIG6FCeu13X6nYgt3wWeIRaXfX7stEWGLWz7WF9w0
JKmO1NnmrkVu/Kkyj9wLU7hstuT5sLaxBDB6Vk3noNg9wHRujBooks0B5D1v0ubf
cu1MzSCirK+bAijZhJsXXtYPc9AGu6CT10S6/d2NmJEHLLM1+gwukOvVZ4YAveAh
X6qepEZOw1MbpyXzYdHFDdrxyD/tCAgq+KNxVLJZXaSaxbwqavaMgcWNRqJ6cSmj
4cZDyUZhjU8aLm33w6sFtCI38UzIBnY29mZMrQIDAQABAoIBAGngsx+o5kTqPxab
12arVrsX151r+b6PkqmRLfJ0HjT0k4aNGehn/iAssSGfY6UMgeHTCt/0npsfXjBk
apyrxDohteDSvz9lCfwPRZaYWpNMNTGsLnSo9WpSwZkzUHtXBqXYzQJtzCKpRMPn
Amwng6p04XF/IPeq9m4Ht/uB4il7OVxDejq6xGUqKSkaaeJ8eKcioW37He8F1Ggg
wkOa9O/LNnpxZMrAWPafYdcFKvTLb2uXRP7jORLpXngr5VxRa+TW2+hbZTVDE8vK
qKIJyuzq6PikTcnm2Ze5rRe1Mgit0PpqMmu+udhAEWZRDfq8lD3Fnyb4M5qCsDf8
sH4we2ECgYEA7jSZd3DmtzgfPt0Tpj5qHz+a73kFVONFzrg/2N95dmi6xFtEobeR
PInrFvAqOO/vz446Yf13kK0Nq68WAnBOs5gSrluv0DBHiUu7U0R6mjsPf4rdNtzO
fS2CjRIpvexvbtKB9GIHcKgDHJ+En+GeRnV+3OkptSZxuTlcRdwsmAUCgYEA2lX9
TvUPGRQ/fEvDeoaFbtU25ZkD1ucvywCxfReMuTmzRv9Io7Jrllf4Md2j3N3VdyGr
0Hi4kzj9GXZdF3lF1RdiTpQxVy4AGg0Bai9/gCClOkpdB5EjrR2mFwFw/8Pae/L/
Z1H8YPSAeHSt7RdbyU1wYbE6vAz76VemzcVRyokCgYAZ+EAXBocQyJyXdPDUeg+F
0qBopVAQfiq5K9tCILMUVryt9alY3DOIXxzzRkHELVx+y2nQDxs++a743cDPiUD7
UYQP4E0drHXQISKOJHQdZnz9Eb2mYpJckV6fVLCaVTGc6nRimWFoRdj5AOcrqyRf
WCX5na3/Yu6ZHAjUUPnHpQKBgC2rBszZHUtVnOHWxxB9yrMgDdeAZfkxaiHAB1/u
6RRlKUaUZxE2ZKKRy+xCO+Aa1meQt2tnlNPWe7ozs80RJLYpqfpdrORbTtIkHkOj
o7udGHJU05idlyTCqtbtCkG1KaH7dciasXtmKOkJHsgUtrIobHVCqNJktNxd5Rnt
R+phAoGBAKSr+OhUiJZU1n+Tn1eri/CTw9g9HtmnrdWAfjBhhikZoD9qBDFlf8qn
8ZYxVOYiFpiR7iDskpY9Xn5U/jvX8TTd9OKL/SH32VKMKNtA4JmekVFauhF4NeM7
C2ZujRSJ4KOeGJFdn7VksHMB/J2UY2AWgR/r2FfUah72qUis3ud+
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUDQl9lGAFVCp4uzp2CyNIBevz9ZMwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC+u6XURlYwJh3spBKnYAgu2pApo1dPx2lT8MrjWRlrafrG
N+eSEryqlnUzuUBb9ps5RbIB3Ojux183ZzuMal5AJGBMUz20WvoG24bp756Pi+Vw
kbWxw6U8z6CIDNF1gzokIhgUxQOrgcTXM3beR47CuOw9TPsjyHXp8EuOP4hvcVEO
XK9TiqKE/655j5DoWzcR5iR956McJ+er8uUgEuHDGWUld+7PNw7xeKUn22G2rbXU
mdOTL6uqdaKFsLM1Rpc5RYDn99PiSmtOEMr7hApTZHbzMGyQQlrRe44TBO6bAv3L
2c/eGQ1c9vapj3242NS2T498uZCQmP5+XBKQ83v9AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAoAt81WNkFGQW5viqHVOy/
Yrgtm+FP0wWKI8bL+elljQoZv81Ya/sgfw9A5X5+5QcKGpciEg9J2OcE1Xijtah7
tMBS0oqupNw5EgPc1q0uelS+2///K+K3AwM40O3kd/S40Z93vSs/VstkljmgsWfL
0Umpq0Cn6TQLwCnZad7GBA7uUpCameM8Mz9Bqk/5Qtyq5cOepKcdCPFH3NoE+aZX
4tYMWPXMUy4NvFWMsCMWrRAvOs3uMZJwLLSGpV3Z9NElilPcQeFvsSiWCzMITvEy
MipcUFAug6Cz6oda1XkNmK3QOL4ZV9cxNXATvAb4XsE5CHcMiUq1GEFGEd1Nz/L/
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAvrul1EZWMCYd7KQSp2AILtqQKaNXT8dpU/DK41kZa2n6xjfn
khK8qpZ1M7lAW/abOUWyAdzo7sdfN2c7jGpeQCRgTFM9tFr6BtuG6e+ej4vlcJG1
scOlPM+giAzRdYM6JCIYFMUDq4HE1zN23keOwrjsPUz7I8h16fBLjj+Ib3FRDlyv
U4qihP+ueY+Q6Fs3EeYkfeejHCfnq/LlIBLhwxllJXfuzzcO8XilJ9thtq211JnT
ky+rqnWihbCzNUaXOUWA5/fT4kprThDK+4QKU2R28zBskEJa0XuOEwTumwL9y9nP
3hkNXPb2qY99uNjUtk+PfLmQkJj+flwSkPN7/QIDAQABAoIBAFdyMvpa8SMMJsYb
B05jsfzBSj083Uf/diP9Dxgi/ouHwGjmsq3/Fy7i4oM/WOmQ6+PbN1yxSr5G/Dmr
g9rB3cpsoxX7SBwLZfyE45sXuEu56QyuUW5Z88UosEIQFmxZKOvuEbpcBW25hmTf
/Iy2pBZUsEL+q1nhi2YhPJLQQB5PPCgwumbmNF/GK8Ua8OEU2b9FYGOzp1eAS7TI
+dB1vu3bOdnvyTpFJv8phlAIn9+CQRAMPzL/PKRm8SIhmMwSp0v76TYhu5jWEWuH
khneCW+SaRUVsjF6i6zfJOs+MQQvhuq5oeOobbkRn9jjn4F1CHKteR4ynztiyl4e
Dks47SECgYEA3w3h/satsDk6N72ZfFBnEEGDnC8EvEeWMWTee0iWJt27pYz5g9fG
l6uS33f1gAzczqyfHi3NY6HysBpU0OyuhFtSmREVceK9EN6xBeLTrWIrUffi5xq5
aBVUGKi3VWp1CzaYHXAlK151Kl2lmc30m1244TxH6bR1/kJYArB1A/kCgYEA2uei
ziKC7jThy/Cz0hYch39tS8xtjjifWcri+bKvRG3P/KPWRkduIz8LBH3egQUfpfeZ
p8MQ4m980zXFQE3uppBjwEw7BL3+ZO00si2nyhP+nXeRlcpah62EsdPBCJF29bUt
JDyrnO95jSi42rt5IxpTQVfz6zCr/MJSQUPRcSUCgYEAiyziYlIddeN/S+BlsIeK
hz4ZnI5J6iDQuikyGMKFzeJ0fyujVHyCUYigsAbti+R6sgpLjk0N5qjaAL+tRF8p
1TQWKaPbOaA8UBZjZkTNx1WFqjN9xK2MGkGUo35CRm2ScliyOUwMJS9e8/xSo9E6
WubzwLYYON588RT8TVFE8iECgYA44u89EFzkGFwBSpkAZHyffa7ifsqNpgtLI11e
tF+1sa/WIKGDe/aUNELhtPAIqVMzJygIH7oYjg5rONL8xgPZxzYU9/pyXglpIveJ
wjGTYyTMuRDdU0u5bI9KQxQr7Nl0OtPzUczrKJR26Xk4ZnWxeJrgJUIfAXQAaGNF
0KDx/QKBgGWQw8SzVmPlEx9WSmoRyWQaaCD5ZAfwOg6Ph0FOSf0GZZXjApjno2Ri
g5lYAtTVv2vix0jDlD0MD86Ou+tGmZ/x7/Y/cHOYLiZJKiUugeX9Asf+lf/03mEs
/qXGNK0JOo8699Lbq8ZflN79bRrEOFyxlGKgtFSrcQniDTW3EGKR
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUNt5wFFEHInmQV+maGlazlOTq18YwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC9icCXt+50NDRtDYOA9SznDkajEonkL/tWDRgkWPfyrQjs
MgxK4thx8h2pzFFO0orpKhcBH9D/yJ+IyhOzrv9MqWIEXQ4I3BUWQvwUyJiAARbu
Udj51pFZiNcRJPGg29eIf8cJFfSTQ3LyU65BkYjxKScHi7psh3t6jCElxDnou5yY
brMytE9zUzV7xC6wTiN3BJk7A0W/d6fKpOziJ/487IlaBP6FIxUS/o5u8hG9VPXQ
ZCXBWpGB2xLahQS6xANGSCwYKtkFgUeIJLZwX+6+XAYppXthrffos2jKNmXj3GC7
XCKUEfp0rWBxcw6jlJZuOyqHPVOXzAmVlKVPnPQJAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAJV9THcfc7PMB8oJxoL3lu
gP29VWYHaSxblJ9OPsMVtFQEBwa72q1z1pCb9wKWQ0B1Hkz4YBtbYDHLqdsK3xfz
CXAo8zDEk+D5QPPzScWM3R/tK1wYUZ62Y2J40M7G7NP24aNzmlOKZOMOLbBqJ1ZU
vbuZ3XPDDv/CEWv+RkXUjc5ICzHCo+MtOJ/FlMvR5H8j3l7nj8sj4WjrhdqBh7AA
74eHvlVqpIZaZw0HVAtDASJAYO+PTh0G61alVDWfoRmNtCeS9f/CXsNeiOwwWLBZ
ZO0evHv/iAaNk2FTTGwglURsIjphpOnVScLQtc9lDc2dpKm5d9rqs7binU4dupwU
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAvYnAl7fudDQ0bQ2DgPUs5w5GoxKJ5C/7Vg0YJFj38q0I7DIM
SuLYcfIdqcxRTtKK6SoXAR/Q/8ifiMoTs67/TKliBF0OCNwVFkL8FMiYgAEW7lHY
+daRWYjXESTxoNvXiH/HCRX0k0Ny8lOuQZGI8SknB4u6bId7eowhJcQ56LucmG6z
MrRPc1M1e8QusE4jdwSZOwNFv3enyqTs4if+POyJWgT+hSMVEv6ObvIRvVT10GQl
wVqRgdsS2oUEusQDRkgsGCrZBYFHiCS2cF/uvlwGKaV7Ya336LNoyjZl49xgu1wi
lBH6dK1gcXMOo5SWbjsqhz1Tl8wJlZSlT5z0CQIDAQABAoIBAQCZYOHzZKqYaq6K
GUdzkfP2Pn029YeUmqd/KTWCJGTxgskXqiB8cTnKa61JfMfHS2WR7beT91U/x/Ah
17U90L1UIjXpZgw3azG9RBOOFg4id79AuAcnllUk6TFw9D58d6rhENXWKmgyy4A3
TTRUZxs0XKLy3kXMEY8AymkAkNxz0gkVmKKJlwoSPheMPNIOGG37eFgX2YGrnuIY
mUUAfWI8mpBCAD74vfleM4Y8c4jaKMbqn9O1sxdIGh6mGDlTFQyc0wCtT5rRNUnZ
l3WS3bKFGZ7xFWtnR6eZwAcnMU+axccXy5Hlvhiqz8ZT3DlUGNnYmofzbqr5xm/G
vREX+fhJAoGBAO1I1Ue9N/rlKSbZqr1m9W1U3Jvv+bLiLau3yhzDDh8wxV7MNHqn
TyOU2TMRnBSCukALU3d1Kw6/FF98OF200vyKG0298IxphIj8QHyn78U1fH3jFAng
TUXcJJKmWCZtKCd5p4rDEve31IYsAHdWaKOWglhE8m0g02lXBJjqELUvAoGBAMx8
1xSUcGPDnmQekaonpq2jYrLZSLlZpsqs+il7VdR09vB9sIkm+RyFRqve9rckGitG
FICWWtWCwKTT/8AAfqeX+8x7JarqyMLWm8td0iLIVFaNnwZDaXx4oPGA+wN2aF8S
/FM6CxiDXSrYy/kvBVKOj4wI21qVR0zRIOGdK4xHAoGAWahKhmfVziRmrzpRzG0p
0RzemsFLLS9PKHIymTmOjXSFLzOjpLCxM3WbuDMwMYPP0kE1UY7hLRpAHXA3cBjS
HAAnHvHlAXkhTg1aZH+kFnUGTB7QRIcPS5VJ8GuQJTzbjkbmaoUZFqbMU8IujukE
csN9DtNGcruThlsN7qWKmJsCgYEAvi2w/sPbDv3E1oqToLOF0eGtjnaEq1VUyRQ9
CM1bEt/BNgM/Zx8m+b597qTLwaJC8FIaCUlMq1wSfHlqVxBeutGf7hnt+1qmYoaj
mGzmXVEBFwpZhsK1XXz2+gSh7yN1iE6o+2J1JVQvFwVQFq0Dfzd1C6DFGSbSi//H
W+0HrksCgYBm21cIB4AWBMyDnMAS/pEqhBvHbGO7L6wELhQ4FYchRKdS4GHctbOW
q1E6zhGmLXql67567l9lHTF+78KxxKGzpAzXrz7EjRBSvIZUFTiWj6obhXqNPynr
ODifrZzJ7xQxDRqR+X4vSpvY1TOKM7Rkvjd9bIVCcbT0o/rHL67zTQ==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIURDIvwbpBQzGaYcY5NjIvLi2K2z4wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDFaJpx21ia50KpGQRSKamxsjHUHVDHRccMQlHTD1urBNpE
3ulAJhSiJVx5TAlQCZeaP8xq9CG2I+hRqZDq32JCW2RuJKS0NgI6HU+L5OLkLXYf
MXbZe9rMAoexVHNLxHdcTPBeEJWJhd9H6XjVJ+o0UudooVzUrGbl+xzGUxv8dyzi
LOIisbo9QVPf+MNgKD9TaH0aHSuh7BBd0lEJiV3kDntcBwjqfoC8FWMp9ykjQOQj
OICPVGVwAPo0sox7/WgKoiGQlSyI8als8NmGuLvqXnIGv5M7dDVUZSRIonmiz3k9
xnnc/bSxDorWTzgZ725CzD/8Aev3bJYxbSySe6jfAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCppINk17Ykk89Jdi1blQnp
RYEHvrP9q4BIK9g0nasjPq+GQLoiiJXT8LbisEV+0V54PVHV+Y1wcIMDXVTqhHnA
OpNgvud31bb1XQOoRdbtsS88QIB2ab4/urWLvuHBmksG/C2n7VKcbdeU6+xkUbfm
rPNWiN4vPyqfzz3FKSWbLKy52+HOp6/fQsdoH1TUO7keC9qG5JDLHvsHP/qsJKWG
D8LczKzlqVgxvxUrMdYngQcBlrP8Z4Oz0NCe0AF5/LI0q3YRLpLPLdsdAKDm44Lb
BAe1y2G1jeOvkSQBPWCpW5iTFuW+CMtGAiiDXRhkxdORDvW3YfBCjiWO0tOliydz
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAxWiacdtYmudCqRkEUimpsbIx1B1Qx0XHDEJR0w9bqwTaRN7p
QCYUoiVceUwJUAmXmj/MavQhtiPoUamQ6t9iQltkbiSktDYCOh1Pi+Ti5C12HzF2
2XvazAKHsVRzS8R3XEzwXhCViYXfR+l41SfqNFLnaKFc1Kxm5fscxlMb/Hcs4izi
IrG6PUFT3/jDYCg/U2h9Gh0roewQXdJRCYld5A57XAcI6n6AvBVjKfcpI0DkIziA
j1RlcAD6NLKMe/1oCqIhkJUsiPGpbPDZhri76l5yBr+TO3Q1VGUkSKJ5os95PcZ5
3P20sQ6K1k84Ge9uQsw//AHr92yWMW0sknuo3wIDAQABAoIBABR0pWRc7U6H3jF1
hSwaYxols+Id84vioCCWErKDKeWLyC5Qxuy9xW+T3YQ4K9LeW5ZBPCZtC7069UzY
/EpKQX1MyRhctbBy1EI/XUnKuvQX/eB3mLAqlF6FeJgYfyX/wrqOwm2M3GH2vE9Q
UxQLYcpwOMhvyBXFk5gLME0guYqshBEe2w/2dYRoY9dmpypl+IpDHHhFvrFxs/d/
0wtk60k0avgvdgBaR6vnP6FHPC6qGSliY2IRODNqog4G2TkuthZ0IKd/7FurhHpX
FwO27/Ur8FjOg9pWXQHSj2vG7+6lepHl9RxAOIj/cF1QrCLFMoZPx+4MubY8IlTs
fTKebxkCgYEA7eZjyQ3lp45apRo2KyIj342SwRd0NKLfmvW+VrGggBAeNWl6fTb7
2Pj946J82QPUkdq+xz/hL2n/2MvyucjK9P2ZcFeYFIDoHIMufGGWvOgxymwsFfSw
gEJQW2/8cjPJwXi5QgA80mq3vKRGt0HHCU4bOr1tf3hksOcOVp4MCWMCgYEA1G2O
z8R7pbTSsaU1gudiZIOKAudlo63L+zkdkfPJtARtkkLTyTEkyfvnc792fPxkX7kE
kgz3tKlGs4kPKmtsrleNfpwSeTEYDuXHlyFdazt6SnbYOUbU6/zzEwVrRTwUCNd3
LxvYfYCoQUF80bAJIelVS3FLkIk2/tjL2cu8uVUCgYBSuH2R92cXcARMzGRxcxmO
LigNRB5//vJJa5GXi4QHg5M9d0PELk48D7gYYvOOciqD3M/hcHDYj78Knz/zIcKQ
lW25Bnw3BOuwnlyXm0dSwFovzJU3vTFyJ5zRbosVGrTYtSWVsYd0ku74hRahuhl/
Ps1xC1T7sd0xNeZib+o3iQKBgCk62m0ZBaaz4fD4z9oIbuBzZ2YI44FRSjYIb+TU
HGIEOgAZWGHEWA+cBOBCWQ0JL7Ikhu6R9cHq2P4frAHft8he1eetAyjijnjVwFdk
8mzNrn6lcnIrfUgQYF1gv+FAN+M/brKGBQ7W2dFQlJleQWeDkjqCUthKyZHNIkOz
d33BAoGAEnkimK5bjPYsCBm7uhmrRbzfZQ5cfBLUMSBlG2dzcvVc2eFmHX4lVYZp
rHQVghmK2/4qup8Dmkm2gWV4WesOJGOc1y/luItTStiOmFdex1F1+8MOY11zWLqt
51hIXW17KNSZHiQBYUQAtH4OJvDAoir9nk2RvdR5SNvAdV+InNQ=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIULUbwce/xEqn+x6vr9oE80QQ3d8QwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQClktgQ/ipScugjip0UN0Ukgkro8RUsfMKWCrQTx2THJhBf
C0mCuci1Pu4+kiJAXUkIs1zzYTE2Cus5OQOoIzkB/dFbn3nf1WSNrNsPKfsSeyoL
EQpBX2xxiPxI6zDzEv6NpwhaKSnkfVuZPn5v1PeXb87KZMLHlXZbS1HB1VcJqb9K
vDwvdOk9D/RjaqwMjlmtShMf4VAprWxtYZoKEvqWTeiBLQt1UVSa2Q8wQGsWHthm
4bpQ/v1VqOBZvLbn1zkWBAvhzzd+yvMK2lzphjNnP5rFJ7Baem5UY9Dg5TP4Xz5l
/gDQZDm/bMrz8VN+IFfjb3Wm/33cGhTQX9YGzPUJAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQDHpjstiqVts7VnJ9fueQb+
0CDiYjSkvfEzNEkRnoBunNW8/1ztJa1RfZlcg5EyI2AdneFNoiKFbJU/GlEeo2M3
hyz2t26/IsMjLOpLMRdTn+lOxdRd7qtC7KrC8/raeRiD5w1puS5miCi+DqRLbUfZ
oY212iyiiPDJM87ubwxFfySMkdKBd6Ai0gIYfHQnorMVAfgbDY4vfuvfzYXWKJyo
eP1LnyTGjcuswo1+1lMCkjcwyQdnwvapi+TqzlS8Ay4lSnbDhyK67jUHDZDNOuWu
+oDWpIWt2PPpJZUnBQu7XbHNup91PaWG3lGokssosgybkvZoNKTKtpe+XJDZ7j8T
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApZLYEP4qUnLoI4qdFDdFJIJK6PEVLHzClgq0E8dkxyYQXwtJ
grnItT7uPpIiQF1JCLNc82ExNgrrOTkDqCM5Af3RW59539VkjazbDyn7EnsqCxEK
QV9scYj8SOsw8xL+jacIWikp5H1bmT5+b9T3l2/OymTCx5V2W0tRwdVXCam/Srw8
L3TpPQ/0Y2qsDI5ZrUoTH+FQKa1sbWGaChL6lk3ogS0LdVFUmtkPMEBrFh7YZuG6
UP79VajgWby259c5FgQL4c83fsrzCtpc6YYzZz+axSewWnpuVGPQ4OUz+F8+Zf4A
0GQ5v2zK8/FTfiBX4291pv993BoU0F/WBsz1CQIDAQABAoIBAFXzfdCMcKHuXo2c
tmA5NN53+LUl+Wznswe6tLKTzsAHBXahYF7JXOShr4Gx0LAC/RfULIt3R9mbH3LM
IxbUehKLlXPvvI+ysglN00Xy8BAu+atXBDDdfWkOyJB97yIwGQ6lyBMtzT58yOEr
bO1W69SkSQAOAIMlFpTb66wouI8dxnpxqY7x+csWmAwHERMPLUupe+YU7L/YUvtc
dP+smTmpxKTrjgxxv0IdLuk8yjfvL717JaqQgeFzGIqljEGr8n9qlO+VIusgB48P
Jm3R4xT8XqrqgySZ7GxHDTOZ2NDDVfXs1A9TNnPUQo9vQRVPOMmUTKBjcuHXZ4N8
zBSoCVECgYEA1TlD1s7eOlylsu9E2/yN7lq91qz/QYT0oLo9/xkSNcRAEgtR5omI
C4rZWtN+zWz2JVY0aQZNjuPNGlO/UN0e97Qfu9otjtKQqVe/nc+72ly0MB0pfyeX
WKbxsa2UtJ8IheStR0eCko5QQVPCTrpxD2fcKDfo4pgcOqiwrXZS9y0CgYEAxspe
JF+yWJrO3ke4fBPh7RxdFtnM8ajnsuh0zWEBLvZ/HPwcgxftlkw3WZhv/cbTefhA
ouKMjoXtXdKI6n26CZk8YygR+ECxEZRK8kq8lAddoYwW+nKfDZgrchiKfNiedsJi
MJkOwhmfDymYQ3qjt4MZeZlgfXkN2N59DeaU3s0CgYEAzmawlK+Lz1L/00ZqkcjY
W3LbcYPlU7cwVqXyfY33YrSmkNEEZvWbDBFMde9lP9XKMDpSYZgIW9mIIYQQHmbu
Iznpvh5lG2wZPNQEWO9OGQLEKg8QrFXW26o/LI+q820/At1qHyXJ77RzW8mIvk0c
RJ11MDlu5mn4aZAB9ugjR8ECgYBGGsfoe/chWDbsHM7qsvhR7lbF4DluX+qWJXRL
mZIZRcS+LArCEIYxIt/CMQgNrziVIv9ocgyvlnuHQuAWEhCxoeCx90efDPFlCa8E
k2a9rXtPpV/VIucEnE12B0GPlbUMnLCUAuY5fV+isUCJS47BAPLS90wX88D2YkAn
ztFhYQKBgGYz3CSBBOYpdic3yQgItOx3Ytvb/g34Eac3y7uQuOMqJAIe6snBSK/J
Nr82Aey3h1YnpNn9J0x2UKV5OoVupgvYE+DOFBjTaDL9ZlqVArJvKlKSxgN7if8a
0BNmTXVsDiPrEucK4AVRrfFTJbzRkLsDruScQpFnytCUB9wyWjrc
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUPASsrsYzDmz/DkwIqjt0/8jCYMswDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDTC7KkVFiP877ALH2osPDSkV0+ElIk6dTIJ4dnMo6Caxq+
iL48E9xXK229yKBayaUHny75umllbXpAv/WpHDR9PdK6sy27d9PFRxIgysDEwNIG
AdfnXtyDnjuL2AUMdXByBUEATl3t3L0fFe1CZOQRnTdpr753tgkUwgnycWhYKlDN
FwkBG6OBODhwwwZ338Nn9G9kVWwZe5kcDxLngrYjvm9oZoGtep5zO7GJi+ccppul
LCwzkstJIfi3U7IYEEeHHn+r7jZb6kgFv9EOySfzPqWukkokA7JcQvoggccf+1Dw
12pQ/wCLDjy++8bwsCh/BlbvUvaQUBbWFhw7egpHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCnaO8umnXPXwTOJiWSt2C7
hP3ybwzmGrPo13RXia6QvaSH71QwYUi1NmwmNUVgRy7y/8uOEIVf8bXqa69I+b9+
qviIBgk45yPDfbCHGX5bbd2qV/XyYybT2X2FawTM7bN9gVU/EjMrvu/VAyiW5yYl
/O4WO+pvnThlXiEAJjgT1T8vXtf+YjxSfhuRfTRK1AW3SQCtYw09mREjeTCThlFN
zeAtI8H1VSgdUe+ATJ9wWDkqDSFP8Jof8Jv0aT8oLFfXrNCff+nTWPEpXkMqwoxO
wIn7lnNJMpehGLgCm/6vtoT8VvQUvcViKIkijwI4VcoK1tRWFURNm3YQZ1586wo7
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA0wuypFRYj/O+wCx9qLDw0pFdPhJSJOnUyCeHZzKOgmsavoi+
PBPcVyttvcigWsmlB58u+bppZW16QL/1qRw0fT3SurMtu3fTxUcSIMrAxMDSBgHX
517cg547i9gFDHVwcgVBAE5d7dy9HxXtQmTkEZ03aa++d7YJFMIJ8nFoWCpQzRcJ
ARujgTg4cMMGd9/DZ/RvZFVsGXuZHA8S54K2I75vaGaBrXqeczuxiYvnHKabpSws
M5LLSSH4t1OyGBBHhx5/q+42W+pIBb/RDskn8z6lrpJKJAOyXEL6IIHHH/tQ8Ndq
UP8Aiw48vvvG8LAofwZW71L2kFAW1hYcO3oKRwIDAQABAoIBAQCCWXFG6gmhL60b
SN97931msP3kPrCZuAsCbNfGt4UprDligVbuCF5JQLuRQn84U98oK/t5ptc+HDYs
E+QJRTBuQmcLhWuzpDkaWeEqe9BANdACgdT2RLLyYCLrJstHfKms4u3Y4I5HQdVV
g9d88I+lCXOWRUPg8H//YDGAmucVvD0ficfN594SlAX83lEHJFlB9hY97vAliEST
L5xaEmMS/f5tSLMsiwf78ksaME7IN4maHNbd5/8bLmuRPlFGI1espG/b7ZEWKKWT
Nsr+DzoTKlWcl0yTiFzW2Nqq1A19RQlekvuOA3AZGwiPlLyUjH2SbL6e9DQs6kA/
N9nBMjVhAoGBAPrrGeKk4Mq9V/oPa8lXSaiwdXfi8PK/R5153106COBamfunlD+0
qXW5dc6cUXaUgqFCkdROJOPSIAKwkaNWsT0a4X6tBLl4eK/Ll4bWqKw5NDbF0M95
2mWko/bABAxVtExPSmqerg6SYbUn1AZ9jyl33DU6eYtbSqsddHvbB3pZAoGBANdR
3/XhFTD2dUTQF5cnDckEE4N6OcvbmR9YPXMB8LOjQ9ZuceVZZv51rrhCUh/uFpWG
hdiUsuwprPTAQQx9A1M6yxKTSWKOJ3yaXLfUKWMih8DKvzhkYmTrZRJn3533u+oo
0/VBRGWXTwGVrgfoVsdA4RcyePBavMIqsrI+MdWfAoGAD6+c2adXCjWWB2LpaRfU
2f/WCB2e1H4SuwyAYzKalXP0hl/ui6D+qwZiD/2DtjcIh45C0ZPlCHz9VU22fRCR
WfGRQTsNvY6DdPH0UhCfUMzur7HkIORMO+hz+5v7ZM4CzHZ0f3/V/8E07H9F6PX2
ejAtCwLR0F1vqIzZ2FhT+lkCgYEAguIc7hwkwn99pxeKz3GI2qDkr63zRey1di0w
JSGPy9I5YTX/e7dNeO3WB+EghJI4HioIYC97Vzy6Coh2wf2XsNbzK9Zl7EeWzxIR
vBh2E/GgbVuQwtmaSdggtwB3GFHHYz3wIYvL5KkF+GOgxuO/JB1W9b/Tbd7qEGjd
+KT/q+cCgYEAtq28/NaNeKx/0rPAorNGKYWeeUftlVY/Zb9AXdnmuieKkRvU6D2u
nppPdtr/m/OrO8whggpMYAt5wCvFN5YPCsjm/X/tuUtyEqIab3PdC/8R8VGXCgNj
rSTc/FNwCKfX+aS8iti4XETgC32z36SKoh+k2ckGMJdv6QybS6Vv+q4=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUfp7Qhve3TfaAj3jjcY/WUN1nozMwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDN93Shy0G+A51fMBzkH+j0LwpNhKMTMeNxsc7QpqwolyAm
/KBvbpFYO56c0o7zqNU0PdyO7D8x0qX19znVdXsYweEMhM11cTl3QV5QCjN+ldQ1
i0APjCmColWk9hfF5LX136jLurHhQrMaMTVZj7s6m9Zun7t1FOKqCliCGTP1mSPK
E1uxZi4Y9XCGwTjb6B8ffmgixPMxbb91YxC9FSa8m3iH+69cQ+edqvDCbmZrnJf2
5qVlKpy3fiavqmrKcuD9eYsfngyfgMGb13Rswpd+gfaQP/gWUwSNX7VaHU97wkCN
OwJ+VX+4hL7rxdpprYrkiBlWoA3hUxhjtzIDyhN5AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAz/00Fvtg1+h6addocNGW/
y4RyLP14YefUkyBDJs3kxcDq2HvbzACc4nOMvmJ7QkE/TOCfDGCv+3pFd+a4SHdk
ifCI8YXTY3dv14CK4oLnHCCffnM8bzSCd0s6aTjYvGkiDKVOC1K8bcGBPjCsqY/U
U15vlfHAOkN5wYbDEFcoN/izozHOFiY1z5X+CBdVSXmqQv69jqXzQyLr9ul6v0gO
EOoNyl/yqfvjND7ytWcksJOM00ogVc8mdbOfVddq5od5i98KRwcDni79GXrELs66
ebCJ6M4lmzuktRiOzOskQmaXiVgYXYtR6EsQl1bGFv4jnES6l1EyJxaae9lm4cvw
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAzfd0octBvgOdXzAc5B/o9C8KTYSjEzHjcbHO0KasKJcgJvyg
b26RWDuenNKO86jVND3cjuw/MdKl9fc51XV7GMHhDITNdXE5d0FeUAozfpXUNYtA
D4wpgqJVpPYXxeS19d+oy7qx4UKzGjE1WY+7OpvWbp+7dRTiqgpYghkz9ZkjyhNb
sWYuGPVwhsE42+gfH35oIsTzMW2/dWMQvRUmvJt4h/uvXEPnnarwwm5ma5yX9ual
ZSqct34mr6pqynLg/XmLH54Mn4DBm9d0bMKXfoH2kD/4FlMEjV+1Wh1Pe8JAjTsC
flV/uIS+68Xaaa2K5IgZVqAN4VMYY7cyA8oTeQIDAQABAoIBAQDEYzPxZZYc8ONo
NL8Hgamk0wmW2maH0eTVrr3NU28KEPdWVUFAnwO1Rru5OkeV6yDHfEjGelrTTdBy
1DVv5GHoPE0ym5owZjJuFIUx+lgZVhGOsGT3riSSa+kPrpsCVU5uz8Dp6OzdJbUS
v2LoL9VNT/RJbMLYI37wtYapHhDeFlvCzxxqKmr6j/Q3z2V8sxrl+siZAuyKtp8R
BsvSCiGxR3AGACOTi41lAgLAyUMos2s/4kLrqrLsKQVmSgumlxvo4MP4aE+SCF8I
7RBZwljpH1E5Tl3AWGuzThIZTSb0+eESU4RJDAccuMyfPDhb2gUHJps67mHq7EPK
WAuvSfxVAoGBAP6Ebau1ZW5vzJA+JcroSWgJ9rZOJoeHKdfVdi9D7HPDSwUlaJ3m
RgzM9QAg8Agvkr9+6DciMtxn484aZjp4F+3N66BZrqgx8MtX5txxGnR11lAMB2Rt
7fHgECD8wHfXWueKGKIgE8s0A8Wv9imOFpu6SpF7ozIP0xg1XmJA6zTPAoGBAM8q
nyXth6cx+3PbTubKz2PUh1gUlkUZnQvWShPjYQOEkLw4B4Tsl1axmC2izOgUxesF
g1RCj0YzWA4AQSdAyATc+EsMrRhb0MrUqxqdq8nTapKXccqWeqmY47+DkVH+jX8F
Ucwt5c6No81vecatNpFLz3VbRRrep2ErHYLr91U3AoGBAKV1mApxsZAa9CStkkoX
umj9WTrpEVk4AHbE2cEeaiBTzHh6+kj0Q4Pc1kWQJBteOgttyC7Xd7MbgtghB2Zp
Xj0FinHC+61yUfUPnxCeIrGlTX7aYw/h+zcsD7AyQDlocjtl5l+3dMa8eNtSajhX
m9D/SazMcKqB6RyqzUIYrA+3AoGAA1w2np/ermiSIovxGK87c+wTkesrkM1cjb+Z
Df+HKE5zJopmHNLVlZNl23+jgTQtDaXWPnyh5Eqa6Ac7B072r5WB9X2sJRQAK/oN
GG5sRebG+L+6GcYdETkooIeayNCvLNtCO2SXMKV9fayMNhvDIdIv+EBVu5zW7C2N
2fzH0zsCgYEAou6RMrCA7hPRVJtB/mDCi89maGDYRokwd/6554Bc2/QRtAXgmv9B
JkwUcfKEtMK81sZ27ySm+/WrkpkNIvTOdgcplteN3xncjtaf68SPBkDHkps2atQA
ubqQMVhhsQuRmd/OAOabSUv33MGzqvISV4IaQb0XEgn0LCzsBwNThXk=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUY8wJZA8KJ65kDzfXRlw/GtLkNLAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQD72WS1saIIDnLCq9rqmzXiyHJxMshwXlruH68D1kLKPpjD
L/E9u1KacaRr22g17yuJvwumRcGsDBEN0g3uDPQ8c1EVIuobm2pRd6nmTTrKWO/W
T2TpEQxrs6U1A5/xpkkCItn6z9V5ukSyFA68x+WDY8f7EEtwsJ2dJMx/7MgtXaab
ywapOA42YCX5V8vh1848hWw5qBLjz3JtmfqjMAEMLP592Wpqb4EjIw9EqUEAkjBo
JeJD4H05oFMfRFcA/30n+SRBCIAw8rvJV9zky9rbh7imLOf/EEGwvntnbZo3Mcil
Q4zvV90HGN7RZim+NopdhwnAyZ8ElXCDIL0CJXqdAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBca+x7FGg99wVVnCibFKCi
MvFM/csSYRbdIU2SEc8Odudy7o62rOnuBv3Pvt7hTNVcOFl8KjWAkDTheNqD3RdW
GAf+7XIuyHm6icXFNb4ODeLbIZwanWaa09hOSLfMkXUWe72zkGRw5Y7IK/vSF5F4
hFlPai5p+YJ+x94quL+mZM8sBgOLlY/YhWq8PUqEti+w8+iwHtgOHIks3XW5I2oK
0aCcCbx6gs5XNr7iYzKIi/QinICAaXjm9AAIU5D0u9GLFm7YlWajMG+p0s0QgZlJ
KLa2WhXRqWH0i1g2xTaQ2Gr8+PyM5Rb10+DVFoREO3wXWuQpsSBPKAEpjxbGKBRB
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA+9lktbGiCA5ywqva6ps14shycTLIcF5a7h+vA9ZCyj6Ywy/x
PbtSmnGka9toNe8rib8LpkXBrAwRDdIN7gz0PHNRFSLqG5tqUXep5k06yljv1k9k
6REMa7OlNQOf8aZJAiLZ+s/VebpEshQOvMflg2PH+xBLcLCdnSTMf+zILV2mm8sG
qTgONmAl+VfL4dfOPIVsOagS489ybZn6ozABDCz+fdlqam+BIyMPRKlBAJIwaCXi
Q+B9OaBTH0RXAP99J/kkQQiAMPK7yVfc5Mva24e4pizn/xBBsL57Z22aNzHIpUOM
71fdBxje0WYpvjaKXYcJwMmfBJVwgyC9AiV6nQIDAQABAoIBAQCsOakOO3BT1BWU
nNNzFjsOYAcq9BBwD4ZdSxtzI0W/ankrGZD+pyhA57AJ9hvYrjr20sfTp+Zekk3j
Rp8yCHfJEw8CxkKUKH7XQV7VWED4+ULiKp8WZws4Z7x1eYoaRZ2tsUmhpBkXSlMJ
+H9vh7+jT0wFm8oLQSw3t1+Fp9XodsRcBQgljXANUTF+emCOTJS0lOXcIhGYXgv+
kxUJylEtHEYumyCFYY/gRnhMhw9kMhopZUEQFu/MbleYWa5IoiajGC/FjJTHC6VI
vzg/NUk8Y2L8k1v9SNL9GpEsH+jbsYs6U5560LtxDDiQFKklPuQkQ8kzGJza3jSJ
yYk8YzUhAoGBAP9aB5VzWRDm534jaJ56dRqFXtD43rUhXQs7b+tp78tCZFYwQsEg
+nlrHd9u0IdlZkX07euvReuxvN1L4hGtz/Fk3ctkZTM7XXgAejHKIsMMMcCcyAIw
z7K9ogF0XYZUC+f0NKirAM8h8qdwSKyC98P36ddQwOsEqp8QhXOGEXjVAoGBAPx9
FldcGVLrWoZ3pSR0bmaA+T/tc/FtPznmqTx8uGeZ5YTjfWhDU9vA6vKkNMscwPuh
GJEY1t3Bxjm5fUBQSYXq0BFgT8aytu+TCDH0EP/mnWcKXnIKSxcJGv1Y2i8XNizB
Q6rCtUHO37sjmaEdkJlPby7p90gMoFpIEWnchN6pAoGAW2Q9kp/WINaDxAGoUBBE
GVnitahdDTcDtiFvzTH9QSJiBvb+7WCARTSxXGas+8iu8hrXjKMOw2y5y/p8zxcG
db9EIqesEMoOigSht3BBQM38gJOcgiw2KiL0+NBNKOar3DjrH/MUNw5Pat4lJJk7
VEhGyWl9op/o8UVYfiBd4IECgYBZvCtAiR8G9VaLC+LJfgfurk/nhID8gRNDhNMJ
CFqRl4SXIjLj52naZEocSnfo6CM+SxbsGqPi1Iea5G27ec1npvij9FLmD4Ysx1jW
SCPyjwfKI0lFxprBaR8Kg5WnvtwmM9nUyraY2OlzHUfwlw1ZL34YclbMaJBlBdAK
i7E9YQKBgQD47sj72TSpCt+xL/Y8jzwZNx/ZggwCRrYtHcR+8RxwQXQuFJJ3b5Nd
+7vA800/kS/FPCVmgTW/BaqZwh11ma5eh0yXz5Jms5jUb2hmRrrSznLwzXVE4mLN
aKvlwOd6LW06tVK0CnTx9LwvQ4wAtzCAmnxiJm6Z/A6O42oDus+mww==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIULEE9q3QPcGx/aF56Kcjpmm1ioFgwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC3vG+t/eMT7XSPOqYmHBKFP7McTUIanto6rHDJPqU8A8Wl
7SexsxiHFxHDCRzy9Khcy4UR45LyfVKl3CkZJtV9CH6s08iXjmEeaFodkwOcPpFV
Bx48Id8Wcru9623+4zQJxrTRZXH7sKoTggSn0r2yAtCMzLiiMkko8EmRi20O79uz
5L/TWHKSdf0wm9re9H+TeYDdew/A8t8H5PCMNaNO+QNSWNDTCc+ChLdFQupbqWSl
3SpAvTkeGH1XjO/dxhUslzHrv7c92ZjvpHm8m2etcGP9VWW/6Lsa2/jDZaIGlc2P
z+2TGeC1E41wQNMXZbCnREjIvxlH18jknyxpuD/zAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBlmVB8gJE4++G5jc6nSW8v
sa0QsV3RRdPmBAAgY8A8L/7ACQZ179DmsXOkq760XMBftt4klfCznvD60MHxGnqv
PwIA1Y7TvhAK0WIiS1hgtNs3owkTx7jUfYmgaFmNMSdffod+mtu9VPzc7PsJgPpd
92uWyGDhoQcIWe1hqCWQqyNUI1BtX3LY/iIJRSKXpBlvGm9iPVzwyUNwn/W/Fpp/
nw0vwbvcgdvLzWi5gWxfLI9gTolr4ptKRlXB2IhmGBI/u1FCJiIr2qTuN/A0YUzj
7jhY0gEtutoz1XR9NXBhu4Y83ipJYcgHpRp8umv8HABdsSFSaOHahuYdUtnEPN8i
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAt7xvrf3jE+10jzqmJhwShT+zHE1CGp7aOqxwyT6lPAPFpe0n
sbMYhxcRwwkc8vSoXMuFEeOS8n1SpdwpGSbVfQh+rNPIl45hHmhaHZMDnD6RVQce
PCHfFnK7vett/uM0Cca00WVx+7CqE4IEp9K9sgLQjMy4ojJJKPBJkYttDu/bs+S/
01hyknX9MJva3vR/k3mA3XsPwPLfB+TwjDWjTvkDUljQ0wnPgoS3RULqW6lkpd0q
QL05Hhh9V4zv3cYVLJcx67+3PdmY76R5vJtnrXBj/VVlv+i7Gtv4w2WiBpXNj8/t
kxngtRONcEDTF2Wwp0RIyL8ZR9fI5J8sabg/8wIDAQABAoIBAE/7fp4+REibeL8U
59j1JXbN+PlcBGe0OQmLoXlphOJwPezyJPJtJUNBXqEJaYm1yUjD68SSzZgzx/Od
uGJTjmHkfchcVRjsiQiEop33Ln4omnlqJNZGZGfQQDv3raVkYHXVA0eYIptPF2pw
kfhAfAVuxjxUrhclTsW8fDoYeLwkHuL58MWFbGDyw0SudAtz8n7NdxvSbMvkWbQ+
Ep+ubuveJEfwUyARmbROSQW3xoXE2TFN7+AqVgB/EO7mmePbxenZNxioAw2Yg7bN
p1zXgandu7SsIy6Ef55n+Wa6L4COkAP3MI9zzMjQLZPfic8MjBLiWS3IKdWvaQ8b
o0PAzfECgYEA5Sg1kPQvzi1hMyy/IC47yJTDff0tDtVNUeia5PR0+TLMSQ+zV8aV
SF0jSWelubeForH8idRIRGXYsUOTpzqsrUEEat/a76EXZWKzjFu3Ec6K1lbEivE+
XPGERyPrZsodDNvHG6NCtkPzaSpVewPaFPRAvjkmfwa/nDOMTpIuu5kCgYEAzUIt
JyQ70a4ND6cwLwMrJKRr9tKLNs1uo1ydbTc+dMUY1RcA7/f2azjMiCYFh5jGr8fB
IzxihfIOBK6bNZLaAKG0KvKYziFn+xQcq7UNzjxL5d9sF6GvYfeP7CQEZo2CW6is
IT8QEELeT1OhJ8tqIKvN8Wl5bsMNiyGcY27s72sCgYAkki0yS/YRJmbbvullnltG
II+uXKhDNMFZMBEANw8v8e5uPoY1nOiYGt0VyufE4sf99f/Ck1FRMRvK9mjrCE8k
ezrUP5N2KLROJtlWrhBiVB8OI9zL+8IjHRwqKk5YIitOsQhunbh41BFVmD76GdxE
+dIXSZGeNhqAOC3NIEE7CQKBgDrTz5sbQGW9C5ND6IRg1RmgYi0QdMPVJvN9FMV7
gtP2tUJFYIhmOeLLGZufwg/10mQIzSrrIJWhJTFkVamKGB78OWXht7fETUfhoMH5
lyZXk60jVpiDR3+9cytLu1MlFYptkj/JEjKG5642msaL/zOz6cdZ4mrDTntku6yn
2xJXAoGACRTWI9QLv+ShImNhQiB8LY3lzWS7Aq/kj67Ckgnkmnx4hZYXAK9GhAbQ
/1GtPqVen6nheXIT4nPd5IsrJDiqGtRqkrPVnaMRY+LFlWqhSgfuRvpvU4OLLYTz
YguYBnaUWT39A1lMrPctjnoZ8AOPm+PNWDYRKspw0fO1qu9amV4=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUbQFwdJUJU+uQu6TnBtgwRJEi7wEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgxNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDN3kuiEl8fBuuVoTMZzBz317N5YG3fo2nA72B0U9WnL/2+
sJKlNZaw470ySXMzhTnoqUDMIwQEQ5Rg1A8x6HXfbbji8QRLXuLzQjAQ4FyWut5J
7CYx77zmIIm6VFkiIYVe3HTbPCXT0B8NO1xZKTSL8paxZMhwP8ayi5HrA6AhDjOU
YV/wuT6J0LKhDmYzmYQ83psJRjByuVusXMME2zNqDVFWntaiYisOTCHLLHOwGpbu
Xl3bjANI1h8krrvlIuPwC6aPsKTFn46gSVt6knt7DHsx2hb+25yiTp+q6GZRdowI
nesrczxajB3JCgkMZ9PAwYLZy6+0j+W6O376K2lRAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQALkQ8XNZHvx78zevHQduhO
2XETc4jnJgckpNvlytugIO5z5RvoGk7AGK8JLoxJFW+kU4qzGCVdZkskv8wMQfvu
+MNfRaMRqNvopXaSXRToKjxYp4BJCyiwvf6vaN7TVy46LVANv+lC6OPcLjmhR7h6
ZrOTrIiPl0U/Z5/2Lj3rRsYXsP5zYwQvnlH6xRoV7Vvy1/1JvJpn8pDGXqP2MNNS
RQvE+pTglxjjy8iFJo0ZUrjF3McGsC6OfAzAjM/ZVlzglko63S7VLcMlwjofy4OH
KUTPkS2bMqOmWwEeikF+7KfBCTPBNPj0Z5jvlaUwBt47PD/bLeaHD/hfcZn7yL52
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAzd5LohJfHwbrlaEzGcwc99ezeWBt36NpwO9gdFPVpy/9vrCS
pTWWsOO9MklzM4U56KlAzCMEBEOUYNQPMeh132244vEES17i80IwEOBclrreSewm
Me+85iCJulRZIiGFXtx02zwl09AfDTtcWSk0i/KWsWTIcD/GsouR6wOgIQ4zlGFf
8Lk+idCyoQ5mM5mEPN6bCUYwcrlbrFzDBNszag1RVp7WomIrDkwhyyxzsBqW7l5d
24wDSNYfJK675SLj8Aumj7CkxZ+OoElbepJ7ewx7MdoW/tucok6fquhmUXaMCJ3r
K3M8WowdyQoJDGfTwMGC2cuvtI/lujt++itpUQIDAQABAoIBAQCBUBbWERAq3x/v
9zewBqRTkewsW8PobC8rf7FooJhd0iljNGqI1+Z16jeXdMemHxNG77nCAGSvgPuc
7tc0lD4mQDeYZag657lK79JdZ3EBRRQH/wvm5h4Tt3CL2Bu88q1h7ryAUYG5UMuQ
di8F2nolRhYeC55T09utnznjE33sBG0dy92Y1fNMsOe9U26I0zcSBErth2wrLEWI
786uACcMa0C4fG6wK5apdmdhVzhk+6cvzLe3apBDuHFS9C8cFF+aR2YB1tqNX+uz
xvLjRl4r1cEcuuOwqXosG5PTkiZ9jnDzbaCCPqffDAR1zGkZ1jcIYPJjUVhKbACK
fRqKEWP5AoGBAOxz7KVDlf70YE5VsX425kOXNJU+nTNkkJi+J1wrXahFiFXO8588
B1YmpAgYeIry+zPomz1CQHy7c8lEpmtug6xh1qhbVIn1amR6ZzTD3sgmibYhCQf+
AF5DbvAOVSUKh6s0mVyE8BJlD2Z+kNcmmGsqf4tzeQI75WZFSEPByqkfAoGBAN7j
G743dRYAWZ26pVrusntoCmHRQyCvVVhlcCVuBpKjjb5tKE4RzaYlYIeySeGsS2CD
d9WDWoby0c5JK1Z4EWHgRocrosJrP/2vnJWd9MB2elsuxBieytVdIlOEgkcJlfji
Dlu7eYMAHzOt0X7Fo4YY6ce2fxTtcHvPQrmgje+PAoGAVodpr2TXTFDDuYb0iDqw
80UvMfqS7o67t5nGr50TDhQ7+yLb1obSLH3Bg1DpM/gNY4aY4McQ8FRs39emiyQL
PZckRcH+YuoTgCenAxE2wsoPlT3rnygdnGFTBLhKAl8jHM0H3mqrrB+djiV8/a8b
EgSgXjjorJ+cqFtsQZd2gYMCgYEA1FLm19J+oGHe/OmToccnkXWwBjTRzK4aECY5
qf5hFonlelUEAzLkg/SxOzM1PFzkRWGX43bI4ysngGqldS7V6DY9GYERAEIo6GLF
OKYLRNjYgEpRld6W/KBHFeZyMHfKPRgjc3FpNMkF8DYSDsD5oMHU2mJYNzhlYhwz
xR9UdrMCgYEAs+q1rX1EW/xyY66dEBpITgWeQTWijcq1//F4Eo6BB4Iv3eFi4XXA
QkmhyEIO9bv6m4O06x+TPEOdOAqUVc0+J7ZOlN7COFhdHOJZpYviTcOSYiK6vhSS
wanMzuVabo1DgS3/vlJwUL8YvE4Vcj97zdDiKNVGWjUVugqWS2vLDso=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_9: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_9: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
