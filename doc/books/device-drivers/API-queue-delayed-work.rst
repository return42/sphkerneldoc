
.. _API-queue-delayed-work:

==================
queue_delayed_work
==================

*man queue_delayed_work(9)*

*4.6.0-rc1*

queue work on a workqueue after delay


Synopsis
========

.. c:function:: bool queue_delayed_work( struct workqueue_struct * wq, struct delayed_work * dwork, unsigned long delay )

Arguments
=========

``wq``
    workqueue to use

``dwork``
    delayable work to queue

``delay``
    number of jiffies to wait before queueing


Description
===========

Equivalent to ``queue_delayed_work_on`` but tries to use the local CPU.
