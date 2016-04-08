
.. _API-struct-ieee80211-tx-rate:

========================
struct ieee80211_tx_rate
========================

*man struct ieee80211_tx_rate(9)*

*4.6.0-rc1*

rate selection/status


Synopsis
========

.. code-block:: c

    struct ieee80211_tx_rate {
      s8 idx;
      u16 count:5;
      u16 flags:11;
    };


Members
=======

idx
    rate index to attempt to send with

count
    number of tries in this rate before going to the next rate

flags
    rate control flags (``enum`` mac80211_rate_control_flags)


Description
===========

A value of -1 for ``idx`` indicates an invalid rate and, if used in an array of retry rates, that no more rates should be tried.

When used for transmit status reporting, the driver should always report the rate along with the flags it used.

``struct ieee80211_tx_info`` contains an array of these structs in the control information, and it will be filled by the rate control algorithm according to what should be sent.
For example, if this array contains, in the format { <idx>, <count> } the information { 3, 2 }, { 2, 2 }, { 1, 4 }, { -1, 0 }, { -1, 0 } then this means that the frame should be
transmitted up to twice at rate 3, up to twice at rate 2, and up to four times at rate 1 if it doesn't get acknowledged. Say it gets acknowledged by the peer after the fifth
attempt, the status information should then contain { 3, 2 }, { 2, 2 }, { 1, 1 }, { -1, 0 } ... since it was transmitted twice at rate 3, twice at rate 2 and once at rate 1 after
which we received an acknowledgement.
