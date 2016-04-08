
.. _API-z8530-rx-clear:

==============
z8530_rx_clear
==============

*man z8530_rx_clear(9)*

*4.6.0-rc1*

Handle RX events from a stopped chip


Synopsis
========

.. c:function:: void z8530_rx_clear( struct z8530_channel * c )

Arguments
=========

``c``
    Z8530 channel to shut up


Description
===========

Receive interrupt vectors for a Z8530 that is in 'parked' mode. For machines with PCI Z85x30 cards, or level triggered interrupts (eg the MacII) we must clear the interrupt cause
or die.
