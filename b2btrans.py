# location: /usr/local/lib/sems/py_sems

from py_sems_log import *
from py_sems import *
from py_sems_lib import *

class PySemsScript(PySemsB2ABDialog):
# PySemsB2ABDialog includes access to the audio stream.
  "attempt to control lifetime of callee session"

  def __init__(self):
    debug("b2btrans--> __init__ ")
    self.calleeSession = None
    PySemsB2ABDialog.__init__(self)

  def onSessionStart(self,req):
    debug("b2btrans--> onSessionStart")
    PySemsB2ABDialog.onSessionStart(self,req)

  def onInvite(self,req):
    debug("b2btrans--> onInvite")
    PySemsB2ABDialog.onInvite(self,req)

  def onBye(self,req):
    debug("b2btrans--> onBye")
    PySemsB2ABDialog.onBye(self,req)

  def onCancel(self):
    debug("b2btrans--> onCancel")
    PySemsB2ABDialog.onCancel(self)

  def onDtmf(self,evt,duration):
    debug("b2btrans--> onDtmf")
    debug("p1=%d;p2=%d",(evt,duration))
    if evt == 1:
      debug("connectCallee 1 start")
      self.connectCallee("<sip:iphone@192.168.1.108>","sip:iphone@192.168.1.108","<sip:shaun@192.168.1.135>","sip:shaun@192.168.1.135")
      debug("connectCallee 1 stop")
    elif evt == 2:
      debug("connectCallee 2 start")
      self.connectCallee("<sip:11@192.168.1.111>","sip:11@192.168.1.111","<sip:shaun@192.168.1.135>","sip:shaun@192.168.1.135")
      debug("connectCallee 2 stop")
    elif evt == 3:
      debug("disconnecting callee session 3 start")
      if not self.calleeSession == None:
	self.calleeSession.disconnectSession()
      debug("disconnecting callee session 3 stop")
    elif evt == 4:
      debug("reconnecting callee session 4 start")
      if not self.calleeSession == None:
	self.calleeSession.connectSession()
      debug("reconnecting callee session 4 stop")
      
    PySemsB2ABDialog.onDtmf(self,evt,duration)

  def process(self,evt):
    debug("b2btrans--> process")
    debug("evt=%s",str(evt))
    PySemsB2ABDialog.process(self,evt)

  def createCalleeSession(self):
    debug("b2btrans--> createCalleeSession")
    self.calleeSession = PySemsB2ABDialog.createCalleeSession(self)
    return self.calleeSession

  def onB2ABEvent(self,evt):
    debug("b2btrans--> onB2ABEvent")
    debug("evt=%s",str(evt))
    PySemsB2ABDialog.onB2ABEvent(self,evt)

  def relayEvent(self,evt):
    debug("b2btrans--> relayEvent")
    debug("evt=%s",str(evt))
    PySemsB2ABDialog.relayEvent(self,evt)

# In PySemsB2ABDialog, there is a connectSession() and disconnectSession(). If I keep hold of the sessions, maybe they can be swapped?
