
.. _API-struct-rio-mport-attr:

=====================
struct rio_mport_attr
=====================

*man struct rio_mport_attr(9)*

*4.6.0-rc1*

RIO mport device attributes


Synopsis
========

.. code-block:: c

    struct rio_mport_attr {
      int flags;
      int link_speed;
      int link_width;
      int dma_max_sge;
      int dma_max_size;
      int dma_align;
    };


Members
=======

flags
    mport device capability flags

link_speed
    SRIO link speed value (as defined by RapidIO specification)

link_width
    SRIO link width value (as defined by RapidIO specification)

dma_max_sge
    number of SG list entries that can be handled by DMA channel(s)

dma_max_size
    max number of bytes in single DMA transfer (SG entry)

dma_align
    alignment shift for DMA operations (as for other DMA operations)
