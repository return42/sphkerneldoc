.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/mesh_ps.c

.. _`mps_qos_null_get`:

mps_qos_null_get
================

.. c:function:: struct sk_buff *mps_qos_null_get(struct sta_info *sta)

    create pre-addressed QoS Null frame for mesh powersave

    :param sta:
        *undescribed*
    :type sta: struct sta_info \*

.. _`mps_qos_null_tx`:

mps_qos_null_tx
===============

.. c:function:: void mps_qos_null_tx(struct sta_info *sta)

    send a QoS Null to indicate link-specific power mode

    :param sta:
        *undescribed*
    :type sta: struct sta_info \*

.. _`ieee80211_mps_local_status_update`:

ieee80211_mps_local_status_update
=================================

.. c:function:: u32 ieee80211_mps_local_status_update(struct ieee80211_sub_if_data *sdata)

    track status of local link-specific PMs

    :param sdata:
        local mesh subif
    :type sdata: struct ieee80211_sub_if_data \*

.. _`ieee80211_mps_local_status_update.description`:

Description
-----------

sets the non-peer power mode and triggers the driver PS (re-)configuration
Return BSS_CHANGED_BEACON if a beacon update is necessary.

.. _`ieee80211_mps_set_sta_local_pm`:

ieee80211_mps_set_sta_local_pm
==============================

.. c:function:: u32 ieee80211_mps_set_sta_local_pm(struct sta_info *sta, enum nl80211_mesh_power_mode pm)

    set local PM towards a mesh STA

    :param sta:
        mesh STA
    :type sta: struct sta_info \*

    :param pm:
        the power mode to set
        Return BSS_CHANGED_BEACON if a beacon update is in order.
    :type pm: enum nl80211_mesh_power_mode

.. _`ieee80211_mps_set_frame_flags`:

ieee80211_mps_set_frame_flags
=============================

.. c:function:: void ieee80211_mps_set_frame_flags(struct ieee80211_sub_if_data *sdata, struct sta_info *sta, struct ieee80211_hdr *hdr)

    set mesh PS flags in FC (and QoS Control)

    :param sdata:
        local mesh subif
    :type sdata: struct ieee80211_sub_if_data \*

    :param sta:
        mesh STA
    :type sta: struct sta_info \*

    :param hdr:
        802.11 frame header
    :type hdr: struct ieee80211_hdr \*

.. _`ieee80211_mps_set_frame_flags.description`:

Description
-----------

see IEEE802.11-2012 8.2.4.1.7 and 8.2.4.5.11

.. _`ieee80211_mps_set_frame_flags.note`:

NOTE
----

sta must be given when an individually-addressed QoS frame header
is handled, for group-addressed and management frames it is not used

.. _`ieee80211_mps_sta_status_update`:

ieee80211_mps_sta_status_update
===============================

.. c:function:: void ieee80211_mps_sta_status_update(struct sta_info *sta)

    update buffering status of neighbor STA

    :param sta:
        mesh STA
    :type sta: struct sta_info \*

.. _`ieee80211_mps_sta_status_update.description`:

Description
-----------

called after change of peering status or non-peer/peer-specific power mode

.. _`ieee80211_mps_rx_h_sta_process`:

ieee80211_mps_rx_h_sta_process
==============================

.. c:function:: void ieee80211_mps_rx_h_sta_process(struct sta_info *sta, struct ieee80211_hdr *hdr)

    frame receive handler for mesh powersave

    :param sta:
        STA info that transmitted the frame
    :type sta: struct sta_info \*

    :param hdr:
        IEEE 802.11 (QoS) Header
    :type hdr: struct ieee80211_hdr \*

.. _`mpsp_qos_null_append`:

mpsp_qos_null_append
====================

.. c:function:: void mpsp_qos_null_append(struct sta_info *sta, struct sk_buff_head *frames)

    append QoS Null frame to MPSP skb queue if needed

    :param sta:
        *undescribed*
    :type sta: struct sta_info \*

    :param frames:
        *undescribed*
    :type frames: struct sk_buff_head \*

.. _`mpsp_qos_null_append.description`:

Description
-----------

To properly end a mesh MPSP the last transmitted frame has to set the EOSP
flag in the QoS Control field. In case the current tailing frame is not a
QoS Data frame, append a QoS Null to carry the flag.

.. _`mps_frame_deliver`:

mps_frame_deliver
=================

.. c:function:: void mps_frame_deliver(struct sta_info *sta, int n_frames)

    transmit frames during mesh powersave

    :param sta:
        STA info to transmit to
    :type sta: struct sta_info \*

    :param n_frames:
        number of frames to transmit. -1 for all
    :type n_frames: int

.. _`ieee80211_mpsp_trigger_process`:

ieee80211_mpsp_trigger_process
==============================

.. c:function:: void ieee80211_mpsp_trigger_process(u8 *qc, struct sta_info *sta, bool tx, bool acked)

    track status of mesh Peer Service Periods

    :param qc:
        QoS Control field
    :type qc: u8 \*

    :param sta:
        peer to start a MPSP with
    :type sta: struct sta_info \*

    :param tx:
        frame was transmitted by the local STA
    :type tx: bool

    :param acked:
        frame has been transmitted successfully
    :type acked: bool

.. _`ieee80211_mpsp_trigger_process.note`:

NOTE
----

active mode STA may only serve as MPSP owner

.. _`ieee80211_mps_frame_release`:

ieee80211_mps_frame_release
===========================

.. c:function:: void ieee80211_mps_frame_release(struct sta_info *sta, struct ieee802_11_elems *elems)

    release frames buffered due to mesh power save

    :param sta:
        mesh STA
    :type sta: struct sta_info \*

    :param elems:
        IEs of beacon or probe response
    :type elems: struct ieee802_11_elems \*

.. _`ieee80211_mps_frame_release.description`:

Description
-----------

For peers if we have individually-addressed frames buffered or the peer
indicates buffered frames, send a corresponding MPSP trigger frame. Since
we do not evaluate the awake window duration, QoS Nulls are used as MPSP
trigger frames. If the neighbour STA is not a peer, only send single frames.

.. This file was automatic generated / don't edit.

