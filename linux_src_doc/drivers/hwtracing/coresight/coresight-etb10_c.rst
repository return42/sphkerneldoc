.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-etb10.c

.. _`etb_drvdata`:

struct etb_drvdata
==================

.. c:type:: struct etb_drvdata

    specifics associated to an ETB component

.. _`etb_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct etb_drvdata {
        void __iomem *base;
        struct device *dev;
        struct clk *atclk;
        struct coresight_device *csdev;
        struct miscdevice miscdev;
        spinlock_t spinlock;
        local_t reading;
        local_t mode;
        u8 *buf;
        u32 buffer_depth;
        u32 trigger_cntr;
    }

.. _`etb_drvdata.members`:

Members
-------

base
    memory mapped base address for this component.

dev
    the device entity associated to this component.

atclk
    optional clock for the core parts of the ETB.

csdev
    component vitals needed by the framework.

miscdev
    specifics to handle "/dev/xyz.etb" entry.

spinlock
    only one at a time pls.

reading
    synchronise user space access to etb buffer.

mode
    this ETB is being used.

buf
    area of memory where ETB buffer content gets sent.

buffer_depth
    size of \ ``buf``\ .

trigger_cntr
    amount of words to store after a trigger.

.. This file was automatic generated / don't edit.

