.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-key-conf:

=========================
struct ieee80211_key_conf
=========================

*man struct ieee80211_key_conf(9)*

*4.6.0-rc5*

key information


Synopsis
========

.. code-block:: c

    struct ieee80211_key_conf {
      atomic64_t tx_pn;
      u32 cipher;
      u8 icv_len;
      u8 iv_len;
      u8 hw_key_idx;
      u8 flags;
      s8 keyidx;
      u8 keylen;
      u8 key[0];
    };


Members
=======

tx_pn
    PN used for TX keys, may be used by the driver as well if it needs
    to do software PN assignment by itself (e.g. due to TSO)

cipher
    The key's cipher suite selector.

icv_len
    The ICV length for this key type

iv_len
    The IV length for this key type

hw_key_idx
    To be set by the driver, this is the key index the driver wants to
    be given when a frame is transmitted and needs to be encrypted in
    hardware.

flags
    key flags, see ``enum`` ieee80211_key_flags.

keyidx
    the key index (0-3)

keylen
    key material length

key[0]
    key material. For ALG_TKIP the key is encoded as a 256-bit (32
    byte)


Description
===========

This key information is given by mac80211 to the driver by the
``set_key`` callback in ``struct ieee80211_ops``.


data block
==========

- Temporal Encryption Key (128 bits) - Temporal Authenticator Tx MIC Key
(64 bits) - Temporal Authenticator Rx MIC Key (64 bits)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
