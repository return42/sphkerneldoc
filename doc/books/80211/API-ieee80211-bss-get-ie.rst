.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-bss-get-ie:

====================
ieee80211_bss_get_ie
====================

*man ieee80211_bss_get_ie(9)*

*4.6.0-rc5*

find IE with given ID


Synopsis
========

.. c:function:: const u8 * ieee80211_bss_get_ie( struct cfg80211_bss * bss, u8 ie )

Arguments
=========

``bss``
    the bss to search

``ie``
    the IE ID


Description
===========

Note that the return value is an RCU-protected pointer, so
``rcu_read_lock`` must be held when calling this function.


Return
======

``NULL`` if not found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
