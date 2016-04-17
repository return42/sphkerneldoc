.. -*- coding: utf-8; mode: rst -*-

==========
irq_poll.c
==========


.. _`irq_poll_sched`:

irq_poll_sched
==============

.. c:function:: void irq_poll_sched (struct irq_poll *iop)

    Schedule a run of the iopoll handler

    :param struct irq_poll \*iop:
        The parent iopoll structure



.. _`irq_poll_sched.description`:

Description
-----------

Add this irq_poll structure to the pending poll list and trigger the
raise of the blk iopoll softirq.



.. _`__irq_poll_complete`:

__irq_poll_complete
===================

.. c:function:: void __irq_poll_complete (struct irq_poll *iop)

    Mark this @iop as un-polled again

    :param struct irq_poll \*iop:
        The parent iopoll structure



.. _`__irq_poll_complete.description`:

Description
-----------

See :c:func:`irq_poll_complete`. This function must be called with interrupts
disabled.



.. _`irq_poll_complete`:

irq_poll_complete
=================

.. c:function:: void irq_poll_complete (struct irq_poll *iop)

    Mark this @iop as un-polled again

    :param struct irq_poll \*iop:
        The parent iopoll structure



.. _`irq_poll_complete.description`:

Description
-----------

If a driver consumes less than the assigned budget in its run of the
iopoll handler, it'll end the polled mode by calling this function. The
iopoll handler will not be invoked again before :c:func:`irq_poll_sched`
is called.



.. _`irq_poll_disable`:

irq_poll_disable
================

.. c:function:: void irq_poll_disable (struct irq_poll *iop)

    Disable iopoll on this @iop

    :param struct irq_poll \*iop:
        The parent iopoll structure



.. _`irq_poll_disable.description`:

Description
-----------

Disable io polling and wait for any pending callbacks to have completed.



.. _`irq_poll_enable`:

irq_poll_enable
===============

.. c:function:: void irq_poll_enable (struct irq_poll *iop)

    Enable iopoll on this @iop

    :param struct irq_poll \*iop:
        The parent iopoll structure



.. _`irq_poll_enable.description`:

Description
-----------

Enable iopoll on this ``iop``\ . Note that the handler run will not be
scheduled, it will only mark it as active.



.. _`irq_poll_init`:

irq_poll_init
=============

.. c:function:: void irq_poll_init (struct irq_poll *iop, int weight, irq_poll_fn *poll_fn)

    Initialize this @iop

    :param struct irq_poll \*iop:
        The parent iopoll structure

    :param int weight:
        The default weight (or command completion budget)

    :param irq_poll_fn \*poll_fn:
        The handler to invoke



.. _`irq_poll_init.description`:

Description
-----------

Initialize and enable this irq_poll structure.

