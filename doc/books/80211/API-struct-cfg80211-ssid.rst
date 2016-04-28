.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-ssid:

====================
struct cfg80211_ssid
====================

*man struct cfg80211_ssid(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
