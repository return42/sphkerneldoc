.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/distributed-arp-table.c

.. _`batadv_dat_start_timer`:

batadv_dat_start_timer
======================

.. c:function:: void batadv_dat_start_timer(struct batadv_priv *bat_priv)

    initialise the DAT periodic worker

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_dat_entry_release`:

batadv_dat_entry_release
========================

.. c:function:: void batadv_dat_entry_release(struct kref *ref)

    release dat_entry from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the dat_entry

.. _`batadv_dat_entry_put`:

batadv_dat_entry_put
====================

.. c:function:: void batadv_dat_entry_put(struct batadv_dat_entry *dat_entry)

    decrement the dat_entry refcounter and possibly release it

    :param struct batadv_dat_entry \*dat_entry:
        dat_entry to be free'd

.. _`batadv_dat_to_purge`:

batadv_dat_to_purge
===================

.. c:function:: bool batadv_dat_to_purge(struct batadv_dat_entry *dat_entry)

    check whether a dat_entry has to be purged or not

    :param struct batadv_dat_entry \*dat_entry:
        the entry to check

.. _`batadv_dat_to_purge.return`:

Return
------

true if the entry has to be purged now, false otherwise.

.. _`__batadv_dat_purge`:

\__batadv_dat_purge
===================

.. c:function:: void __batadv_dat_purge(struct batadv_priv *bat_priv, bool (*to_purge)(struct batadv_dat_entry *))

    delete entries from the DAT local storage

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param bool (\*to_purge)(struct batadv_dat_entry \*):
        function in charge to decide whether an entry has to be purged or
        not. This function takes the dat_entry as argument and has to
        returns a boolean value: true is the entry has to be deleted,
        false otherwise

.. _`__batadv_dat_purge.description`:

Description
-----------

Loops over each entry in the DAT local storage and deletes it if and only if
the to_purge function passed as argument returns true.

.. _`batadv_dat_purge`:

batadv_dat_purge
================

.. c:function:: void batadv_dat_purge(struct work_struct *work)

    periodic task that deletes old entries from the local DAT hash table

    :param struct work_struct \*work:
        kernel work struct

.. _`batadv_compare_dat`:

batadv_compare_dat
==================

.. c:function:: bool batadv_compare_dat(const struct hlist_node *node, const void *data2)

    comparing function used in the local DAT hash table

    :param const struct hlist_node \*node:
        node in the local table

    :param const void \*data2:
        second object to compare the node to

.. _`batadv_compare_dat.return`:

Return
------

true if the two entries are the same, false otherwise.

.. _`batadv_arp_hw_src`:

batadv_arp_hw_src
=================

.. c:function:: u8 *batadv_arp_hw_src(struct sk_buff *skb, int hdr_size)

    extract the hw_src field from an ARP packet

    :param struct sk_buff \*skb:
        ARP packet

    :param int hdr_size:
        size of the possible header before the ARP packet

.. _`batadv_arp_hw_src.return`:

Return
------

the value of the hw_src field in the ARP packet.

.. _`batadv_arp_ip_src`:

batadv_arp_ip_src
=================

.. c:function:: __be32 batadv_arp_ip_src(struct sk_buff *skb, int hdr_size)

    extract the ip_src field from an ARP packet

    :param struct sk_buff \*skb:
        ARP packet

    :param int hdr_size:
        size of the possible header before the ARP packet

.. _`batadv_arp_ip_src.return`:

Return
------

the value of the ip_src field in the ARP packet.

.. _`batadv_arp_hw_dst`:

batadv_arp_hw_dst
=================

.. c:function:: u8 *batadv_arp_hw_dst(struct sk_buff *skb, int hdr_size)

    extract the hw_dst field from an ARP packet

    :param struct sk_buff \*skb:
        ARP packet

    :param int hdr_size:
        size of the possible header before the ARP packet

.. _`batadv_arp_hw_dst.return`:

Return
------

the value of the hw_dst field in the ARP packet.

.. _`batadv_arp_ip_dst`:

batadv_arp_ip_dst
=================

.. c:function:: __be32 batadv_arp_ip_dst(struct sk_buff *skb, int hdr_size)

    extract the ip_dst field from an ARP packet

    :param struct sk_buff \*skb:
        ARP packet

    :param int hdr_size:
        size of the possible header before the ARP packet

.. _`batadv_arp_ip_dst.return`:

Return
------

the value of the ip_dst field in the ARP packet.

.. _`batadv_hash_dat`:

batadv_hash_dat
===============

.. c:function:: u32 batadv_hash_dat(const void *data, u32 size)

    compute the hash value for an IP address

    :param const void \*data:
        data to hash

    :param u32 size:
        size of the hash table

.. _`batadv_hash_dat.return`:

Return
------

the selected index in the hash table for the given data.

.. _`batadv_dat_entry_hash_find`:

batadv_dat_entry_hash_find
==========================

.. c:function:: struct batadv_dat_entry *batadv_dat_entry_hash_find(struct batadv_priv *bat_priv, __be32 ip, unsigned short vid)

    look for a given dat_entry in the local hash table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param __be32 ip:
        search key

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_dat_entry_hash_find.return`:

