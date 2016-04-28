.. -*- coding: utf-8; mode: rst -*-

.. _API-kstat-irqs-usr:

==============
kstat_irqs_usr
==============

*man kstat_irqs_usr(9)*

*4.6.0-rc5*

Get the statistics for an interrupt


Synopsis
========

.. c:function:: unsigned int kstat_irqs_usr( unsigned int irq )

Arguments
=========

``irq``
    The interrupt number


Description
===========

Returns the sum of interrupt counts on all cpus since boot for ``irq``.
Contrary to ``kstat_irqs`` this can be called from any preemptible
context. It's protected against concurrent removal of an interrupt
descriptor when sparse irqs are enabled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
