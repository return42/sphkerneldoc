.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/mesh_hwmp.c

.. _`mesh_path_error_tx`:

mesh_path_error_tx
==================

.. c:function:: int mesh_path_error_tx(struct ieee80211_sub_if_data *sdata, u8 ttl, const u8 *target, u32 target_sn, u16 target_rcode, const u8 *ra)

    Sends a PERR mesh management frame

    :param struct ieee80211_sub_if_data \*sdata:
        local mesh subif

    :param u8 ttl:
        allowed remaining hops

    :param const u8 \*target:
        broken destination

    :param u32 target_sn:
        SN of the broken destination

    :param u16 target_rcode:
        reason code for this PERR

    :param const u8 \*ra:
        node this frame is addressed to

.. _`mesh_path_error_tx.note`:

Note
----

This function may be called with driver locks taken that the driver
also acquires in the TX path.  To avoid a deadlock we don't transmit the
frame directly but add it to the pending queue instead.

.. _`hwmp_route_info_get`:

hwmp_route_info_get
===================

.. c:function:: u32 hwmp_route_info_get(struct ieee80211_sub_if_data *sdata, struct ieee80211_mgmt *mgmt, const u8 *hwmp_ie, enum mpath_frame_type action)

    Update routing info to originator and transmitter

    :param struct ieee80211_sub_if_data \*sdata:
        local mesh subif

    :param struct ieee80211_mgmt \*mgmt:
        mesh management frame

    :param const u8 \*hwmp_ie:
        hwmp information element (PREP or PREQ)

    :param enum mpath_frame_type action:
        type of hwmp ie

.. _`hwmp_route_info_get.description`:

Description
-----------

This function updates the path routing information to the originator and the
transmitter of a HWMP PREQ or PREP frame.

.. _`hwmp_route_info_get.return`:

Return
------

metric to frame originator or 0 if the frame should not be further
processed

.. _`hwmp_route_info_get.notes`:

Notes
-----

this function is the only place (besides user-provided info) where
path routing information is updated.

.. _`mesh_queue_preq`:

mesh_queue_preq
===============

.. c:function:: void mesh_queue_preq(struct mesh_path *mpath, u8 flags)

    queue a PREQ to a given destination

    :param struct mesh_path \*mpath:
        mesh path to discover

    :param u8 flags:
        special attributes of the PREQ to be sent

.. _`mesh_queue_preq.locking`:

Locking
-------

the function must be called from within a rcu read lock block.

.. _`mesh_path_start_discovery`:

mesh_path_start_discovery
=========================

.. c:function:: void mesh_path_start_discovery(struct ieee80211_sub_if_data *sdata)

    launch a path discovery from the PREQ queue

    :param struct ieee80211_sub_if_data \*sdata:
        local mesh subif

.. _`mesh_nexthop_resolve`:

mesh_nexthop_resolve
====================

.. c:function:: int mesh_nexthop_resolve(struct ieee80211_sub_if_data *sdata, struct sk_buff *skb)

    lookup next hop; conditionally start path discovery

    :param struct ieee80211_sub_if_data \*sdata:
        network subif the frame will be sent through

    :param struct sk_buff \*skb:
        802.11 frame to be sent

.. _`mesh_nexthop_resolve.description`:

Description
-----------

Lookup next hop for given skb and start path discovery if no
forwarding information is found.

.. _`mesh_nexthop_resolve.return`:

Return
------

0 if the next hop was found and -ENOENT if the frame was queued.
skb is freeed here if no mpath could be allocated.

.. _`mesh_nexthop_lookup`:

mesh_nexthop_lookup
===================

.. c:function:: int mesh_nexthop_lookup(struct ieee80211_sub_if_data *sdata, struct sk_buff *skb)

    put the appropriate next hop on a mesh frame. Calling this function is considered "using" the associated mpath, so preempt a path refresh if this mpath expires soon.

    :param struct ieee80211_sub_if_data \*sdata:
        network subif the frame will be sent through

    :param struct sk_buff \*skb:
        802.11 frame to be sent

.. _`mesh_nexthop_lookup.return`:

Return
------

0 if the next hop was found. Nonzero otherwise.

.. This file was automatic generated / don't edit.

