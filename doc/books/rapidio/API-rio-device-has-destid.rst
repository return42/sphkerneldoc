.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-device-has-destid:

=====================
rio_device_has_destid
=====================

*man rio_device_has_destid(9)*

*4.6.0-rc5*

Test if a device contains a destination ID register


Synopsis
========

.. c:function:: int rio_device_has_destid( struct rio_mport * port, int src_ops, int dst_ops )

Arguments
=========

``port``
    Master port to issue transaction

``src_ops``
    RIO device source operations

``dst_ops``
    RIO device destination operations


Description
===========

Checks the provided ``src_ops`` and ``dst_ops`` for the necessary
transaction capabilities that indicate whether or not a device will
implement a destination ID register. Returns 1 if true or 0 if false.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
