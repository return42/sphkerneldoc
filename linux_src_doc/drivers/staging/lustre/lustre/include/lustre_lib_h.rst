.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre_lib.h

.. _`add_wait_queue_exclusive_head`:

add_wait_queue_exclusive_head
=============================

.. c:function::  add_wait_queue_exclusive_head( waitq,  link)

    waiting threads, which is not always desirable because all threads will be waken up again and again, even user only needs a few of them to be active most time. This is not good for performance because cache can be polluted by different threads.

    :param  waitq:
        *undescribed*

    :param  link:
        *undescribed*

.. _`add_wait_queue_exclusive_head.description`:

Description
-----------

LIFO list can resolve this problem because we always wakeup the most
recent active thread by default.

NB: please don't call non-exclusive & exclusive wait on the same
waitq if add_wait_queue_exclusive_head is used.

.. This file was automatic generated / don't edit.

