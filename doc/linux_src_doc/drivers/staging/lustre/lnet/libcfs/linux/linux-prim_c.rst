.. -*- coding: utf-8; mode: rst -*-

============
linux-prim.c
============


.. _`add_wait_queue_exclusive_head`:

add_wait_queue_exclusive_head
=============================

.. c:function:: void add_wait_queue_exclusive_head (wait_queue_head_t *waitq, wait_queue_t *link)

    :param wait_queue_head_t \*waitq:

        *undescribed*

    :param wait_queue_t \*link:

        *undescribed*



.. _`add_wait_queue_exclusive_head.description`:

Description
-----------

waiting threads, which is not always desirable because all threads will
be waken up again and again, even user only needs a few of them to be
active most time. This is not good for performance because cache can
be polluted by different threads.

LIFO list can resolve this problem because we always wakeup the most
recent active thread by default.



.. _`add_wait_queue_exclusive_head.nb`:

NB
--

please don't call non-exclusive & exclusive wait on the same
waitq if add_wait_queue_exclusive_head is used.

