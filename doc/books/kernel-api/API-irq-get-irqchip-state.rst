
.. _API-irq-get-irqchip-state:

=====================
irq_get_irqchip_state
=====================

*man irq_get_irqchip_state(9)*

*4.6.0-rc1*

returns the irqchip state of a interrupt.


Synopsis
========

.. c:function:: int irq_get_irqchip_state( unsigned int irq, enum irqchip_irq_state which, bool * state )

Arguments
=========

``irq``
    Interrupt line that is forwarded to a VM

``which``
    One of IRQCHIP_STATE_⋆ the caller wants to know about

``state``
    a pointer to a boolean where the state is to be storeed


Description
===========

This call snapshots the internal irqchip state of an interrupt, returning into ``state`` the bit corresponding to stage ``which``

This function should be called with preemption disabled if the interrupt controller has per-cpu registers.
