
.. _API-ieee80211-sta-ps-transition-ni:

==============================
ieee80211_sta_ps_transition_ni
==============================

*man ieee80211_sta_ps_transition_ni(9)*

*4.6.0-rc1*

PS transition for connected sta (in process context)


Synopsis
========

.. c:function:: int ieee80211_sta_ps_transition_ni( struct ieee80211_sta * sta, bool start )

Arguments
=========

``sta``
    currently connected sta

``start``
    start or stop PS


Description
===========

Like ``ieee80211_sta_ps_transition`` but can be called in process context (internally disables bottom halves). Concurrent call restriction still applies.


Return
======

Like ``ieee80211_sta_ps_transition``.
