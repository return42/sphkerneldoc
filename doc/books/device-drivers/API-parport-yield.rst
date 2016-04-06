
.. _API-parport-yield:

=============
parport_yield
=============

*man parport_yield(9)*

*4.6.0-rc1*

relinquish a parallel port temporarily


Synopsis
========

.. c:function:: int parport_yield( struct pardevice * dev )

Arguments
=========

``dev``
    a device on the parallel port


Description
===========

This function relinquishes the port if it would be helpful to other drivers to do so. Afterwards it tries to reclaim the port using ``parport_claim``, and the return value is the
same as for ``parport_claim``. If it fails, the port is left unclaimed and it is the driver's responsibility to reclaim the port.

The ``parport_yield`` and ``parport_yield_blocking`` functions are for marking points in the driver at which other drivers may claim the port and use their devices. Yielding the
port is similar to releasing it and reclaiming it, but is more efficient because no action is taken if there are no other devices needing the port. In fact, nothing is done even if
there are other devices waiting but the current device is still within its “timeslice”. The default timeslice is half a second, but it can be adjusted via the /proc interface.
