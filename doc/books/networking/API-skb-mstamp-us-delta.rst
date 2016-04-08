
.. _API-skb-mstamp-us-delta:

===================
skb_mstamp_us_delta
===================

*man skb_mstamp_us_delta(9)*

*4.6.0-rc1*

compute the difference in usec between two skb_mstamp


Synopsis
========

.. c:function:: u32 skb_mstamp_us_delta( const struct skb_mstamp * t1, const struct skb_mstamp * t0 )

Arguments
=========

``t1``
    pointer to newest sample

``t0``
    pointer to oldest sample
