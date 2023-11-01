import sims4.commands
import services
from alarms import add_alarm, cancel_alarm
from date_and_time import TimeSpan
from sims4.directory_watcher_handler import DirectoryWatcherHandler#Maybe use

@sims4.commands.Command('start', command_type=sims4.commands.CommandType.Live, console_type=sims4.commands.CommandType.Cheat)
def start(_connection=None):
    sim = services.get_active_sim()
    sim.co = 0
    output = sims4.commands.CheatOutput(_connection)
    alarms.start(alarms)
    output("Creating handle.last name change soon")
class alarms:
    def __init__(self):
        self._alarm_handle = None
    def start(self):
        self._alarm_handle = add_alarm(self, TimeSpan.ONE, self._tick, repeating=True)
        sim = services.get_active_sim()
        sim.sim_info.first_name = "created alarmhandle" + str(self._alarm_handle) + "." + "Owner:" + str(self._alarm_handle.owner)
    def _tick(self):
        sim = services.get_active_sim()
        sim.co += 1
        sim.sim_info.last_name = "Count:" + str(sim.co)
        
"""
Alarmhandler need class

import the from alarms import add_alarm, cancel_alarm
from date_and_time import TimeSpan

Write the
add_alarm(self, TimeSpan.ONE, self._tick, repeating=True)

create def _tick
def _tick(self):
  #Do somethings from here
  pass
?
"""
