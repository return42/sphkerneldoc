.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/musb/cppi_dma.c

.. _`cppi_next_rx_segment`:

cppi_next_rx_segment
====================

.. c:function:: void cppi_next_rx_segment(struct musb *musb, struct cppi_channel *rx, int onepacket)

    dma read for the next chunk of a buffer

    :param musb:
        the controller
    :type musb: struct musb \*

    :param rx:
        dma channel
    :type rx: struct cppi_channel \*

    :param onepacket:
        true unless caller treats short reads as errors, and
        performs fault recovery above usbcore.
    :type onepacket: int

.. _`cppi_next_rx_segment.context`:

Context
-------

controller irqlocked

.. _`cppi_next_rx_segment.description`:

Description
-----------

See above notes about why we can't use multi-BD RX queues except in
rare cases (mass storage class), and can never use the hardware "rndis"
mode (since it's not a "true" RNDIS mode) with complete safety..

It's ESSENTIAL that callers specify "onepacket" mode unless they kick in
code to recover from corrupted datastreams after each short transfer.

.. _`cppi_channel_program`:

cppi_channel_program
====================

.. c:function:: int cppi_channel_program(struct dma_channel *ch, u16 maxpacket, u8 mode, dma_addr_t dma_addr, u32 len)

    program channel for data transfer

    :param ch:
        the channel
    :type ch: struct dma_channel \*

    :param maxpacket:
        max packet size
    :type maxpacket: u16

    :param mode:
        For RX, 1 unless the usb protocol driver promised to treat
        all short reads as errors and kick in high level fault recovery.
        For TX, ignored because of RNDIS mode races/glitches.
    :type mode: u8

    :param dma_addr:
        dma address of buffer
    :type dma_addr: dma_addr_t

    :param len:
        length of buffer
    :type len: u32

.. _`cppi_channel_program.context`:

Context
-------

controller irqlocked

.. This file was automatic generated / don't edit.

