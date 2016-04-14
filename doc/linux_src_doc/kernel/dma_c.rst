.. -*- coding: utf-8; mode: rst -*-

=====
dma.c
=====

.. _`request_dma`:

request_dma
===========

.. c:function:: int request_dma (unsigned int dmanr, const char *device_id)

    request and reserve a system DMA channel

    :param unsigned int dmanr:
        DMA channel number

    :param const char \*device_id:
        reserving device ID string, used in /proc/dma


.. _`free_dma`:

free_dma
========

.. c:function:: void free_dma (unsigned int dmanr)

    free a reserved system DMA channel

    :param unsigned int dmanr:
        DMA channel number

