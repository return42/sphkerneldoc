.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/translation-table.c

.. _`batadv_compare_tt`:

batadv_compare_tt
=================

.. c:function:: bool batadv_compare_tt(const struct hlist_node *node, const void *data2)

    check if two TT entries are the same

    :param node:
        the list element pointer of the first TT entry
    :type node: const struct hlist_node \*

    :param data2:
        pointer to the tt_common_entry of the second TT entry
    :type data2: const void \*

.. _`batadv_compare_tt.description`:

Description
-----------

Compare the MAC address and the VLAN ID of the two TT entries and check if
they are the same TT client.

.. _`batadv_compare_tt.return`:

Return
------

true if the two TT clients are the same, false otherwise

.. _`batadv_choose_tt`:

batadv_choose_tt
================

.. c:function:: u32 batadv_choose_tt(const void *data, u32 size)

    return the index of the tt entry in the hash table

    :param data:
        pointer to the tt_common_entry object to map
    :type data: const void \*

    :param size:
        the size of the hash table
    :type size: u32

.. _`batadv_choose_tt.return`:

Return
------

the hash index where the object represented by 'data' should be
stored at.

.. _`batadv_tt_hash_find`:

batadv_tt_hash_find
===================

.. c:function:: struct batadv_tt_common_entry *batadv_tt_hash_find(struct batadv_hashtable *hash, const u8 *addr, unsigned short vid)

    look for a client in the given hash table

    :param hash:
        the hash table to search
    :type hash: struct batadv_hashtable \*

    :param addr:
        the mac address of the client to look for
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_hash_find.return`:

Return
------

a pointer to the tt_common struct belonging to the searched client if
found, NULL otherwise.

.. _`batadv_tt_local_hash_find`:

batadv_tt_local_hash_find
=========================

.. c:function:: struct batadv_tt_local_entry *batadv_tt_local_hash_find(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    search the local table for a given client

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the client to look for
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_local_hash_find.return`:

Return
------

a pointer to the corresponding tt_local_entry struct if the client is
found, NULL otherwise.

.. _`batadv_tt_global_hash_find`:

batadv_tt_global_hash_find
==========================

