
.. _API-dev-set-mtu:

===========
dev_set_mtu
===========

*man dev_set_mtu(9)*

*4.6.0-rc1*

Change maximum transfer unit


Synopsis
========

.. c:function:: int dev_set_mtu( struct net_device * dev, int new_mtu )

Arguments
=========

``dev``
    device

``new_mtu``
    new transfer unit


Description
===========

Change the maximum transfer size of the network device.
