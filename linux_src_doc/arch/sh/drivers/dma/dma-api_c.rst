.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/drivers/dma/dma-api.c

.. _`request_dma_bycap`:

request_dma_bycap
=================

.. c:function:: int request_dma_bycap(const char **dmac, const char **caps, const char *dev_id)

    Allocate a DMA channel based on its capabilities

    :param dmac:
        List of DMA controllers to search
    :type dmac: const char \*\*

    :param caps:
        List of capabilities
    :type caps: const char \*\*

    :param dev_id:
        *undescribed*
    :type dev_id: const char \*

.. _`request_dma_bycap.description`:

Description
-----------

Search all channels of all DMA controllers to find a channel which
matches the requested capabilities. The result is the channel
number if a match is found, or \ ``-ENODEV``\  if no match is found.

Note that not all DMA controllers export capabilities, in which
case they can never be allocated using this API, and so
\ :c:func:`request_dma`\  must be used specifying the channel number.

.. This file was automatic generated / don't edit.