.. c:function:: struct batadv_tt_global_entry *batadv_tt_global_hash_find(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    search the global table for a given client

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the client to look for
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_global_hash_find.return`:

Return
------

a pointer to the corresponding tt_global_entry struct if the client
is found, NULL otherwise.

.. _`batadv_tt_local_entry_free_rcu`:

batadv_tt_local_entry_free_rcu
==============================

.. c:function:: void batadv_tt_local_entry_free_rcu(struct rcu_head *rcu)

    free the tt_local_entry

    :param rcu:
        rcu pointer of the tt_local_entry
    :type rcu: struct rcu_head \*

.. _`batadv_tt_local_entry_release`:

batadv_tt_local_entry_release
=============================

.. c:function:: void batadv_tt_local_entry_release(struct kref *ref)

    release tt_local_entry from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the nc_node
    :type ref: struct kref \*

.. _`batadv_tt_local_entry_put`:

batadv_tt_local_entry_put
=========================

.. c:function:: void batadv_tt_local_entry_put(struct batadv_tt_local_entry *tt_local_entry)

    decrement the tt_local_entry refcounter and possibly release it

    :param tt_local_entry:
        tt_local_entry to be free'd
    :type tt_local_entry: struct batadv_tt_local_entry \*

.. _`batadv_tt_global_entry_free_rcu`:

batadv_tt_global_entry_free_rcu
===============================

.. c:function:: void batadv_tt_global_entry_free_rcu(struct rcu_head *rcu)

    free the tt_global_entry

    :param rcu:
        rcu pointer of the tt_global_entry
    :type rcu: struct rcu_head \*

.. _`batadv_tt_global_entry_release`:

batadv_tt_global_entry_release
==============================

.. c:function:: void batadv_tt_global_entry_release(struct kref *ref)

    release tt_global_entry from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the nc_node
    :type ref: struct kref \*

.. _`batadv_tt_global_entry_put`:

batadv_tt_global_entry_put
==========================

.. c:function:: void batadv_tt_global_entry_put(struct batadv_tt_global_entry *tt_global_entry)

    decrement the tt_global_entry refcounter and possibly release it

    :param tt_global_entry:
        tt_global_entry to be free'd
    :type tt_global_entry: struct batadv_tt_global_entry \*

.. _`batadv_tt_global_hash_count`:

batadv_tt_global_hash_count
===========================

.. c:function:: int batadv_tt_global_hash_count(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    count the number of orig entries

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the client to count entries for
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_global_hash_count.return`:

Return
------

the number of originators advertising the given address/data
(excluding ourself).

.. _`batadv_tt_local_size_mod`:

batadv_tt_local_size_mod
========================

.. c:function:: void batadv_tt_local_size_mod(struct batadv_priv *bat_priv, unsigned short vid, int v)

    change the size by v of the local table identified by vid

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        the VLAN identifier of the sub-table to change
    :type vid: unsigned short

    :param v:
        the amount to sum to the local table size
    :type v: int

.. _`batadv_tt_local_size_inc`:

batadv_tt_local_size_inc
========================

.. c:function:: void batadv_tt_local_size_inc(struct batadv_priv *bat_priv, unsigned short vid)

    increase by one the local table size for the given vid

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        the VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_local_size_dec`:

batadv_tt_local_size_dec
========================

.. c:function:: void batadv_tt_local_size_dec(struct batadv_priv *bat_priv, unsigned short vid)

    decrease by one the local table size for the given vid

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        the VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_global_size_mod`:

batadv_tt_global_size_mod
=========================

.. c:function:: void batadv_tt_global_size_mod(struct batadv_orig_node *orig_node, unsigned short vid, int v)

    change the size by v of the global table for orig_node identified by vid

    :param orig_node:
        the originator for which the table has to be modified
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        the VLAN identifier
    :type vid: unsigned short

    :param v:
        the amount to sum to the global table size
    :type v: int

.. _`batadv_tt_global_size_inc`:

batadv_tt_global_size_inc
=========================

.. c:function:: void batadv_tt_global_size_inc(struct batadv_orig_node *orig_node, unsigned short vid)

    increase by one the global table size for the given vid

    :param orig_node:
        the originator which global table size has to be decreased
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        the vlan identifier
    :type vid: unsigned short

.. _`batadv_tt_global_size_dec`:

batadv_tt_global_size_dec
=========================

.. c:function:: void batadv_tt_global_size_dec(struct batadv_orig_node *orig_node, unsigned short vid)

    decrease by one the global table size for the given vid

    :param orig_node:
        the originator which global table size has to be decreased
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        the vlan identifier
    :type vid: unsigned short

.. _`batadv_tt_orig_list_entry_free_rcu`:

batadv_tt_orig_list_entry_free_rcu
==================================

.. c:function:: void batadv_tt_orig_list_entry_free_rcu(struct rcu_head *rcu)

    free the orig_entry

    :param rcu:
        rcu pointer of the orig_entry
    :type rcu: struct rcu_head \*

.. _`batadv_tt_orig_list_entry_release`:

batadv_tt_orig_list_entry_release
=================================

.. c:function:: void batadv_tt_orig_list_entry_release(struct kref *ref)

    release tt orig entry from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the tt orig entry
    :type ref: struct kref \*

.. _`batadv_tt_orig_list_entry_put`:

batadv_tt_orig_list_entry_put
=============================

.. c:function:: void batadv_tt_orig_list_entry_put(struct batadv_tt_orig_list_entry *orig_entry)

    decrement the tt orig entry refcounter and possibly release it

    :param orig_entry:
        tt orig entry to be free'd
    :type orig_entry: struct batadv_tt_orig_list_entry \*

.. _`batadv_tt_local_event`:

batadv_tt_local_event
=====================

.. c:function:: void batadv_tt_local_event(struct batadv_priv *bat_priv, struct batadv_tt_local_entry *tt_local_entry, u8 event_flags)

    store a local TT event (ADD/DEL)

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_local_entry:
        the TT entry involved in the event
    :type tt_local_entry: struct batadv_tt_local_entry \*

    :param event_flags:
        flags to store in the event structure
    :type event_flags: u8

.. _`batadv_tt_len`:

batadv_tt_len
=============

.. c:function:: int batadv_tt_len(int changes_num)

    compute length in bytes of given number of tt changes

    :param changes_num:
        number of tt changes
    :type changes_num: int

.. _`batadv_tt_len.return`:

Return
------

computed length in bytes.

.. _`batadv_tt_entries`:

batadv_tt_entries
=================

.. c:function:: u16 batadv_tt_entries(u16 tt_len)

    compute the number of entries fitting in tt_len bytes

    :param tt_len:
        available space
    :type tt_len: u16

.. _`batadv_tt_entries.return`:

Return
------

the number of entries.

.. _`batadv_tt_local_table_transmit_size`:

batadv_tt_local_table_transmit_size
===================================

.. c:function:: int batadv_tt_local_table_transmit_size(struct batadv_priv *bat_priv)

    calculates the local translation table size when transmitted over the air

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_tt_local_table_transmit_size.return`:

Return
------

local translation table size in bytes.

.. _`batadv_tt_local_add`:

batadv_tt_local_add
===================

.. c:function:: bool batadv_tt_local_add(struct net_device *soft_iface, const u8 *addr, unsigned short vid, int ifindex, u32 mark)

    add a new client to the local table or update an existing client

    :param soft_iface:
        netdev struct of the mesh interface
    :type soft_iface: struct net_device \*

    :param addr:
        the mac address of the client to add
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

    :param ifindex:
        index of the interface where the client is connected to (useful to
        identify wireless clients)
    :type ifindex: int

    :param mark:
        the value contained in the skb->mark field of the received packet (if
        any)
    :type mark: u32

.. _`batadv_tt_local_add.return`:

Return
------

true if the client was successfully added, false otherwise.

.. _`batadv_tt_prepare_tvlv_global_data`:

batadv_tt_prepare_tvlv_global_data
==================================

.. c:function:: u16 batadv_tt_prepare_tvlv_global_data(struct batadv_orig_node *orig_node, struct batadv_tvlv_tt_data **tt_data, struct batadv_tvlv_tt_change **tt_change, s32 *tt_len)

    prepare the TVLV TT header to send within a TT Response directed to another node

    :param orig_node:
        originator for which the TT data has to be prepared
    :type orig_node: struct batadv_orig_node \*

    :param tt_data:
        uninitialised pointer to the address of the TVLV buffer
    :type tt_data: struct batadv_tvlv_tt_data \*\*

    :param tt_change:
        uninitialised pointer to the address of the area where the TT
        changed can be stored
    :type tt_change: struct batadv_tvlv_tt_change \*\*

    :param tt_len:
        pointer to the length to reserve to the tt_change. if -1 this
        function reserves the amount of space needed to send the entire global TT
        table. In case of success the value is updated with the real amount of
        reserved bytes
        Allocate the needed amount of memory for the entire TT TVLV and write its
        header made up by one tvlv_tt_data object and a series of tvlv_tt_vlan_data
        objects, one per active VLAN served by the originator node.
    :type tt_len: s32 \*

.. _`batadv_tt_prepare_tvlv_global_data.return`:

Return
------

the size of the allocated buffer or 0 in case of failure.

.. _`batadv_tt_prepare_tvlv_local_data`:

batadv_tt_prepare_tvlv_local_data
=================================

.. c:function:: u16 batadv_tt_prepare_tvlv_local_data(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data **tt_data, struct batadv_tvlv_tt_change **tt_change, s32 *tt_len)

    allocate and prepare the TT TVLV for this node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_data:
        uninitialised pointer to the address of the TVLV buffer
    :type tt_data: struct batadv_tvlv_tt_data \*\*

    :param tt_change:
        uninitialised pointer to the address of the area where the TT
        changes can be stored
    :type tt_change: struct batadv_tvlv_tt_change \*\*

    :param tt_len:
        pointer to the length to reserve to the tt_change. if -1 this
        function reserves the amount of space needed to send the entire local TT
        table. In case of success the value is updated with the real amount of
        reserved bytes
    :type tt_len: s32 \*

.. _`batadv_tt_prepare_tvlv_local_data.description`:

Description
-----------

Allocate the needed amount of memory for the entire TT TVLV and write its
header made up by one tvlv_tt_data object and a series of tvlv_tt_vlan_data
objects, one per active VLAN.

.. _`batadv_tt_prepare_tvlv_local_data.return`:

Return
------

the size of the allocated buffer or 0 in case of failure.

.. _`batadv_tt_tvlv_container_update`:

batadv_tt_tvlv_container_update
===============================

.. c:function:: void batadv_tt_tvlv_container_update(struct batadv_priv *bat_priv)

    update the translation table tvlv container after local tt changes have been committed

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_tt_local_seq_print_text`:

batadv_tt_local_seq_print_text
==============================

.. c:function:: int batadv_tt_local_seq_print_text(struct seq_file *seq, void *offset)

    Print the local tt table in a seq file

    :param seq:
        seq file to print on
    :type seq: struct seq_file \*

    :param offset:
        not used
    :type offset: void \*

.. _`batadv_tt_local_seq_print_text.return`:

Return
------

always 0

.. _`batadv_tt_local_dump_entry`:

batadv_tt_local_dump_entry
==========================

.. c:function:: int batadv_tt_local_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_tt_common_entry *common)

    Dump one TT local entry into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param common:
        tt local & tt global common data
    :type common: struct batadv_tt_common_entry \*

