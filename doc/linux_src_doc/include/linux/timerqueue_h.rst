.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/timerqueue.h

.. _`timerqueue_getnext`:

timerqueue_getnext
==================

.. c:function:: struct timerqueue_node *timerqueue_getnext(struct timerqueue_head *head)

    Returns the timer with the earliest expiration time

    :param struct timerqueue_head \*head:
        head of timerqueue

.. _`timerqueue_getnext.description`:

Description
-----------

Returns a pointer to the timer node that has the
earliest expiration time.

.. This file was automatic generated / don't edit.

