.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-mac80211-tx-control-flags:

==============================
enum mac80211_tx_control_flags
==============================

*man enum mac80211_tx_control_flags(9)*

*4.6.0-rc5*

flags to describe transmit control


Synopsis
========

.. code-block:: c

    enum mac80211_tx_control_flags {
      IEEE80211_TX_CTRL_PORT_CTRL_PROTO,
      IEEE80211_TX_CTRL_PS_RESPONSE,
      IEEE80211_TX_CTRL_RATE_INJECT
    };


Constants
=========

IEEE80211_TX_CTRL_PORT_CTRL_PROTO
    this frame is a port control protocol frame (e.g. EAP)

IEEE80211_TX_CTRL_PS_RESPONSE
    This frame is a response to a poll frame (PS-Poll or uAPSD).

IEEE80211_TX_CTRL_RATE_INJECT
    This frame is injected with rate information


Description
===========

These flags are used in tx_info->control.flags.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
