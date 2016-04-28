.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-cpu-offline:

===============
irq_cpu_offline
===============

*man irq_cpu_offline(9)*

*4.6.0-rc5*

Invoke all irq_cpu_offline functions.


Synopsis
========

.. c:function:: void irq_cpu_offline( void )

Arguments
=========

``void``
    no arguments


Description
===========

Iterate through all irqs and invoke the chip.\ ``irq_cpu_offline`` for
each.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
