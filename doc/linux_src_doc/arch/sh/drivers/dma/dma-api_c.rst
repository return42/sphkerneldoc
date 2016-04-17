.. -*- coding: utf-8; mode: rst -*-

=========
dma-api.c
=========


.. _`request_dma_bycap`:

request_dma_bycap
=================

.. c:function:: int request_dma_bycap (const char **dmac, const char **caps, const char *dev_id)

    Allocate a DMA channel based on its capabilities

    :param const char \*\*dmac:
        List of DMA controllers to search

    :param const char \*\*caps:
        List of capabilities

    :param const char \*dev_id:

        *undescribed*



.. _`request_dma_bycap.description`:

Description
-----------

Search all channels of all DMA controllers to find a channel which
matches the requested capabilities. The result is the channel
number if a match is found, or ``-ENODEV`` if no match is found.

Note that not all DMA controllers export capabilities, in which
case they can never be allocated using this API, and so
:c:func:`request_dma` must be used specifying the channel number.

