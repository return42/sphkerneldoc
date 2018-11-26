.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8192u/r8192U_core.c

.. _`rtl819x_ifcheck_resetornot`:

rtl819x_ifcheck_resetornot
==========================

.. c:function:: RESET_TYPE rtl819x_ifcheck_resetornot(struct net_device *dev)

    ask OS to reset driver

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`rtl819x_ifcheck_resetornot.description`:

Description
-----------

\param pAdapter      The adapter context for this miniport

Note:NIC with USB interface sholud not call this function because we
cannot scan descriptor to judge whether there is tx stuck.

.. _`rtl819x_ifcheck_resetornot.note`:

Note
----

This function may be required to be rewrite for Vista OS.
<<<Assumption: Tx spinlock has been acquired >>>

8185 and 8185b does not implement this function.

.. _`updaterxpkttimestamp8190`:

UpdateRxPktTimeStamp8190
========================

.. c:function:: void UpdateRxPktTimeStamp8190(struct net_device *dev, struct ieee80211_rx_stats *stats)

    UpdateRxPktTimeStamp

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param stats:
        *undescribed*
    :type stats: struct ieee80211_rx_stats \*

.. _`updaterxpkttimestamp8190.overview`:

Overview
--------

Record the TSF time stamp when receiving a packet

.. _`updaterxpkttimestamp8190.input`:

Input
-----

PADAPTER        Adapter
PRT_RFD         pRfd,

.. _`updaterxpkttimestamp8190.output`:

Output
------

PRT_RFD         pRfd
(pRfd->Status.TimeStampHigh is updated)
(pRfd->Status.TimeStampLow is updated)

.. _`updaterxpkttimestamp8190.return`:

Return
------

None

.. _`updatereceivedratehistogramstatistics8190`:

UpdateReceivedRateHistogramStatistics8190
=========================================

.. c:function:: void UpdateReceivedRateHistogramStatistics8190(struct net_device *dev, struct ieee80211_rx_stats *stats)

    UpdateReceivedRateHistogramStatistics

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param stats:
        *undescribed*
    :type stats: struct ieee80211_rx_stats \*

.. _`updatereceivedratehistogramstatistics8190.overview`:

Overview
--------

Record the received data rate

.. _`updatereceivedratehistogramstatistics8190.input`:

Input
-----

struct net_device \*dev
struct ieee80211_rx_stats \*stats

.. _`updatereceivedratehistogramstatistics8190.output`:

Output
------


(priv->stats.ReceivedRateHistogram[] is updated)

.. _`updatereceivedratehistogramstatistics8190.return`:

Return
------

None

.. This file was automatic generated / don't edit.

