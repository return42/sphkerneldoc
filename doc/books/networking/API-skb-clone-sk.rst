
.. _API-skb-clone-sk:

============
skb_clone_sk
============

*man skb_clone_sk(9)*

*4.6.0-rc1*

create clone of skb, and take reference to socket


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_clone_sk( struct sk_buff * skb )

Arguments
=========

``skb``
    the skb to clone


Description
===========

This function creates a clone of a buffer that holds a reference on sk_refcnt. Buffers created via this function are meant to be returned using sock_queue_err_skb, or free via
kfree_skb.

When passing buffers allocated with this function to sock_queue_err_skb it is necessary to wrap the call with sock_hold/sock_put in order to prevent the socket from being
released prior to being enqueued on the sk_error_queue.
