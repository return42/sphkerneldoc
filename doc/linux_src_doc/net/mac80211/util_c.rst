.. -*- coding: utf-8; mode: rst -*-

======
util.c
======


.. _`ieee80211_calculate_rx_timestamp`:

ieee80211_calculate_rx_timestamp
================================

.. c:function:: u64 ieee80211_calculate_rx_timestamp (struct ieee80211_local *local, struct ieee80211_rx_status *status, unsigned int mpdu_len, unsigned int mpdu_offset)

    calculate timestamp in frame

    :param struct ieee80211_local \*local:
        mac80211 hw info struct

    :param struct ieee80211_rx_status \*status:
        RX status

    :param unsigned int mpdu_len:
        total MPDU length (including FCS)

    :param unsigned int mpdu_offset:
        offset into MPDU to calculate timestamp at



.. _`ieee80211_calculate_rx_timestamp.description`:

Description
-----------

This function calculates the RX timestamp at the given MPDU offset, taking
into account what the RX timestamp was. An offset of 0 will just normalize
the timestamp to TSF at beginning of MPDU reception.

