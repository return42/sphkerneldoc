.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-setup-device:

================
rio_setup_device
================

*man rio_setup_device(9)*

*4.6.0-rc5*

Allocates and sets up a RIO device


Synopsis
========

.. c:function:: struct rio_dev * rio_setup_device( struct rio_net * net, struct rio_mport * port, u16 destid, u8 hopcount, int do_enum )

Arguments
=========

``net``
    RIO network

``port``
    Master port to send transactions

``destid``
    Current destination ID

``hopcount``
    Current hopcount

``do_enum``
    Enumeration/Discovery mode flag


Description
===========

Allocates a RIO device and configures fields based on configuration
space contents. If device has a destination ID register, a destination
ID is either assigned in enumeration mode or read from configuration
space in discovery mode. If the device has switch capabilities, then a
switch is allocated and configured appropriately. Returns a pointer to a
RIO device on success or NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
