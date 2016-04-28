.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-sync:

========
spi_sync
========

*man spi_sync(9)*

*4.6.0-rc5*

blocking/synchronous SPI data transfers


Synopsis
========

.. c:function:: int spi_sync( struct spi_device * spi, struct spi_message * message )

Arguments
=========

``spi``
    device with which data will be exchanged

``message``
    describes the data transfers


Context
=======

can sleep


Description
===========

This call may only be used from a context that may sleep. The sleep is
non-interruptible, and has no timeout. Low-overhead controller drivers
may DMA directly into and out of the message buffers.

Note that the SPI device's chip select is active during the message, and
then is normally disabled between messages. Drivers for some
frequently-used devices may want to minimize costs of selecting a chip,
by leaving it selected in anticipation that the next message will go to
the same chip. (That may increase power usage.)

Also, the caller is guaranteeing that the memory associated with the
message will not be freed before this call returns.


Return
======

zero on success, else a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
