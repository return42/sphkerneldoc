
.. _API-queue-delayed-work-on:

=====================
queue_delayed_work_on
=====================

*man queue_delayed_work_on(9)*

*4.6.0-rc1*

queue work on specific CPU after delay


Synopsis
========

.. c:function:: bool queue_delayed_work_on( int cpu, struct workqueue_struct * wq, struct delayed_work * dwork, unsigned long delay )

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


Return
======

``false`` if ``work`` was already on a queue, ``true`` otherwise. If ``delay`` is zero and ``dwork`` is idle, it will be scheduled for immediate execution.
