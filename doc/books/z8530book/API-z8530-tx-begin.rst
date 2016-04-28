.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-tx-begin:

==============
z8530_tx_begin
==============

*man z8530_tx_begin(9)*

*4.6.0-rc5*

Begin packet transmission


Synopsis
========

.. c:function:: void z8530_tx_begin( struct z8530_channel * c )

Arguments
=========

``c``
    The Z8530 channel to kick


Description
===========

This is the speed sensitive side of transmission. If we are called and
no buffer is being transmitted we commence the next buffer. If nothing
is queued we idle the sync.


Note
====

We are handling this code path in the interrupt path, keep it fast or
bad things will happen.

Called with the lock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
