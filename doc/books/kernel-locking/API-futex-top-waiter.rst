.. -*- coding: utf-8; mode: rst -*-

.. _API-futex-top-waiter:

================
futex_top_waiter
================

*man futex_top_waiter(9)*

*4.6.0-rc5*

Return the highest priority waiter on a futex


Synopsis
========

.. c:function:: struct futex_q * futex_top_waiter( struct futex_hash_bucket * hb, union futex_key * key )

Arguments
=========

``hb``
    the hash bucket the futex_q's reside in

``key``
    the futex key (to distinguish it from other futex futex_q's)


Description
===========

Must be called with the hb lock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
