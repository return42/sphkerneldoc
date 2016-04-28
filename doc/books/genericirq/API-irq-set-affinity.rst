.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-affinity:

================
irq_set_affinity
================

*man irq_set_affinity(9)*

*4.6.0-rc5*

Set the irq affinity of a given irq


Synopsis
========

.. c:function:: int irq_set_affinity( unsigned int irq, const struct cpumask * cpumask )

Arguments
=========

``irq``
    Interrupt to set affinity

``cpumask``
    cpumask


Description
===========

Fails if cpumask does not contain an online CPU


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
