.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/mesh_pathtbl.c

.. _`mesh_path_lookup`:

mesh_path_lookup
================

.. c:function:: struct mesh_path *mesh_path_lookup(struct ieee80211_sub_if_data *sdata, const u8 *dst)

    look up a path in the mesh path table

    :param sdata:
        local subif
    :type sdata: struct ieee80211_sub_if_data \*

    :param dst:
        hardware address (ETH_ALEN length) of destination
    :type dst: const u8 \*

.. _`mesh_path_lookup.return`:

Return
------

pointer to the mesh path structure, or NULL if not found

.. _`mesh_path_lookup.locking`:

Locking
-------

must be called within a read rcu section.

.. _`mesh_path_lookup_by_idx`:

mesh_path_lookup_by_idx
=======================

.. c:function:: struct mesh_path *mesh_path_lookup_by_idx(struct ieee80211_sub_if_data *sdata, int idx)

    look up a path in the mesh path table by its index

    :param sdata:
        local subif, or NULL for all entries
    :type sdata: struct ieee80211_sub_if_data \*

    :param idx:
        index
    :type idx: int

.. _`mesh_path_lookup_by_idx.return`:

Return
------

pointer to the mesh path structure, or NULL if not found.

.. _`mesh_path_lookup_by_idx.locking`:

Locking
-------

must be called within a read rcu section.

.. _`mpp_path_lookup_by_idx`:

mpp_path_lookup_by_idx
======================

.. c:function:: struct mesh_path *mpp_path_lookup_by_idx(struct ieee80211_sub_if_data *sdata, int idx)

    look up a path in the proxy path table by its index

    :param sdata:
        local subif, or NULL for all entries
    :type sdata: struct ieee80211_sub_if_data \*

    :param idx:
        index
    :type idx: int

.. _`mpp_path_lookup_by_idx.return`:

Return
------

pointer to the proxy path structure, or NULL if not found.

.. _`mpp_path_lookup_by_idx.locking`:

Locking
-------

must be called within a read rcu section.

.. _`mesh_path_add_gate`:

mesh_path_add_gate
==================

.. c:function:: int mesh_path_add_gate(struct mesh_path *mpath)

    add the given mpath to a mesh gate to our path table

    :param mpath:
        gate path to add to table
    :type mpath: struct mesh_path \*

.. _`mesh_gate_del`:

mesh_gate_del
=============

.. c:function:: void mesh_gate_del(struct mesh_table *tbl, struct mesh_path *mpath)

    remove a mesh gate from the list of known gates

    :param tbl:
        table which holds our list of known gates
    :type tbl: struct mesh_table \*

    :param mpath:
        gate mpath
    :type mpath: struct mesh_path \*

.. _`mesh_gate_num`:

mesh_gate_num
=============

.. c:function:: int mesh_gate_num(struct ieee80211_sub_if_data *sdata)

    number of gates known to this interface

    :param sdata:
        subif data
    :type sdata: struct ieee80211_sub_if_data \*

.. _`mesh_path_add`:

mesh_path_add
=============

.. c:function:: struct mesh_path *mesh_path_add(struct ieee80211_sub_if_data *sdata, const u8 *dst)

    allocate and add a new path to the mesh path table

    :param sdata:
        local subif
    :type sdata: struct ieee80211_sub_if_data \*

    :param dst:
        destination address of the path (ETH_ALEN length)
    :type dst: const u8 \*

.. _`mesh_path_add.return`:

Return
------

0 on success

.. _`mesh_path_add.state`:

State
-----

the initial state of the new path is set to 0

.. _`mesh_plink_broken`:

mesh_plink_broken
=================

.. c:function:: void mesh_plink_broken(struct sta_info *sta)

    deactivates paths and sends perr when a link breaks

    :param sta:
        broken peer link
    :type sta: struct sta_info \*

.. _`mesh_plink_broken.description`:

Description
-----------

This function must be called from the rate control algorithm if enough
delivery errors suggest that a peer link is no longer usable.

.. _`mesh_path_flush_by_nexthop`:

mesh_path_flush_by_nexthop
==========================

.. c:function:: void mesh_path_flush_by_nexthop(struct sta_info *sta)

    Deletes mesh paths if their next hop matches

    :param sta:
        mesh peer to match
    :type sta: struct sta_info \*

.. _`mesh_path_flush_by_nexthop.rcu-notes`:

RCU notes
---------

