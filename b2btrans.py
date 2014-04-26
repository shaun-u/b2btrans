# location: /usr/local/lib/sems/py_sems

from py_sems_log import *
from py_sems import *
from py_sems_lib import *

class PySemsScript(PySemsB2ABDialog):
# PySemsB2ABDialog includes access to the audio stream.

  def __init__(self):
    debug("b2btrans--> __init__ ")
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
      self.connectCallee("<sip:shaun@10.0.2.15>","sip:shaun@10.0.2.15","<sip:me@mars.com>","sip:me@mars.com")
      debug("connectCallee 1 stop")
    PySemsB2ABDialog.onDtmf(self,evt,duration)

  def process(self,evt):
    debug("b2btrans--> process")
    debug("evt=%s",str(evt))
    PySemsB2ABDialog.process(self,evt)

  def createCalleeSession(self):
    debug("b2btrans--> createCalleeSession")
    return PySemsB2ABDialog.createCalleeSession(self)

  def onB2ABEvent(self,evt):
    debug("b2btrans--> onB2ABEvent")
    debug("evt=%s",str(evt))
    PySemsB2ABDialog.onB2ABEvent(self,evt)

  def relayEvent(self,evt):
    debug("b2btrans--> relayEvent")
    debug("evt=%s",str(evt))
    PySemsB2ABDialog.relayEvent(self,evt)


