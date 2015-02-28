
from .nut import PyNUTClient



def get_data(sensor):

    results = []

    client = PyNUTClient(host=sensor.get("host", "127.0.0.1"))

    ups = sensor.get("name", None)

    for metric, value in client.GetUPSVars(ups = ups or client.get_avail_ups).iteritems():

        try:
            val = float(value)
        except Exception, e:
            pass

        results.append((metric, val))

    return results
