
.. _API-dev-hold:

========
dev_hold
========

*man dev_hold(9)*

*4.6.0-rc1*

get reference to device


Synopsis
========

.. c:function:: void dev_hold( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Hold reference to device to keep it from being freed.
