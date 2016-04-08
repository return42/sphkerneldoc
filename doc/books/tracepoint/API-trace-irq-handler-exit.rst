
.. _API-trace-irq-handler-exit:

======================
trace_irq_handler_exit
======================

*man trace_irq_handler_exit(9)*

*4.6.0-rc1*

called immediately after the irq action handler returns


Synopsis
========

.. c:function:: void trace_irq_handler_exit( int irq, struct irqaction * action, int ret )

Arguments
=========

``irq``
    irq number

``action``
    pointer to struct irqaction

``ret``
    return value


Description
===========

If the ``ret`` value is set to IRQ_HANDLED, then we know that the corresponding ``action``->handler scuccessully handled this irq. Otherwise, the irq might be a shared irq line,
or the irq was not handled successfully. Can be used in conjunction with the irq_handler_entry to understand irq handler latencies.
