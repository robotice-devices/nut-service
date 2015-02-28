"""
TODO

{'beeper.on': 'Obsolete (use beeper.enable)',
 'beeper.mute': 'Temporarily mute the UPS beeper', 
 'load.off.delay': 'Turn off the load with a delay (seconds)', 
 'shutdown.stop': 'Stop a shutdown in progress', 
 'beeper.disable': 'Disable the UPS beeper', 
 'load.off': 'Turn off the load immediately', 
 'beeper.off': 'Obsolete (use beeper.disable or beeper.mute)', 
 'beeper.enable': 'Enable the UPS beeper'}
"""

from .nut import PyNUTClient


def run(device, model_data, real_data=None):

    result = []

    client = PyNUTClient(host=device.get("host", "127.0.0.1"))

    ups = device.get("name", None)

    result = client.RunUPSCommand(ups=ups or client.get_avail_ups, command=model_data)

   	return result


