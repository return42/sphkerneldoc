
.. _API-struct-cfg80211-ssid:

====================
struct cfg80211_ssid
====================

*man struct cfg80211_ssid(9)*

*4.6.0-rc1*

SSID description


Synopsis
========

.. code-block:: c

    struct cfg80211_ssid {
      u8 ssid[IEEE80211_MAX_SSID_LEN];
      u8 ssid_len;
    };


Members
=======

ssid[IEEE80211_MAX_SSID_LEN]
    the SSID

ssid_len
    length of the ssid