.. _`batadv_tt_local_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_tt_local_dump_bucket`:

batadv_tt_local_dump_bucket
===========================

.. c:function:: int batadv_tt_local_dump_bucket(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct hlist_head *head, int *idx_s)

    Dump one TT local bucket into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param head:
        Pointer to the list containing the local tt entries
    :type head: struct hlist_head \*

    :param idx_s:
        Number of entries to skip
    :type idx_s: int \*

.. _`batadv_tt_local_dump_bucket.return`:

Return
------

Error code, or 0 on success

.. _`batadv_tt_local_dump`:

batadv_tt_local_dump
====================

.. c:function:: int batadv_tt_local_dump(struct sk_buff *msg, struct netlink_callback *cb)

    Dump TT local entries into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        Parameters from query
    :type cb: struct netlink_callback \*

.. _`batadv_tt_local_dump.return`:

Return
------

Error code, or 0 on success

.. _`batadv_tt_local_remove`:

batadv_tt_local_remove
======================

.. c:function:: u16 batadv_tt_local_remove(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid, const char *message, bool roaming)

    logically remove an entry from the local table

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the MAC address of the client to remove
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

    :param message:
        message to append to the log on deletion
    :type message: const char \*

    :param roaming:
        true if the deletion is due to a roaming event
    :type roaming: bool

.. _`batadv_tt_local_remove.return`:

Return
------

the flags assigned to the local entry before being deleted

.. _`batadv_tt_local_purge_list`:

batadv_tt_local_purge_list
==========================

.. c:function:: void batadv_tt_local_purge_list(struct batadv_priv *bat_priv, struct hlist_head *head, int timeout)

    purge inactive tt local entries

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param head:
        pointer to the list containing the local tt entries
    :type head: struct hlist_head \*

    :param timeout:
        parameter deciding whether a given tt local entry is considered
        inactive or not
    :type timeout: int

.. _`batadv_tt_local_purge`:

batadv_tt_local_purge
=====================

.. c:function:: void batadv_tt_local_purge(struct batadv_priv *bat_priv, int timeout)

    purge inactive tt local entries

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param timeout:
        parameter deciding whether a given tt local entry is considered
        inactive or not
    :type timeout: int

.. _`batadv_tt_global_orig_entry_find`:

batadv_tt_global_orig_entry_find
================================

.. c:function:: struct batadv_tt_orig_list_entry *batadv_tt_global_orig_entry_find(const struct batadv_tt_global_entry *entry, const struct batadv_orig_node *orig_node)

    find a TT orig_list_entry

    :param entry:
        the TT global entry where the orig_list_entry has to be
        extracted from
    :type entry: const struct batadv_tt_global_entry \*

    :param orig_node:
        the originator for which the orig_list_entry has to be found
    :type orig_node: const struct batadv_orig_node \*

.. _`batadv_tt_global_orig_entry_find.description`:

Description
-----------

retrieve the orig_tt_list_entry belonging to orig_node from the
batadv_tt_global_entry list

.. _`batadv_tt_global_orig_entry_find.return`:

Return
------

it with an increased refcounter, NULL if not found

.. _`batadv_tt_global_entry_has_orig`:

batadv_tt_global_entry_has_orig
===============================

.. c:function:: bool batadv_tt_global_entry_has_orig(const struct batadv_tt_global_entry *entry, const struct batadv_orig_node *orig_node, u8 *flags)

    check if a TT global entry is also handled by a given originator

    :param entry:
        the TT global entry to check
    :type entry: const struct batadv_tt_global_entry \*

    :param orig_node:
        the originator to search in the list
    :type orig_node: const struct batadv_orig_node \*

    :param flags:
        a pointer to store TT flags for the given \ ``entry``\  received
        from \ ``orig_node``\ 
    :type flags: u8 \*

.. _`batadv_tt_global_entry_has_orig.description`:

Description
-----------

find out if an orig_node is already in the list of a tt_global_entry.

.. _`batadv_tt_global_entry_has_orig.return`:

Return
------

true if found, false otherwise

.. _`batadv_tt_global_sync_flags`:

batadv_tt_global_sync_flags
===========================

