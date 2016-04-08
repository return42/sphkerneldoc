
.. _API-skb-frag-dma-map:

================
skb_frag_dma_map
================

*man skb_frag_dma_map(9)*

*4.6.0-rc1*

maps a paged fragment via the DMA API


Synopsis
========

.. c:function:: dma_addr_t skb_frag_dma_map( struct device * dev, const skb_frag_t * frag, size_t offset, size_t size, enum dma_data_direction dir )

Arguments
=========

``dev``
    the device to map the fragment to

``frag``
    the paged fragment to map

``offset``
    the offset within the fragment (starting at the fragment's own offset)

``size``
    the number of bytes to map

``dir``
    the direction of the mapping (``PCI_DMA_``\ ⋆)


Description
===========

Maps the page associated with ``frag`` to ``device``.