Return
------

the dat_entry if found, NULL otherwise.

.. _`batadv_dat_entry_add`:

batadv_dat_entry_add
====================

.. c:function:: void batadv_dat_entry_add(struct batadv_priv *bat_priv, __be32 ip, u8 *mac_addr, unsigned short vid)

    add a new dat entry or update it if already exists

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param __be32 ip:
        ipv4 to add/edit

    :param u8 \*mac_addr:
        mac address to assign to the given ipv4

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_dbg_arp`:

batadv_dbg_arp
==============

.. c:function:: void batadv_dbg_arp(struct batadv_priv *bat_priv, struct sk_buff *skb, int hdr_size, char *msg)

    print a debug message containing all the ARP packet details

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        ARP packet

    :param int hdr_size:
        size of the possible header before the ARP packet

    :param char \*msg:
        message to print together with the debugging information

.. _`batadv_is_orig_node_eligible`:

batadv_is_orig_node_eligible
============================

.. c:function:: bool batadv_is_orig_node_eligible(struct batadv_dat_candidate *res, int select, batadv_dat_addr_t tmp_max, batadv_dat_addr_t max, batadv_dat_addr_t last_max, struct batadv_orig_node *candidate, struct batadv_orig_node *max_orig_node)

    check whether a node can be a DHT candidate

    :param struct batadv_dat_candidate \*res:
        the array with the already selected candidates

    :param int select:
        number of already selected candidates

    :param batadv_dat_addr_t tmp_max:
        address of the currently evaluated node

    :param batadv_dat_addr_t max:
        current round max address

    :param batadv_dat_addr_t last_max:
        address of the last selected candidate

    :param struct batadv_orig_node \*candidate:
        orig_node under evaluation

    :param struct batadv_orig_node \*max_orig_node:
        last selected candidate

.. _`batadv_is_orig_node_eligible.return`:

Return
------

true if the node has been elected as next candidate or false
otherwise.

.. _`batadv_choose_next_candidate`:

batadv_choose_next_candidate
============================

.. c:function:: void batadv_choose_next_candidate(struct batadv_priv *bat_priv, struct batadv_dat_candidate *cands, int select, batadv_dat_addr_t ip_key, batadv_dat_addr_t *last_max)

    select the next DHT candidate

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_dat_candidate \*cands:
        candidates array

    :param int select:
        number of candidates already present in the array

    :param batadv_dat_addr_t ip_key:
        key to look up in the DHT

    :param batadv_dat_addr_t \*last_max:
        pointer where the address of the selected candidate will be saved

.. _`batadv_dat_select_candidates`:

batadv_dat_select_candidates
============================

.. c:function:: struct batadv_dat_candidate *batadv_dat_select_candidates(struct batadv_priv *bat_priv, __be32 ip_dst, unsigned short vid)

    select the nodes which the DHT message has to be sent to

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param __be32 ip_dst:
        ipv4 to look up in the DHT

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_dat_select_candidates.description`:

Description
-----------

An originator O is selected if and only if its DHT_ID value is one of three
closest values (from the LEFT, with wrap around if needed) then the hash
value of the key. ip_dst is the key.

.. _`batadv_dat_select_candidates.return`:

Return
------

the candidate array of size BATADV_DAT_CANDIDATE_NUM.

.. _`batadv_dat_send_data`:

batadv_dat_send_data
====================

.. c:function:: bool batadv_dat_send_data(struct batadv_priv *bat_priv, struct sk_buff *skb, __be32 ip, unsigned short vid, int packet_subtype)

    send a payload to the selected candidates

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        payload to send

    :param __be32 ip:
        the DHT key

    :param unsigned short vid:
        VLAN identifier

    :param int packet_subtype:
        unicast4addr packet subtype to use

.. _`batadv_dat_send_data.description`:

Description
-----------

This function copies the skb with \ :c:func:`pskb_copy`\  and is sent as unicast packet
to each of the selected candidates.

.. _`batadv_dat_send_data.return`:

Return
------

true if the packet is sent to at least one candidate, false
otherwise.

.. _`batadv_dat_tvlv_container_update`:

batadv_dat_tvlv_container_update
================================

.. c:function:: void batadv_dat_tvlv_container_update(struct batadv_priv *bat_priv)

    update the dat tvlv container after dat setting change

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_dat_status_update`:

batadv_dat_status_update
========================

.. c:function:: void batadv_dat_status_update(struct net_device *net_dev)

    update the dat tvlv container after dat setting change

    :param struct net_device \*net_dev:
        the soft interface net device

.. _`batadv_dat_tvlv_ogm_handler_v1`:

batadv_dat_tvlv_ogm_handler_v1
==============================

.. c:function:: void batadv_dat_tvlv_ogm_handler_v1(struct batadv_priv *bat_priv, struct batadv_orig_node *orig, u8 flags, void *tvlv_value, u16 tvlv_value_len)

    process incoming dat tvlv container

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

.. _`batadv_dat_hash_free`:

batadv_dat_hash_free
====================

.. c:function:: void batadv_dat_hash_free(struct batadv_priv *bat_priv)

    free the local DAT hash table

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_dat_init`:

batadv_dat_init
===============

.. c:function:: int batadv_dat_init(struct batadv_priv *bat_priv)

    initialise the DAT internals

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_dat_init.return`:

Return
------

0 in case of success, a negative error code otherwise

.. _`batadv_dat_free`:

batadv_dat_free
===============

.. c:function:: void batadv_dat_free(struct batadv_priv *bat_priv)

    free the DAT internals

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_dat_cache_seq_print_text`:

batadv_dat_cache_seq_print_text
===============================

