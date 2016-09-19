.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/translation-table.c

.. _`batadv_compare_tt`:

batadv_compare_tt
=================

.. c:function:: bool batadv_compare_tt(const struct hlist_node *node, const void *data2)

    check if two TT entries are the same

    :param const struct hlist_node \*node:
        the list element pointer of the first TT entry

    :param const void \*data2:
        pointer to the tt_common_entry of the second TT entry

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

    :param const void \*data:
        pointer to the tt_common_entry object to map

    :param u32 size:
        the size of the hash table

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

    :param struct batadv_hashtable \*hash:
        the hash table to search

    :param const u8 \*addr:
        the mac address of the client to look for

    :param unsigned short vid:
        VLAN identifier

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the mac address of the client to look for

    :param unsigned short vid:
        VLAN identifier

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the mac address of the client to look for

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_tt_global_hash_find.return`:

Return
------

a pointer to the corresponding tt_global_entry struct if the client
is found, NULL otherwise.

.. _`batadv_tt_local_entry_release`:

batadv_tt_local_entry_release
=============================

.. c:function:: void batadv_tt_local_entry_release(struct kref *ref)

    release tt_local_entry from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the nc_node

.. _`batadv_tt_local_entry_put`:

batadv_tt_local_entry_put
=========================

.. c:function:: void batadv_tt_local_entry_put(struct batadv_tt_local_entry *tt_local_entry)

    decrement the tt_local_entry refcounter and possibly release it

    :param struct batadv_tt_local_entry \*tt_local_entry:
        tt_local_entry to be free'd

.. _`batadv_tt_global_entry_release`:

batadv_tt_global_entry_release
==============================

.. c:function:: void batadv_tt_global_entry_release(struct kref *ref)

    release tt_global_entry from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the nc_node

.. _`batadv_tt_global_entry_put`:

batadv_tt_global_entry_put
==========================

.. c:function:: void batadv_tt_global_entry_put(struct batadv_tt_global_entry *tt_global_entry)

    decrement the tt_global_entry refcounter and possibly release it

    :param struct batadv_tt_global_entry \*tt_global_entry:
        tt_global_entry to be free'd

.. _`batadv_tt_global_hash_count`:

batadv_tt_global_hash_count
===========================

.. c:function:: int batadv_tt_global_hash_count(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    count the number of orig entries

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the mac address of the client to count entries for

    :param unsigned short vid:
        VLAN identifier

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned short vid:
        the VLAN identifier of the sub-table to change

    :param int v:
        the amount to sum to the local table size

.. _`batadv_tt_local_size_inc`:

batadv_tt_local_size_inc
========================

.. c:function:: void batadv_tt_local_size_inc(struct batadv_priv *bat_priv, unsigned short vid)

    increase by one the local table size for the given vid

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned short vid:
        the VLAN identifier

.. _`batadv_tt_local_size_dec`:

batadv_tt_local_size_dec
========================

.. c:function:: void batadv_tt_local_size_dec(struct batadv_priv *bat_priv, unsigned short vid)

    decrease by one the local table size for the given vid

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned short vid:
        the VLAN identifier

.. _`batadv_tt_global_size_mod`:

batadv_tt_global_size_mod
=========================

.. c:function:: void batadv_tt_global_size_mod(struct batadv_orig_node *orig_node, unsigned short vid, int v)

    change the size by v of the global table for orig_node identified by vid

    :param struct batadv_orig_node \*orig_node:
        the originator for which the table has to be modified

    :param unsigned short vid:
        the VLAN identifier

    :param int v:
        the amount to sum to the global table size

.. _`batadv_tt_global_size_inc`:

batadv_tt_global_size_inc
=========================

.. c:function:: void batadv_tt_global_size_inc(struct batadv_orig_node *orig_node, unsigned short vid)

    increase by one the global table size for the given vid

    :param struct batadv_orig_node \*orig_node:
        the originator which global table size has to be decreased

    :param unsigned short vid:
        the vlan identifier

.. _`batadv_tt_global_size_dec`:

batadv_tt_global_size_dec
=========================

.. c:function:: void batadv_tt_global_size_dec(struct batadv_orig_node *orig_node, unsigned short vid)

    decrease by one the global table size for the given vid

    :param struct batadv_orig_node \*orig_node:
        the originator which global table size has to be decreased

    :param unsigned short vid:
        the vlan identifier

.. _`batadv_tt_orig_list_entry_release`:

batadv_tt_orig_list_entry_release
=================================

.. c:function:: void batadv_tt_orig_list_entry_release(struct kref *ref)

    release tt orig entry from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the tt orig entry

.. _`batadv_tt_orig_list_entry_put`:

batadv_tt_orig_list_entry_put
=============================

.. c:function:: void batadv_tt_orig_list_entry_put(struct batadv_tt_orig_list_entry *orig_entry)

    decrement the tt orig entry refcounter and possibly release it

    :param struct batadv_tt_orig_list_entry \*orig_entry:
        tt orig entry to be free'd

.. _`batadv_tt_local_event`:

batadv_tt_local_event
=====================

.. c:function:: void batadv_tt_local_event(struct batadv_priv *bat_priv, struct batadv_tt_local_entry *tt_local_entry, u8 event_flags)

    store a local TT event (ADD/DEL)

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tt_local_entry \*tt_local_entry:
        the TT entry involved in the event

    :param u8 event_flags:
        flags to store in the event structure

.. _`batadv_tt_len`:

batadv_tt_len
=============

.. c:function:: int batadv_tt_len(int changes_num)

    compute length in bytes of given number of tt changes

    :param int changes_num:
        number of tt changes

.. _`batadv_tt_len.return`:

Return
------

computed length in bytes.

.. _`batadv_tt_entries`:

batadv_tt_entries
=================

.. c:function:: u16 batadv_tt_entries(u16 tt_len)

    compute the number of entries fitting in tt_len bytes

    :param u16 tt_len:
        available space

.. _`batadv_tt_entries.return`:

Return
------

the number of entries.

.. _`batadv_tt_local_table_transmit_size`:

batadv_tt_local_table_transmit_size
===================================

.. c:function:: int batadv_tt_local_table_transmit_size(struct batadv_priv *bat_priv)

    calculates the local translation table size when transmitted over the air

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tt_local_table_transmit_size.return`:

