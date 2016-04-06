
.. _API-kthread-park:

============
kthread_park
============

*man kthread_park(9)*

*4.6.0-rc1*

park a thread created by ``kthread_create``.


Synopsis
========

.. c:function:: int kthread_park( struct task_struct * k )

Arguments
=========

``k``
    thread created by ``kthread_create``.


Description
===========

Sets ``kthread_should_park`` for ``k`` to return true, wakes it, and waits for it to return. This can also be called after ``kthread_create`` instead of calling
``wake_up_process``: the thread will park without calling ``threadfn``.

Returns 0 if the thread is parked, -ENOSYS if the thread exited. If called by the kthread itself just the park bit is set.
