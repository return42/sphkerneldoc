.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/brcmnand/brcmnand.c

.. _`brcmnand_fill_dma_desc`:

brcmnand_fill_dma_desc
======================

.. c:function:: int brcmnand_fill_dma_desc(struct brcmnand_host *host, struct brcm_nand_dma_desc *desc, u64 addr, dma_addr_t buf, u32 len, u8 dma_cmd, bool begin, bool end, dma_addr_t next_desc)

    :param host:
        *undescribed*
    :type host: struct brcmnand_host \*

    :param desc:
        *undescribed*
    :type desc: struct brcm_nand_dma_desc \*

    :param addr:
        *undescribed*
    :type addr: u64

    :param buf:
        *undescribed*
    :type buf: dma_addr_t

    :param len:
        *undescribed*
    :type len: u32

    :param dma_cmd:
        *undescribed*
    :type dma_cmd: u8

    :param begin:
        *undescribed*
    :type begin: bool

    :param end:
        *undescribed*
    :type end: bool

    :param next_desc:
        *undescribed*
    :type next_desc: dma_addr_t

.. _`brcmnand_fill_dma_desc.following-ahead-of-time`:

following ahead of time
-----------------------

- Is this descriptor the beginning or end of a linked list?
- What is the (DMA) address of the next descriptor in the linked list?

.. _`brcmnand_dma_run`:

brcmnand_dma_run
================

.. c:function:: void brcmnand_dma_run(struct brcmnand_host *host, dma_addr_t desc)

    :param host:
        *undescribed*
    :type host: struct brcmnand_host \*

    :param desc:
        *undescribed*
    :type desc: dma_addr_t

.. This file was automatic generated / don't edit.

