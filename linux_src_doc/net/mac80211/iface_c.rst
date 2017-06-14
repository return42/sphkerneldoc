.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/iface.c

.. _`interface-list-locking`:

Interface list locking
======================

The interface list in each struct ieee80211_local is protected
three-fold:

(1) modifications may only be done under the RTNL
(2) modifications and readers are protected against each other by
the iflist_mtx.
(3) modifications are done in an RCU manner so atomic readers
can traverse the list in RCU-safe blocks.

As a consequence, reads (traversals) of the list can be protected
by either the RTNL, the iflist_mtx or RCU.

.. This file was automatic generated / don't edit.

