.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/network-coding.c

.. _`batadv_nc_init`:

batadv_nc_init
==============

.. c:function:: int batadv_nc_init( void)

    one-time initialization for network coding

    :param  void:
        no arguments

.. _`batadv_nc_init.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_nc_start_timer`:

batadv_nc_start_timer
=====================

.. c:function:: void batadv_nc_start_timer(struct batadv_priv *bat_priv)

    initialise the nc periodic worker

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_tvlv_container_update`:

batadv_nc_tvlv_container_update
===============================

.. c:function:: void batadv_nc_tvlv_container_update(struct batadv_priv *bat_priv)

    update the network coding tvlv container after network coding setting change

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_status_update`:

batadv_nc_status_update
=======================

.. c:function:: void batadv_nc_status_update(struct net_device *net_dev)

    update the network coding tvlv container after network coding setting change

    :param struct net_device \*net_dev:
        the soft interface net device

.. _`batadv_nc_tvlv_ogm_handler_v1`:

batadv_nc_tvlv_ogm_handler_v1
=============================

.. c:function:: void batadv_nc_tvlv_ogm_handler_v1(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

    process incoming nc tvlv container

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

.. _`batadv_nc_mesh_init`:

batadv_nc_mesh_init
===================

.. c:function:: int batadv_nc_mesh_init(struct batadv_priv *bat_priv)

    initialise coding hash table and start house keeping

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_mesh_init.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_nc_init_bat_priv`:

batadv_nc_init_bat_priv
=======================

.. c:function:: void batadv_nc_init_bat_priv(struct batadv_priv *bat_priv)

    initialise the nc specific bat_priv variables

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_init_orig`:

batadv_nc_init_orig
===================

.. c:function:: void batadv_nc_init_orig(struct batadv_orig_node *orig_node)

    initialise the nc fields of an orig_node

    :param struct batadv_orig_node \*orig_node:
        the orig_node which is going to be initialised

.. _`batadv_nc_node_release`:

batadv_nc_node_release
======================

.. c:function:: void batadv_nc_node_release(struct kref *ref)

    release nc_node from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the nc_node

.. _`batadv_nc_node_put`:

batadv_nc_node_put
==================

.. c:function:: void batadv_nc_node_put(struct batadv_nc_node *nc_node)

    decrement the nc_node refcounter and possibly release it

    :param struct batadv_nc_node \*nc_node:
        nc_node to be free'd

.. _`batadv_nc_path_release`:

batadv_nc_path_release
======================

.. c:function:: void batadv_nc_path_release(struct kref *ref)

    release nc_path from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the nc_path

.. _`batadv_nc_path_put`:

batadv_nc_path_put
==================

.. c:function:: void batadv_nc_path_put(struct batadv_nc_path *nc_path)

    decrement the nc_path refcounter and possibly release it

    :param struct batadv_nc_path \*nc_path:
        nc_path to be free'd

.. _`batadv_nc_packet_free`:

batadv_nc_packet_free
=====================

.. c:function:: void batadv_nc_packet_free(struct batadv_nc_packet *nc_packet, bool dropped)

    frees nc packet

    :param struct batadv_nc_packet \*nc_packet:
        the nc packet to free

    :param bool dropped:
        whether the packet is freed because is is dropped

.. _`batadv_nc_to_purge_nc_node`:

batadv_nc_to_purge_nc_node
==========================

.. c:function:: bool batadv_nc_to_purge_nc_node(struct batadv_priv *bat_priv, struct batadv_nc_node *nc_node)

    checks whether an nc node has to be purged

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_nc_node \*nc_node:
        the nc node to check

.. _`batadv_nc_to_purge_nc_node.return`:

Return
------

true if the entry has to be purged now, false otherwise

.. _`batadv_nc_to_purge_nc_path_coding`:

batadv_nc_to_purge_nc_path_coding
=================================

.. c:function:: bool batadv_nc_to_purge_nc_path_coding(struct batadv_priv *bat_priv, struct batadv_nc_path *nc_path)

    checks whether an nc path has timed out

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_nc_path \*nc_path:
        the nc path to check

.. _`batadv_nc_to_purge_nc_path_coding.return`:

Return
------

true if the entry has to be purged now, false otherwise

.. _`batadv_nc_to_purge_nc_path_decoding`:

batadv_nc_to_purge_nc_path_decoding
===================================

.. c:function:: bool batadv_nc_to_purge_nc_path_decoding(struct batadv_priv *bat_priv, struct batadv_nc_path *nc_path)

    checks whether an nc path has timed out

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_nc_path \*nc_path:
        the nc path to check

.. _`batadv_nc_to_purge_nc_path_decoding.return`:

Return
------

true if the entry has to be purged now, false otherwise

.. _`batadv_nc_purge_orig_nc_nodes`:

batadv_nc_purge_orig_nc_nodes
=============================

.. c:function:: void batadv_nc_purge_orig_nc_nodes(struct batadv_priv *bat_priv, struct list_head *list, spinlock_t *lock, bool (*to_purge)(struct batadv_priv *, struct batadv_nc_node *))

    go through list of nc nodes and purge stale entries

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct list_head \*list:
        list of nc nodes

    :param spinlock_t \*lock:
        nc node list lock

    :param bool (\*to_purge)(struct batadv_priv \*, struct batadv_nc_node \*):
        function in charge to decide whether an entry has to be purged or
        not. This function takes the nc node as argument and has to return
        a boolean value: true if the entry has to be deleted, false
        otherwise

.. _`batadv_nc_purge_orig`:

batadv_nc_purge_orig
====================

.. c:function:: void batadv_nc_purge_orig(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, bool (*to_purge)(struct batadv_priv *, struct batadv_nc_node *))

    purges all nc node data attached of the given originator

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig_node with the nc node entries to be purged

    :param bool (\*to_purge)(struct batadv_priv \*, struct batadv_nc_node \*):
        function in charge to decide whether an entry has to be purged or
        not. This function takes the nc node as argument and has to return
        a boolean value: true is the entry has to be deleted, false
        otherwise

.. _`batadv_nc_purge_orig_hash`:

batadv_nc_purge_orig_hash
=========================

.. c:function:: void batadv_nc_purge_orig_hash(struct batadv_priv *bat_priv)

    traverse entire originator hash to check if they have timed out nc nodes

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_purge_paths`:

batadv_nc_purge_paths
=====================

.. c:function:: void batadv_nc_purge_paths(struct batadv_priv *bat_priv, struct batadv_hashtable *hash, bool (*to_purge)(struct batadv_priv *, struct batadv_nc_path *))

    traverse all nc paths part of the hash and remove unused ones

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hashtable \*hash:
        hash table containing the nc paths to check

    :param bool (\*to_purge)(struct batadv_priv \*, struct batadv_nc_path \*):
        function in charge to decide whether an entry has to be purged or
        not. This function takes the nc node as argument and has to return
        a boolean value: true is the entry has to be deleted, false
        otherwise

.. _`batadv_nc_hash_key_gen`:

batadv_nc_hash_key_gen
======================

.. c:function:: void batadv_nc_hash_key_gen(struct batadv_nc_path *key, const char *src, const char *dst)

    computes the nc_path hash key

    :param struct batadv_nc_path \*key:
        buffer to hold the final hash key

    :param const char \*src:
        source ethernet mac address going into the hash key

    :param const char \*dst:
        destination ethernet mac address going into the hash key

.. _`batadv_nc_hash_choose`:

batadv_nc_hash_choose
=====================

.. c:function:: u32 batadv_nc_hash_choose(const void *data, u32 size)

    compute the hash value for an nc path

    :param const void \*data:
        data to hash

    :param u32 size:
        size of the hash table

.. _`batadv_nc_hash_choose.return`:

Return
------

the selected index in the hash table for the given data.

.. _`batadv_nc_hash_compare`:

batadv_nc_hash_compare
======================

.. c:function:: bool batadv_nc_hash_compare(const struct hlist_node *node, const void *data2)

    comparing function used in the network coding hash tables

    :param const struct hlist_node \*node:
        node in the local table

    :param const void \*data2:
        second object to compare the node to

.. _`batadv_nc_hash_compare.return`:

Return
------

true if the two entry are the same, false otherwise

.. _`batadv_nc_hash_find`:

batadv_nc_hash_find
===================

.. c:function:: struct batadv_nc_path *batadv_nc_hash_find(struct batadv_hashtable *hash, void *data)

    search for an existing nc path and return it

    :param struct batadv_hashtable \*hash:
        hash table containing the nc path

    :param void \*data:
        search key

.. _`batadv_nc_hash_find.return`:

Return
------

the nc_path if found, NULL otherwise.

.. _`batadv_nc_send_packet`:

batadv_nc_send_packet
=====================

.. c:function:: void batadv_nc_send_packet(struct batadv_nc_packet *nc_packet)

    send non-coded packet and free nc_packet struct

    :param struct batadv_nc_packet \*nc_packet:
        the nc packet to send

.. _`batadv_nc_sniffed_purge`:

batadv_nc_sniffed_purge
=======================

.. c:function:: bool batadv_nc_sniffed_purge(struct batadv_priv *bat_priv, struct batadv_nc_path *nc_path, struct batadv_nc_packet *nc_packet)

    Checks timestamp of given sniffed nc_packet.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_nc_path \*nc_path:
        the nc path the packet belongs to

    :param struct batadv_nc_packet \*nc_packet:
        the nc packet to be checked

.. _`batadv_nc_sniffed_purge.description`:

Description
-----------

Checks whether the given sniffed (overheard) nc_packet has hit its buffering
timeout. If so, the packet is no longer kept and the entry deleted from the
queue. Has to be called with the appropriate locks.

.. _`batadv_nc_sniffed_purge.return`:

Return
------

false as soon as the entry in the fifo queue has not been timed out
yet and true otherwise.

.. _`batadv_nc_fwd_flush`:

batadv_nc_fwd_flush
===================

.. c:function:: bool batadv_nc_fwd_flush(struct batadv_priv *bat_priv, struct batadv_nc_path *nc_path, struct batadv_nc_packet *nc_packet)

    Checks the timestamp of the given nc packet.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_nc_path \*nc_path:
        the nc path the packet belongs to

    :param struct batadv_nc_packet \*nc_packet:
        the nc packet to be checked

.. _`batadv_nc_fwd_flush.description`:

Description
-----------

Checks whether the given nc packet has hit its forward timeout. If so, the
packet is no longer delayed, immediately sent and the entry deleted from the
queue. Has to be called with the appropriate locks.

.. _`batadv_nc_fwd_flush.return`:

Return
------

false as soon as the entry in the fifo queue has not been timed out
yet and true otherwise.

.. _`batadv_nc_process_nc_paths`:

batadv_nc_process_nc_paths
==========================

.. c:function:: void batadv_nc_process_nc_paths(struct batadv_priv *bat_priv, struct batadv_hashtable *hash, bool (*process_fn)(struct batadv_priv *, struct batadv_nc_path *, struct batadv_nc_packet *))

    traverse given nc packet pool and free timed out nc packets

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hashtable \*hash:
        to be processed hash table

    :param bool (\*process_fn)(struct batadv_priv \*, struct batadv_nc_path \*, struct batadv_nc_packet \*):
        Function called to process given nc packet. Should return true
        to encourage this function to proceed with the next packet.
        Otherwise the rest of the current queue is skipped.

.. _`batadv_nc_worker`:

batadv_nc_worker
================

.. c:function:: void batadv_nc_worker(struct work_struct *work)

    periodic task for house keeping related to network coding

    :param struct work_struct \*work:
        kernel work struct

.. _`batadv_can_nc_with_orig`:

batadv_can_nc_with_orig
=======================

.. c:function:: bool batadv_can_nc_with_orig(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_ogm_packet *ogm_packet)

    checks whether the given orig node is suitable for coding or not

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        neighboring orig node which may be used as nc candidate

    :param struct batadv_ogm_packet \*ogm_packet:
        incoming ogm packet also used for the checks

.. _`batadv_can_nc_with_orig.return`:

Return
------

true if:
1) The OGM must have the most recent sequence number.
2) The TTL must be decremented by one and only one.
3) The OGM must be received from the first hop from orig_node.
4) The TQ value of the OGM must be above bat_priv->nc.min_tq.

.. _`batadv_nc_find_nc_node`:

batadv_nc_find_nc_node
======================

.. c:function:: struct batadv_nc_node *batadv_nc_find_nc_node(struct batadv_orig_node *orig_node, struct batadv_orig_node *orig_neigh_node, bool in_coding)

    search for an existing nc node and return it

    :param struct batadv_orig_node \*orig_node:
        orig node originating the ogm packet

    :param struct batadv_orig_node \*orig_neigh_node:
        neighboring orig node from which we received the ogm packet
        (can be equal to orig_node)

    :param bool in_coding:
        traverse incoming or outgoing network coding list

.. _`batadv_nc_find_nc_node.return`:

Return
------

the nc_node if found, NULL otherwise.

.. _`batadv_nc_get_nc_node`:

batadv_nc_get_nc_node
=====================

.. c:function:: struct batadv_nc_node *batadv_nc_get_nc_node(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_orig_node *orig_neigh_node, bool in_coding)

    retrieves an nc node or creates the entry if it was not found

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node originating the ogm packet

    :param struct batadv_orig_node \*orig_neigh_node:
        neighboring orig node from which we received the ogm packet
        (can be equal to orig_node)

    :param bool in_coding:
        traverse incoming or outgoing network coding list

.. _`batadv_nc_get_nc_node.return`:

Return
------

the nc_node if found or created, NULL in case of an error.

.. _`batadv_nc_update_nc_node`:

batadv_nc_update_nc_node
========================

.. c:function:: void batadv_nc_update_nc_node(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_orig_node *orig_neigh_node, struct batadv_ogm_packet *ogm_packet, int is_single_hop_neigh)

    updates stored incoming and outgoing nc node structs (best called on incoming OGMs)

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node originating the ogm packet

    :param struct batadv_orig_node \*orig_neigh_node:
        neighboring orig node from which we received the ogm packet
        (can be equal to orig_node)

    :param struct batadv_ogm_packet \*ogm_packet:
        incoming ogm packet

    :param int is_single_hop_neigh:
        orig_node is a single hop neighbor

.. _`batadv_nc_get_path`:

batadv_nc_get_path
==================

.. c:function:: struct batadv_nc_path *batadv_nc_get_path(struct batadv_priv *bat_priv, struct batadv_hashtable *hash, u8 *src, u8 *dst)

    get existing nc_path or allocate a new one

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hashtable \*hash:
        hash table containing the nc path

    :param u8 \*src:
        ethernet source address - first half of the nc path search key

    :param u8 \*dst:
        ethernet destination address - second half of the nc path search key

.. _`batadv_nc_get_path.return`:

Return
------

pointer to nc_path if the path was found or created, returns NULL
on error.

.. _`batadv_nc_random_weight_tq`:

batadv_nc_random_weight_tq
==========================

.. c:function:: u8 batadv_nc_random_weight_tq(u8 tq)

    scale the receivers TQ-value to avoid unfair selection of a receiver with slightly lower TQ than the other

    :param u8 tq:
        to be weighted tq value

.. _`batadv_nc_random_weight_tq.return`:

Return
------

scaled tq value

.. _`batadv_nc_memxor`:

batadv_nc_memxor
================

.. c:function:: void batadv_nc_memxor(char *dst, const char *src, unsigned int len)

    XOR destination with source

    :param char \*dst:
        byte array to XOR into

    :param const char \*src:
        byte array to XOR from

    :param unsigned int len:
        length of destination array

.. _`batadv_nc_code_packets`:

batadv_nc_code_packets
======================

.. c:function:: bool batadv_nc_code_packets(struct batadv_priv *bat_priv, struct sk_buff *skb, struct ethhdr *ethhdr, struct batadv_nc_packet *nc_packet, struct batadv_neigh_node *neigh_node)

    code a received unicast_packet with an nc packet into a coded_packet and send it

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        data skb to forward

    :param struct ethhdr \*ethhdr:
        pointer to the ethernet header inside the skb

    :param struct batadv_nc_packet \*nc_packet:
        structure containing the packet to the skb can be coded with

    :param struct batadv_neigh_node \*neigh_node:
        next hop to forward packet to

.. _`batadv_nc_code_packets.return`:

Return
------

true if both packets are consumed, false otherwise.

.. _`batadv_nc_skb_coding_possible`:

batadv_nc_skb_coding_possible
=============================

.. c:function:: bool batadv_nc_skb_coding_possible(struct sk_buff *skb, u8 *dst, u8 *src)

    true if a decoded skb is available at dst.

    :param struct sk_buff \*skb:
        data skb to forward

    :param u8 \*dst:
        destination mac address of the other skb to code with

    :param u8 \*src:
        source mac address of skb

.. _`batadv_nc_skb_coding_possible.description`:

Description
-----------

Whenever we network code a packet we have to check whether we received it in
a network coded form. If so, we may not be able to use it for coding because
some neighbors may also have received (overheard) the packet in the network
coded form without being able to decode it. It is hard to know which of the
neighboring nodes was able to decode the packet, therefore we can only
re-code the packet if the source of the previous encoded packet is involved.
Since the source encoded the packet we can be certain it has all necessary
decode information.

.. _`batadv_nc_skb_coding_possible.return`:

Return
------

true if coding of a decoded packet is allowed.

.. _`batadv_nc_path_search`:

batadv_nc_path_search
=====================

.. c:function:: struct batadv_nc_packet *batadv_nc_path_search(struct batadv_priv *bat_priv, struct batadv_nc_node *in_nc_node, struct batadv_nc_node *out_nc_node, struct sk_buff *skb, u8 *eth_dst)

    Find the coding path matching in_nc_node and out_nc_node to retrieve a buffered packet that can be used for coding.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_nc_node \*in_nc_node:
        pointer to skb next hop's neighbor nc node

    :param struct batadv_nc_node \*out_nc_node:
        pointer to skb source's neighbor nc node

    :param struct sk_buff \*skb:
        data skb to forward

    :param u8 \*eth_dst:
        next hop mac address of skb

.. _`batadv_nc_path_search.return`:

Return
------

true if coding of a decoded skb is allowed.

.. _`batadv_nc_skb_src_search`:

batadv_nc_skb_src_search
========================

.. c:function:: struct batadv_nc_packet *batadv_nc_skb_src_search(struct batadv_priv *bat_priv, struct sk_buff *skb, u8 *eth_dst, u8 *eth_src, struct batadv_nc_node *in_nc_node)

    Loops through the list of neighoring nodes of the skb's sender (may be equal to the originator).

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        data skb to forward

    :param u8 \*eth_dst:
        next hop mac address of skb

    :param u8 \*eth_src:
        source mac address of skb

    :param struct batadv_nc_node \*in_nc_node:
        pointer to skb next hop's neighbor nc node

.. _`batadv_nc_skb_src_search.return`:

Return
------

an nc packet if a suitable coding packet was found, NULL otherwise.

.. _`batadv_nc_skb_store_before_coding`:

batadv_nc_skb_store_before_coding
=================================

.. c:function:: void batadv_nc_skb_store_before_coding(struct batadv_priv *bat_priv, struct sk_buff *skb, u8 *eth_dst_new)

    set the ethernet src and dst of the unicast skb before it is stored for use in later decoding

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        data skb to store

    :param u8 \*eth_dst_new:
        new destination mac address of skb

.. _`batadv_nc_skb_dst_search`:

batadv_nc_skb_dst_search
========================

.. c:function:: bool batadv_nc_skb_dst_search(struct sk_buff *skb, struct batadv_neigh_node *neigh_node, struct ethhdr *ethhdr)

    Loops through list of neighboring nodes to dst.

    :param struct sk_buff \*skb:
        data skb to forward

    :param struct batadv_neigh_node \*neigh_node:
        next hop to forward packet to

    :param struct ethhdr \*ethhdr:
        pointer to the ethernet header inside the skb

.. _`batadv_nc_skb_dst_search.description`:

Description
-----------

Loops through list of neighboring nodes the next hop has a good connection to
(receives OGMs with a sufficient quality). We need to find a neighbor of our
next hop that potentially sent a packet which our next hop also received
(overheard) and has stored for later decoding.

.. _`batadv_nc_skb_dst_search.return`:

Return
------

true if the skb was consumed (encoded packet sent) or false otherwise

.. _`batadv_nc_skb_add_to_path`:

batadv_nc_skb_add_to_path
=========================

.. c:function:: bool batadv_nc_skb_add_to_path(struct sk_buff *skb, struct batadv_nc_path *nc_path, struct batadv_neigh_node *neigh_node, __be32 packet_id)

    buffer skb for later encoding / decoding

    :param struct sk_buff \*skb:
        skb to add to path

    :param struct batadv_nc_path \*nc_path:
        path to add skb to

    :param struct batadv_neigh_node \*neigh_node:
        next hop to forward packet to

    :param __be32 packet_id:
        checksum to identify packet

.. _`batadv_nc_skb_add_to_path.return`:

Return
------

true if the packet was buffered or false in case of an error.

.. _`batadv_nc_skb_forward`:

batadv_nc_skb_forward
=====================

.. c:function:: bool batadv_nc_skb_forward(struct sk_buff *skb, struct batadv_neigh_node *neigh_node)

    try to code a packet or add it to the coding packet buffer

    :param struct sk_buff \*skb:
        data skb to forward

    :param struct batadv_neigh_node \*neigh_node:
        next hop to forward packet to

.. _`batadv_nc_skb_forward.return`:

Return
------

true if the skb was consumed (encoded packet sent) or false otherwise

.. _`batadv_nc_skb_store_for_decoding`:

batadv_nc_skb_store_for_decoding
================================

.. c:function:: void batadv_nc_skb_store_for_decoding(struct batadv_priv *bat_priv, struct sk_buff *skb)

    save a clone of the skb which can be used when decoding coded packets

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        data skb to store

.. _`batadv_nc_skb_store_sniffed_unicast`:

batadv_nc_skb_store_sniffed_unicast
===================================

.. c:function:: void batadv_nc_skb_store_sniffed_unicast(struct batadv_priv *bat_priv, struct sk_buff *skb)

    check if a received unicast packet should be saved in the decoding buffer and, if so, store it there

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        unicast skb to store

.. _`batadv_nc_skb_decode_packet`:

batadv_nc_skb_decode_packet
===========================

.. c:function:: struct batadv_unicast_packet *batadv_nc_skb_decode_packet(struct batadv_priv *bat_priv, struct sk_buff *skb, struct batadv_nc_packet *nc_packet)

    decode given skb using the decode data stored in nc_packet

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        unicast skb to decode

    :param struct batadv_nc_packet \*nc_packet:
        decode data needed to decode the skb

.. _`batadv_nc_skb_decode_packet.return`:

Return
------

pointer to decoded unicast packet if the packet was decoded or NULL
in case of an error.

.. _`batadv_nc_find_decoding_packet`:

batadv_nc_find_decoding_packet
==============================

.. c:function:: struct batadv_nc_packet *batadv_nc_find_decoding_packet(struct batadv_priv *bat_priv, struct ethhdr *ethhdr, struct batadv_coded_packet *coded)

    search through buffered decoding data to find the data needed to decode the coded packet

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct ethhdr \*ethhdr:
        pointer to the ethernet header inside the coded packet

    :param struct batadv_coded_packet \*coded:
        coded packet we try to find decode data for

.. _`batadv_nc_find_decoding_packet.return`:

Return
------

pointer to nc packet if the needed data was found or NULL otherwise.

.. _`batadv_nc_recv_coded_packet`:

batadv_nc_recv_coded_packet
===========================

.. c:function:: int batadv_nc_recv_coded_packet(struct sk_buff *skb, struct batadv_hard_iface *recv_if)

    try to decode coded packet and enqueue the resulting unicast packet

    :param struct sk_buff \*skb:
        incoming coded packet

    :param struct batadv_hard_iface \*recv_if:
        pointer to interface this packet was received on

.. _`batadv_nc_recv_coded_packet.return`:

Return
------

NET_RX_SUCCESS if the packet has been consumed or NET_RX_DROP
otherwise.

.. _`batadv_nc_mesh_free`:

batadv_nc_mesh_free
===================

.. c:function:: void batadv_nc_mesh_free(struct batadv_priv *bat_priv)

    clean up network coding memory

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_nodes_seq_print_text`:

batadv_nc_nodes_seq_print_text
==============================

.. c:function:: int batadv_nc_nodes_seq_print_text(struct seq_file *seq, void *offset)

    print the nc node information

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_nc_nodes_seq_print_text.return`:

Return
------

always 0

.. _`batadv_nc_init_debugfs`:

batadv_nc_init_debugfs
======================

.. c:function:: int batadv_nc_init_debugfs(struct batadv_priv *bat_priv)

    create nc folder and related files in debugfs

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_nc_init_debugfs.return`:

Return
------

0 on success or negative error number in case of failure

.. This file was automatic generated / don't edit.

