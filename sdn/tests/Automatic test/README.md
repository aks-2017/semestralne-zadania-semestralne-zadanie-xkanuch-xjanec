# Automatic testing 
(not so reliable)

1. Change IP addres on line 48 in script to IP address of your controller:

    `47: def myTest():`

        `48: c = RemoteController('c', '192.168.56.102', 6633)`

2. Run script (Before running we recommend run command *sudo mn -c*):

    `sudo python test.py`

3. Look at your output in */tmp/output.txt*

    `cat /tmp/output.txt`

4. You can change configuration of link down in script adding or removing following line:

    `66: net.configLinkStatus('s1','s3','down')`


