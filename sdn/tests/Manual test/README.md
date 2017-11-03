# Manual test

1. Run mininet:

    `sudo mn --controller=remote,ip=ipaddress --custom topologyFile --topo=mytopo --link=tc --mac`

    *ipaddress* - ip address of your controller

    *topologyFile* -  [topology file](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xkanuch-xjanec/blob/master/sdn/topology/topologySDN.py)

2. Test connectivity:

    `pingall`

3. Run *HTTP server* on host h2:

    `h2 python -m SimpleHTTPServer 80 &`

4. Run *tcpping* on host h1:

    `xterm h1`

and in h1 console run:

    `tcpping h2`

5. Put link down in mininet:

    `link s1 s2 down`

    and take a look at response time from h2 in h1 console

6. You can give more lines down, which makes loop in our topology
