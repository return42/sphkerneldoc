.. -*- coding: utf-8; mode: rst -*-

.. _API-ieee80211-tx-info-clear-status:

==============================
ieee80211_tx_info_clear_status
==============================

*man ieee80211_tx_info_clear_status(9)*

*4.6.0-rc5*

clear TX status


Synopsis
========

.. c:function:: void ieee80211_tx_info_clear_status( struct ieee80211_tx_info * info )

Arguments
=========

``info``
    The ``struct ieee80211_tx_info`` to be cleared.


Description
===========

When the driver passes an skb back to mac80211, it must report a number
of things in TX status. This function clears everything in the TX status
but the rate control information (it does clear the count since you need
to fill that in anyway).


NOTE
====

You can only use this function if you do NOT use info->driver_data! Use
info->rate_driver_data instead if you need only the less space that
allows.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
