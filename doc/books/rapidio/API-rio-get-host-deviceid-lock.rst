
.. _API-rio-get-host-deviceid-lock:

==========================
rio_get_host_deviceid_lock
==========================

*man rio_get_host_deviceid_lock(9)*

*4.6.0-rc1*

Reads the Host Device ID Lock CSR on a device


Synopsis
========

.. c:function:: u16 rio_get_host_deviceid_lock( struct rio_mport * port, u8 hopcount )

Arguments
=========

``port``
    Master port to send transaction

``hopcount``
    Number of hops to the device


Description
===========

Used during enumeration to read the Host Device ID Lock CSR on a RIO device. Returns the value of the lock register.
