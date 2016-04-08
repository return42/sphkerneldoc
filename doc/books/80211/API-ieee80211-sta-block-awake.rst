
.. _API-ieee80211-sta-block-awake:

=========================
ieee80211_sta_block_awake
=========================

*man ieee80211_sta_block_awake(9)*

*4.6.0-rc1*

block station from waking up


Synopsis
========

.. c:function:: void ieee80211_sta_block_awake( struct ieee80211_hw * hw, struct ieee80211_sta * pubsta, bool block )

Arguments
=========

``hw``
    the hardware

``pubsta``
    the station

``block``
    whether to block or unblock


Description
===========

Some devices require that all frames that are on the queues for a specific station that went to sleep are flushed before a poll response or frames after the station woke up can be
delivered to that it. Note that such frames must be rejected by the driver as filtered, with the appropriate status flag.

This function allows implementing this mode in a race-free manner.

To do this, a driver must keep track of the number of frames still enqueued for a specific station. If this number is not zero when the station goes to sleep, the driver must call
this function to force mac80211 to consider the station to be asleep regardless of the station's actual state. Once the number of outstanding frames reaches zero, the driver must
call this function again to unblock the station. That will cause mac80211 to be able to send ps-poll responses, and if the station queried in the meantime then frames will also be
sent out as a result of this. Additionally, the driver will be notified that the station woke up some time after it is unblocked, regardless of whether the station actually woke up
while blocked or not.
