
.. _API-irq-wake-thread:

===============
irq_wake_thread
===============

*man irq_wake_thread(9)*

*4.6.0-rc1*

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
