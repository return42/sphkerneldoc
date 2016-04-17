.. -*- coding: utf-8; mode: rst -*-

==========
brcmnand.c
==========


.. _`brcmnand_fill_dma_desc`:

brcmnand_fill_dma_desc
======================

.. c:function:: int brcmnand_fill_dma_desc (struct brcmnand_host *host, struct brcm_nand_dma_desc *desc, u64 addr, dma_addr_t buf, u32 len, u8 dma_cmd, bool begin, bool end, dma_addr_t next_desc)

    :param struct brcmnand_host \*host:

        *undescribed*

    :param struct brcm_nand_dma_desc \*desc:

        *undescribed*

    :param u64 addr:

        *undescribed*

    :param dma_addr_t buf:

        *undescribed*

    :param u32 len:

        *undescribed*

    :param u8 dma_cmd:

        *undescribed*

    :param bool begin:

        *undescribed*

    :param bool end:

        *undescribed*

    :param dma_addr_t next_desc:

        *undescribed*



.. _`brcmnand_fill_dma_desc.following-ahead-of-time`:

following ahead of time
-----------------------

- Is this descriptor the beginning or end of a linked list?
- What is the (DMA) address of the next descriptor in the linked list?



.. _`brcmnand_dma_run`:

brcmnand_dma_run
================

.. c:function:: void brcmnand_dma_run (struct brcmnand_host *host, dma_addr_t desc)

    :param struct brcmnand_host \*host:

        *undescribed*

    :param dma_addr_t desc:

        *undescribed*

