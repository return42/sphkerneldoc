
.. _API-z8530-tx-clear:

==============
z8530_tx_clear
==============

*man z8530_tx_clear(9)*

*4.6.0-rc1*

Handle TX events from a stopped chip


Synopsis
========

.. c:function:: void z8530_tx_clear( struct z8530_channel * c )

Arguments
=========

``c``
    Z8530 channel to shut up


Description
===========

Transmit interrupt vectors for a Z8530 that is in 'parked' mode. For machines with PCI Z85x30 cards, or level triggered interrupts (eg the MacII) we must clear the interrupt cause
or die.
