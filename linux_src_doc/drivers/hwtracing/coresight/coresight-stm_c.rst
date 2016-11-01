.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-stm.c

.. _`channel_space`:

struct channel_space
====================

.. c:type:: struct channel_space

    central management entity for extended ports

.. _`channel_space.definition`:

Definition
----------

.. code-block:: c

    struct channel_space {
        void __iomem *base;
        phys_addr_t phys;
        unsigned long *guaranteed;
    }

.. _`channel_space.members`:

Members
-------

base
    memory mapped base address where channels start.

phys
    physical base address of channel region.

guaranteed
    *undescribed*

.. _`stm_drvdata`:

struct stm_drvdata
==================

.. c:type:: struct stm_drvdata

    specifics associated to an STM component

.. _`stm_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct stm_drvdata {
        void __iomem *base;
        struct device *dev;
        struct clk *atclk;
        struct coresight_device *csdev;
        spinlock_t spinlock;
        struct channel_space chs;
        struct stm_data stm;
        local_t mode;
        u8 traceid;
        u32 write_bytes;
        u32 stmsper;
        u32 stmspscr;
        u32 numsp;
        u32 stmheer;
        u32 stmheter;
        u32 stmhebsr;
    }

.. _`stm_drvdata.members`:

Members
-------

base
    memory mapped base address for this component.

dev
    the device entity associated to this component.

atclk
    optional clock for the core parts of the STM.

csdev
    component vitals needed by the framework.

spinlock
    only one at a time pls.

chs
    the channels accociated to this STM.

stm
    structure associated to the generic STM interface.

mode
    this tracer's mode, i.e sysFS, or disabled.

traceid
    value of the current ID for this component.

write_bytes
    Maximus bytes this STM can write at a time.

stmsper
    settings for register STMSPER.

stmspscr
    settings for register STMSPSCR.

numsp
    the total number of stimulus port support by this STM.

stmheer
    settings for register STMHEER.

stmheter
    settings for register STMHETER.

stmhebsr
    settings for register STMHEBSR.

.. This file was automatic generated / don't edit.

