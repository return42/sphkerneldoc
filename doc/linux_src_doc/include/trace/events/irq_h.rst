.. -*- coding: utf-8; mode: rst -*-

=====
irq.h
=====

.. _`trace_irq_handler_entry`:

trace_irq_handler_entry
=======================

.. c:function:: void trace_irq_handler_entry (int irq, struct irqaction *action)

    called immediately before the irq action handler

    :param int irq:
        irq number

    :param struct irqaction \*action:
        pointer to struct irqaction


.. _`trace_irq_handler_entry.description`:

Description
-----------

The struct irqaction pointed to by ``action`` contains various
information about the handler, including the device name,
``action``\ ->name, and the device id, ``action``\ ->dev_id. When used in
conjunction with the irq_handler_exit tracepoint, we can figure
out irq handler latencies.


.. _`trace_irq_handler_exit`:

trace_irq_handler_exit
======================

.. c:function:: void trace_irq_handler_exit (int irq, struct irqaction *action, int ret)

    called immediately after the irq action handler returns

    :param int irq:
        irq number

    :param struct irqaction \*action:
        pointer to struct irqaction

    :param int ret:
        return value


.. _`trace_irq_handler_exit.description`:

Description
-----------

If the ``ret`` value is set to IRQ_HANDLED, then we know that the corresponding
``action``\ ->handler scuccessully handled this irq. Otherwise, the irq might be
a shared irq line, or the irq was not handled successfully. Can be used in
conjunction with the irq_handler_entry to understand irq handler latencies.


.. _`trace_softirq_entry`:

trace_softirq_entry
===================

.. c:function:: void trace_softirq_entry (unsigned int vec_nr)

    called immediately before the softirq handler

    :param unsigned int vec_nr:
        softirq vector number


.. _`trace_softirq_entry.description`:

Description
-----------

When used in combination with the softirq_exit tracepoint
we can determine the softirq handler routine.


.. _`trace_softirq_exit`:

trace_softirq_exit
==================

.. c:function:: void trace_softirq_exit (unsigned int vec_nr)

    called immediately after the softirq handler returns

    :param unsigned int vec_nr:
        softirq vector number


.. _`trace_softirq_exit.description`:

Description
-----------

When used in combination with the softirq_entry tracepoint
we can determine the softirq handler routine.


.. _`trace_softirq_raise`:

trace_softirq_raise
===================

.. c:function:: void trace_softirq_raise (unsigned int vec_nr)

    called immediately when a softirq is raised

    :param unsigned int vec_nr:
        softirq vector number


.. _`trace_softirq_raise.description`:

Description
-----------

When used in combination with the softirq_entry tracepoint
we can determine the softirq raise to run latency.

