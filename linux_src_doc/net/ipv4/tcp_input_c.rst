.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/tcp_input.c

.. _`tcp_try_coalesce`:

tcp_try_coalesce
================

.. c:function:: bool tcp_try_coalesce(struct sock *sk, struct sk_buff *to, struct sk_buff *from, bool *fragstolen)

    try to merge skb to prior one

    :param sk:
        socket
    :type sk: struct sock \*

    :param to:
        prior buffer
    :type to: struct sk_buff \*

    :param from:
        buffer to add in queue
    :type from: struct sk_buff \*

    :param fragstolen:
        pointer to boolean
    :type fragstolen: bool \*

.. _`tcp_try_coalesce.description`:

Description
-----------

Before queueing skb \ ``from``\  after \ ``to``\ , try to merge them
to reduce overall memory use and queue lengths, if cost is small.
Packets in ofo or receive queues can stay a long time.
Better try to coalesce them right now to avoid future collapses.
Returns true if caller should free \ ``from``\  instead of queueing it

.. This file was automatic generated / don't edit.

