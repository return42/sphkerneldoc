.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-irqchip-state:

=====================
irq_set_irqchip_state
=====================

*man irq_set_irqchip_state(9)*

*4.6.0-rc5*

set the state of a forwarded interrupt.


Synopsis
========

.. c:function:: int irq_set_irqchip_state( unsigned int irq, enum irqchip_irq_state which, bool val )

Arguments
=========

``irq``
    Interrupt line that is forwarded to a VM

``which``
    State to be restored (one of IRQCHIP_STATE_*)

``val``
    Value corresponding to ``which``


Description
===========

This call sets the internal irqchip state of an interrupt, depending on
the value of ``which``.

This function should be called with preemption disabled if the interrupt
controller has per-cpu registers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
