
.. _API-ieee80211-bss-get-ie:

====================
ieee80211_bss_get_ie
====================

*man ieee80211_bss_get_ie(9)*

*4.6.0-rc1*

find IE with given ID


Synopsis
========

.. c:function:: const u8 ⋆ ieee80211_bss_get_ie( struct cfg80211_bss * bss, u8 ie )

Arguments
=========

``bss``
    the bss to search

``ie``
    the IE ID


Description
===========

Note that the return value is an RCU-protected pointer, so ``rcu_read_lock`` must be held when calling this function.


Return
======

``NULL`` if not found.
