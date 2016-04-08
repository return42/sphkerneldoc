
.. _API-enum-mac80211-tx-info-flags:

===========================
enum mac80211_tx_info_flags
===========================

*man enum mac80211_tx_info_flags(9)*

*4.6.0-rc1*

flags to describe transmission information/status


Synopsis
========

.. code-block:: c

    enum mac80211_tx_info_flags {
      IEEE80211_TX_CTL_REQ_TX_STATUS,
      IEEE80211_TX_CTL_ASSIGN_SEQ,
      IEEE80211_TX_CTL_NO_ACK,
      IEEE80211_TX_CTL_CLEAR_PS_FILT,
      IEEE80211_TX_CTL_FIRST_FRAGMENT,
      IEEE80211_TX_CTL_SEND_AFTER_DTIM,
      IEEE80211_TX_CTL_AMPDU,
      IEEE80211_TX_CTL_INJECTED,
      IEEE80211_TX_STAT_TX_FILTERED,
      IEEE80211_TX_STAT_ACK,
      IEEE80211_TX_STAT_AMPDU,
      IEEE80211_TX_STAT_AMPDU_NO_BACK,
      IEEE80211_TX_CTL_RATE_CTRL_PROBE,
      IEEE80211_TX_INTFL_OFFCHAN_TX_OK,
      IEEE80211_TX_INTFL_NEED_TXPROCESSING,
      IEEE80211_TX_INTFL_RETRIED,
      IEEE80211_TX_INTFL_DONT_ENCRYPT,
      IEEE80211_TX_CTL_NO_PS_BUFFER,
      IEEE80211_TX_CTL_MORE_FRAMES,
      IEEE80211_TX_INTFL_RETRANSMISSION,
      IEEE80211_TX_INTFL_MLME_CONN_TX,
      IEEE80211_TX_INTFL_NL80211_FRAME_TX,
      IEEE80211_TX_CTL_LDPC,
      IEEE80211_TX_CTL_STBC,
      IEEE80211_TX_CTL_TX_OFFCHAN,
      IEEE80211_TX_INTFL_TKIP_MIC_FAILURE,
      IEEE80211_TX_CTL_NO_CCK_RATE,
      IEEE80211_TX_STATUS_EOSP,
      IEEE80211_TX_CTL_USE_MINRATE,
      IEEE80211_TX_CTL_DONTFRAG,
      IEEE80211_TX_STAT_NOACK_TRANSMITTED
    };


Constants
=========

IEEE80211_TX_CTL_REQ_TX_STATUS
    require TX status callback for this frame.

IEEE80211_TX_CTL_ASSIGN_SEQ
    The driver has to assign a sequence number to this frame, taking care of not overwriting the fragment number and increasing the sequence number only when the
    IEEE80211_TX_CTL_FIRST_FRAGMENT flag is set. mac80211 will properly assign sequence numbers to QoS-data frames but cannot do so correctly for non-QoS-data and management
    frames because beacons need them from that counter as well and mac80211 cannot guarantee proper sequencing. If this flag is set, the driver should instruct the hardware to
    assign a sequence number to the frame or assign one itself. Cf. IEEE 802.11-2007 7.1.3.4.1 paragraph 3. This flag will always be set for beacons and always be clear for frames
    without a sequence number field.

IEEE80211_TX_CTL_NO_ACK
    tell the low level not to wait for an ack

IEEE80211_TX_CTL_CLEAR_PS_FILT
    clear powersave filter for destination station

IEEE80211_TX_CTL_FIRST_FRAGMENT
    this is a first fragment of the frame

IEEE80211_TX_CTL_SEND_AFTER_DTIM
    send this frame after DTIM beacon

IEEE80211_TX_CTL_AMPDU
    this frame should be sent as part of an A-MPDU

IEEE80211_TX_CTL_INJECTED
    Frame was injected, internal to mac80211.

IEEE80211_TX_STAT_TX_FILTERED
    The frame was not transmitted because the destination STA was in powersave mode. Note that to avoid race conditions, the filter must be set by the hardware or firmware upon
    receiving a frame that indicates that the station went to sleep (must be done on device to filter frames already on the queue) and may only be unset after mac80211 gives the OK
    for that by setting the IEEE80211_TX_CTL_CLEAR_PS_FILT (see above), since only then is it guaranteed that no more frames are in the hardware queue.

