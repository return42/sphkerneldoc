.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/hw.h

.. _`dwc2_dma_desc`:

struct dwc2_dma_desc
====================

.. c:type:: struct dwc2_dma_desc

    DMA descriptor structure, used for both host and gadget modes

.. _`dwc2_dma_desc.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_dma_desc {
        u32 status;
        u32 buf;
    }

.. _`dwc2_dma_desc.members`:

Members
-------

status
    DMA descriptor status quadlet

buf
    DMA descriptor data buffer pointer

.. _`dwc2_dma_desc.dma-descriptor-structure-contains-two-quadlets`:

DMA Descriptor structure contains two quadlets
----------------------------------------------

Status quadlet and Data buffer pointer.

.. This file was automatic generated / don't edit.

