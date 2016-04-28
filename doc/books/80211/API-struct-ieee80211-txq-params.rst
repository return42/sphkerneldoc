.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-txq-params:

===========================
struct ieee80211_txq_params
===========================

*man struct ieee80211_txq_params(9)*

*4.6.0-rc5*

TX queue parameters


Synopsis
========

.. code-block:: c

    struct ieee80211_txq_params {
      enum nl80211_ac ac;
      u16 txop;
      u16 cwmin;
      u16 cwmax;
      u8 aifs;
    };


Members
=======

ac
    AC identifier

txop
    Maximum burst time in units of 32 usecs, 0 meaning disabled

cwmin
    Minimum contention window [a value of the form 2^n-1 in the range
    1..32767]

cwmax
    Maximum contention window [a value of the form 2^n-1 in the range
    1..32767]

aifs
    Arbitration interframe space [0..255]


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