IEEE80211_TX_STAT_ACK
    Frame was acknowledged

IEEE80211_TX_STAT_AMPDU
    The frame was aggregated, so status is for the whole aggregation.

IEEE80211_TX_STAT_AMPDU_NO_BACK
    no block ack was returned, so consider using block ack request (BAR).

IEEE80211_TX_CTL_RATE_CTRL_PROBE
    internal to mac80211, can be set by rate control algorithms to indicate probe rate, will be cleared for fragmented frames (except on the last fragment)

IEEE80211_TX_INTFL_OFFCHAN_TX_OK
    Internal to mac80211. Used to indicate that a frame can be transmitted while the queues are stopped for off-channel operation.

IEEE80211_TX_INTFL_NEED_TXPROCESSING
    completely internal to mac80211, used to indicate that a pending frame requires TX processing before it can be sent out.

IEEE80211_TX_INTFL_RETRIED
    completely internal to mac80211, used to indicate that a frame was already retried due to PS

IEEE80211_TX_INTFL_DONT_ENCRYPT
    completely internal to mac80211, used to indicate frame should not be encrypted

IEEE80211_TX_CTL_NO_PS_BUFFER
    This frame is a response to a poll frame (PS-Poll or uAPSD) or a non-bufferable MMPDU and must be sent although the station is in powersave mode.

IEEE80211_TX_CTL_MORE_FRAMES
    More frames will be passed to the transmit function after the current frame, this can be used by drivers to kick the DMA queue only if unset or when the queue gets full.

IEEE80211_TX_INTFL_RETRANSMISSION
    This frame is being retransmitted after TX status because the destination was asleep, it must not be modified again (no seqno assignment, crypto, etc.)

IEEE80211_TX_INTFL_MLME_CONN_TX
    This frame was transmitted by the MLME code for connection establishment, this indicates that its status should kick the MLME state machine.

IEEE80211_TX_INTFL_NL80211_FRAME_TX
    Frame was requested through nl80211 MLME command (internal to mac80211 to figure out whether to send TX status to user space)

IEEE80211_TX_CTL_LDPC
    tells the driver to use LDPC for this frame

IEEE80211_TX_CTL_STBC
    Enables Space-Time Block Coding (STBC) for this frame and selects the maximum number of streams that it can use.

IEEE80211_TX_CTL_TX_OFFCHAN
    Marks this packet to be transmitted on the off-channel channel when a remain-on-channel offload is done in hardware -- normal packets still flow and are expected to be handled
    properly by the device.

IEEE80211_TX_INTFL_TKIP_MIC_FAILURE
    Marks this packet to be used for TKIP testing. It will be sent out with incorrect Michael MIC key to allow TKIP countermeasures to be tested.

IEEE80211_TX_CTL_NO_CCK_RATE
    This frame will be sent at non CCK rate. This flag is actually used for management frame especially for P2P frames not being sent at CCK rate in 2GHz band.

IEEE80211_TX_STATUS_EOSP
    This packet marks the end of service period, when its status is reported the service period ends. For frames in an SP that mac80211 transmits, it is already set; for driver
    frames the driver may set this flag. It is also used to do the same for PS-Poll responses.

IEEE80211_TX_CTL_USE_MINRATE
    This frame will be sent at lowest rate. This flag is used to send nullfunc frame at minimum rate when the nullfunc is used for connection monitoring purpose.

IEEE80211_TX_CTL_DONTFRAG
    Don't fragment this packet even if it would be fragmented by size (this is optional, only used for monitor injection).

IEEE80211_TX_STAT_NOACK_TRANSMITTED
    A frame that was marked with IEEE80211_TX_CTL_NO_ACK has been successfully transmitted without any errors (like issues specific to the driver/HW). This flag must not be set
    for frames that don't request no-ack behaviour with IEEE80211_TX_CTL_NO_ACK.


Description
===========

These flags are used with the ``flags`` member of ``ieee80211_tx_info``.


Note
====

If you have to add new flags to the enumeration, then don't forget to update ``IEEE80211_TX_TEMPORARY_FLAGS`` when necessary.
