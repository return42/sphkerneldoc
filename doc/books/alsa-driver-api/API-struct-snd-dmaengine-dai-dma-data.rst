.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-dmaengine-dai-dma-data:

=================================
struct snd_dmaengine_dai_dma_data
=================================

*man struct snd_dmaengine_dai_dma_data(9)*

*4.6.0-rc5*

DAI DMA configuration data


Synopsis
========

.. code-block:: c

    struct snd_dmaengine_dai_dma_data {
      dma_addr_t addr;
      enum dma_slave_buswidth addr_width;
      u32 maxburst;
      unsigned int slave_id;
      void * filter_data;
      const char * chan_name;
      unsigned int fifo_size;
    };


Members
=======

addr
    Address of the DAI data source or destination register.

addr_width
    Width of the DAI data source or destination register.

maxburst
    Maximum number of words(note: words, as in units of the
    src_addr_width member, not bytes) that can be send to or received
    from the DAI in one burst.

slave_id
    Slave requester id for the DMA channel.

filter_data
    Custom DMA channel filter data, this will usually be used when
    requesting the DMA channel.

chan_name
    Custom channel name to use when requesting DMA channel.

fifo_size
    FIFO size of the DAI controller in bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
