
.. _API-dev-change-proto-down:

=====================
dev_change_proto_down
=====================

*man dev_change_proto_down(9)*

*4.6.0-rc1*

update protocol port state information


Synopsis
========

.. c:function:: int dev_change_proto_down( struct net_device * dev, bool proto_down )

Arguments
=========

``dev``
    device

``proto_down``
    new value


Description
===========

This info can be used by switch drivers to set the phys state of the port.
