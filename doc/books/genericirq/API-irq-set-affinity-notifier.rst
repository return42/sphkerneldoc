.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-affinity-notifier:

=========================
irq_set_affinity_notifier
=========================

*man irq_set_affinity_notifier(9)*

*4.6.0-rc5*

control notification of IRQ affinity changes


Synopsis
========

.. c:function:: int irq_set_affinity_notifier( unsigned int irq, struct irq_affinity_notify * notify )

Arguments
=========

``irq``
    Interrupt for which to enable/disable notification

``notify``
    Context for notification, or ``NULL`` to disable notification.
    Function pointers must be initialised; the other fields will be
    initialised by this function.


Description
===========

Must be called in process context. Notification may only be enabled
after the IRQ is allocated and must be disabled before the IRQ is freed
using ``free_irq``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
