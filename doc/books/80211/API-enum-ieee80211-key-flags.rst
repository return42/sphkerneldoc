
.. _API-enum-ieee80211-key-flags:

========================
enum ieee80211_key_flags
========================

*man enum ieee80211_key_flags(9)*

*4.6.0-rc1*

key flags


Synopsis
========

.. code-block:: c

    enum ieee80211_key_flags {
      IEEE80211_KEY_FLAG_GENERATE_IV_MGMT,
      IEEE80211_KEY_FLAG_GENERATE_IV,
      IEEE80211_KEY_FLAG_GENERATE_MMIC,
      IEEE80211_KEY_FLAG_PAIRWISE,
      IEEE80211_KEY_FLAG_SW_MGMT_TX,
      IEEE80211_KEY_FLAG_PUT_IV_SPACE,
      IEEE80211_KEY_FLAG_RX_MGMT,
      IEEE80211_KEY_FLAG_RESERVE_TAILROOM
    };


Constants
=========

IEEE80211_KEY_FLAG_GENERATE_IV_MGMT
    This flag should be set by the driver for a CCMP/GCMP key to indicate that is requires IV generation only for managment frames (MFP).

IEEE80211_KEY_FLAG_GENERATE_IV
    This flag should be set by the driver to indicate that it requires IV generation for this particular key. Setting this flag does not necessarily mean that SKBs will have
    sufficient tailroom for ICV or MIC.

IEEE80211_KEY_FLAG_GENERATE_MMIC
    This flag should be set by the driver for a TKIP key if it requires Michael MIC generation in software.

IEEE80211_KEY_FLAG_PAIRWISE
    Set by mac80211, this flag indicates that the key is pairwise rather then a shared key.

IEEE80211_KEY_FLAG_SW_MGMT_TX
    This flag should be set by the driver for a CCMP/GCMP key if it requires CCMP/GCMP encryption of management frames (MFP) to be done in software.

IEEE80211_KEY_FLAG_PUT_IV_SPACE
    This flag should be set by the driver if space should be prepared for the IV, but the IV itself should not be generated. Do not set together with
    ``IEEE80211_KEY_FLAG_GENERATE_IV`` on the same key. Setting this flag does not necessarily mean that SKBs will have sufficient tailroom for ICV or MIC.

IEEE80211_KEY_FLAG_RX_MGMT
    This key will be used to decrypt received management frames. The flag can help drivers that have a hardware crypto implementation that doesn't deal with management frames
    properly by allowing them to not upload the keys to hardware and fall back to software crypto. Note that this flag deals only with RX, if your crypto engine can't deal with TX
    you can also set the ``IEEE80211_KEY_FLAG_SW_MGMT_TX`` flag to encrypt such frames in SW.

IEEE80211_KEY_FLAG_RESERVE_TAILROOM
    This flag should be set by the driver for a key to indicate that sufficient tailroom must always be reserved for ICV or MIC, even when HW encryption is enabled.


Description
===========

These flags are used for communication about keys between the driver and mac80211, with the ``flags`` parameter of ``struct ieee80211_key_conf``.
