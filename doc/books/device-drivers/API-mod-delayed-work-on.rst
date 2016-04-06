
.. _API-mod-delayed-work-on:

===================
mod_delayed_work_on
===================

*man mod_delayed_work_on(9)*

*4.6.0-rc1*

modify delay of or queue a delayed work on specific CPU


Synopsis
========

.. c:function:: bool mod_delayed_work_on( int cpu, struct workqueue_struct * wq, struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``cpu``
    CPU number to execute work on

``wq``
    workqueue to use

``dwork``
    work to queue

``delay``
    number of jiffies to wait before queueing


Description
===========

If ``dwork`` is idle, equivalent to ``queue_delayed_work_on``; otherwise, modify ``dwork``'s timer so that it expires after ``delay``. If ``delay`` is zero, ``work`` is guaranteed
to be scheduled immediately regardless of its current state.


Return
======

``false`` if ``dwork`` was idle and queued, ``true`` if ``dwork`` was pending and its timer was modified.

This function is safe to call from any context including IRQ handler. See ``try_to_grab_pending`` for details.
