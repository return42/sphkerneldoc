.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-dfsdm.h

.. _`stm32_dfsdm_filter`:

struct stm32_dfsdm_filter
=========================

.. c:type:: struct stm32_dfsdm_filter

    structure relative to stm32 FDSDM filter

.. _`stm32_dfsdm_filter.definition`:

Definition
----------

.. code-block:: c

    struct stm32_dfsdm_filter {
        unsigned int iosr;
        unsigned int fosr;
        enum stm32_dfsdm_sinc_order ford;
        u64 res;
        unsigned int sync_mode;
        unsigned int fast;
    }

.. _`stm32_dfsdm_filter.members`:

Members
-------

iosr
    integrator oversampling

fosr
    filter oversampling

ford
    filter order

res
    output sample resolution

sync_mode
    filter synchronized with filter 0

fast
    filter fast mode

.. _`stm32_dfsdm_channel`:

struct stm32_dfsdm_channel
==========================

.. c:type:: struct stm32_dfsdm_channel

    structure relative to stm32 FDSDM channel

.. _`stm32_dfsdm_channel.definition`:

Definition
----------

.. code-block:: c

    struct stm32_dfsdm_channel {
        unsigned int id;
        unsigned int type;
        unsigned int src;
        unsigned int alt_si;
    }

.. _`stm32_dfsdm_channel.members`:

Members
-------

id
    id of the channel

type
    interface type linked to stm32_dfsdm_chan_type

src
    interface type linked to stm32_dfsdm_chan_src

alt_si
    alternative serial input interface

.. _`stm32_dfsdm`:

struct stm32_dfsdm
==================

.. c:type:: struct stm32_dfsdm

    stm32 FDSDM driver common data (for all instances)

.. _`stm32_dfsdm.definition`:

Definition
----------

.. code-block:: c

    struct stm32_dfsdm {
        void __iomem *base;
        phys_addr_t phys_base;
        struct regmap *regmap;
        struct stm32_dfsdm_filter *fl_list;
        unsigned int num_fls;
        struct stm32_dfsdm_channel *ch_list;
        unsigned int num_chs;
        unsigned int spi_master_freq;
    }

.. _`stm32_dfsdm.members`:

Members
-------

base
    control registers base cpu addr

phys_base
    DFSDM IP register physical address

regmap
    regmap for register read/write

fl_list
    filter resources list

num_fls
    number of filter resources available

ch_list
    channel resources list

num_chs
    number of channel resources available

spi_master_freq
    SPI clock out frequency

.. This file was automatic generated / don't edit.

