
.. _API-ieee80211-start-tx-ba-cb-irqsafe:

================================
ieee80211_start_tx_ba_cb_irqsafe
================================

*man ieee80211_start_tx_ba_cb_irqsafe(9)*

*4.6.0-rc1*

low level driver ready to aggregate.


Synopsis
========

.. c:function:: void ieee80211_start_tx_ba_cb_irqsafe( struct ieee80211_vif * vif, const u8 * ra, u16 tid )

Arguments
=========

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback

``ra``
    receiver address of the BA session recipient.

``tid``
    the TID to BA on.


Description
===========

This function must be called by low level driver once it has finished with preparations for the BA session. It can be called from any context.
