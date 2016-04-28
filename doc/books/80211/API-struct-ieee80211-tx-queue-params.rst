.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-tx-queue-params:

================================
struct ieee80211_tx_queue_params
================================

*man struct ieee80211_tx_queue_params(9)*

*4.6.0-rc5*

transmit queue configuration


Synopsis
========

.. code-block:: c

    struct ieee80211_tx_queue_params {
      u16 txop;
      u16 cw_min;
      u16 cw_max;
      u8 aifs;
      bool acm;
      bool uapsd;
    };


Members
=======

txop
    maximum burst time in units of 32 usecs, 0 meaning disabled

cw_min
    minimum contention window [a value of the form 2^n-1 in the range
    1..32767]

cw_max
    maximum contention window [like ``cw_min``]

aifs
    arbitration interframe space [0..255]

acm
    is mandatory admission control required for the access category

uapsd
    is U-APSD mode enabled for the queue


Description
===========

The information provided in this structure is required for QoS transmit
queue configuration. Cf. IEEE 802.11 7.3.2.29.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
