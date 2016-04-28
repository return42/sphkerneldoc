.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-wake-thread:

===============
irq_wake_thread
===============

*man irq_wake_thread(9)*

*4.6.0-rc5*

wake the irq thread for the action identified by dev_id


Synopsis
========

.. c:function:: void irq_wake_thread( unsigned int irq, void * dev_id )

Arguments
=========

``irq``
    Interrupt line

``dev_id``
    Device identity for which the thread should be woken


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
