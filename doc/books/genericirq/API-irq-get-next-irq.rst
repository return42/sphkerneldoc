.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-get-next-irq:

================
irq_get_next_irq
================

*man irq_get_next_irq(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
