.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/dma.c

.. _`request_dma`:

request_dma
===========

.. c:function:: int request_dma(unsigned int dmanr, const char *device_id)

    request and reserve a system DMA channel

    :param dmanr:
        DMA channel number
    :type dmanr: unsigned int

    :param device_id:
        reserving device ID string, used in /proc/dma
    :type device_id: const char \*

.. _`free_dma`:

free_dma
========

.. c:function:: void free_dma(unsigned int dmanr)

    free a reserved system DMA channel

    :param dmanr:
        DMA channel number
    :type dmanr: unsigned int

.. This file was automatic generated / don't edit.

