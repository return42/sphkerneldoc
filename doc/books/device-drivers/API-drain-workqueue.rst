
.. _API-drain-workqueue:

===============
drain_workqueue
===============

*man drain_workqueue(9)*

*4.6.0-rc1*

drain a workqueue


Synopsis
========

.. c:function:: void drain_workqueue( struct workqueue_struct * wq )

Arguments
=========

``wq``
    workqueue to drain


Description
===========

Wait until the workqueue becomes empty. While draining is in progress, only chain queueing is allowed. IOW, only currently pending or running work items on ``wq`` can queue further
work items on it. ``wq`` is flushed repeatedly until it becomes empty. The number of flushing is determined by the depth of chaining and should be relatively short. Whine if it
takes too long.
