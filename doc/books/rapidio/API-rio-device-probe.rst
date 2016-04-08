
.. _API-rio-device-probe:

================
rio_device_probe
================

*man rio_device_probe(9)*

*4.6.0-rc1*

Tell if a RIO device structure has a matching RIO device id structure


Synopsis
========

.. c:function:: int rio_device_probe( struct device * dev )

Arguments
=========

``dev``
    the RIO device structure to match against


Description
===========

return 0 and set rio_dev->driver when drv claims rio_dev, else error
