.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-tmc.h

.. _`tmc_drvdata`:

struct tmc_drvdata
==================

.. c:type:: struct tmc_drvdata

    specifics associated to an TMC component

.. _`tmc_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct tmc_drvdata {
        void __iomem *base;
        struct device *dev;
        struct coresight_device *csdev;
        struct miscdevice miscdev;
        spinlock_t spinlock;
        bool reading;
        char *buf;
        dma_addr_t paddr;
        void __iomem *vaddr;
        u32 size;
        u32 len;
        u32 mode;
        enum tmc_config_type config_type;
        enum tmc_mem_intf_width memwidth;
        u32 trigger_cntr;
    }

.. _`tmc_drvdata.members`:

Members
-------

base
    memory mapped base address for this component.

dev
    the device entity associated to this component.

csdev
    component vitals needed by the framework.

miscdev
    specifics to handle "/dev/xyz.tmc" entry.

spinlock
    only one at a time pls.

reading
    *undescribed*

buf
    area of memory where trace data get sent.

paddr
    DMA start location in RAM.

vaddr
    virtual representation of \ ``paddr``\ .

size
    trace buffer size.

len
    size of the available trace.

mode
    how this TMC is being used.

config_type
    TMC variant, must be of type \ ``tmc_config_type``\ .

memwidth
    width of the memory interface databus, in bytes.

trigger_cntr
    amount of words to store after a trigger.

.. This file was automatic generated / don't edit.

