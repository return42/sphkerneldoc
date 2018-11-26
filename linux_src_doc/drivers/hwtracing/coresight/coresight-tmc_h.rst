.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-tmc.h

.. _`etr_buf`:

struct etr_buf
==============

.. c:type:: struct etr_buf

    Details of the buffer used by ETR

.. _`etr_buf.definition`:

Definition
----------

.. code-block:: c

    struct etr_buf {
        enum etr_mode mode;
        bool full;
        ssize_t size;
        dma_addr_t hwaddr;
        unsigned long offset;
        s64 len;
        const struct etr_buf_operations *ops;
        void *private;
    }

.. _`etr_buf.members`:

Members
-------

mode
    Mode of the ETR buffer, contiguous, Scatter Gather etc.

full
    Trace data overflow

size
    Size of the buffer.

hwaddr
    Address to be programmed in the TMC:DBA{LO,HI}

offset
    Offset of the trace data in the buffer for consumption.

len
    Available trace data \ ``buf``\  (may round up to the beginning).

ops
    ETR buffer operations for the mode.

private
    Backend specific information for the buf

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
        union {
            char *buf;
            struct etr_buf *etr_buf;
        } ;
        u32 len;
        u32 size;
        u32 mode;
        enum tmc_config_type config_type;
        enum tmc_mem_intf_width memwidth;
        u32 trigger_cntr;
        u32 etr_caps;
        struct etr_buf *sysfs_buf;
        void *perf_data;
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

{unnamed_union}
    anonymous

buf
    Snapshot of the trace data for ETF/ETB.

etr_buf
    details of buffer used in TMC-ETR

len
    size of the available trace for ETF/ETB.

size
    trace buffer size for this TMC (common for all modes).

mode
    how this TMC is being used.

config_type
    TMC variant, must be of type \ ``tmc_config_type``\ .

memwidth
    width of the memory interface databus, in bytes.

trigger_cntr
    amount of words to store after a trigger.

etr_caps
    Bitmask of capabilities of the TMC ETR, inferred from the
    device configuration register (DEVID)

sysfs_buf
    *undescribed*

perf_data
    PERF buffer for ETR.

.. _`tmc_pages`:

struct tmc_pages
================

.. c:type:: struct tmc_pages

    Collection of pages used for SG.

.. _`tmc_pages.definition`:

Definition
----------

.. code-block:: c

    struct tmc_pages {
        int nr_pages;
        dma_addr_t *daddrs;
        struct page **pages;
    }

.. _`tmc_pages.members`:

Members
-------

nr_pages
    Number of pages in the list.

daddrs
    Array of DMA'able page address.

pages
    Array pages for the buffer.

.. This file was automatic generated / don't edit.

