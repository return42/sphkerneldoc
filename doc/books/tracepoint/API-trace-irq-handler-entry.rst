
.. _API-trace-irq-handler-entry:

=======================
trace_irq_handler_entry
=======================

*man trace_irq_handler_entry(9)*

*4.6.0-rc1*

called immediately before the irq action handler


Synopsis
========

.. c:function:: void trace_irq_handler_entry( int irq, struct irqaction * action )

Arguments
=========

``irq``
    irq number

``action``
    pointer to struct irqaction


Description
===========

The struct irqaction pointed to by ``action`` contains various information about the handler, including the device name, ``action``->name, and the device id, ``action``->dev_id.
When used in conjunction with the irq_handler_exit tracepoint, we can figure out irq handler latencies.
