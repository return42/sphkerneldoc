.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-irq-type:

================
irq_set_irq_type
================

*man irq_set_irq_type(9)*

*4.6.0-rc5*

set the irq trigger type for an irq


Synopsis
========

.. c:function:: int irq_set_irq_type( unsigned int irq, unsigned int type )

Arguments
=========

``irq``
    irq number

``type``
    IRQ_TYPE_{LEVEL,EDGE}_* value - see include/linux/irq.h


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
