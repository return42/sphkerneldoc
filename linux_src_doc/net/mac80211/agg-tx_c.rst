.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/agg-tx.c

.. _`tx-a-mpdu-aggregation`:

TX A-MPDU aggregation
=====================

Aggregation on the TX side requires setting the hardware flag
\ ``IEEE80211_HW_AMPDU_AGGREGATION``\ . The driver will then be handed
packets with a flag indicating A-MPDU aggregation. The driver
or device is responsible for actually aggregating the frames,
as well as deciding how many and which to aggregate.

When TX aggregation is started by some subsystem (usually the rate
control algorithm would be appropriate) by calling the
\ :c:func:`ieee80211_start_tx_ba_session`\  function, the driver will be
notified via its \ ``ampdu_action``\  function, with the
\ ``IEEE80211_AMPDU_TX_START``\  action.

In response to that, the driver is later required to call the
\ :c:func:`ieee80211_start_tx_ba_cb_irqsafe`\  function, which will really
start the aggregation session after the peer has also responded.
If the peer responds negatively, the session will be stopped
again right away. Note that it is possible for the aggregation
session to be stopped before the driver has indicated that it
is done setting it up, in which case it must not indicate the
setup completion.

Also note that, since we also need to wait for a response from
the peer, the driver is notified of the completion of the
handshake by the \ ``IEEE80211_AMPDU_TX_OPERATIONAL``\  action to the
\ ``ampdu_action``\  callback.

Similarly, when the aggregation session is stopped by the peer
or something calling \ :c:func:`ieee80211_stop_tx_ba_session`\ , the driver's
\ ``ampdu_action``\  function will be called with the action
\ ``IEEE80211_AMPDU_TX_STOP``\ . In this case, the call must not fail,
and the driver must later call \ :c:func:`ieee80211_stop_tx_ba_cb_irqsafe`\ .
Note that the sta can get destroyed before the BA tear down is
complete.

.. This file was automatic generated / don't edit.

