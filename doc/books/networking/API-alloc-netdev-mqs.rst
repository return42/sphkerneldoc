
.. _API-alloc-netdev-mqs:

================
alloc_netdev_mqs
================

*man alloc_netdev_mqs(9)*

*4.6.0-rc1*

allocate network device


Synopsis
========

.. c:function:: struct net_device ⋆ alloc_netdev_mqs( int sizeof_priv, const char * name, unsigned char name_assign_type, void (*setup) struct net_device *, unsigned int txqs, unsigned int rxqs )

Arguments
=========

``sizeof_priv``
    size of private data to allocate space for

``name``
    device name format string

``name_assign_type``
    origin of device name

``setup``
    callback to initialize device

``txqs``
    the number of TX subqueues to allocate

``rxqs``
    the number of RX subqueues to allocate


Description
===========

Allocates a struct net_device with private data area for driver use and performs basic initialization. Also allocates subqueue structs for each queue on the device.
