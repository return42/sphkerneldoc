
.. _API-flush-kthread-work:

==================
flush_kthread_work
==================

*man flush_kthread_work(9)*

*4.6.0-rc1*

flush a kthread_work


Synopsis
========

.. c:function:: void flush_kthread_work( struct kthread_work * work )

Arguments
=========

``work``
    work to flush


Description
===========

If ``work`` is queued or executing, wait for it to finish execution.
