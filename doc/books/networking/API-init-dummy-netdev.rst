
.. _API-init-dummy-netdev:

=================
init_dummy_netdev
=================

*man init_dummy_netdev(9)*

*4.6.0-rc1*

init a dummy network device for NAPI


Synopsis
========

.. c:function:: int init_dummy_netdev( struct net_device * dev )

Arguments
=========

``dev``
    device to init


Description
===========

This takes a network device structure and initialize the minimum amount of fields so it can be used to schedule NAPI polls without registering a full blown interface. This is to be
used by drivers that need to tie several hardware interfaces to a single NAPI poll scheduler due to HW limitations.
