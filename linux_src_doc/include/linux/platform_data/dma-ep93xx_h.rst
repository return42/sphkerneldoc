.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/dma-ep93xx.h

.. _`ep93xx_dma_data`:

struct ep93xx_dma_data
======================

.. c:type:: struct ep93xx_dma_data

    configuration data for the EP93xx dmaengine

.. _`ep93xx_dma_data.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_dma_data {
        int port;
        enum dma_transfer_direction direction;
        const char *name;
    }

.. _`ep93xx_dma_data.members`:

Members
-------

port
    peripheral which is requesting the channel

direction
    TX/RX channel

name
    optional name for the channel, this is displayed in /proc/interrupts

.. _`ep93xx_dma_data.description`:

Description
-----------

This information is passed as private channel parameter in a filter
function. Note that this is only needed for slave/cyclic channels.  For
memcpy channels \ ``NULL``\  data should be passed.

.. _`ep93xx_dma_chan_data`:

struct ep93xx_dma_chan_data
===========================

.. c:type:: struct ep93xx_dma_chan_data

    platform specific data for a DMA channel

.. _`ep93xx_dma_chan_data.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_dma_chan_data {
        const char *name;
        void __iomem *base;
        int irq;
    }

.. _`ep93xx_dma_chan_data.members`:

Members
-------

name
    name of the channel, used for getting the right clock for the channel

base
    mapped registers

irq
    interrupt number used by this channel

.. _`ep93xx_dma_platform_data`:

struct ep93xx_dma_platform_data
===============================

.. c:type:: struct ep93xx_dma_platform_data

    platform data for the dmaengine driver

.. _`ep93xx_dma_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_dma_platform_data {
        struct ep93xx_dma_chan_data *channels;
        size_t num_channels;
    }

.. _`ep93xx_dma_platform_data.members`:

Members
-------

channels
    array of channels which are passed to the driver

num_channels
    number of channels in the array

.. _`ep93xx_dma_platform_data.description`:

Description
-----------

This structure is passed to the DMA engine driver via platform data. For
M2P channels, contract is that even channels are for TX and odd for RX.
There is no requirement for the M2M channels.

.. _`ep93xx_dma_chan_direction`:

ep93xx_dma_chan_direction
=========================

.. c:function:: enum dma_transfer_direction ep93xx_dma_chan_direction(struct dma_chan *chan)

    returns direction the channel can be used

    :param struct dma_chan \*chan:
        channel

.. _`ep93xx_dma_chan_direction.description`:

Description
-----------

This function can be used in filter functions to find out whether the
channel supports given DMA direction. Only M2P channels have such
limitation, for M2M channels the direction is configurable.

.. This file was automatic generated / don't edit.

