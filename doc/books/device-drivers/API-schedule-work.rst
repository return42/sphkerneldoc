
.. _API-schedule-work:

=============
schedule_work
=============

*man schedule_work(9)*

*4.6.0-rc1*

put work task in global workqueue


Synopsis
========

.. c:function:: bool schedule_work( struct work_struct * work )

Arguments
=========

``work``
    job to be done


Description
===========

Returns ``false`` if ``work`` was already on the kernel-global workqueue and ``true`` otherwise.

This puts a job in the kernel-global workqueue if it was not already queued and leaves it in the same position on the kernel-global workqueue otherwise.