Return
------

local translation table size in bytes.

.. _`batadv_tt_local_add`:

batadv_tt_local_add
===================

.. c:function:: bool batadv_tt_local_add(struct net_device *soft_iface, const u8 *addr, unsigned short vid, int ifindex, u32 mark)

    add a new client to the local table or update an existing client

    :param struct net_device \*soft_iface:
        netdev struct of the mesh interface

    :param const u8 \*addr:
        the mac address of the client to add

    :param unsigned short vid:
        VLAN identifier

    :param int ifindex:
        index of the interface where the client is connected to (useful to
        identify wireless clients)

    :param u32 mark:
        the value contained in the skb->mark field of the received packet (if
        any)

.. _`batadv_tt_local_add.return`:

Return
------

true if the client was successfully added, false otherwise.

.. _`batadv_tt_prepare_tvlv_global_data`:

batadv_tt_prepare_tvlv_global_data
==================================

.. c:function:: u16 batadv_tt_prepare_tvlv_global_data(struct batadv_orig_node *orig_node, struct batadv_tvlv_tt_data **tt_data, struct batadv_tvlv_tt_change **tt_change, s32 *tt_len)

    prepare the TVLV TT header to send within a TT Response directed to another node

    :param struct batadv_orig_node \*orig_node:
        originator for which the TT data has to be prepared

    :param struct batadv_tvlv_tt_data \*\*tt_data:
        uninitialised pointer to the address of the TVLV buffer

    :param struct batadv_tvlv_tt_change \*\*tt_change:
        uninitialised pointer to the address of the area where the TT
        changed can be stored

    :param s32 \*tt_len:
        pointer to the length to reserve to the tt_change. if -1 this
        function reserves the amount of space needed to send the entire global TT
        table. In case of success the value is updated with the real amount of
        reserved bytes
        Allocate the needed amount of memory for the entire TT TVLV and write its
        header made up by one tvlv_tt_data object and a series of tvlv_tt_vlan_data
        objects, one per active VLAN served by the originator node.

.. _`batadv_tt_prepare_tvlv_global_data.return`:

Return
------

the size of the allocated buffer or 0 in case of failure.

.. _`batadv_tt_prepare_tvlv_local_data`:

batadv_tt_prepare_tvlv_local_data
=================================

