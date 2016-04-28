.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-async:

=========
spi_async
=========

*man spi_async(9)*

*4.6.0-rc5*

asynchronous SPI transfer


Synopsis
========

.. c:function:: int spi_async( struct spi_device * spi, struct spi_message * message )

Arguments
=========

``spi``
    device with which data will be exchanged

``message``
    describes the data transfers, including completion callback


Context
=======

any (irqs may be blocked, etc)


Description
===========

This call may be used in_irq and other contexts which can't sleep, as
well as from task contexts which can sleep.

The completion callback is invoked in a context which can't sleep.
Before that invocation, the value of message->status is undefined. When
the callback is issued, message->status holds either zero (to indicate
complete success) or a negative error code. After that callback returns,
the driver which issued the transfer request may deallocate the
associated memory; it's no longer in use by any SPI core or controller
driver code.

Note that although all messages to a spi_device are handled in FIFO
order, messages may go to different devices in other orders. Some device
might be higher priority, or have various “hard” access time
requirements, for example.

On detection of any fault during the transfer, processing of the entire
message is aborted, and the device is deselected. Until returning from
the associated message completion callback, no other spi_message queued
to that device will be processed. (This rule applies equally to all the
synchronous transfer calls, which are wrappers around this core
asynchronous primitive.)


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
