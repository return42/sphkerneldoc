.. -*- coding: utf-8; mode: rst -*-

.. _API-kthread-stop:

============
kthread_stop
============

*man kthread_stop(9)*

*4.6.0-rc5*

stop a thread created by ``kthread_create``.


Synopsis
========

.. c:function:: int kthread_stop( struct task_struct * k )

Arguments
=========

``k``
    thread created by ``kthread_create``.


Description
===========

Sets ``kthread_should_stop`` for ``k`` to return true, wakes it, and
waits for it to exit. This can also be called after ``kthread_create``
instead of calling ``wake_up_process``: the thread will exit without
calling ``threadfn``.

If ``threadfn`` may call ``do_exit`` itself, the caller must ensure
task_struct can't go away.

Returns the result of ``threadfn``, or ``-EINTR`` if ``wake_up_process``
was never called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