.. c:function:: void batadv_tt_global_sync_flags(struct batadv_tt_global_entry *tt_global)

    update TT sync flags

    :param tt_global:
        the TT global entry to update sync flags in
    :type tt_global: struct batadv_tt_global_entry \*

.. _`batadv_tt_global_sync_flags.description`:

Description
-----------

Updates the sync flag bits in the tt_global flag attribute with a logical
OR of all sync flags from any of its TT orig entries.

.. _`batadv_tt_global_orig_entry_add`:

batadv_tt_global_orig_entry_add
===============================

.. c:function:: void batadv_tt_global_orig_entry_add(struct batadv_tt_global_entry *tt_global, struct batadv_orig_node *orig_node, int ttvn, u8 flags)

    add or update a TT orig entry

    :param tt_global:
        the TT global entry to add an orig entry in
    :type tt_global: struct batadv_tt_global_entry \*

    :param orig_node:
        the originator to add an orig entry for
    :type orig_node: struct batadv_orig_node \*

    :param ttvn:
        translation table version number of this changeset
    :type ttvn: int

    :param flags:
        TT sync flags
    :type flags: u8

.. _`batadv_tt_global_add`:

batadv_tt_global_add
====================

.. c:function:: bool batadv_tt_global_add(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, const unsigned char *tt_addr, unsigned short vid, u16 flags, u8 ttvn)

    add a new TT global entry or update an existing one

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        the originator announcing the client
    :type orig_node: struct batadv_orig_node \*

    :param tt_addr:
        the mac address of the non-mesh client
    :type tt_addr: const unsigned char \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

    :param flags:
        TT flags that have to be set for this non-mesh client
    :type flags: u16

    :param ttvn:
        the tt version number ever announcing this non-mesh client
    :type ttvn: u8

.. _`batadv_tt_global_add.description`:

Description
-----------

Add a new TT global entry for the given originator. If the entry already
exists add a new reference to the given originator (a global entry can have
references to multiple originators) and adjust the flags attribute to reflect
the function argument.
If a TT local entry exists for this non-mesh client remove it.

The caller must hold orig_node refcount.

.. _`batadv_tt_global_add.return`:

Return
------

true if the new entry has been added, false otherwise

.. _`batadv_transtable_best_orig`:

batadv_transtable_best_orig
===========================

.. c:function:: struct batadv_tt_orig_list_entry *batadv_transtable_best_orig(struct batadv_priv *bat_priv, struct batadv_tt_global_entry *tt_global_entry)

    Get best originator list entry from tt entry

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_global_entry:
        global translation table entry to be analyzed
    :type tt_global_entry: struct batadv_tt_global_entry \*

.. _`batadv_transtable_best_orig.description`:

Description
-----------

This functon assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_transtable_best_orig.return`:

Return
------

best originator list entry or NULL on errors.

.. _`batadv_tt_global_print_entry`:

batadv_tt_global_print_entry
============================

.. c:function:: void batadv_tt_global_print_entry(struct batadv_priv *bat_priv, struct batadv_tt_global_entry *tt_global_entry, struct seq_file *seq)

    print all orig nodes who announce the address for this global entry

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_global_entry:
        global translation table entry to be printed
    :type tt_global_entry: struct batadv_tt_global_entry \*

    :param seq:
        debugfs table seq_file struct
    :type seq: struct seq_file \*

.. _`batadv_tt_global_print_entry.description`:

Description
-----------

This functon assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_tt_global_seq_print_text`:

batadv_tt_global_seq_print_text
===============================

.. c:function:: int batadv_tt_global_seq_print_text(struct seq_file *seq, void *offset)

    Print the global tt table in a seq file

    :param seq:
        seq file to print on
    :type seq: struct seq_file \*

    :param offset:
        not used
    :type offset: void \*

.. _`batadv_tt_global_seq_print_text.return`:

Return
------

always 0

.. _`batadv_tt_global_dump_subentry`:

batadv_tt_global_dump_subentry
==============================

.. c:function:: int batadv_tt_global_dump_subentry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_tt_common_entry *common, struct batadv_tt_orig_list_entry *orig, bool best)

    Dump all TT local entries into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param common:
        tt local & tt global common data
    :type common: struct batadv_tt_common_entry \*

    :param orig:
        Originator node announcing a non-mesh client
    :type orig: struct batadv_tt_orig_list_entry \*

    :param best:
        Is the best originator for the TT entry
    :type best: bool

.. _`batadv_tt_global_dump_subentry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_tt_global_dump_entry`:

batadv_tt_global_dump_entry
===========================

.. c:function:: int batadv_tt_global_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct batadv_tt_common_entry *common, int *sub_s)

    Dump one TT global entry into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param common:
        tt local & tt global common data
    :type common: struct batadv_tt_common_entry \*

    :param sub_s:
        Number of entries to skip
    :type sub_s: int \*

.. _`batadv_tt_global_dump_entry.description`:

Description
-----------

This function assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`batadv_tt_global_dump_entry.return`:

Return
------

Error code, or 0 on success

.. _`batadv_tt_global_dump_bucket`:

batadv_tt_global_dump_bucket
============================

.. c:function:: int batadv_tt_global_dump_bucket(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_priv *bat_priv, struct hlist_head *head, int *idx_s, int *sub)

    Dump one TT local bucket into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param bat_priv:
        The bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param head:
        Pointer to the list containing the global tt entries
    :type head: struct hlist_head \*

    :param idx_s:
        Number of entries to skip
    :type idx_s: int \*

    :param sub:
        Number of entries to skip
    :type sub: int \*

.. _`batadv_tt_global_dump_bucket.return`:

Return
------

Error code, or 0 on success

.. _`batadv_tt_global_dump`:

batadv_tt_global_dump
=====================

.. c:function:: int batadv_tt_global_dump(struct sk_buff *msg, struct netlink_callback *cb)

    Dump TT global entries into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        Parameters from query
    :type cb: struct netlink_callback \*

.. _`batadv_tt_global_dump.return`:

Return
------

Error code, or length of message on success

.. _`_batadv_tt_global_del_orig_entry`:

