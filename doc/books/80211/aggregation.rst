.. -*- coding: utf-8; mode: rst -*-

.. _aggregation:

===========
Aggregation
===========


TX A-MPDU aggregation
=====================

Aggregation on the TX side requires setting the hardware flag
``IEEE80211_HW_AMPDU_AGGREGATION``. The driver will then be handed
packets with a flag indicating A-MPDU aggregation. The driver or device
is responsible for actually aggregating the frames, as well as deciding
how many and which to aggregate.

When TX aggregation is started by some subsystem (usually the rate
control algorithm would be appropriate) by calling the
``ieee80211_start_tx_ba_session`` function, the driver will be notified
via its ``ampdu_action`` function, with the ``IEEE80211_AMPDU_TX_START``
action.

In response to that, the driver is later required to call the
``ieee80211_start_tx_ba_cb_irqsafe`` function, which will really start
the aggregation session after the peer has also responded. If the peer
responds negatively, the session will be stopped again right away. Note
that it is possible for the aggregation session to be stopped before the
driver has indicated that it is done setting it up, in which case it
must not indicate the setup completion.

Also note that, since we also need to wait for a response from the peer,
the driver is notified of the completion of the handshake by the
``IEEE80211_AMPDU_TX_OPERATIONAL`` action to the ``ampdu_action``
callback.

Similarly, when the aggregation session is stopped by the peer or
something calling ``ieee80211_stop_tx_ba_session``, the driver's
``ampdu_action`` function will be called with the action
``IEEE80211_AMPDU_TX_STOP``. In this case, the call must not fail, and
the driver must later call ``ieee80211_stop_tx_ba_cb_irqsafe``. Note
that the sta can get destroyed before the BA tear down is complete.


RX A-MPDU aggregation
=====================

Aggregation on the RX side requires only implementing the
``ampdu_action`` callback that is invoked to start/stop any block-ack
sessions for RX aggregation.

When RX aggregation is started by the peer, the driver is notified via
``ampdu_action`` function, with the ``IEEE80211_AMPDU_RX_START`` action,
and may reject the request in which case a negative response is sent to
the peer, if it accepts it a positive response is sent.

While the session is active, the device/driver are required to
de-aggregate frames and pass them up one by one to mac80211, which will
handle the reorder buffer.

When the aggregation session is stopped again by the peer or ourselves,
the driver's ``ampdu_action`` function will be called with the action
``IEEE80211_AMPDU_RX_STOP``. In this case, the call must not fail.


.. toctree::
    :maxdepth: 1

    API-enum-ieee80211-ampdu-mlme-action




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
