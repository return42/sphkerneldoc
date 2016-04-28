.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-ieee80211-ampdu-mlme-action:

================================
enum ieee80211_ampdu_mlme_action
================================

*man enum ieee80211_ampdu_mlme_action(9)*

*4.6.0-rc5*

A-MPDU actions


Synopsis
========

.. code-block:: c

    enum ieee80211_ampdu_mlme_action {
      IEEE80211_AMPDU_RX_START,
      IEEE80211_AMPDU_RX_STOP,
      IEEE80211_AMPDU_TX_START,
      IEEE80211_AMPDU_TX_STOP_CONT,
      IEEE80211_AMPDU_TX_STOP_FLUSH,
      IEEE80211_AMPDU_TX_STOP_FLUSH_CONT,
      IEEE80211_AMPDU_TX_OPERATIONAL
    };


Constants
=========

IEEE80211_AMPDU_RX_START
    start RX aggregation

IEEE80211_AMPDU_RX_STOP
    stop RX aggregation

IEEE80211_AMPDU_TX_START
    start TX aggregation

IEEE80211_AMPDU_TX_STOP_CONT
    stop TX aggregation but continue transmitting queued packets, now
    unaggregated. After all packets are transmitted the driver has to
    call ``ieee80211_stop_tx_ba_cb_irqsafe``.

IEEE80211_AMPDU_TX_STOP_FLUSH
    stop TX aggregation and flush all packets, called when the station
    is removed. There's no need or reason to call
    ``ieee80211_stop_tx_ba_cb_irqsafe`` in this case as mac80211 assumes
    the session is gone and removes the station.

IEEE80211_AMPDU_TX_STOP_FLUSH_CONT
    called when TX aggregation is stopped but the driver hasn't called
    ``ieee80211_stop_tx_ba_cb_irqsafe`` yet and now the connection is
    dropped and the station will be removed. Drivers should clean up and
    drop remaining packets when this is called.

IEEE80211_AMPDU_TX_OPERATIONAL
    TX aggregation has become operational


Description
===========

These flags are used with the ``ampdu_action`` callback in
``struct ieee80211_ops`` to indicate which action is needed.

Note that drivers MUST be able to deal with a TX aggregation session
being stopped even before they OK'ed starting it by calling
ieee80211_start_tx_ba_cb_irqsafe, because the peer might receive
the addBA frame and send a delBA right away!


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