.. c:function:: u16 batadv_tt_prepare_tvlv_local_data(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data **tt_data, struct batadv_tvlv_tt_change **tt_change, s32 *tt_len)

    allocate and prepare the TT TVLV for this node

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_tt_data \*\*tt_data:
        uninitialised pointer to the address of the TVLV buffer

    :param struct batadv_tvlv_tt_change \*\*tt_change:
        uninitialised pointer to the address of the area where the TT
        changes can be stored

    :param s32 \*tt_len:
        pointer to the length to reserve to the tt_change. if -1 this
        function reserves the amount of space needed to send the entire local TT
        table. In case of success the value is updated with the real amount of
        reserved bytes

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tt_local_remove`:

batadv_tt_local_remove
======================

.. c:function:: u16 batadv_tt_local_remove(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid, const char *message, bool roaming)

    logically remove an entry from the local table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the MAC address of the client to remove

    :param unsigned short vid:
        VLAN identifier

    :param const char \*message:
        message to append to the log on deletion

    :param bool roaming:
        true if the deletion is due to a roaming event

.. _`batadv_tt_local_remove.return`:

Return
------

the flags assigned to the local entry before being deleted

.. _`batadv_tt_local_purge_list`:

batadv_tt_local_purge_list
==========================

.. c:function:: void batadv_tt_local_purge_list(struct batadv_priv *bat_priv, struct hlist_head *head, int timeout)

    purge inactive tt local entries

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct hlist_head \*head:
        pointer to the list containing the local tt entries

    :param int timeout:
        parameter deciding whether a given tt local entry is considered
        inactive or not

.. _`batadv_tt_local_purge`:

batadv_tt_local_purge
=====================

.. c:function:: void batadv_tt_local_purge(struct batadv_priv *bat_priv, int timeout)

    purge inactive tt local entries

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param int timeout:
        parameter deciding whether a given tt local entry is considered
        inactive or not

.. _`batadv_tt_global_orig_entry_find`:

batadv_tt_global_orig_entry_find
================================

.. c:function:: struct batadv_tt_orig_list_entry *batadv_tt_global_orig_entry_find(const struct batadv_tt_global_entry *entry, const struct batadv_orig_node *orig_node)

    find a TT orig_list_entry

    :param const struct batadv_tt_global_entry \*entry:
        the TT global entry where the orig_list_entry has to be
        extracted from

    :param const struct batadv_orig_node \*orig_node:
        the originator for which the orig_list_entry has to be found

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

.. c:function:: bool batadv_tt_global_entry_has_orig(const struct batadv_tt_global_entry *entry, const struct batadv_orig_node *orig_node)

    check if a TT global entry is also handled by a given originator

    :param const struct batadv_tt_global_entry \*entry:
        the TT global entry to check

    :param const struct batadv_orig_node \*orig_node:
        the originator to search in the list

.. _`batadv_tt_global_entry_has_orig.description`:

Description
-----------

find out if an orig_node is already in the list of a tt_global_entry.

.. _`batadv_tt_global_entry_has_orig.return`:

Return
------

true if found, false otherwise

.. _`batadv_tt_global_add`:

batadv_tt_global_add
====================

.. c:function:: bool batadv_tt_global_add(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, const unsigned char *tt_addr, unsigned short vid, u16 flags, u8 ttvn)

    add a new TT global entry or update an existing one

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        the originator announcing the client

    :param const unsigned char \*tt_addr:
        the mac address of the non-mesh client

    :param unsigned short vid:
        VLAN identifier

    :param u16 flags:
        TT flags that have to be set for this non-mesh client

    :param u8 ttvn:
        the tt version number ever announcing this non-mesh client

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tt_global_entry \*tt_global_entry:
        global translation table entry to be analyzed

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tt_global_entry \*tt_global_entry:
        global translation table entry to be printed

    :param struct seq_file \*seq:
        debugfs table seq_file struct

.. _`batadv_tt_global_print_entry.description`:

Description
-----------

This functon assumes the caller holds \ :c:func:`rcu_read_lock`\ .

.. _`_batadv_tt_global_del_orig_entry`:

_batadv_tt_global_del_orig_entry
================================

.. c:function:: void _batadv_tt_global_del_orig_entry(struct batadv_tt_global_entry *tt_global_entry, struct batadv_tt_orig_list_entry *orig_entry)

    remove and free an orig_entry

    :param struct batadv_tt_global_entry \*tt_global_entry:
        the global entry to remove the orig_entry from

    :param struct batadv_tt_orig_list_entry \*orig_entry:
        the orig entry to remove and free

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tt_global_entry \*tt_global_entry:
        the global entry to remove the orig_node from

    :param struct batadv_orig_node \*orig_node:
        the originator announcing the client

    :param const char \*message:
        message to append to the log on deletion

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        an originator serving this client

    :param const unsigned char \*addr:
        the mac address of the client

    :param unsigned short vid:
        VLAN identifier

    :param const char \*message:
        a message explaining the reason for deleting the client to print
        for debugging purpose

    :param bool roaming:
        true if the deletion has been triggered by a roaming event

.. _`batadv_tt_global_del_orig`:

batadv_tt_global_del_orig
=========================

.. c:function:: void batadv_tt_global_del_orig(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, s32 match_vid, const char *message)

    remove all the TT global entries belonging to the given originator matching the provided vid

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        the originator owning the entries to remove

    :param s32 match_vid:
        the VLAN identifier to match. If negative all the entries will be
        removed

    :param const char \*message:
        debug message to print as "reason"

.. _`batadv_transtable_search`:

batadv_transtable_search
========================

.. c:function:: struct batadv_orig_node *batadv_transtable_search(struct batadv_priv *bat_priv, const u8 *src, const u8 *addr, unsigned short vid)

    get the mesh destination for a given client

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*src:
        mac address of the source client

    :param const u8 \*addr:
        mac address of the destination client

    :param unsigned short vid:
        VLAN identifier

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        originator for which the CRC should be computed

    :param unsigned short vid:
        VLAN identifier for which the CRC32 has to be computed

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned short vid:
        VLAN identifier for which the CRC32 has to be computed

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

    :param struct kref \*ref:
        kref pointer of the tt req_node entry

.. _`batadv_tt_req_node_put`:

batadv_tt_req_node_put
======================

.. c:function:: void batadv_tt_req_node_put(struct batadv_tt_req_node *tt_req_node)

    decrement the tt_req_node refcounter and possibly release it

    :param struct batadv_tt_req_node \*tt_req_node:
        tt_req_node to be free'd

.. _`batadv_tt_req_node_new`:

batadv_tt_req_node_new
======================

.. c:function:: struct batadv_tt_req_node *batadv_tt_req_node_new(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    search and possibly create a tt_req_node object

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node this request is being issued for

.. _`batadv_tt_req_node_new.return`:

Return
------

the pointer to the new tt_req_node struct if no request
has already been issued for this orig_node, NULL otherwise.

.. _`batadv_tt_local_valid`:

batadv_tt_local_valid
=====================

.. c:function:: bool batadv_tt_local_valid(const void *entry_ptr, const void *data_ptr)

    verify that given tt entry is a valid one

    :param const void \*entry_ptr:
        to be checked local tt entry

    :param const void \*data_ptr:
        not used but definition required to satisfy the callback prototype

.. _`batadv_tt_local_valid.return`:

Return
------

true if the entry is a valid, false otherwise.

.. _`batadv_tt_tvlv_generate`:

batadv_tt_tvlv_generate
=======================

.. c:function:: void batadv_tt_tvlv_generate(struct batadv_priv *bat_priv, struct batadv_hashtable *hash, void *tvlv_buff, u16 tt_len, bool (*valid_cb)(const void *, const void *), void *cb_data)

    fill the tvlv buff with the tt entries from the specified tt hash

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hashtable \*hash:
        hash table containing the tt entries

    :param void \*tvlv_buff:
        pointer to the buffer to fill with the TT data

    :param u16 tt_len:
        expected tvlv tt data buffer length in number of bytes

    :param bool (\*valid_cb)(const void \*, const void \*):
        function to filter tt change entries

    :param void \*cb_data:
        data passed to the filter function as argument

.. _`batadv_tt_global_check_crc`:

batadv_tt_global_check_crc
==========================

.. c:function:: bool batadv_tt_global_check_crc(struct batadv_orig_node *orig_node, struct batadv_tvlv_tt_vlan_data *tt_vlan, u16 num_vlan)

    check if all the CRCs are correct

    :param struct batadv_orig_node \*orig_node:
        originator for which the CRCs have to be checked

    :param struct batadv_tvlv_tt_vlan_data \*tt_vlan:
        pointer to the first tvlv VLAN entry

    :param u16 num_vlan:
        number of tvlv VLAN entries

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tt_global_update_crc`:

