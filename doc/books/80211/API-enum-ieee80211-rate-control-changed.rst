
.. _API-enum-ieee80211-rate-control-changed:

===================================
enum ieee80211_rate_control_changed
===================================

*man enum ieee80211_rate_control_changed(9)*

*4.6.0-rc1*

flags to indicate what changed


Synopsis
========

.. code-block:: c

    enum ieee80211_rate_control_changed {
      IEEE80211_RC_BW_CHANGED,
      IEEE80211_RC_SMPS_CHANGED,
      IEEE80211_RC_SUPP_RATES_CHANGED,
      IEEE80211_RC_NSS_CHANGED
    };


Constants
=========

IEEE80211_RC_BW_CHANGED
    The bandwidth that can be used to transmit to this station changed. The actual bandwidth is in the station information -- for HT20/40 the IEEE80211_HT_CAP_SUP_WIDTH_20_40
    flag changes, for HT and VHT the bandwidth field changes.

IEEE80211_RC_SMPS_CHANGED
    The SMPS state of the station changed.

IEEE80211_RC_SUPP_RATES_CHANGED
    The supported rate set of this peer changed (in IBSS mode) due to discovering more information about the peer.

IEEE80211_RC_NSS_CHANGED
    N_SS (number of spatial streams) was changed by the peer
