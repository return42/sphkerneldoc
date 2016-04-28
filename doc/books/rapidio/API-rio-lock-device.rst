.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-lock-device:

===============
rio_lock_device
===============

*man rio_lock_device(9)*

*4.6.0-rc5*

Acquires host device lock for specified device


Synopsis
========

.. c:function:: int rio_lock_device( struct rio_mport * port, u16 destid, u8 hopcount, int wait_ms )

Arguments
=========

``port``
    Master port to send transaction

``destid``
    Destination ID for device/switch

``hopcount``
    Hopcount to reach switch

``wait_ms``
    Max wait time in msec (0 = no timeout)


Description
===========

Attepts to acquire host device lock for specified device Returns 0 if
device lock acquired or EINVAL if timeout expires.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
