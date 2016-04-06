
.. _API-parport-open:

============
parport_open
============

*man parport_open(9)*

*4.6.0-rc1*

find a device by canonical device number


Synopsis
========

.. c:function:: struct pardevice ⋆ parport_open( int devnum, const char * name )

Arguments
=========

``devnum``
    canonical device number

``name``
    name to associate with the device


Description
===========

This function is similar to ``parport_register_device``, except that it locates a device by its number rather than by the port it is attached to.

All parameters except for ``devnum`` are the same as for ``parport_register_device``. The return value is the same as for ``parport_register_device``.
