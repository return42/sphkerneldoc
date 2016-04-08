
.. _API-skb-try-coalesce:

================
skb_try_coalesce
================

*man skb_try_coalesce(9)*

*4.6.0-rc1*

try to merge skb to prior one


Synopsis
========

.. c:function:: bool skb_try_coalesce( struct sk_buff * to, struct sk_buff * from, bool * fragstolen, int * delta_truesize )

Arguments
=========

``to``
    prior buffer

``from``
    buffer to add

``fragstolen``
    pointer to boolean

``delta_truesize``
    how much more was allocated than was requested
