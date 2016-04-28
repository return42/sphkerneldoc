.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-mport-chk-dev-access:

========================
rio_mport_chk_dev_access
========================

*man rio_mport_chk_dev_access(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