\_batadv_tt_global_del_orig_entry
=================================

.. c:function:: void _batadv_tt_global_del_orig_entry(struct batadv_tt_global_entry *tt_global_entry, struct batadv_tt_orig_list_entry *orig_entry)

    remove and free an orig_entry

    :param tt_global_entry:
        the global entry to remove the orig_entry from
    :type tt_global_entry: struct batadv_tt_global_entry \*

    :param orig_entry:
        the orig entry to remove and free
    :type orig_entry: struct batadv_tt_orig_list_entry \*

.. _`_batadv_tt_global_del_orig_entry.description`:

Description
-----------

Remove an orig_entry from its list in the given tt_global_entry and
free this orig_entry afterwards.

Caller must hold tt_global_entry->list_lock and ensure orig_entry->list is
part of a list.

.. _`batadv_tt_global_del_orig_node`:

batadv_tt_global_del_orig_node
==============================

.. c:function:: void batadv_tt_global_del_orig_node(struct batadv_priv *bat_priv, struct batadv_tt_global_entry *tt_global_entry, struct batadv_orig_node *orig_node, const char *message)

    remove orig_node from a global tt entry

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_global_entry:
        the global entry to remove the orig_node from
    :type tt_global_entry: struct batadv_tt_global_entry \*

    :param orig_node:
        the originator announcing the client
    :type orig_node: struct batadv_orig_node \*

    :param message:
        message to append to the log on deletion
    :type message: const char \*

.. _`batadv_tt_global_del_orig_node.description`:

Description
-----------

Remove the given orig_node and its according orig_entry from the given
global tt entry.

.. _`batadv_tt_global_del`:

batadv_tt_global_del
====================

.. c:function:: void batadv_tt_global_del(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, const unsigned char *addr, unsigned short vid, const char *message, bool roaming)

    remove a client from the global table

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        an originator serving this client
    :type orig_node: struct batadv_orig_node \*

    :param addr:
        the mac address of the client
    :type addr: const unsigned char \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

    :param message:
        a message explaining the reason for deleting the client to print
        for debugging purpose
    :type message: const char \*

    :param roaming:
        true if the deletion has been triggered by a roaming event
    :type roaming: bool

.. _`batadv_tt_global_del_orig`:

batadv_tt_global_del_orig
=========================

.. c:function:: void batadv_tt_global_del_orig(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, s32 match_vid, const char *message)

    remove all the TT global entries belonging to the given originator matching the provided vid

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        the originator owning the entries to remove
    :type orig_node: struct batadv_orig_node \*

    :param match_vid:
        the VLAN identifier to match. If negative all the entries will be
        removed
    :type match_vid: s32

    :param message:
        debug message to print as "reason"
    :type message: const char \*

.. _`batadv_transtable_search`:

batadv_transtable_search
========================

.. c:function:: struct batadv_orig_node *batadv_transtable_search(struct batadv_priv *bat_priv, const u8 *src, const u8 *addr, unsigned short vid)

    get the mesh destination for a given client

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param src:
        mac address of the source client
    :type src: const u8 \*

    :param addr:
        mac address of the destination client
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_transtable_search.return`:

Return
------

a pointer to the originator that was selected as destination in the
mesh for contacting the client 'addr', NULL otherwise.
In case of multiple originators serving the same client, the function returns
the best one (best in terms of metric towards the destination node).

If the two clients are AP isolated the function returns NULL.

.. _`batadv_tt_global_crc`:

batadv_tt_global_crc
====================

.. c:function:: u32 batadv_tt_global_crc(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, unsigned short vid)

    calculates the checksum of the local table belonging to the given orig_node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        originator for which the CRC should be computed
    :type orig_node: struct batadv_orig_node \*

    :param vid:
        VLAN identifier for which the CRC32 has to be computed
    :type vid: unsigned short

.. _`batadv_tt_global_crc.description`:

Description
-----------

This function computes the checksum for the global table corresponding to a
specific originator. In particular, the checksum is computed as follows: For
each client connected to the originator the CRC32C of the MAC address and the
VID is computed and then all the CRC32Cs of the various clients are xor'ed
together.

The idea behind is that CRC32C should be used as much as possible in order to
produce a unique hash of the table, but since the order which is used to feed
the CRC32C function affects the result and since every node in the network
probably sorts the clients differently, the hash function cannot be directly
computed over the entire table. Hence the CRC32C is used only on
the single client entry, while all the results are then xor'ed together
because the XOR operation can combine them all while trying to reduce the
noise as much as possible.

.. _`batadv_tt_global_crc.return`:

Return
------

the checksum of the global table of a given originator.

.. _`batadv_tt_local_crc`:

batadv_tt_local_crc
===================

.. c:function:: u32 batadv_tt_local_crc(struct batadv_priv *bat_priv, unsigned short vid)

    calculates the checksum of the local table

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        VLAN identifier for which the CRC32 has to be computed
    :type vid: unsigned short

.. _`batadv_tt_local_crc.description`:

Description
-----------

For details about the computation, please refer to the documentation for
\ :c:func:`batadv_tt_global_crc`\ .

.. _`batadv_tt_local_crc.return`:

Return
------

the checksum of the local table

.. _`batadv_tt_req_node_release`:

batadv_tt_req_node_release
==========================

.. c:function:: void batadv_tt_req_node_release(struct kref *ref)

    free tt_req node entry

    :param ref:
        kref pointer of the tt req_node entry
    :type ref: struct kref \*

.. _`batadv_tt_req_node_put`:

batadv_tt_req_node_put
======================

.. c:function:: void batadv_tt_req_node_put(struct batadv_tt_req_node *tt_req_node)

    decrement the tt_req_node refcounter and possibly release it

    :param tt_req_node:
        tt_req_node to be free'd
    :type tt_req_node: struct batadv_tt_req_node \*

.. _`batadv_tt_req_node_new`:

batadv_tt_req_node_new
======================

.. c:function:: struct batadv_tt_req_node *batadv_tt_req_node_new(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    search and possibly create a tt_req_node object

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        orig node this request is being issued for
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_tt_req_node_new.return`:

