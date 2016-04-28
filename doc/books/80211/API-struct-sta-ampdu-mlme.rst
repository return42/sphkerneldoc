.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-sta-ampdu-mlme:

=====================
struct sta_ampdu_mlme
=====================

*man struct sta_ampdu_mlme(9)*

*4.6.0-rc5*

STA aggregation information.


Synopsis
========

.. code-block:: c

    struct sta_ampdu_mlme {
      struct mutex mtx;
      struct tid_ampdu_rx __rcu * tid_rx[IEEE80211_NUM_TIDS];
      unsigned long tid_rx_timer_expired[BITS_TO_LONGS(IEEE80211_NUM_TIDS)];
      unsigned long tid_rx_stop_requested[BITS_TO_LONGS(IEEE80211_NUM_TIDS)];
      unsigned long agg_session_valid[BITS_TO_LONGS(IEEE80211_NUM_TIDS)];
      struct work_struct work;
      struct tid_ampdu_tx __rcu * tid_tx[IEEE80211_NUM_TIDS];
      struct tid_ampdu_tx * tid_start_tx[IEEE80211_NUM_TIDS];
      unsigned long last_addba_req_time[IEEE80211_NUM_TIDS];
      u8 addba_req_num[IEEE80211_NUM_TIDS];
      u8 dialog_token_allocator;
    };


Members
=======

mtx
    mutex to protect all TX data (except non-NULL assignments to
    tid_tx[idx], which are protected by the sta spinlock)
    tid_start_tx is also protected by sta->lock.

tid_rx[IEEE80211_NUM_TIDS]
    aggregation info for Rx per TID -- RCU protected

tid_rx_timer_expired[BITS_TO_LONGS(IEEE80211_NUM_TIDS)]
    bitmap indicating on which TIDs the RX timer expired until the work
    for it runs

tid_rx_stop_requested[BITS_TO_LONGS(IEEE80211_NUM_TIDS)]
    bitmap indicating which BA sessions per TID the driver requested to
    close until the work for it runs

agg_session_valid[BITS_TO_LONGS(IEEE80211_NUM_TIDS)]
    bitmap indicating which TID has a rx BA session open on

work
    work struct for starting/stopping aggregation

tid_tx[IEEE80211_NUM_TIDS]
    aggregation info for Tx per TID

tid_start_tx[IEEE80211_NUM_TIDS]
    sessions where start was requested

last_addba_req_time[IEEE80211_NUM_TIDS]
    timestamp of the last addBA request.

addba_req_num[IEEE80211_NUM_TIDS]
    number of times addBA request has been sent.

dialog_token_allocator
    dialog token enumerator for each new session;


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