.. c:function:: int batadv_dat_cache_seq_print_text(struct seq_file *seq, void *offset)

    print the local DAT hash table

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_dat_cache_seq_print_text.return`:

Return
------

always 0

.. _`batadv_arp_get_type`:

batadv_arp_get_type
===================

.. c:function:: u16 batadv_arp_get_type(struct batadv_priv *bat_priv, struct sk_buff *skb, int hdr_size)

    parse an ARP packet and gets the type

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        packet to analyse

    :param int hdr_size:
        size of the possible header before the ARP packet in the skb

.. _`batadv_arp_get_type.return`:

Return
------

the ARP type if the skb contains a valid ARP packet, 0 otherwise.

.. _`batadv_dat_get_vid`:

batadv_dat_get_vid
==================

.. c:function:: unsigned short batadv_dat_get_vid(struct sk_buff *skb, int *hdr_size)

    extract the VLAN identifier from skb if any

    :param struct sk_buff \*skb:
        the buffer containing the packet to extract the VID from

    :param int \*hdr_size:
        the size of the batman-adv header encapsulating the packet

.. _`batadv_dat_get_vid.return`:

Return
------

If the packet embedded in the skb is vlan tagged this function
returns the VID with the BATADV_VLAN_HAS_TAG flag. Otherwise BATADV_NO_FLAGS
is returned.

.. _`batadv_dat_arp_create_reply`:

batadv_dat_arp_create_reply
===========================

.. c:function:: struct sk_buff *batadv_dat_arp_create_reply(struct batadv_priv *bat_priv, __be32 ip_src, __be32 ip_dst, u8 *hw_src, u8 *hw_dst, unsigned short vid)

    create an ARP Reply

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param __be32 ip_src:
        ARP sender IP

    :param __be32 ip_dst:
        ARP target IP

    :param u8 \*hw_src:
        Ethernet source and ARP sender MAC

    :param u8 \*hw_dst:
        Ethernet destination and ARP target MAC

    :param unsigned short vid:
        VLAN identifier (optional, set to zero otherwise)

.. _`batadv_dat_arp_create_reply.description`:

Description
-----------

Creates an ARP Reply from the given values, optionally encapsulated in a
VLAN header.

.. _`batadv_dat_arp_create_reply.return`:

Return
------

An skb containing an ARP Reply.

.. _`batadv_dat_snoop_outgoing_arp_request`:

batadv_dat_snoop_outgoing_arp_request
=====================================

.. c:function:: bool batadv_dat_snoop_outgoing_arp_request(struct batadv_priv *bat_priv, struct sk_buff *skb)

    snoop the ARP request and try to answer using DAT

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        packet to check

.. _`batadv_dat_snoop_outgoing_arp_request.return`:

Return
------

true if the message has been sent to the dht candidates, false
otherwise. In case of a positive return value the message has to be enqueued
to permit the fallback.

.. _`batadv_dat_snoop_incoming_arp_request`:

batadv_dat_snoop_incoming_arp_request
=====================================

.. c:function:: bool batadv_dat_snoop_incoming_arp_request(struct batadv_priv *bat_priv, struct sk_buff *skb, int hdr_size)

    snoop the ARP request and try to answer using the local DAT storage

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        packet to check

    :param int hdr_size:
        size of the encapsulation header

.. _`batadv_dat_snoop_incoming_arp_request.return`:

Return
------

true if the request has been answered, false otherwise.

.. _`batadv_dat_snoop_outgoing_arp_reply`:

batadv_dat_snoop_outgoing_arp_reply
===================================

.. c:function:: void batadv_dat_snoop_outgoing_arp_reply(struct batadv_priv *bat_priv, struct sk_buff *skb)

    snoop the ARP reply and fill the DHT

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        packet to check

.. _`batadv_dat_snoop_incoming_arp_reply`:

batadv_dat_snoop_incoming_arp_reply
===================================

.. c:function:: bool batadv_dat_snoop_incoming_arp_reply(struct batadv_priv *bat_priv, struct sk_buff *skb, int hdr_size)

    snoop the ARP reply and fill the local DAT storage only

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        packet to check

    :param int hdr_size:
        size of the encapsulation header

.. _`batadv_dat_snoop_incoming_arp_reply.return`:

Return
------

true if the packet was snooped and consumed by DAT. False if the
packet has to be delivered to the interface

.. _`batadv_dat_drop_broadcast_packet`:

batadv_dat_drop_broadcast_packet
================================

.. c:function:: bool batadv_dat_drop_broadcast_packet(struct batadv_priv *bat_priv, struct batadv_forw_packet *forw_packet)

    check if an ARP request has to be dropped (because the node has already obtained the reply via DAT) or not

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_forw_packet \*forw_packet:
        the broadcast packet

.. _`batadv_dat_drop_broadcast_packet.return`:

Return
------

true if the node can drop the packet, false otherwise.

.. This file was automatic generated / don't edit.

