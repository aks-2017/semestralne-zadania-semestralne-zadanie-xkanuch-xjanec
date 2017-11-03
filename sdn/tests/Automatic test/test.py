from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from time import sleep
from mininet.node import RemoteController

m = 2
n = 10

class MyTopo( Topo ):
    "Topology of n switches and m hosts"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        hosts = []
        switches = []
        # Add hosts and switches
        for h in range(m):
                hosts.append(self.addHost('h%s' % (h+1)))

        for s in range(n):
                switches.append(self.addSwitch('s%s' % (s+1)))

        self.addLink(hosts[0], switches[0])
        self.addLink(hosts[1], switches[9])
        self.addLink(switches[0],switches[1])
        self.addLink( switches[0], switches[2] )
        self.addLink( switches[0], switches[3] )
        self.addLink( switches[1], switches[5] )
        self.addLink( switches[2], switches[3] )
        self.addLink( switches[2], switches[4] )
        self.addLink( switches[4], switches[6] )
        self.addLink( switches[4], switches[7] )
        self.addLink( switches[5], switches[7] )
        self.addLink( switches[5], switches[8] )
        self.addLink( switches[6], switches[9] )
        self.addLink( switches[7], switches[9] )
        self.addLink( switches[8], switches[9] )

def myTest():
        c = RemoteController('c', '192.168.56.102', 6633)
        topo = MyTopo()
        net = Mininet(topo, controller=None)
        net.addController(c)
        net.start()
        print "Testing connectivity"
        sleep(10)
        net.pingAll()
        sleep(10)
        net.pingAll()
        print "Running test"
        h1, h2 = net.get('h1', 'h2')
        h2.cmd('python -m SimpleHTTPServer 80 &')
        sleep(2)
        h1.cmd('tcpping 10.0.0.2 > /tmp/output.txt &')
        sleep(15)
        net.configLinkStatus('s1','s3','down')
        sleep(15)
        h1.cmd('kill %tcpping')
        h2.cmd('kill %python')
        net.stop()

if __name__ == '__main__':
       setLogLevel('info')
       myTest()

