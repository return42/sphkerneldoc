.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-stop-tx-ba-session:

============================
ieee80211_stop_tx_ba_session
============================

*man ieee80211_stop_tx_ba_session(9)*

*4.6.0-rc5*

Stop a Block Ack session.


Synopsis
========

.. c:function:: int ieee80211_stop_tx_ba_session( struct ieee80211_sta * sta, u16 tid )

Arguments
=========

``sta``
    the station whose BA session to stop

``tid``
    the TID to stop BA.


Return
======

negative error if the TID is invalid, or no aggregation active

Although mac80211/low level driver/user space application can estimate
the need to stop aggregation on a certain RA/TID, the session level will
be managed by the mac80211.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
