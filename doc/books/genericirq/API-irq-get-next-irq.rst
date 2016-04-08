
.. _API-irq-get-next-irq:

================
irq_get_next_irq
================

*man irq_get_next_irq(9)*

*4.6.0-rc1*

get next allocated irq number


Synopsis
========

.. c:function:: unsigned int irq_get_next_irq( unsigned int offset )

Arguments
=========

``offset``
    where to start the search


Description
===========

Returns next irq number after offset or nr_irqs if none is found.
