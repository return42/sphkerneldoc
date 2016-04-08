
.. _API-z8530-shutdown:

==============
z8530_shutdown
==============

*man z8530_shutdown(9)*

*4.6.0-rc1*

Shutdown a Z8530 device


Synopsis
========

.. c:function:: int z8530_shutdown( struct z8530_dev * dev )

Arguments
=========

``dev``
    The Z8530 chip to shutdown


Description
===========

We set the interrupt handlers to silence any interrupts. We then reset the chip and wait 100uS to be sure the reset completed. Just in case the caller then tries to do stuff.

This is called without the lock held
