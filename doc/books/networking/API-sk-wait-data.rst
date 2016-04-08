
.. _API-sk-wait-data:

============
sk_wait_data
============

*man sk_wait_data(9)*

*4.6.0-rc1*

wait for data to arrive at sk_receive_queue


Synopsis
========

.. c:function:: int sk_wait_data( struct sock * sk, long * timeo, const struct sk_buff * skb )

Arguments
=========

``sk``
    sock to wait on

``timeo``
    for how long

``skb``
    last skb seen on sk_receive_queue


Description
===========

Now socket state including sk->sk_err is changed only under lock, hence we may omit checks after joining wait queue. We check receive queue before ``schedule`` only as
optimization; it is very likely that ``release_sock`` added new data.
