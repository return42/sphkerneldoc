
.. _API-cfg80211-check-combinations:

===========================
cfg80211_check_combinations
===========================

*man cfg80211_check_combinations(9)*

*4.6.0-rc1*

check interface combinations


Synopsis
========

.. c:function:: int cfg80211_check_combinations( struct wiphy * wiphy, const int num_different_channels, const u8 radar_detect, const int iftype_num[NUM_NL80211_IFTYPES] )

Arguments
=========

``wiphy``
    the wiphy

``num_different_channels``
    the number of different channels we want to use for verification

``radar_detect``
    a bitmap where each bit corresponds to a channel width where radar detection is needed, as in the definition of ``struct ieee80211_iface_combination``.\ ``radar_detect_widths``

``iftype_num[NUM_NL80211_IFTYPES]``
    array with the numbers of interfaces of each interface type. The index is the interface type as specified in ``enum`` nl80211_iftype.


Description
===========

This function can be called by the driver to check whether a combination of interfaces and their types are allowed according to the interface combinations.
