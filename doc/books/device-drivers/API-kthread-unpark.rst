
.. _API-kthread-unpark:

==============
kthread_unpark
==============

*man kthread_unpark(9)*

*4.6.0-rc1*

unpark a thread created by ``kthread_create``.


Synopsis
========

.. c:function:: void kthread_unpark( struct task_struct * k )

Arguments
=========

``k``
    thread created by ``kthread_create``.


Description
===========

Sets ``kthread_should_park`` for ``k`` to return false, wakes it, and waits for it to return. If the thread is marked percpu then its bound to the cpu again.
