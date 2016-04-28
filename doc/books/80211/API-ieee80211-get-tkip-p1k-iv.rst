.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-get-tkip-p1k-iv:

=========================
ieee80211_get_tkip_p1k_iv
=========================

*man ieee80211_get_tkip_p1k_iv(9)*

*4.6.0-rc5*

get a TKIP phase 1 key for IV32


Synopsis
========

.. c:function:: void ieee80211_get_tkip_p1k_iv( struct ieee80211_key_conf * keyconf, u32 iv32, u16 * p1k )

Arguments
=========

``keyconf``
    the parameter passed with the set key

``iv32``
    IV32 to get the P1K for

``p1k``
    a buffer to which the key will be written, as 5 u16 values


Description
===========

This function returns the TKIP phase 1 key for the given IV32.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
