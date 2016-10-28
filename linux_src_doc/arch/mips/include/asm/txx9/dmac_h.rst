.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/txx9/dmac.h

.. _`txx9dmac_platform_data`:

struct txx9dmac_platform_data
=============================

.. c:type:: struct txx9dmac_platform_data

    Controller configuration parameters

.. _`txx9dmac_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct txx9dmac_platform_data {
        int memcpy_chan;
        bool have_64bit_regs;
    }

.. _`txx9dmac_platform_data.members`:

Members
-------

memcpy_chan
    Channel used for DMA_MEMCPY

have_64bit_regs
    DMAC have 64 bit registers

.. _`txx9dmac_chan_platform_data`:

struct txx9dmac_chan_platform_data
==================================

.. c:type:: struct txx9dmac_chan_platform_data

    Channel configuration parameters

.. _`txx9dmac_chan_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct txx9dmac_chan_platform_data {
        struct platform_device *dmac_dev;
    }

.. _`txx9dmac_chan_platform_data.members`:

Members
-------

dmac_dev
    A platform device for DMAC

.. _`txx9dmac_slave`:

struct txx9dmac_slave
=====================

.. c:type:: struct txx9dmac_slave

    Controller-specific information about a slave

.. _`txx9dmac_slave.definition`:

Definition
----------

.. code-block:: c

    struct txx9dmac_slave {
        u64 tx_reg;
        u64 rx_reg;
        unsigned int reg_width;
    }

.. _`txx9dmac_slave.members`:

Members
-------

tx_reg
    physical address of data register used for
    memory-to-peripheral transfers

rx_reg
    physical address of data register used for
    peripheral-to-memory transfers

reg_width
    peripheral register width

.. This file was automatic generated / don't edit.

