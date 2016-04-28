.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-rx-done:

=============
z8530_rx_done
=============

*man z8530_rx_done(9)*

*4.6.0-rc5*

Receive completion callback


Synopsis
========

.. c:function:: void z8530_rx_done( struct z8530_channel * c )

Arguments
=========

``c``
    The channel that completed a receive


Description
===========

A new packet is complete. Our goal here is to get back into receive mode
as fast as possible. On the Z85230 we could change to using ESCC mode,
but on the older chips we have no choice. We flip to the new buffer
immediately in DMA mode so that the DMA of the next frame can occur
while we are copying the previous buffer to an sk_buff

Called with the lock held


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
