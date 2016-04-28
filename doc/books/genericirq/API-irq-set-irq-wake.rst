.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-irq-wake:

================
irq_set_irq_wake
================

*man irq_set_irq_wake(9)*

*4.6.0-rc5*

control irq power management wakeup


Synopsis
========

.. c:function:: int irq_set_irq_wake( unsigned int irq, unsigned int on )

Arguments
=========

``irq``
    interrupt to control

``on``
    enable/disable power management wakeup


Description
===========

Enable/disable power management wakeup mode, which is disabled by
default. Enables and disables must match, just as they match for
non-wakeup mode support.

Wakeup mode lets this IRQ wake the system from sleep states like
“suspend to RAM”.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
