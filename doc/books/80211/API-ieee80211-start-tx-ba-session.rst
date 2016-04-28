.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-start-tx-ba-session:

=============================
ieee80211_start_tx_ba_session
=============================

*man ieee80211_start_tx_ba_session(9)*

*4.6.0-rc5*

Start a tx Block Ack session.


Synopsis
========

.. c:function:: int ieee80211_start_tx_ba_session( struct ieee80211_sta * sta, u16 tid, u16 timeout )

Arguments
=========

``sta``
    the station for which to start a BA session

``tid``
    the TID to BA on.

``timeout``
    session timeout value (in TUs)


Return
======

success if addBA request was sent, failure otherwise

Although mac80211/low level driver/user space application can estimate
the need to start aggregation on a certain RA/TID, the session level
will be managed by the mac80211.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
