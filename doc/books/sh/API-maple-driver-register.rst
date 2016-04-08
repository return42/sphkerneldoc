
.. _API-maple-driver-register:

=====================
maple_driver_register
=====================

*man maple_driver_register(9)*

*4.6.0-rc1*

register a maple driver


Synopsis
========

.. c:function:: int maple_driver_register( struct maple_driver * drv )

Arguments
=========

``drv``
    maple driver to be registered.


Description
===========

Registers the passed in ``drv``, while updating the bus type. Devices with matching function IDs will be automatically probed.
