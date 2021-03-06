.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/da8xx_remoteproc.c

.. _`da8xx_rproc_mem`:

struct da8xx_rproc_mem
======================

.. c:type:: struct da8xx_rproc_mem

    internal memory structure

.. _`da8xx_rproc_mem.definition`:

Definition
----------

.. code-block:: c

    struct da8xx_rproc_mem {
        void __iomem *cpu_addr;
        phys_addr_t bus_addr;
        u32 dev_addr;
        size_t size;
    }

.. _`da8xx_rproc_mem.members`:

Members
-------

cpu_addr
    MPU virtual address of the memory region

bus_addr
    Bus address used to access the memory region

dev_addr
    Device address of the memory region from DSP view

size
    Size of the memory region

.. _`da8xx_rproc`:

struct da8xx_rproc
==================

.. c:type:: struct da8xx_rproc

    da8xx remote processor instance state

.. _`da8xx_rproc.definition`:

Definition
----------

.. code-block:: c

    struct da8xx_rproc {
        struct rproc *rproc;
        struct da8xx_rproc_mem *mem;
        int num_mems;
        struct clk *dsp_clk;
        struct reset_control *dsp_reset;
        void (*ack_fxn)(struct irq_data *data);
        struct irq_data *irq_data;
        void __iomem *chipsig;
        void __iomem *bootreg;
        int irq;
    }

.. _`da8xx_rproc.members`:

Members
-------

rproc
    rproc handle

mem
    internal memory regions data

num_mems
    number of internal memory regions

dsp_clk
    placeholder for platform's DSP clk

dsp_reset
    *undescribed*

ack_fxn
    chip-specific ack function for ack'ing irq

irq_data
    ack_fxn function parameter

chipsig
    virt ptr to DSP interrupt registers (CHIPSIG & CHIPSIG_CLR)

bootreg
    virt ptr to DSP boot address register (HOST1CFG)

irq
    irq # used by this instance

.. _`handle_event`:

handle_event
============

.. c:function:: irqreturn_t handle_event(int irq, void *p)

    inbound virtqueue message workqueue function

    :param irq:
        *undescribed*
    :type irq: int

    :param p:
        *undescribed*
    :type p: void \*

.. _`handle_event.description`:

Description
-----------

This function is registered as a kernel thread and is scheduled by the
kernel handler.

.. _`da8xx_rproc_callback`:

da8xx_rproc_callback
====================

.. c:function:: irqreturn_t da8xx_rproc_callback(int irq, void *p)

    inbound virtqueue message handler

    :param irq:
        *undescribed*
    :type irq: int

    :param p:
        *undescribed*
    :type p: void \*

.. _`da8xx_rproc_callback.description`:

Description
-----------

This handler is invoked directly by the kernel whenever the remote
core (DSP) has modified the state of a virtqueue.  There is no
"payload" message indicating the virtqueue index as is the case with
mailbox-based implementations on OMAP4.  As such, this handler "polls"
each known virtqueue index for every invocation.

.. This file was automatic generated / don't edit.