Return
------

the pointer to the new tt_req_node struct if no request
has already been issued for this orig_node, NULL otherwise.

.. _`batadv_tt_local_valid`:

batadv_tt_local_valid
=====================

.. c:function:: bool batadv_tt_local_valid(const void *entry_ptr, const void *data_ptr, u8 *flags)

    verify local tt entry and get flags

    :param entry_ptr:
        to be checked local tt entry
    :type entry_ptr: const void \*

    :param data_ptr:
        not used but definition required to satisfy the callback prototype
    :type data_ptr: const void \*

    :param flags:
        a pointer to store TT flags for this client to
    :type flags: u8 \*

.. _`batadv_tt_local_valid.description`:

Description
-----------

Checks the validity of the given local TT entry. If it is, then the provided
flags pointer is updated.

.. _`batadv_tt_local_valid.return`:

Return
------

true if the entry is a valid, false otherwise.

.. _`batadv_tt_global_valid`:

batadv_tt_global_valid
======================

.. c:function:: bool batadv_tt_global_valid(const void *entry_ptr, const void *data_ptr, u8 *flags)

    verify global tt entry and get flags

    :param entry_ptr:
        to be checked global tt entry
    :type entry_ptr: const void \*

    :param data_ptr:
        an orig_node object (may be NULL)
    :type data_ptr: const void \*

    :param flags:
        a pointer to store TT flags for this client to
    :type flags: u8 \*

.. _`batadv_tt_global_valid.description`:

Description
-----------

Checks the validity of the given global TT entry. If it is, then the provided
flags pointer is updated either with the common (summed) TT flags if data_ptr
is NULL or the specific, per originator TT flags otherwise.

.. _`batadv_tt_global_valid.return`:

Return
------

true if the entry is a valid, false otherwise.

.. _`batadv_tt_tvlv_generate`:

batadv_tt_tvlv_generate
=======================

.. c:function:: void batadv_tt_tvlv_generate(struct batadv_priv *bat_priv, struct batadv_hashtable *hash, void *tvlv_buff, u16 tt_len, bool (*valid_cb)(const void *, const void *, u8 *flags), void *cb_data)

    fill the tvlv buff with the tt entries from the specified tt hash

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param hash:
        hash table containing the tt entries
    :type hash: struct batadv_hashtable \*

    :param tvlv_buff:
        pointer to the buffer to fill with the TT data
    :type tvlv_buff: void \*

    :param tt_len:
        expected tvlv tt data buffer length in number of bytes
    :type tt_len: u16

    :param bool (\*valid_cb)(const void \*, const void \*, u8 \*flags):
        function to filter tt change entries and to return TT flags

    :param cb_data:
        data passed to the filter function as argument
    :type cb_data: void \*

.. _`batadv_tt_tvlv_generate.description`:

Description
-----------

Fills the tvlv buff with the tt entries from the specified hash. If valid_cb
is not provided then this becomes a no-op.

.. _`batadv_tt_global_check_crc`:

batadv_tt_global_check_crc
==========================

.. c:function:: bool batadv_tt_global_check_crc(struct batadv_orig_node *orig_node, struct batadv_tvlv_tt_vlan_data *tt_vlan, u16 num_vlan)

    check if all the CRCs are correct

    :param orig_node:
        originator for which the CRCs have to be checked
    :type orig_node: struct batadv_orig_node \*

    :param tt_vlan:
        pointer to the first tvlv VLAN entry
    :type tt_vlan: struct batadv_tvlv_tt_vlan_data \*

    :param num_vlan:
        number of tvlv VLAN entries
    :type num_vlan: u16

.. _`batadv_tt_global_check_crc.return`:

Return
------

true if all the received CRCs match the locally stored ones, false
otherwise

.. _`batadv_tt_local_update_crc`:

batadv_tt_local_update_crc
==========================

.. c:function:: void batadv_tt_local_update_crc(struct batadv_priv *bat_priv)

    update all the local CRCs

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_tt_global_update_crc`:

batadv_tt_global_update_crc
===========================

.. c:function:: void batadv_tt_global_update_crc(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    update all the global CRCs for this orig_node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        the orig_node for which the CRCs have to be updated
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_send_tt_request`:

batadv_send_tt_request
======================

.. c:function:: bool batadv_send_tt_request(struct batadv_priv *bat_priv, struct batadv_orig_node *dst_orig_node, u8 ttvn, struct batadv_tvlv_tt_vlan_data *tt_vlan, u16 num_vlan, bool full_table)

    send a TT Request message to a given node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst_orig_node:
        the destination of the message
    :type dst_orig_node: struct batadv_orig_node \*

    :param ttvn:
        the version number that the source of the message is looking for
    :type ttvn: u8

    :param tt_vlan:
        pointer to the first tvlv VLAN object to request
    :type tt_vlan: struct batadv_tvlv_tt_vlan_data \*

    :param num_vlan:
        number of tvlv VLAN entries
    :type num_vlan: u16

    :param full_table:
        ask for the entire translation table if true, while only for the
        last TT diff otherwise
    :type full_table: bool

.. _`batadv_send_tt_request.return`:

Return
------

true if the TT Request was sent, false otherwise

.. _`batadv_send_other_tt_response`:

batadv_send_other_tt_response
=============================

.. c:function:: bool batadv_send_other_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *req_src, u8 *req_dst)

    send reply to tt request concerning another node's translation table

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_data:
        tt data containing the tt request information
    :type tt_data: struct batadv_tvlv_tt_data \*

    :param req_src:
        mac address of tt request sender
    :type req_src: u8 \*

    :param req_dst:
        mac address of tt request recipient
    :type req_dst: u8 \*

.. _`batadv_send_other_tt_response.return`:

Return
------

true if tt request reply was sent, false otherwise.

.. _`batadv_send_my_tt_response`:

batadv_send_my_tt_response
==========================

