
.. _API-irq-set-chip:

============
irq_set_chip
============

*man irq_set_chip(9)*

*4.6.0-rc1*

set the irq chip for an irq


Synopsis
========

.. c:function:: int irq_set_chip( unsigned int irq, struct irq_chip * chip )

Arguments
=========

``irq``
    irq number

``chip``
    pointer to irq chip description structure
