from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )
        s9 = self.addSwitch( 's9' )
#       s10 = self.addSwitch( 's10' )
#       s11 = self.addSwitch( 's11' )
        s12 = self.addSwitch( 's12' )
#       s13 = self.addSwitch( 's13' )
#       s14 = self.addSwitch( 's14' )
#       s15 = self.addSwitch( 's15' )
#       s16 = self.addSwitch( 's16' )
#       s17 = self.addSwitch( 's17' )
#       s18 = self.addSwitch( 's18' )
#       s19 = self.addSwitch( 's19' )
#       s20 = self.addSwitch( 's20' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( s1, s3 )
        self.addLink( s1, s4 )
        self.addLink( s1, s2 )
        self.addLink( s2, s6 )
        self.addLink( s3, s4 )
        self.addLink( s3, s5 )
        self.addLink( s5, s7 )
        self.addLink( s5, s8 )
        self.addLink( s6, s8 )
        self.addLink( s6, s9 )
#       self.addLink( s7, 10 )
        self.addLink( s7, s12 )
        self.addLink( s8, s12 )
#       self.addLink( s9, s11 )
        self.addLink( s9, s12 )
#       self.addLink( s10, s13 )
#       self.addLink( s10, s15 )
#       self.addLink( s11, s13 )
#       self.addLink( s11, s16 )
#       self.addLink( s13, s15 )
#       self.addLink( s14, s16 )
#       self.addLink( s14, s19 )
#       self.addLink( s15, s16 )
#       self.addLink( s15, s18 )
#       self.addLink( s17, s18 )
#       self.addLink( s17, s19 )
#       self.addLink( s17, s20 )
#       self.addLink( s18, s20 )
#       self.addLink( s19, s20 )
#       self.addLink( s20, h2 )

topos = { 'mytopo': ( lambda: MyTopo() ) }