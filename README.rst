
=================
Network UPS tools
=================

This repo contains Robotice drivers for NUT.

The primary goal of the Network UPS Tools (NUT) project is to provide support for Power Devices, such as Uninterruptible Power Supplies, Power Distribution Units and Solar Controllers.

NUT provides many control and monitoring features, with a uniform control and management interface.

More than 100 different manufacturers, and several thousands models are compatible.


Requirements
------------

* installed NUT and configured driver for you UPS


Installation
------------

* TODO

Usage
-----

.. code-block:: bash

    # search first available ups on localhost
    python driver.py

    python driver.py 127.0.0.1 eaton5e


Read More
---------

* http://www.networkupstools.org/
* https://raw.githubusercontent.com/networkupstools/nut/master/scripts/python/module/PyNUT.py