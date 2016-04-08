
.. _API-handle-percpu-devid-irq:

=======================
handle_percpu_devid_irq
=======================

*man handle_percpu_devid_irq(9)*

*4.6.0-rc1*

Per CPU local irq handler with per cpu dev ids


Synopsis
========

.. c:function:: void handle_percpu_devid_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Per CPU interrupts on SMP machines without locking requirements. Same as ``handle_percpu_irq`` above but with the following extras:

action->percpu_dev_id is a pointer to percpu variables which contain the real device id for the cpu on which this handler is called
