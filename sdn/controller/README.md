# Installation of controller HP VAN SDN

1. Download Controller from:
    
    `https://h10145.www1.hp.com/downloads/DownloadSoftware.aspx?SoftwareReleaseUId=17523&ProductNumber=J9863AAE&lang=&cc=&prodSeriesId=&SaidNumber=`

2. Unzip hpe-van-sdn-ctlr-2.7.18-x64

3. Edit line 17 in install.bash if you have another version than hp-sdn-ctl_2.7.18.0503_amd64.deb

4. Run install script:
    
    `./install.bash`

5. Go to website (Replace __ipaddress__ with ip address of your server - see `ifconfig`):
    
    `https://ipaddress:8443/sdn/ui/`

6. Username and password:
    
    `username: sdn`
    `password: skyline`