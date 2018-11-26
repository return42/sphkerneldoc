.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/mac80211-ops.c

.. _`ath5k_set_coverage_class`:

ath5k_set_coverage_class
========================

.. c:function:: void ath5k_set_coverage_class(struct ieee80211_hw *hw, s16 coverage_class)

    Set IEEE 802.11 coverage class

    :param hw:
        struct ieee80211_hw pointer
    :type hw: struct ieee80211_hw \*

    :param coverage_class:
        IEEE 802.11 coverage class number
    :type coverage_class: s16

.. _`ath5k_set_coverage_class.description`:

Description
-----------

Mac80211 callback. Sets slot time, ACK timeout and CTS timeout for given
coverage class. The values are persistent, they are restored after device
reset.

.. This file was automatic generated / don't edit.

