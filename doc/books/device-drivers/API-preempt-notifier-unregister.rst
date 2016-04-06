
.. _API-preempt-notifier-unregister:

===========================
preempt_notifier_unregister
===========================

*man preempt_notifier_unregister(9)*

*4.6.0-rc1*

no longer interested in preemption notifications


Synopsis
========

.. c:function:: void preempt_notifier_unregister( struct preempt_notifier * notifier )

Arguments
=========

``notifier``
    notifier struct to unregister


Description
===========

This is ⋆not⋆ safe to call from within a preemption notifier.
