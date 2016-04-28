.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-reset:

===========
relay_reset
===========

*man relay_reset(9)*

*4.6.0-rc5*

reset the channel


Synopsis
========

.. c:function:: void relay_reset( struct rchan * chan )

Arguments
=========

``chan``
    the channel


Description
===========

This has the effect of erasing all data from all channel buffers and
restarting the channel in its initial state. The buffers are not freed,
so any mappings are still in effect.

NOTE. Care should be taken that the channel isn't actually being used by
anything when this call is made.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
