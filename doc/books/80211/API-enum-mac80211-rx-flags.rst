
.. _API-enum-mac80211-rx-flags:

======================
enum mac80211_rx_flags
======================

*man enum mac80211_rx_flags(9)*

*4.6.0-rc1*

receive flags


Synopsis
========

.. code-block:: c

    enum mac80211_rx_flags {
      RX_FLAG_MMIC_ERROR,
      RX_FLAG_DECRYPTED,
      RX_FLAG_MACTIME_PLCP_START,
      RX_FLAG_MMIC_STRIPPED,
      RX_FLAG_IV_STRIPPED,
      RX_FLAG_FAILED_FCS_CRC,
      RX_FLAG_FAILED_PLCP_CRC,
      RX_FLAG_MACTIME_START,
      RX_FLAG_SHORTPRE,
      RX_FLAG_HT,
      RX_FLAG_40MHZ,
      RX_FLAG_SHORT_GI,
      RX_FLAG_NO_SIGNAL_VAL,
      RX_FLAG_HT_GF,
      RX_FLAG_AMPDU_DETAILS,
      RX_FLAG_PN_VALIDATED,
      RX_FLAG_DUP_VALIDATED,
      RX_FLAG_AMPDU_LAST_KNOWN,
      RX_FLAG_AMPDU_IS_LAST,
      RX_FLAG_AMPDU_DELIM_CRC_ERROR,
      RX_FLAG_AMPDU_DELIM_CRC_KNOWN,
      RX_FLAG_MACTIME_END,
      RX_FLAG_VHT,
      RX_FLAG_LDPC,
      RX_FLAG_ONLY_MONITOR,
      RX_FLAG_SKIP_MONITOR,
      RX_FLAG_STBC_MASK,
      RX_FLAG_10MHZ,
      RX_FLAG_5MHZ,
      RX_FLAG_AMSDU_MORE,
      RX_FLAG_RADIOTAP_VENDOR_DATA
    };


Constants
=========

RX_FLAG_MMIC_ERROR
    Michael MIC error was reported on this frame. Use together with ``RX_FLAG_MMIC_STRIPPED``.

RX_FLAG_DECRYPTED
    This frame was decrypted in hardware.

RX_FLAG_MACTIME_PLCP_START
    The timestamp passed in the RX status (``mactime`` field) is valid and contains the time the SYNC preamble was received.

RX_FLAG_MMIC_STRIPPED
    the Michael MIC is stripped off this frame, verification has been done by the hardware.

RX_FLAG_IV_STRIPPED
    The IV/ICV are stripped from this frame. If this flag is set, the stack cannot do any replay detection hence the driver or hardware will have to do that.

RX_FLAG_FAILED_FCS_CRC
    Set this flag if the FCS check failed on the frame.

RX_FLAG_FAILED_PLCP_CRC
    Set this flag if the PCLP check failed on the frame.

RX_FLAG_MACTIME_START
    The timestamp passed in the RX status (``mactime`` field) is valid and contains the time the first symbol of the MPDU was received. This is useful in monitor mode and for
    proper IBSS merging.

RX_FLAG_SHORTPRE
    Short preamble was used for this frame

RX_FLAG_HT
    HT MCS was used and rate_idx is MCS index

RX_FLAG_40MHZ
    HT40 (40 MHz) was used

RX_FLAG_SHORT_GI
    Short guard interval was used

RX_FLAG_NO_SIGNAL_VAL
    The signal strength value is not present. Valid only for data frames (mainly A-MPDU)

RX_FLAG_HT_GF
    This frame was received in a HT-greenfield transmission, if the driver fills this value it should add ``IEEE80211_RADIOTAP_MCS_HAVE_FMT`` to hw.radiotap_mcs_details to
    advertise that fact

RX_FLAG_AMPDU_DETAILS
    A-MPDU details are known, in particular the reference number (``ampdu_reference``) must be populated and be a distinct number for each A-MPDU

RX_FLAG_PN_VALIDATED
    Currently only valid for CCMP/GCMP frames, this flag indicates that the PN was verified for replay protection. Note that this flag is also currently only supported when a frame
    is also decrypted (ie. ``RX_FLAG_DECRYPTED`` must be set)

RX_FLAG_DUP_VALIDATED
    -- undescribed --

RX_FLAG_AMPDU_LAST_KNOWN
    last subframe is known, should be set on all subframes of a single A-MPDU

RX_FLAG_AMPDU_IS_LAST
    this subframe is the last subframe of the A-MPDU

RX_FLAG_AMPDU_DELIM_CRC_ERROR
    A delimiter CRC error has been detected on this subframe

RX_FLAG_AMPDU_DELIM_CRC_KNOWN
    The delimiter CRC field is known (the CRC is stored in the ``ampdu_delimiter_crc`` field)

RX_FLAG_MACTIME_END
    The timestamp passed in the RX status (``mactime`` field) is valid and contains the time the last symbol of the MPDU (including FCS) was received.

RX_FLAG_VHT
    VHT MCS was used and rate_index is MCS index

RX_FLAG_LDPC
    LDPC was used

RX_FLAG_ONLY_MONITOR
    Report frame only to monitor interfaces without processing it in any regular way. This is useful if drivers offload some frames but still want to report them for sniffing
    purposes.

RX_FLAG_SKIP_MONITOR
    Process and report frame to all interfaces except monitor interfaces. This is useful if drivers offload some frames but still want to report them for sniffing purposes.

RX_FLAG_STBC_MASK
    STBC 2 bit bitmask. 1 - Nss=1, 2 - Nss=2, 3 - Nss=3

RX_FLAG_10MHZ
    10 MHz (half channel) was used

RX_FLAG_5MHZ
    5 MHz (quarter channel) was used

RX_FLAG_AMSDU_MORE
    Some drivers may prefer to report separate A-MSDU subframes instead of a one huge frame for performance reasons. All, but the last MSDU from an A-MSDU should have this flag
    set. E.g. if an A-MSDU has 3 frames, the first 2 must have the flag set, while the 3rd (last) one must not have this flag set. The flag is used to deal with
    retransmission/duplication recovery properly since A-MSDU subframes share the same sequence number. Reported subframes can be either regular MSDU or singly A-MSDUs. Subframes
    must not be interleaved with other frames.

RX_FLAG_RADIOTAP_VENDOR_DATA
    This frame contains vendor-specific radiotap data in the skb->data (before the frame) as described by the ``struct ieee80211_vendor_radiotap``.


Description
===========

These flags are used with the ``flag`` member of ``struct ieee80211_rx_status``.
