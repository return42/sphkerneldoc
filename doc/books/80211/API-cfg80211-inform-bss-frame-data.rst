.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-inform-bss-frame-data:

==============================
cfg80211_inform_bss_frame_data
==============================

*man cfg80211_inform_bss_frame_data(9)*

*4.6.0-rc5*

inform cfg80211 of a received BSS frame


Synopsis
========

.. c:function:: struct cfg80211_bss * cfg80211_inform_bss_frame_data( struct wiphy * wiphy, struct cfg80211_inform_bss * data, struct ieee80211_mgmt * mgmt, size_t len, gfp_t gfp )

Arguments
=========

``wiphy``
    the wiphy reporting the BSS

``data``
    the BSS metadata

``mgmt``
    the management frame (probe response or beacon)

``len``
    length of the management frame

``gfp``
    context flags


Description
===========

This informs cfg80211 that BSS information was found and the BSS should
be updated/added.


Return
======

A referenced struct, must be released with ``cfg80211_put_bss``! Or
``NULL`` on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
