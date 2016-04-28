.. -*- coding: utf-8; mode: rst -*-

.. _API-kthread-unpark:

==============
kthread_unpark
==============

*man kthread_unpark(9)*

*4.6.0-rc5*

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

Sets ``kthread_should_park`` for ``k`` to return false, wakes it, and
waits for it to return. If the thread is marked percpu then its bound to
the cpu again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
