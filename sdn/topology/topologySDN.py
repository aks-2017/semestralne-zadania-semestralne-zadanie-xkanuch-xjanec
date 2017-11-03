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
        self.addLink( hosts[0], switches[0] ) 
        self.addLink( hosts[1], switches[9] )
        self.addLink( switches[0], switches[1] )
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

topos = { 'mytopo': MyTopo }
