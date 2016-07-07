.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/da8xx_remoteproc.c

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
        struct clk *dsp_clk;
        void (* ack_fxn) (struct irq_data *data);
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

dsp_clk
    placeholder for platform's DSP clk

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

    :param int irq:
        *undescribed*

    :param void \*p:
        *undescribed*

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

    :param int irq:
        *undescribed*

    :param void \*p:
        *undescribed*

.. _`da8xx_rproc_callback.description`:

Description
-----------

This handler is invoked directly by the kernel whenever the remote
core (DSP) has modified the state of a virtqueue.  There is no
"payload" message indicating the virtqueue index as is the case with
mailbox-based implementations on OMAP4.  As such, this handler "polls"
each known virtqueue index for every invocation.

.. This file was automatic generated / don't edit.

