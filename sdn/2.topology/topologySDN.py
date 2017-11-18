from mininet.topo import Topo

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

        # Add links
        self.addLink( hosts[0], switches[0], bw=10, delay='1.5ms', loss=0 ) 
        self.addLink( hosts[1], switches[9], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[0], switches[1], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[0], switches[2], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[0], switches[3], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[1], switches[5], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[2], switches[3], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[2], switches[4], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[4], switches[6], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[4], switches[7], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[5], switches[7], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[5], switches[8], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[6], switches[9], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[7], switches[9], bw=10, delay='1.5ms', loss=0 )
        self.addLink( switches[8], switches[9], bw=10, delay='1.5ms', loss=0 )

topos = { 'mytopo': MyTopo }
