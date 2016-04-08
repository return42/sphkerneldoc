
.. _API---skb-queue-head-init:

=====================
__skb_queue_head_init
=====================

*man __skb_queue_head_init(9)*

*4.6.0-rc1*

initialize non-spinlock portions of sk_buff_head


Synopsis
========

.. c:function:: void __skb_queue_head_init( struct sk_buff_head * list )

Arguments
=========

``list``
    queue to initialize


Description
===========

This initializes only the list and queue length aspects of an sk_buff_head object. This allows to initialize the list aspects of an sk_buff_head without reinitializing things
like the spinlock. It can also be used for on-stack sk_buff_head objects where the spinlock is known to not be used.
