.. -*- coding: utf-8; mode: rst -*-

===========
dma-atmel.h
===========


.. _`at_dma_platform_data`:

struct at_dma_platform_data
===========================

.. c:type:: at_dma_platform_data

    Controller configuration parameters


.. _`at_dma_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct at_dma_platform_data {
    unsigned int nr_channels;
    dma_cap_mask_t cap_mask;
  };


.. _`at_dma_platform_data.members`:

Members
-------

:``nr_channels``:
    Number of channels supported by hardware (max 8)

:``cap_mask``:
    dma_capability flags supported by the platform




.. _`at_dma_slave`:

struct at_dma_slave
===================

.. c:type:: at_dma_slave

    Controller-specific information about a slave


.. _`at_dma_slave.definition`:

Definition
----------

.. code-block:: c

  struct at_dma_slave {
    struct device * dma_dev;
    u32 cfg;
  };


.. _`at_dma_slave.members`:

Members
-------

:``dma_dev``:
    required DMA master device

:``cfg``:
    Platform-specific initializer for the CFG register


