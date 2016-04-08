
.. _API-struct-cfg80211-disassoc-request:

================================
struct cfg80211_disassoc_request
================================

*man struct cfg80211_disassoc_request(9)*

*4.6.0-rc1*

Disassociation request data


Synopsis
========

.. code-block:: c

    struct cfg80211_disassoc_request {
      struct cfg80211_bss * bss;
      const u8 * ie;
      size_t ie_len;
      u16 reason_code;
      bool local_state_change;
    };


Members
=======

bss
    the BSS to disassociate from

ie
    Extra IEs to add to Disassociation frame or ``NULL``

ie_len
    Length of ie buffer in octets

reason_code
    The reason code for the disassociation

local_state_change
    This is a request for a local state only, i.e., no Disassociation frame is to be transmitted.


Description
===========

This structure provides information needed to complete IEEE 802.11 disassocation.
