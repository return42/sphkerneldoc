
.. _API-queue-work-on:

=============
queue_work_on
=============

*man queue_work_on(9)*

*4.6.0-rc1*

queue work on specific cpu


Synopsis
========

.. c:function:: bool queue_work_on( int cpu, struct workqueue_struct * wq, struct work_struct * work )

Arguments
=========

``cpu``
    CPU number to execute work on

``wq``
    workqueue to use

``work``
    work to queue


Description
===========

We queue the work to a specific CPU, the caller must ensure it can't go away.


Return
======

``false`` if ``work`` was already on a queue, ``true`` otherwise.
