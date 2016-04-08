
.. _API-ieee80211-stop-tx-ba-cb-irqsafe:

===============================
ieee80211_stop_tx_ba_cb_irqsafe
===============================

*man ieee80211_stop_tx_ba_cb_irqsafe(9)*

*4.6.0-rc1*

low level driver ready to stop aggregate.


Synopsis
========

.. c:function:: void ieee80211_stop_tx_ba_cb_irqsafe( struct ieee80211_vif * vif, const u8 * ra, u16 tid )

Arguments
=========

``vif``
    ``struct ieee80211_vif`` pointer from the add_interface callback

``ra``
    receiver address of the BA session recipient.

``tid``
    the desired TID to BA on.


Description
===========

This function must be called by low level driver once it has finished with preparations for the BA session tear down. It can be called from any context.
