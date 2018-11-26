.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/dma-ste-dma40.h

.. _`stedma40_half_channel_info`:

struct stedma40_half_channel_info
=================================

.. c:type:: struct stedma40_half_channel_info

    dst/src channel configuration

.. _`stedma40_half_channel_info.definition`:

Definition
----------

.. code-block:: c

    struct stedma40_half_channel_info {
        bool big_endian;
        enum dma_slave_buswidth data_width;
        int psize;
        enum stedma40_flow_ctrl flow_ctrl;
    }

.. _`stedma40_half_channel_info.members`:

Members
-------

big_endian
    true if the src/dst should be read as big endian

data_width
    Data width of the src/dst hardware

psize
    *undescribed*

flow_ctrl
    Flow control on/off.

.. _`stedma40_chan_cfg`:

struct stedma40_chan_cfg
========================

.. c:type:: struct stedma40_chan_cfg

    Structure to be filled by client drivers.

.. _`stedma40_chan_cfg.definition`:

Definition
----------

.. code-block:: c

    struct stedma40_chan_cfg {
        enum dma_transfer_direction dir;
        bool high_priority;
        bool realtime;
        enum stedma40_mode mode;
        enum stedma40_mode_opt mode_opt;
        int dev_type;
        struct stedma40_half_channel_info src_info;
        struct stedma40_half_channel_info dst_info;
        bool use_fixed_channel;
        int phy_channel;
    }

.. _`stedma40_chan_cfg.members`:

Members
-------

dir
    MEM 2 MEM, PERIPH 2 MEM , MEM 2 PERIPH, PERIPH 2 PERIPH

high_priority
    true if high-priority

realtime
    true if realtime mode is to be enabled.  Only available on DMA40
    version 3+, i.e DB8500v2+

mode
    channel mode: physical, logical, or operation

mode_opt
    options for the chosen channel mode

dev_type
    src/dst device type (driver uses dir to figure out which)

src_info
    Parameters for dst half channel

dst_info
    Parameters for dst half channel

use_fixed_channel
    if true, use physical channel specified by phy_channel

phy_channel
    physical channel to use, only if use_fixed_channel is true

.. _`stedma40_chan_cfg.description`:

Description
-----------

This structure has to be filled by the client drivers.
It is recommended to do all dma configurations for clients in the machine.

.. _`stedma40_platform_data`:

struct stedma40_platform_data
=============================

.. c:type:: struct stedma40_platform_data

    Configuration struct for the dma device.

.. _`stedma40_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct stedma40_platform_data {
        int disabled_channels[STEDMA40_MAX_PHYS];
        int *soft_lli_chans;
        int num_of_soft_lli_chans;
        bool use_esram_lcla;
        int num_of_memcpy_chans;
        int num_of_phy_chans;
    }

.. _`stedma40_platform_data.members`:

Members
-------

disabled_channels
    A vector, ending with -1, that marks physical channels
    that are for different reasons not available for the driver.

soft_lli_chans
    A vector, that marks physical channels will use LLI by SW
    which avoids HW bug that exists in some versions of the controller.
    SoftLLI introduces relink overhead that could impact performace for
    certain use cases.

num_of_soft_lli_chans
    The number of channels that needs to be configured
    to use SoftLLI.

use_esram_lcla
    flag for mapping the lcla into esram region

num_of_memcpy_chans
    The number of channels reserved for memcpy.

num_of_phy_chans
    The number of physical channels implemented in HW.
    0 means reading the number of channels from DMA HW but this is only valid
    for 'multiple of 4' channels, like 8.

.. _`stedma40_filter`:

stedma40_filter
===============

.. c:function:: bool stedma40_filter(struct dma_chan *chan, void *data)

    Provides stedma40_chan_cfg to the ste_dma40 dma driver via the dmaengine framework. does some checking of what's provided.

    :param chan:
        dmaengine handle.
    :type chan: struct dma_chan \*

    :param data:
        Must be of type: struct stedma40_chan_cfg and is
        the configuration of the framework.
    :type data: void \*

.. _`stedma40_filter.description`:

Description
-----------

Never directly called by client. It used by dmaengine.


.. _`stedma40_slave_mem`:

stedma40_slave_mem
==================

.. c:function:: struct dma_async_tx_descriptor *stedma40_slave_mem(struct dma_chan *chan, dma_addr_t addr, unsigned int size, enum dma_transfer_direction direction, unsigned long flags)

    Transfers a raw data buffer to or from a slave (=device)

    :param chan:
        dmaengine handle
    :type chan: struct dma_chan \*

    :param addr:
        source or destination physicall address.
    :type addr: dma_addr_t

    :param size:
        bytes to transfer
    :type size: unsigned int

    :param direction:
        direction of transfer
    :type direction: enum dma_transfer_direction

    :param flags:
        is actually enum dma_ctrl_flags. See dmaengine.h
    :type flags: unsigned long

.. This file was automatic generated / don't edit.

