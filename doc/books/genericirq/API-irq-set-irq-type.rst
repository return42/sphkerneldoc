
.. _API-irq-set-irq-type:

================
irq_set_irq_type
================

*man irq_set_irq_type(9)*

*4.6.0-rc1*

set the irq trigger type for an irq


Synopsis
========

.. c:function:: int irq_set_irq_type( unsigned int irq, unsigned int type )

Arguments
=========

``irq``
    irq number

``type``
    IRQ_TYPE_{LEVEL,EDGE}_⋆ value - see include/linux/irq.h