batadv_tt_global_update_crc
===========================

.. c:function:: void batadv_tt_global_update_crc(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    update all the global CRCs for this orig_node

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        the orig_node for which the CRCs have to be updated

.. _`batadv_send_tt_request`:

batadv_send_tt_request
======================

.. c:function:: bool batadv_send_tt_request(struct batadv_priv *bat_priv, struct batadv_orig_node *dst_orig_node, u8 ttvn, struct batadv_tvlv_tt_vlan_data *tt_vlan, u16 num_vlan, bool full_table)

    send a TT Request message to a given node

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*dst_orig_node:
        the destination of the message

    :param u8 ttvn:
        the version number that the source of the message is looking for

    :param struct batadv_tvlv_tt_vlan_data \*tt_vlan:
        pointer to the first tvlv VLAN object to request

    :param u16 num_vlan:
        number of tvlv VLAN entries

    :param bool full_table:
        ask for the entire translation table if true, while only for the
        last TT diff otherwise

.. _`batadv_send_tt_request.return`:

Return
------

true if the TT Request was sent, false otherwise

.. _`batadv_send_other_tt_response`:

batadv_send_other_tt_response
=============================

.. c:function:: bool batadv_send_other_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *req_src, u8 *req_dst)

    send reply to tt request concerning another node's translation table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_tt_data \*tt_data:
        tt data containing the tt request information

    :param u8 \*req_src:
        mac address of tt request sender

    :param u8 \*req_dst:
        mac address of tt request recipient