this function is called when a mesh plink transitions from
PLINK_ESTAB to any other state, since PLINK_ESTAB state is the only one that
allows path creation. This will happen before the sta can be freed (because
\ :c:func:`sta_info_destroy`\  calls this) so any reader in a rcu read block will be
protected against the plink disappearing.

.. _`mesh_path_flush_by_iface`:

mesh_path_flush_by_iface
========================

.. c:function:: void mesh_path_flush_by_iface(struct ieee80211_sub_if_data *sdata)

    Deletes all mesh paths associated with a given iface

    :param sdata:
        interface data to match
    :type sdata: struct ieee80211_sub_if_data \*

.. _`mesh_path_flush_by_iface.description`:

Description
-----------

This function deletes both mesh paths as well as mesh portal paths.

.. _`table_path_del`:

table_path_del
==============

.. c:function:: int table_path_del(struct mesh_table *tbl, struct ieee80211_sub_if_data *sdata, const u8 *addr)

    delete a path from the mesh or mpp table

    :param tbl:
        mesh or mpp path table
    :type tbl: struct mesh_table \*

    :param sdata:
        local subif
    :type sdata: struct ieee80211_sub_if_data \*

    :param addr:
        dst address (ETH_ALEN length)
    :type addr: const u8 \*

.. _`table_path_del.return`:

Return
------

0 if successful

.. _`mesh_path_del`:

mesh_path_del
=============

.. c:function:: int mesh_path_del(struct ieee80211_sub_if_data *sdata, const u8 *addr)

    delete a mesh path from the table

    :param sdata:
        local subif
    :type sdata: struct ieee80211_sub_if_data \*

    :param addr:
        dst address (ETH_ALEN length)
    :type addr: const u8 \*

.. _`mesh_path_del.return`:

Return
------

0 if successful

.. _`mesh_path_tx_pending`:

mesh_path_tx_pending
====================

.. c:function:: void mesh_path_tx_pending(struct mesh_path *mpath)

    sends pending frames in a mesh path queue

    :param mpath:
        mesh path to activate
    :type mpath: struct mesh_path \*

.. _`mesh_path_tx_pending.locking`:

Locking
-------

the state_lock of the mpath structure must NOT be held when calling
this function.

.. _`mesh_path_send_to_gates`:

mesh_path_send_to_gates
=======================

.. c:function:: int mesh_path_send_to_gates(struct mesh_path *mpath)

    sends pending frames to all known mesh gates

    :param mpath:
        mesh path whose queue will be emptied
    :type mpath: struct mesh_path \*

.. _`mesh_path_send_to_gates.description`:

Description
-----------

If there is only one gate, the frames are transferred from the failed mpath
queue to that gate's queue.  If there are more than one gates, the frames
are copied from each gate to the next.  After frames are copied, the
mpath queues are emptied onto the transmission queue.

.. _`mesh_path_discard_frame`:

mesh_path_discard_frame
=======================

.. c:function:: void mesh_path_discard_frame(struct ieee80211_sub_if_data *sdata, struct sk_buff *skb)

    discard a frame whose path could not be resolved

    :param sdata:
        network subif the frame was to be sent through
    :type sdata: struct ieee80211_sub_if_data \*

    :param skb:
        frame to discard
    :type skb: struct sk_buff \*

.. _`mesh_path_discard_frame.locking`:

Locking
-------

the function must me called within a rcu_read_lock region

.. _`mesh_path_flush_pending`:

mesh_path_flush_pending
=======================

.. c:function:: void mesh_path_flush_pending(struct mesh_path *mpath)

    free the pending queue of a mesh path

    :param mpath:
        mesh path whose queue has to be freed
    :type mpath: struct mesh_path \*

.. _`mesh_path_flush_pending.locking`:

Locking
-------

the function must me called within a rcu_read_lock region

.. _`mesh_path_fix_nexthop`:

mesh_path_fix_nexthop
=====================

.. c:function:: void mesh_path_fix_nexthop(struct mesh_path *mpath, struct sta_info *next_hop)

    force a specific next hop for a mesh path

    :param mpath:
        the mesh path to modify
    :type mpath: struct mesh_path \*

    :param next_hop:
        the next hop to force
    :type next_hop: struct sta_info \*

.. _`mesh_path_fix_nexthop.locking`:

Locking
-------

this function must be called holding mpath->state_lock

.. This file was automatic generated / don't edit.

