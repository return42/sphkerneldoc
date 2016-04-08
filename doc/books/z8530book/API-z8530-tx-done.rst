
.. _API-z8530-tx-done:

=============
z8530_tx_done
=============

*man z8530_tx_done(9)*

*4.6.0-rc1*

TX complete callback


Synopsis
========

.. c:function:: void z8530_tx_done( struct z8530_channel * c )

Arguments
=========

``c``
    The channel that completed a transmit.


Description
===========

This is called when we complete a packet send. We wake the queue, start the next packet going and then free the buffer of the existing packet. This code is fairly timing sensitive.

Called with the register lock held.
