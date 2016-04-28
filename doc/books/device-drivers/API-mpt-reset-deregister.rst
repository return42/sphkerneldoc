.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-reset-deregister:

====================
mpt_reset_deregister
====================

*man mpt_reset_deregister(9)*

*4.6.0-rc5*

Deregister protocol-specific IOC reset handler.


Synopsis
========

.. c:function:: void mpt_reset_deregister( u8 cb_idx )

Arguments
=========

``cb_idx``
    previously registered callback handle


Description
===========

Each protocol-specific driver should call this routine when it does not
(or can no longer) handle IOC reset handling, or when its module is
unloaded.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
