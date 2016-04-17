.. -*- coding: utf-8; mode: rst -*-

====
hw.h
====


.. _`dwc2_hcd_dma_desc`:

struct dwc2_hcd_dma_desc
========================

.. c:type:: dwc2_hcd_dma_desc

    Host-mode DMA descriptor structure


.. _`dwc2_hcd_dma_desc.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hcd_dma_desc {
    u32 status;
    u32 buf;
  };


.. _`dwc2_hcd_dma_desc.members`:

Members
-------

:``status``:
    DMA descriptor status quadlet

:``buf``:
    DMA descriptor data buffer pointer




.. _`dwc2_hcd_dma_desc.dma-descriptor-structure-contains-two-quadlets`:

DMA Descriptor structure contains two quadlets
----------------------------------------------

Status quadlet and Data buffer pointer.

