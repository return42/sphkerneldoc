
.. _API-rio-mport-chk-dev-access:

========================
rio_mport_chk_dev_access
========================

*man rio_mport_chk_dev_access(9)*

*4.6.0-rc1*

Validate access to the specified device.


Synopsis
========

.. c:function:: int rio_mport_chk_dev_access( struct rio_mport * mport, u16 destid, u8 hopcount )

Arguments
=========

``mport``
    Master port to send transactions

``destid``
    Device destination ID in network

``hopcount``
    Number of hops into the network
