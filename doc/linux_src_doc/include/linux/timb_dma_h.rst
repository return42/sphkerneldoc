.. -*- coding: utf-8; mode: rst -*-

==========
timb_dma.h
==========


.. _`timb_dma_platform_data_channel`:

struct timb_dma_platform_data_channel
=====================================

.. c:type:: timb_dma_platform_data_channel

    Description of each individual DMA channel for the timberdale DMA driver


.. _`timb_dma_platform_data_channel.definition`:

Definition
----------

.. code-block:: c

  struct timb_dma_platform_data_channel {
    bool rx;
    unsigned int bytes_per_line;
    unsigned int descriptors;
    unsigned int descriptor_elements;
  };


.. _`timb_dma_platform_data_channel.members`:

Members
-------

:``rx``:
    true if this channel handles data in the direction to
    the CPU.

:``bytes_per_line``:
    Number of bytes per line, this is specific for channels
    handling video data. For other channels this shall be left to 0.

:``descriptors``:
    Number of descriptors to allocate for this channel.

:``descriptor_elements``:
    Number of elements in each descriptor.




.. _`timb_dma_platform_data`:

struct timb_dma_platform_data
=============================

.. c:type:: timb_dma_platform_data

    Platform data of the timberdale DMA driver


.. _`timb_dma_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct timb_dma_platform_data {
    unsigned nr_channels;
    struct timb_dma_platform_data_channel channels[32];
  };


.. _`timb_dma_platform_data.members`:

Members
-------

:``nr_channels``:
    Number of defined channels in the channels array.

:``channels[32]``:
    Definition of the each channel.


