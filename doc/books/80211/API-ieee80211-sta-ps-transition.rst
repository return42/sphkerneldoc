.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-sta-ps-transition:

===========================
ieee80211_sta_ps_transition
===========================

*man ieee80211_sta_ps_transition(9)*

*4.6.0-rc5*

PS transition for connected sta


Synopsis
========

.. c:function:: int ieee80211_sta_ps_transition( struct ieee80211_sta * sta, bool start )

Arguments
=========

``sta``
    currently connected sta

``start``
    start or stop PS


Description
===========

When operating in AP mode with the ``IEEE80211_HW_AP_LINK_PS`` flag set,
use this function to inform mac80211 about a connected station
entering/leaving PS mode.

This function may not be called in IRQ context or with softirqs enabled.

Calls to this function for a single hardware must be synchronized
against each other.


Return
======

0 on success. -EINVAL when the requested PS mode is already set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
