.. -*- coding: utf-8; mode: rst -*-

.. _API-cfg80211-unlink-bss:

===================
cfg80211_unlink_bss
===================

*man cfg80211_unlink_bss(9)*

*4.6.0-rc5*

unlink BSS from internal data structures


Synopsis
========

.. c:function:: void cfg80211_unlink_bss( struct wiphy * wiphy, struct cfg80211_bss * bss )

Arguments
=========

``wiphy``
    the wiphy

``bss``
    the bss to remove


Description
===========

This function removes the given BSS from the internal data structures
thereby making it no longer show up in scan results etc. Use this
function when you detect a BSS is gone. Normally BSSes will also time
out, so it is not necessary to use this function at all.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
