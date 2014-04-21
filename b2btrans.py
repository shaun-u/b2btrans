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
    debug("b2trans--> onSessionStart")

#next step: connect though invite


