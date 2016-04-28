.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-cfg80211-deauth-request:

==============================
struct cfg80211_deauth_request
==============================

*man struct cfg80211_deauth_request(9)*

*4.6.0-rc5*

Deauthentication request data


Synopsis
========

.. code-block:: c

    struct cfg80211_deauth_request {
      const u8 * bssid;
      const u8 * ie;
      size_t ie_len;
      u16 reason_code;
      bool local_state_change;
    };


Members
=======

bssid
    the BSSID of the BSS to deauthenticate from

ie
    Extra IEs to add to Deauthentication frame or ``NULL``

ie_len
    Length of ie buffer in octets

reason_code
    The reason code for the deauthentication

local_state_change
    if set, change local state only and do not set a deauth frame


Description
===========

This structure provides information needed to complete IEEE 802.11
deauthentication.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
