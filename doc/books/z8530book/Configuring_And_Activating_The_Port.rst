.. -*- coding: utf-8; mode: rst -*-

.. _Configuring_And_Activating_The_Port:

***********************************
Configuring And Activating The Port
***********************************

The Z85230 driver provides helper functions and tables to load the port
registers on the Z8530 chips. When programming the register settings for
a channel be aware that the documentation recommends initialisation
orders. Strange things happen when these are not followed.

:c:func:`z8530_channel_load()` takes an array of pairs of
initialisation values in an array of u8 type. The first value is the
Z8530 register number. Add 16 to indicate the alternate register bank on
the later chips. The array is terminated by a 255.

The driver provides a pair of public tables. The z8530_hdlc_kilostream
table is for the UK 'Kilostream' service and also happens to cover most
other end host configurations. The z8530_hdlc_kilostream_85230 table
is the same configuration using the enhancements of the 85230 chip. The
configuration loaded is standard NRZ encoded synchronous data with HDLC
bitstuffing. All of the timing is taken from the other end of the link.

When writing your own tables be aware that the driver internally tracks
register values. It may need to reload values. You should therefore be
sure to set registers 1-7, 9-11, 14 and 15 in all configurations. Where
the register settings depend on DMA selection the driver will update the
bits itself when you open or close. Loading a new table with the
interface open is not recommended.

There are three standard configurations supported by the core code. In
PIO mode the interface is programmed up to use interrupt driven PIO.
This places high demands on the host processor to avoid latency. The
driver is written to take account of latency issues but it cannot avoid
latencies caused by other drivers, notably IDE in PIO mode. Because the
drivers allocate buffers you must also prevent MTU changes while the
port is open.

Once the port is open it will call the rx_function of each channel
whenever a completed packet arrived. This is invoked from interrupt
context and passes you the channel and a network buffer (struct
sk_buff) holding the data. The data includes the CRC bytes so most
users will want to trim the last two bytes before processing the data.
This function is very timing critical. When you wish to simply discard
data the support code provides the function
:c:func:`z8530_null_rx()` to discard the data.

To active PIO mode sending and receiving the
:c:func:`z8530_sync_open()` is called. This expects to be passed the
network device and the channel. Typically this is called from your
network device open callback. On a failure a non zero error status is
returned. The :c:func:`z8530_sync_close()` function shuts down a PIO
channel. This must be done before the channel is opened again and before
the driver shuts down and unloads.

The ideal mode of operation is dual channel DMA mode. Here the kernel
driver will configure the board for DMA in both directions. The driver
also handles ISA DMA issues such as controller programming and the
memory range limit for you. This mode is activated by calling the
:c:func:`z8530_sync_dma_open()` function. On failure a non zero
error value is returned. Once this mode is activated it can be shut down
by calling the :c:func:`z8530_sync_dma_close()`. You must call the
close function matching the open mode you used.

The final supported mode uses a single DMA channel to drive the transmit
side. As the Z85C30 has a larger FIFO on the receive channel this tends
to increase the maximum speed a little. This is activated by calling the
:c:func:`z8530_sync_txdma_open()`. This returns a non zero error
code on failure. The :c:func:`z8530_sync_txdma_close()` function
closes down the Z8530 interface from this mode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
