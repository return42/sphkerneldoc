
.. _API-rate-control-send-low:

=====================
rate_control_send_low
=====================

*man rate_control_send_low(9)*

*4.6.0-rc1*

helper for drivers for management/no-ack frames


Synopsis
========

.. c:function:: bool rate_control_send_low( struct ieee80211_sta * sta, void * priv_sta, struct ieee80211_tx_rate_control * txrc )

Arguments
=========

``sta``
    ``struct ieee80211_sta`` pointer to the target destination. Note that this may be null.

``priv_sta``
    private rate control structure. This may be null.

``txrc``
    rate control information we sholud populate for mac80211.


Description
===========

Rate control algorithms that agree to use the lowest rate to send management frames and NO_ACK data with the respective hw retries should use this in the beginning of their
mac80211 get_rate callback. If true is returned the rate control can simply return. If false is returned we guarantee that sta and sta and priv_sta is not null.

Rate control algorithms wishing to do more intelligent selection of rate for multicast/broadcast frames may choose to not use this.
