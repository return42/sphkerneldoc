
.. _API-handle-percpu-irq:

=================
handle_percpu_irq
=================

*man handle_percpu_irq(9)*

*4.6.0-rc1*

Per CPU local irq handler


Synopsis
========

.. c:function:: void handle_percpu_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Per CPU interrupts on SMP machines without locking requirements
