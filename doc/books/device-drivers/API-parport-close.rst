
.. _API-parport-close:

=============
parport_close
=============

*man parport_close(9)*

*4.6.0-rc1*

close a device opened with ``parport_open``


Synopsis
========

.. c:function:: void parport_close( struct pardevice * dev )

Arguments
=========

``dev``
    device to close


Description
===========

This is to ``parport_open`` as ``parport_unregister_device`` is to ``parport_register_device``.
