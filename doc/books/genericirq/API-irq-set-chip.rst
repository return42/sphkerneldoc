.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-chip:

============
irq_set_chip
============

*man irq_set_chip(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
