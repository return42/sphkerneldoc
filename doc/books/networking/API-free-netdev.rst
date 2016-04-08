
.. _API-free-netdev:

===========
free_netdev
===========

*man free_netdev(9)*

*4.6.0-rc1*

free network device


Synopsis
========

.. c:function:: void free_netdev( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

This function does the last stage of destroying an allocated device interface. The reference to the device object is released. If this is the last reference then it will be freed.
Must be called in process context.
