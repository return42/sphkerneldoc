
.. _API-flush-kthread-worker:

====================
flush_kthread_worker
====================

*man flush_kthread_worker(9)*

*4.6.0-rc1*

flush all current works on a kthread_worker


Synopsis
========

.. c:function:: void flush_kthread_worker( struct kthread_worker * worker )

Arguments
=========

``worker``
    worker to flush


Description
===========

Wait until all currently executing or pending works on ``worker`` are finished.
