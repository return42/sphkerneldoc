
.. _AP:

=========================
Access point mode support
=========================

TBD

Some parts of the if_conf should be discussed here instead

Insert notes about VLAN interfaces with hw crypto here or in the hw crypto chapter.


.. _ps-client:

support for powersaving clients
===============================

In order to implement AP and P2P GO modes, mac80211 has support for client powersaving, both “legacy” PS (PS-Poll/null data) and uAPSD. There currently is no support for sAPSD.

There is one assumption that mac80211 makes, namely that a client will not poll with PS-Poll and trigger with uAPSD at the same time. Both are supported, and both can be used by
the same client, but they can't be used concurrently by the same client. This simplifies the driver code.

The first thing to keep in mind is that there is a flag for complete driver implementation: ``IEEE80211_HW_AP_LINK_PS``. If this flag is set, mac80211 expects the driver to handle
most of the state machine for powersaving clients and will ignore the PM bit in incoming frames. Drivers then use ``ieee80211_sta_ps_transition`` to inform mac80211 of stations'
powersave transitions. In this mode, mac80211 also doesn't handle PS-Poll/uAPSD.

In the mode without ``IEEE80211_HW_AP_LINK_PS``, mac80211 will check the PM bit in incoming frames for client powersave transitions. When a station goes to sleep, we will stop
transmitting to it. There is, however, a race condition: a station might go to sleep while there is data buffered on hardware queues. If the device has support for this it will
reject frames, and the driver should give the frames back to mac80211 with the ``IEEE80211_TX_STAT_TX_FILTERED`` flag set which will cause mac80211 to retry the frame when the
station wakes up. The driver is also notified of powersave transitions by calling its ``sta_notify`` callback.

When the station is asleep, it has three choices: it can wake up, it can PS-Poll, or it can possibly start a uAPSD service period. Waking up is implemented by simply transmitting
all buffered (and filtered) frames to the station. This is the easiest case. When the station sends a PS-Poll or a uAPSD trigger frame, mac80211 will inform the driver of this with
the ``allow_buffered_frames`` callback; this callback is optional. mac80211 will then transmit the frames as usual and set the ``IEEE80211_TX_CTL_NO_PS_BUFFER`` on each frame. The
last frame in the service period (or the only response to a PS-Poll) also has ``IEEE80211_TX_STATUS_EOSP`` set to indicate that it ends the service period; as this frame must have
TX status report it also sets ``IEEE80211_TX_CTL_REQ_TX_STATUS``. When TX status is reported for this frame, the service period is marked has having ended and a new one can be
started by the peer.

Additionally, non-bufferable MMPDUs can also be transmitted by mac80211 with the ``IEEE80211_TX_CTL_NO_PS_BUFFER`` set in them.

Another race condition can happen on some devices like iwlwifi when there are frames queued for the station and it wakes up or polls; the frames that are already queued could end
up being transmitted first instead, causing reordering and/or wrong processing of the EOSP. The cause is that allowing frames to be transmitted to a certain station is out-of-band
communication to the device. To allow this problem to be solved, the driver can call ``ieee80211_sta_block_awake`` if frames are buffered when it is notified that the station went
to sleep. When all these frames have been filtered (see above), it must call the function again to indicate that the station is no longer blocked.

If the driver buffers frames in the driver for aggregation in any way, it must use the ``ieee80211_sta_set_buffered`` call when it is notified of the station going to sleep to
inform mac80211 of any TIDs that have frames buffered. Note that when a station wakes up this information is reset (hence the requirement to call it when informed of the station
going to sleep). Then, when a service period starts for any reason, ``release_buffered_frames`` is called with the number of frames to be released and which TIDs they are to come
from. In this case, the driver is responsible for setting the EOSP (for uAPSD) and MORE_DATA bits in the released frames, to help the ``more_data`` parameter is passed to tell the
driver if there is more data on other TIDs -- the TIDs to release frames from are ignored since mac80211 doesn't know how many frames the buffers for those TIDs contain.

If the driver also implement GO mode, where absence periods may shorten service periods (or abort PS-Poll responses), it must filter those response frames except in the case of
frames that are buffered in the driver -- those must remain buffered to avoid reordering. Because it is possible that no frames are released in this case, the driver must call
``ieee80211_sta_eosp`` to indicate to mac80211 that the service period ended anyway.

Finally, if frames from multiple TIDs are released from mac80211 but the driver might reorder them, it must clear & set the flags appropriately (only the last frame may have
``IEEE80211_TX_STATUS_EOSP``) and also take care of the EOSP and MORE_DATA bits in the frame. The driver may also use ``ieee80211_sta_eosp`` in this case.

Note that if the driver ever buffers frames other than QoS-data frames, it must take care to never send a non-QoS-data frame as the last frame in a service period, adding a
QoS-nulldata frame after a non-QoS-data frame if needed.


.. toctree::
    :maxdepth: 1

    API-ieee80211-get-buffered-bc
    API-ieee80211-beacon-get
    API-ieee80211-sta-eosp
    API-enum-ieee80211-frame-release-type
    API-ieee80211-sta-ps-transition
    API-ieee80211-sta-ps-transition-ni
    API-ieee80211-sta-set-buffered
    API-ieee80211-sta-block-awake
