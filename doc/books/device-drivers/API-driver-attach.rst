
.. _API-driver-attach:

=============
driver_attach
=============

*man driver_attach(9)*

*4.6.0-rc1*

try to bind driver to devices.


Synopsis
========

.. c:function:: int driver_attach( struct device_driver * drv )

Arguments
=========

``drv``
    driver.


Description
===========

Walk the list of devices that the bus has on it and try to match the driver with each one. If ``driver_probe_device`` returns 0 and the ``dev``->driver is set, we've found a
compatible pair.
