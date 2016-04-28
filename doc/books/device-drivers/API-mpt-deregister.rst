.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-deregister:

==============
mpt_deregister
==============

*man mpt_deregister(9)*

*4.6.0-rc5*

Deregister a protocol drivers resources.


Synopsis
========

.. c:function:: void mpt_deregister( u8 cb_idx )

Arguments
=========

``cb_idx``
    previously registered callback handle


Description
===========

Each protocol-specific driver should call this routine when its module
is unloaded.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