.. _`batadv_send_other_tt_response.return`:

Return
------

true if tt request reply was sent, false otherwise.

.. _`batadv_send_my_tt_response`:

batadv_send_my_tt_response
==========================

.. c:function:: bool batadv_send_my_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *req_src)

    send reply to tt request concerning this node's translation table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_tt_data \*tt_data:
        tt data containing the tt request information

    :param u8 \*req_src:
        mac address of tt request sender

.. _`batadv_send_my_tt_response.return`:

Return
------

true if tt request reply was sent, false otherwise.

.. _`batadv_send_tt_response`:

batadv_send_tt_response
=======================

.. c:function:: bool batadv_send_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *req_src, u8 *req_dst)

    send reply to tt request

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_tt_data \*tt_data:
        tt data containing the tt request information

    :param u8 \*req_src:
        mac address of tt request sender

    :param u8 \*req_dst:
        mac address of tt request recipient

.. _`batadv_send_tt_response.return`:

Return
------

true if tt request reply was sent, false otherwise.

.. _`batadv_is_my_client`:

batadv_is_my_client
===================

.. c:function:: bool batadv_is_my_client(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    check if a client is served by the local node

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the mac address of the client to check

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_is_my_client.return`:

Return
------

true if the client is served by this node, false otherwise.

.. _`batadv_handle_tt_response`:

batadv_handle_tt_response
=========================

.. c:function:: void batadv_handle_tt_response(struct batadv_priv *bat_priv, struct batadv_tvlv_tt_data *tt_data, u8 *resp_src, u16 num_entries)

    process incoming tt reply

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_tvlv_tt_data \*tt_data:
        tt data containing the tt request information

    :param u8 \*resp_src:
        mac address of tt reply sender

    :param u16 num_entries:
        number of tt change entries appended to the tt data

.. _`batadv_tt_check_roam_count`:

batadv_tt_check_roam_count
==========================

.. c:function:: bool batadv_tt_check_roam_count(struct batadv_priv *bat_priv, u8 *client)

    check if a client has roamed too frequently

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*client:
        mac address of the roaming client

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*client:
        mac address of the roaming client

    :param unsigned short vid:
        VLAN identifier

    :param struct batadv_orig_node \*orig_node:
        message destination

.. _`batadv_send_roam_adv.description`:

Description
-----------

Send a ROAMING_ADV message to the node which was previously serving this
client. This is done to inform the node that from now on all traffic destined
for this particular roamed client has to be forwarded to the sender of the
roaming message.

.. _`batadv_tt_local_set_flags`:

batadv_tt_local_set_flags
=========================

.. c:function:: void batadv_tt_local_set_flags(struct batadv_priv *bat_priv, u16 flags, bool enable, bool count)

    set or unset the specified flags on the local table and possibly count them in the TT size

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u16 flags:
        the flag to switch

    :param bool enable:
        whether to set or unset the flag

    :param bool count:
        whether to increase the TT size by the number of changed entries

.. _`batadv_tt_local_commit_changes_nolock`:

batadv_tt_local_commit_changes_nolock
=====================================

.. c:function:: void batadv_tt_local_commit_changes_nolock(struct batadv_priv *bat_priv)

    commit all pending local tt changes which have been queued in the time since the last commit

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tt_local_commit_changes_nolock.description`:

Description
-----------

Caller must hold tt->commit_lock.

.. _`batadv_tt_local_commit_changes`:

batadv_tt_local_commit_changes
==============================

.. c:function:: void batadv_tt_local_commit_changes(struct batadv_priv *bat_priv)

    commit all pending local tt changes which have been queued in the time since the last commit

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tt_update_orig`:

batadv_tt_update_orig
=====================

.. c:function:: void batadv_tt_update_orig(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, const void *tt_buff, u16 tt_num_vlan, struct batadv_tvlv_tt_change *tt_change, u16 tt_num_changes, u8 ttvn)

    update global translation table with new tt information received via ogms

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        the orig_node of the ogm

    :param const void \*tt_buff:
        pointer to the first tvlv VLAN entry

    :param u16 tt_num_vlan:
        number of tvlv VLAN entries

    :param struct batadv_tvlv_tt_change \*tt_change:
        pointer to the first entry in the TT buffer

    :param u16 tt_num_changes:
        number of tt changes inside the tt buffer

    :param u8 ttvn:
        translation table version number of this changeset

.. _`batadv_tt_global_client_is_roaming`:

batadv_tt_global_client_is_roaming
==================================

.. c:function:: bool batadv_tt_global_client_is_roaming(struct batadv_priv *bat_priv, u8 *addr, unsigned short vid)

    check if a client is marked as roaming

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*addr:
        the mac address of the client to check

    :param unsigned short vid:
        VLAN identifier

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*addr:
        the mac address of the local client to query

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_tt_local_client_is_roaming.return`:

Return
------

true if the local client is known to be roaming (it is not served by
this node anymore) or not. If yes, the client is still present in the table
to keep the latter consistent with the node TTVN

.. _`batadv_tt_local_resize_to_mtu`:

batadv_tt_local_resize_to_mtu
=============================

.. c:function:: void batadv_tt_local_resize_to_mtu(struct net_device *soft_iface)

    resize the local translation table fit the maximum packet size that can be transported through the mesh

    :param struct net_device \*soft_iface:
        netdev struct of the mesh interface

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig:
        the orig_node of the ogm

    :param u8 flags:
        flags indicating the tvlv state (see batadv_tvlv_handler_flags)

    :param void \*tvlv_value:
        tvlv buffer containing the gateway data

    :param u16 tvlv_value_len:
        tvlv buffer length

.. _`batadv_tt_tvlv_unicast_handler_v1`:

batadv_tt_tvlv_unicast_handler_v1
=================================

.. c:function:: int batadv_tt_tvlv_unicast_handler_v1(struct batadv_priv *bat_priv, u8 *src, u8 *dst, void *tvlv_value, u16 tvlv_value_len)

    process incoming (unicast) tt tvlv container

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*src:
        mac address of tt tvlv sender

    :param u8 \*dst:
        mac address of tt tvlv recipient

    :param void \*tvlv_value:
        tvlv buffer containing the tt data

    :param u16 tvlv_value_len:
        tvlv buffer length

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*src:
        mac address of tt tvlv sender

    :param u8 \*dst:
        mac address of tt tvlv recipient

    :param void \*tvlv_value:
        tvlv buffer containing the tt data

    :param u16 tvlv_value_len:
        tvlv buffer length

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_tt_init.return`:

Return
------

0 on success or negative error number in case of failure.

.. _`batadv_tt_global_is_isolated`:

batadv_tt_global_is_isolated
============================

.. c:function:: bool batadv_tt_global_is_isolated(struct batadv_priv *bat_priv, const u8 *addr, unsigned short vid)

    check if a client is marked as isolated

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the mac address of the client

    :param unsigned short vid:
        the identifier of the VLAN where this client is connected

.. _`batadv_tt_global_is_isolated.return`:

Return
------

true if the client is marked with the TT_CLIENT_ISOLA flag, false
otherwise

.. This file was automatic generated / don't edit.

