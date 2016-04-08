
.. _API-struct-ieee80211-rx-status:

==========================
struct ieee80211_rx_status
==========================

*man struct ieee80211_rx_status(9)*

*4.6.0-rc1*

receive status


Synopsis
========

.. code-block:: c

    struct ieee80211_rx_status {
      u64 mactime;
      u32 device_timestamp;
      u32 ampdu_reference;
      u32 flag;
      u16 freq;
      u8 vht_flag;
      u8 rate_idx;
      u8 vht_nss;
      u8 rx_flags;
      u8 band;
      u8 antenna;
      s8 signal;
      u8 chains;
      s8 chain_signal[IEEE80211_MAX_CHAINS];
      u8 ampdu_delimiter_crc;
    };


Members
=======

mactime
    value in microseconds of the 64-bit Time Synchronization Function (TSF) timer when the first data symbol (MPDU) arrived at the hardware.

device_timestamp
    arbitrary timestamp for the device, mac80211 doesn't use it but can store it and pass it back to the driver for synchronisation

ampdu_reference
    A-MPDU reference number, must be a different value for each A-MPDU but the same for each subframe within one A-MPDU

flag
    ``RX_FLAG_``\ ⋆

freq
    frequency the radio was tuned to when receiving this frame, in MHz This field must be set for management frames, but isn't strictly needed for data (other) frames - for those
    it only affects radiotap reporting.

vht_flag
    ``RX_VHT_FLAG_``\ ⋆

rate_idx
    index of data rate into band's supported rates or MCS index if HT or VHT is used (``RX_FLAG_HT``/``RX_FLAG_VHT``)

vht_nss
    number of streams (VHT only)

rx_flags
    internal RX flags for mac80211

band
    the active band when this frame was received

antenna
    antenna used

signal
    signal strength when receiving this frame, either in dBm, in dB or unspecified depending on the hardware capabilities flags ``IEEE80211_HW_SIGNAL_``\ ⋆

chains
    bitmask of receive chains for which separate signal strength values were filled.

chain_signal[IEEE80211_MAX_CHAINS]
    per-chain signal strength, in dBm (unlike ``signal``, doesn't support dB or unspecified units)

ampdu_delimiter_crc
    A-MPDU delimiter CRC


Description
===========

The low-level driver should provide this information (the subset supported by hardware) to the 802.11 code with each received frame, in the skb's control buffer (cb).
