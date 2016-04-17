.. -*- coding: utf-8; mode: rst -*-

===========
tcp_input.c
===========


.. _`tcp_try_coalesce`:

tcp_try_coalesce
================

.. c:function:: bool tcp_try_coalesce (struct sock *sk, struct sk_buff *to, struct sk_buff *from, bool *fragstolen)

    try to merge skb to prior one

    :param struct sock \*sk:
        socket

    :param struct sk_buff \*to:
        prior buffer

    :param struct sk_buff \*from:
        buffer to add in queue

    :param bool \*fragstolen:
        pointer to boolean



.. _`tcp_try_coalesce.description`:

Description
-----------

Before queueing skb ``from`` after ``to``\ , try to merge them
to reduce overall memory use and queue lengths, if cost is small.
Packets in ofo or receive queues can stay a long time.
Better try to coalesce them right now to avoid future collapses.
Returns true if caller should free ``from`` instead of queueing it

