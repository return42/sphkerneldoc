
.. _API-flush-workqueue:

===============
flush_workqueue
===============

*man flush_workqueue(9)*

*4.6.0-rc1*

ensure that any scheduled work has run to completion.


Synopsis
========

.. c:function:: void flush_workqueue( struct workqueue_struct * wq )

Arguments
=========

``wq``
    workqueue to flush


Description
===========

This function sleeps until all work items which were queued on entry have finished execution, but it is not livelocked by new incoming ones.
