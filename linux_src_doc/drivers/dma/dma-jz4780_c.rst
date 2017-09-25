.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/dma-jz4780.c

.. _`jz4780_dma_hwdesc`:

struct jz4780_dma_hwdesc
========================

.. c:type:: struct jz4780_dma_hwdesc

    descriptor structure read by the DMA controller.

.. _`jz4780_dma_hwdesc.definition`:

Definition
----------

.. code-block:: c

    struct jz4780_dma_hwdesc {
        uint32_t dcm;
        uint32_t dsa;
        uint32_t dta;
        uint32_t dtc;
        uint32_t sd;
        uint32_t drt;
        uint32_t reserved[2];
    }

.. _`jz4780_dma_hwdesc.members`:

Members
-------

dcm
    value for the DCM (channel command) register

dsa
    source address

dta
    target address

dtc
    transfer count (number of blocks of the transfer size specified in DCM
    to transfer) in the low 24 bits, offset of the next descriptor from the
    descriptor base address in the upper 8 bits.

sd
    target/source stride difference (in stride transfer mode).

drt
    request type

reserved
    *undescribed*

.. This file was automatic generated / don't edit.