.. c:function:: bool batadv_send_my_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *req_src)

    send reply to tt request concerning this node's translation table

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_data:
        tt data containing the tt request information
    :type tt_data: struct batadv_tvlv_tt_data \*

    :param req_src:
        mac address of tt request sender
    :type req_src: u8 \*

.. _`batadv_send_my_tt_response.return`:

Return
------

true if tt request reply was sent, false otherwise.

.. _`batadv_send_tt_response`:

batadv_send_tt_response
=======================

.. c:function:: bool batadv_send_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *req_src, u8 *req_dst)

    send reply to tt request

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_data:
        tt data containing the tt request information
    :type tt_data: struct batadv_tvlv_tt_data \*

    :param req_src:
        mac address of tt request sender
    :type req_src: u8 \*

    :param req_dst:
        mac address of tt request recipient
    :type req_dst: u8 \*

.. _`batadv_send_tt_response.return`:

Return
------

true if tt request reply was sent, false otherwise.

.. _`batadv_is_my_client`:

batadv_is_my_client
===================

.. c:function:: bool batadv_is_my_client(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    check if a client is served by the local node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the client to check
    :type addr: const u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_is_my_client.return`:

Return
------

true if the client is served by this node, false otherwise.

.. _`batadv_handle_tt_response`:

batadv_handle_tt_response
=========================

.. c:function:: void batadv_handle_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *resp_src, u16 num_entries)

    process incoming tt reply

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tt_data:
        tt data containing the tt request information
    :type tt_data: struct batadv_tvlv_tt_data \*

    :param resp_src:
        mac address of tt reply sender
    :type resp_src: u8 \*

    :param num_entries:
        number of tt change entries appended to the tt data
    :type num_entries: u16

.. _`batadv_tt_check_roam_count`:

batadv_tt_check_roam_count
==========================

.. c:function:: bool batadv_tt_check_roam_count(struct batadv_priv *bat_priv, u8 *client)

    check if a client has roamed too frequently

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param client:
        mac address of the roaming client
    :type client: u8 \*

.. _`batadv_tt_check_roam_count.description`:

Description
-----------

This function checks whether the client already reached the
maximum number of possible roaming phases. In this case the ROAMING_ADV
will not be sent.

.. _`batadv_tt_check_roam_count.return`:

Return
------

true if the ROAMING_ADV can be sent, false otherwise

.. _`batadv_send_roam_adv`:

batadv_send_roam_adv
====================

.. c:function:: void batadv_send_roam_adv(struct batadv_priv *bat_priv, u8 *client, unsigned short vid, struct batadv_orig_node *orig_node)

    send a roaming advertisement message

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param client:
        mac address of the roaming client
    :type client: u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

    :param orig_node:
        message destination
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_send_roam_adv.description`:

Description
-----------

Send a ROAMING_ADV message to the node which was previously serving this
client. This is done to inform the node that from now on all traffic destined
for this particular roamed client has to be forwarded to the sender of the
roaming message.

.. _`batadv_tt_free`:

batadv_tt_free
==============

.. c:function:: void batadv_tt_free(struct batadv_priv *bat_priv)

    Free translation table of soft interface

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_tt_local_set_flags`:

batadv_tt_local_set_flags
=========================

.. c:function:: void batadv_tt_local_set_flags(struct batadv_priv *bat_priv, u16 flags, bool enable, bool count)

    set or unset the specified flags on the local table and possibly count them in the TT size

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param flags:
        the flag to switch
    :type flags: u16

    :param enable:
        whether to set or unset the flag
    :type enable: bool

    :param count:
        whether to increase the TT size by the number of changed entries
    :type count: bool

.. _`batadv_tt_local_commit_changes_nolock`:

batadv_tt_local_commit_changes_nolock
=====================================

.. c:function:: void batadv_tt_local_commit_changes_nolock(struct batadv_priv *bat_priv)

    commit all pending local tt changes which have been queued in the time since the last commit

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_tt_local_commit_changes_nolock.description`:

Description
-----------

Caller must hold tt->commit_lock.

.. _`batadv_tt_local_commit_changes`:

batadv_tt_local_commit_changes
==============================

.. c:function:: void batadv_tt_local_commit_changes(struct batadv_priv *bat_priv)

    commit all pending local tt changes which have been queued in the time since the last commit

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_is_ap_isolated`:

batadv_is_ap_isolated
=====================

.. c:function:: bool batadv_is_ap_isolated(struct batadv_priv *bat_priv, u8 *src, u8 *dst, unsigned short vid)

    Check if packet from upper layer should be dropped

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param src:
        source mac address of packet
    :type src: u8 \*

    :param dst:
        destination mac address of packet
    :type dst: u8 \*

    :param vid:
        vlan id of packet
    :type vid: unsigned short

.. _`batadv_is_ap_isolated.return`:

Return
------

true when src+dst(+vid) pair should be isolated, false otherwise

.. _`batadv_tt_update_orig`:

batadv_tt_update_orig
=====================

.. c:function:: void batadv_tt_update_orig(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, const void *tt_buff, u16 tt_num_vlan, struct batadv_tvlv_tt_change *tt_change, u16 tt_num_changes, u8 ttvn)

    update global translation table with new tt information received via ogms

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        the orig_node of the ogm
    :type orig_node: struct batadv_orig_node \*

    :param tt_buff:
        pointer to the first tvlv VLAN entry
    :type tt_buff: const void \*

    :param tt_num_vlan:
        number of tvlv VLAN entries
    :type tt_num_vlan: u16

    :param tt_change:
        pointer to the first entry in the TT buffer
    :type tt_change: struct batadv_tvlv_tt_change \*

    :param tt_num_changes:
        number of tt changes inside the tt buffer
    :type tt_num_changes: u16

    :param ttvn:
        translation table version number of this changeset
    :type ttvn: u8

.. _`batadv_tt_global_client_is_roaming`:

batadv_tt_global_client_is_roaming
==================================

.. c:function:: bool batadv_tt_global_client_is_roaming(struct batadv_priv *bat_priv, u8 *addr, unsigned short vid)

    check if a client is marked as roaming

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the client to check
    :type addr: u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_global_client_is_roaming.return`:

Return
------

true if we know that the client has moved from its old originator
to another one. This entry is still kept for consistency purposes and will be
deleted later by a DEL or because of timeout

.. _`batadv_tt_local_client_is_roaming`:

batadv_tt_local_client_is_roaming
=================================

.. c:function:: bool batadv_tt_local_client_is_roaming(struct batadv_priv *bat_priv, u8 *addr, unsigned short vid)

    tells whether the client is roaming

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the local client to query
    :type addr: u8 \*

    :param vid:
        VLAN identifier
    :type vid: unsigned short

.. _`batadv_tt_local_client_is_roaming.return`:

Return
------

true if the local client is known to be roaming (it is not served by
this node anymore) or not. If yes, the client is still present in the table
to keep the latter consistent with the node TTVN

.. _`batadv_tt_add_temporary_global_entry`:

batadv_tt_add_temporary_global_entry
====================================

.. c:function:: bool batadv_tt_add_temporary_global_entry(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, const unsigned char *addr, unsigned short vid)

    Add temporary entry to global TT

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig_node:
        orig node which the temporary entry should be associated with
    :type orig_node: struct batadv_orig_node \*

    :param addr:
        mac address of the client
    :type addr: const unsigned char \*

    :param vid:
        VLAN id of the new temporary global translation table
    :type vid: unsigned short

.. _`batadv_tt_add_temporary_global_entry.return`:

Return
------

true when temporary tt entry could be added, false otherwise

.. _`batadv_tt_local_resize_to_mtu`:

batadv_tt_local_resize_to_mtu
=============================

.. c:function:: void batadv_tt_local_resize_to_mtu(struct net_device *soft_iface)

    resize the local translation table fit the maximum packet size that can be transported through the mesh

    :param soft_iface:
        netdev struct of the mesh interface
    :type soft_iface: struct net_device \*

.. _`batadv_tt_local_resize_to_mtu.description`:

Description
-----------

Remove entries older than 'timeout' and half timeout if more entries need
to be removed.

.. _`batadv_tt_tvlv_ogm_handler_v1`:

batadv_tt_tvlv_ogm_handler_v1
=============================

.. c:function:: void batadv_tt_tvlv_ogm_handler_v1(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

    process incoming tt tvlv container

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param orig:
        the orig_node of the ogm
    :type orig: struct batadv_orig_node \*

    :param flags:
        flags indicating the tvlv state (see batadv_tvlv_handler_flags)
    :type flags: u8

    :param tvlv_value:
        tvlv buffer containing the gateway data
    :type tvlv_value: void \*

    :param tvlv_value_len:
        tvlv buffer length
    :type tvlv_value_len: u16

.. _`batadv_tt_tvlv_unicast_handler_v1`:

batadv_tt_tvlv_unicast_handler_v1
=================================

.. c:function:: int batadv_tt_tvlv_unicast_handler_v1(struct batadv_priv *bat_priv, u8 *src, u8 *dst, void *tvlv_value, u16 tvlv_value_len)

    process incoming (unicast) tt tvlv container

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param src:
        mac address of tt tvlv sender
    :type src: u8 \*

    :param dst:
        mac address of tt tvlv recipient
    :type dst: u8 \*

    :param tvlv_value:
        tvlv buffer containing the tt data
    :type tvlv_value: void \*

    :param tvlv_value_len:
        tvlv buffer length
    :type tvlv_value_len: u16

.. _`batadv_tt_tvlv_unicast_handler_v1.return`:

Return
------

NET_RX_DROP if the tt tvlv is to be re-routed, NET_RX_SUCCESS
otherwise.

.. _`batadv_roam_tvlv_unicast_handler_v1`:

batadv_roam_tvlv_unicast_handler_v1
===================================

.. c:function:: int batadv_roam_tvlv_unicast_handler_v1(struct batadv_priv *bat_priv, u8 *src, u8 *dst, void *tvlv_value, u16 tvlv_value_len)

    process incoming tt roam tvlv container

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param src:
        mac address of tt tvlv sender
    :type src: u8 \*

    :param dst:
        mac address of tt tvlv recipient
    :type dst: u8 \*

    :param tvlv_value:
        tvlv buffer containing the tt data
    :type tvlv_value: void \*

    :param tvlv_value_len:
        tvlv buffer length
    :type tvlv_value_len: u16

.. _`batadv_roam_tvlv_unicast_handler_v1.return`:

Return
------

NET_RX_DROP if the tt roam tvlv is to be re-routed, NET_RX_SUCCESS
otherwise.

.. _`batadv_tt_init`:

batadv_tt_init
==============

.. c:function:: int batadv_tt_init(struct batadv_priv *bat_priv)

    initialise the translation table internals

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_tt_init.return`:

Return
------

0 on success or negative error number in case of failure.

.. _`batadv_tt_global_is_isolated`:

batadv_tt_global_is_isolated
============================

.. c:function:: bool batadv_tt_global_is_isolated(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    check if a client is marked as isolated

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the mac address of the client
    :type addr: const u8 \*

    :param vid:
        the identifier of the VLAN where this client is connected
    :type vid: unsigned short

.. _`batadv_tt_global_is_isolated.return`:

Return
------

true if the client is marked with the TT_CLIENT_ISOLA flag, false
otherwise

.. _`batadv_tt_cache_init`:

batadv_tt_cache_init
====================

.. c:function:: int batadv_tt_cache_init( void)

    Initialize tt memory object cache

    :param void:
        no arguments
    :type void: 

.. _`batadv_tt_cache_init.return`:

Return
------

0 on success or negative error number in case of failure.

.. _`batadv_tt_cache_destroy`:

batadv_tt_cache_destroy
=======================

.. c:function:: void batadv_tt_cache_destroy( void)

    Destroy tt memory object cache

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

