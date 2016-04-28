.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-mstamp-us-delta:

===================
skb_mstamp_us_delta
===================

*man skb_mstamp_us_delta(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
