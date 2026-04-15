from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpid_to_str
from pox.lib.addresses import EthAddr

log = core.getLogger()

class FailureRecovery (object):
  def __init__ (self):
    core.openflow.addListeners(self)
    core.openflow_discovery.addListeners(self)

  def _handle_LinkEvent (self, event):
    l = event.link
    if event.removed:
      log.warning("LINK FAILURE DETECTED between %s and %s", l.dpid1, l.dpid2)
      # This triggers the spanning tree to find a new path
      core.spanning_tree._handle_LinkEvent(event)

  def _handle_ConnectionUp (self, event):
    log.info("Switch %s has connected", dpid_to_str(event.dpid))
    # Push basic flow rules to allow traffic
    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)

def launch ():
  # Start the required POX modules
  core.registerNew(FailureRecovery)
  import pox.openflow.discovery
  pox.openflow.discovery.launch()
  import pox.openflow.spanning_tree
  pox.openflow.spanning_tree.launch(no_flood = True, hold_down = True)
