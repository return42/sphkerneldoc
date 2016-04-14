.. -*- coding: utf-8; mode: rst -*-

========
agg-rx.c
========

.. _`rx-a-mpdu-aggregation`:

RX A-MPDU aggregation
=====================

Aggregation on the RX side requires only implementing the
``ampdu_action`` callback that is invoked to start/stop any
block-ack sessions for RX aggregation.

When RX aggregation is started by the peer, the driver is
notified via ``ampdu_action`` function, with the
``IEEE80211_AMPDU_RX_START`` action, and may reject the request
in which case a negative response is sent to the peer, if it
accepts it a positive response is sent.

While the session is active, the device/driver are required
to de-aggregate frames and pass them up one by one to mac80211,
which will handle the reorder buffer.

When the aggregation session is stopped again by the peer or
ourselves, the driver's ``ampdu_action`` function will be called
with the action ``IEEE80211_AMPDU_RX_STOP``\ . In this case, the
call must not fail.

