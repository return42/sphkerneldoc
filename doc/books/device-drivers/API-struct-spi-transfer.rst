.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-transfer:

===================
struct spi_transfer
===================

*man struct spi_transfer(9)*

*4.6.0-rc5*

a read/write buffer pair


Synopsis
========

.. code-block:: c

    struct spi_transfer {
      const void * tx_buf;
      void * rx_buf;
      unsigned len;
      dma_addr_t tx_dma;
      dma_addr_t rx_dma;
      struct sg_table tx_sg;
      struct sg_table rx_sg;
      unsigned cs_change:1;
      unsigned tx_nbits:3;
      unsigned rx_nbits:3;
    #define SPI_NBITS_SINGLE    0x01
    #define SPI_NBITS_DUAL      0x02
    #define SPI_NBITS_QUAD      0x04
      u8 bits_per_word;
      u16 delay_usecs;
      u32 speed_hz;
      struct list_head transfer_list;
    };


Members
=======

tx_buf
    data to be written (dma-safe memory), or NULL

rx_buf
    data to be read (dma-safe memory), or NULL

len
    size of rx and tx buffers (in bytes)

tx_dma
    DMA address of tx_buf, if ``spi_message``.is_dma_mapped

rx_dma
    DMA address of rx_buf, if ``spi_message``.is_dma_mapped

tx_sg
    Scatterlist for transmit, currently not for client use

rx_sg
    Scatterlist for receive, currently not for client use

cs_change
    affects chipselect after this transfer completes

tx_nbits
    number of bits used for writing. If 0 the default
    (SPI_NBITS_SINGLE) is used.

rx_nbits
    number of bits used for reading. If 0 the default
    (SPI_NBITS_SINGLE) is used.

bits_per_word
    select a bits_per_word other than the device default for this
    transfer. If 0 the default (from ``spi_device``) is used.

delay_usecs
    microseconds to delay after this transfer before (optionally)
    changing the chipselect status, then starting the next transfer or
    completing this ``spi_message``.

speed_hz
    Select a speed other than the device default for this transfer. If 0
    the default (from ``spi_device``) is used.

transfer_list
    transfers are sequenced through ``spi_message``.transfers


Description
===========

SPI transfers always write the same number of bytes as they read.
Protocol drivers should always provide ``rx_buf`` and/or ``tx_buf``. In
some cases, they may also want to provide DMA addresses for the data
being transferred; that may reduce overhead, when the underlying driver
uses dma.

If the transmit buffer is null, zeroes will be shifted out while filling
``rx_buf``. If the receive buffer is null, the data shifted in will be
discarded. Only “len” bytes shift out (or in). It's an error to try to
shift out a partial word. (For example, by shifting out three bytes with
word size of sixteen or twenty bits; the former uses two bytes per word,
the latter uses four bytes.)

In-memory data values are always in native CPU byte order, translated
from the wire byte order (big-endian except with SPI_LSB_FIRST). So
for example when bits_per_word is sixteen, buffers are 2N bytes long
(``len`` = 2N) and hold N sixteen bit words in CPU byte order.

When the word size of the SPI transfer is not a power-of-two multiple of
eight bits, those in-memory words include extra bits. In-memory words
are always seen by protocol drivers as right-justified, so the undefined
(rx) or unused (tx) bits are always the most significant bits.

All SPI transfers start with the relevant chipselect active. Normally it
stays selected until after the last transfer in a message. Drivers can
affect the chipselect signal using cs_change.

(i) If the transfer isn't the last one in the message, this flag is used
to make the chipselect briefly go inactive in the middle of the message.
Toggling chipselect in this way may be needed to terminate a chip
command, letting a single spi_message perform all of group of chip
transactions together.

(ii) When the transfer is the last one in the message, the chip may stay
selected until the next transfer. On multi-device SPI busses with
nothing blocking messages going to other devices, this is just a
performance hint; starting a message to another device deselects this
one. But in other cases, this can be used to ensure correctness. Some
devices need protocol transactions to be built from a series of
spi_message submissions, where the content of one message is determined
by the results of previous messages and where the whole transaction ends
when the chipselect goes intactive.

When SPI can transfer in 1x,2x or 4x. It can get this transfer
information from device through ``tx_nbits`` and ``rx_nbits``. In
Bi-direction, these two should both be set. User can set transfer mode
with SPI_NBITS_SINGLE(1x) SPI_NBITS_DUAL(2x) and
SPI_NBITS_QUAD(4x) to support these three transfer.

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
