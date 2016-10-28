.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/packets-buffer.c

.. _`iso_packets_buffer_init`:

iso_packets_buffer_init
=======================

.. c:function:: int iso_packets_buffer_init(struct iso_packets_buffer *b, struct fw_unit *unit, unsigned int count, unsigned int packet_size, enum dma_data_direction direction)

    allocates the memory for packets

    :param struct iso_packets_buffer \*b:
        the buffer structure to initialize

    :param struct fw_unit \*unit:
        the device at the other end of the stream

    :param unsigned int count:
        the number of packets

    :param unsigned int packet_size:
        the (maximum) size of a packet, in bytes

    :param enum dma_data_direction direction:
        \ ``DMA_TO_DEVICE``\  or \ ``DMA_FROM_DEVICE``\ 

.. _`iso_packets_buffer_destroy`:

iso_packets_buffer_destroy
==========================

.. c:function:: void iso_packets_buffer_destroy(struct iso_packets_buffer *b, struct fw_unit *unit)

    frees packet buffer resources

    :param struct iso_packets_buffer \*b:
        the buffer structure to free

    :param struct fw_unit \*unit:
        the device at the other end of the stream

.. This file was automatic generated / don't edit.

