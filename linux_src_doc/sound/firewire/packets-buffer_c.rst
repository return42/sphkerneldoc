.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/packets-buffer.c

.. _`iso_packets_buffer_init`:

iso_packets_buffer_init
=======================

.. c:function:: int iso_packets_buffer_init(struct iso_packets_buffer *b, struct fw_unit *unit, unsigned int count, unsigned int packet_size, enum dma_data_direction direction)

    allocates the memory for packets

    :param b:
        the buffer structure to initialize
    :type b: struct iso_packets_buffer \*

    :param unit:
        the device at the other end of the stream
    :type unit: struct fw_unit \*

    :param count:
        the number of packets
    :type count: unsigned int

    :param packet_size:
        the (maximum) size of a packet, in bytes
    :type packet_size: unsigned int

    :param direction:
        \ ``DMA_TO_DEVICE``\  or \ ``DMA_FROM_DEVICE``\ 
    :type direction: enum dma_data_direction

.. _`iso_packets_buffer_destroy`:

iso_packets_buffer_destroy
==========================

.. c:function:: void iso_packets_buffer_destroy(struct iso_packets_buffer *b, struct fw_unit *unit)

    frees packet buffer resources

    :param b:
        the buffer structure to free
    :type b: struct iso_packets_buffer \*

    :param unit:
        the device at the other end of the stream
    :type unit: struct fw_unit \*

.. This file was automatic generated / don't edit.

