.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-message:

==================
struct spi_message
==================

*man struct spi_message(9)*

*4.6.0-rc5*

one multi-segment SPI transaction


Synopsis
========

.. code-block:: c

    struct spi_message {
      struct list_head transfers;
      struct spi_device * spi;
      unsigned is_dma_mapped:1;
      void (* complete) (void *context);
      void * context;
      unsigned frame_length;
      unsigned actual_length;
      int status;
      struct list_head queue;
      void * state;
      struct list_head resources;
    };


Members
=======

transfers
    list of transfer segments in this transaction

spi
    SPI device to which the transaction is queued

is_dma_mapped
    if true, the caller provided both dma and cpu virtual addresses for
    each transfer buffer

complete
    called to report transaction completions

context
    the argument to ``complete`` when it's called

frame_length
    the total number of bytes in the message

actual_length
    the total number of bytes that were transferred in all successful
    segments

status
    zero for success, else negative errno

queue
    for use by whichever driver currently owns the message

state
    for use by whichever driver currently owns the message

resources
    for resource management when the spi message is processed


Description
===========

A ``spi_message`` is used to execute an atomic sequence of data
transfers, each represented by a struct spi_transfer. The sequence is
“atomic” in the sense that no other spi_message may use that SPI bus
until that sequence completes. On some systems, many such sequences can
execute as as single programmed DMA transfer. On all systems, these
messages are queued, and might complete after transactions to other
devices. Messages sent to a given spi_device are always executed in
FIFO order.

The code that submits an spi_message (and its spi_transfers) to the
lower layers is responsible for managing its memory. Zero-initialize
every field you don't set up explicitly, to insulate against future API
updates. After you submit a message and its transfers, ignore them until
its completion callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
