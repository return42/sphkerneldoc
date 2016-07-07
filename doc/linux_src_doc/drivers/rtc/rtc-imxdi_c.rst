.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-imxdi.c

.. _`imxdi_dev`:

struct imxdi_dev
================

.. c:type:: struct imxdi_dev

    private imxdi rtc data

.. _`imxdi_dev.definition`:

Definition
----------

.. code-block:: c

    struct imxdi_dev {
        struct platform_device *pdev;
        struct rtc_device *rtc;
        void __iomem *ioaddr;
        int irq;
        struct clk *clk;
        u32 dsr;
        spinlock_t irq_lock;
        wait_queue_head_t write_wait;
        struct mutex write_mutex;
        struct work_struct work;
    }

.. _`imxdi_dev.members`:

Members
-------

pdev
    pionter to platform dev

rtc
    pointer to rtc struct

ioaddr
    IO registers pointer

irq
    dryice normal interrupt

clk
    input reference clock

dsr
    copy of the DSR register

irq_lock
    interrupt enable register (DIER) lock

write_wait
    registers write complete queue

write_mutex
    serialize registers write

work
    schedule alarm work

.. This file was automatic generated / don't edit.

