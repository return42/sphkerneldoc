
.. _API-preempt-notifier-register:

=========================
preempt_notifier_register
=========================

*man preempt_notifier_register(9)*

*4.6.0-rc1*

tell me when current is being preempted & rescheduled


Synopsis
========

.. c:function:: void preempt_notifier_register( struct preempt_notifier * notifier )

Arguments
=========

``notifier``
    notifier struct to register
