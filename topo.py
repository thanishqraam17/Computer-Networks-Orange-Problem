from mininet.topo import Topo

class RecoveryTopo(Topo):
    def build(self):
        s1, s2, s3 = self.addSwitch('s1'), self.addSwitch('s2'), self.addSwitch('s3')
        h1, h2 = self.addHost('h1', ip='10.0.0.1'), self.addHost('h2', ip='10.0.0.2')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        
        # Redundant paths
        self.addLink(s1, s2) # Primary Path
        self.addLink(s1, s3) # Backup Path
        self.addLink(s3, s2) # Backup Path

topos = {'recovery': (lambda: RecoveryTopo())}
