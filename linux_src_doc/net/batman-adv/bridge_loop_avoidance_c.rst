.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bridge_loop_avoidance.c

.. _`batadv_choose_claim`:

batadv_choose_claim
===================

.. c:function:: u32 batadv_choose_claim(const void *data, u32 size)

    choose the right bucket for a claim.

    :param const void \*data:
        data to hash

    :param u32 size:
        size of the hash table

.. _`batadv_choose_claim.return`:

Return
------

the hash index of the claim

.. _`batadv_choose_backbone_gw`:

batadv_choose_backbone_gw
=========================

.. c:function:: u32 batadv_choose_backbone_gw(const void *data, u32 size)

    choose the right bucket for a backbone gateway.

    :param const void \*data:
        data to hash

    :param u32 size:
        size of the hash table

.. _`batadv_choose_backbone_gw.return`:

Return
------

the hash index of the backbone gateway

.. _`batadv_compare_backbone_gw`:

batadv_compare_backbone_gw
==========================

.. c:function:: bool batadv_compare_backbone_gw(const struct hlist_node *node, const void *data2)

    compare address and vid of two backbone gws

    :param const struct hlist_node \*node:
        list node of the first entry to compare

    :param const void \*data2:
        pointer to the second backbone gateway

.. _`batadv_compare_backbone_gw.return`:

Return
------

true if the backbones have the same data, false otherwise

.. _`batadv_compare_claim`:

batadv_compare_claim
====================

.. c:function:: bool batadv_compare_claim(const struct hlist_node *node, const void *data2)

    compare address and vid of two claims

    :param const struct hlist_node \*node:
        list node of the first entry to compare

    :param const void \*data2:
        pointer to the second claims

.. _`batadv_compare_claim.return`:

Return
------

true if the claim have the same data, 0 otherwise

.. _`batadv_backbone_gw_release`:

batadv_backbone_gw_release
==========================

.. c:function:: void batadv_backbone_gw_release(struct kref *ref)

    release backbone gw from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the backbone gw

.. _`batadv_backbone_gw_put`:

batadv_backbone_gw_put
======================

.. c:function:: void batadv_backbone_gw_put(struct batadv_bla_backbone_gw *backbone_gw)

    decrement the backbone gw refcounter and possibly release it

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        backbone gateway to be free'd

.. _`batadv_claim_release`:

batadv_claim_release
====================

.. c:function:: void batadv_claim_release(struct kref *ref)

    release claim from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the claim

.. _`batadv_claim_put`:

batadv_claim_put
================

.. c:function:: void batadv_claim_put(struct batadv_bla_claim *claim)

    decrement the claim refcounter and possibly release it

    :param struct batadv_bla_claim \*claim:
        claim to be free'd

.. _`batadv_claim_hash_find`:

batadv_claim_hash_find
======================

.. c:function:: struct batadv_bla_claim *batadv_claim_hash_find(struct batadv_priv *bat_priv, struct batadv_bla_claim *data)

    looks for a claim in the claim hash

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_bla_claim \*data:
        search data (may be local/static data)

.. _`batadv_claim_hash_find.return`:

Return
------

claim if found or NULL otherwise.

.. _`batadv_backbone_hash_find`:

batadv_backbone_hash_find
=========================

.. c:function:: struct batadv_bla_backbone_gw *batadv_backbone_hash_find(struct batadv_priv *bat_priv, u8 *addr, unsigned short vid)

    looks for a backbone gateway in the hash

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*addr:
        the address of the originator

    :param unsigned short vid:
        the VLAN ID

.. _`batadv_backbone_hash_find.return`:

Return
------

backbone gateway if found or NULL otherwise

.. _`batadv_bla_del_backbone_claims`:

batadv_bla_del_backbone_claims
==============================

.. c:function:: void batadv_bla_del_backbone_claims(struct batadv_bla_backbone_gw *backbone_gw)

    delete all claims for a backbone

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        backbone gateway where the claims should be removed

.. _`batadv_bla_send_claim`:

batadv_bla_send_claim
=====================

.. c:function:: void batadv_bla_send_claim(struct batadv_priv *bat_priv, u8 *mac, unsigned short vid, int claimtype)

    sends a claim frame according to the provided info

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*mac:
        the mac address to be announced within the claim

    :param unsigned short vid:
        the VLAN ID

    :param int claimtype:
        the type of the claim (CLAIM, UNCLAIM, ANNOUNCE, ...)

.. _`batadv_bla_loopdetect_report`:

batadv_bla_loopdetect_report
============================

.. c:function:: void batadv_bla_loopdetect_report(struct work_struct *work)

    worker for reporting the loop

    :param struct work_struct \*work:
        work queue item

.. _`batadv_bla_loopdetect_report.description`:

Description
-----------

Throws an uevent, as the loopdetect check function can't do that itself
since the kernel may sleep while throwing uevents.

.. _`batadv_bla_get_backbone_gw`:

batadv_bla_get_backbone_gw
==========================

.. c:function:: struct batadv_bla_backbone_gw *batadv_bla_get_backbone_gw(struct batadv_priv *bat_priv, u8 *orig, unsigned short vid, bool own_backbone)

    finds or creates a backbone gateway

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*orig:
        the mac address of the originator

    :param unsigned short vid:
        the VLAN ID

    :param bool own_backbone:
        set if the requested backbone is local

.. _`batadv_bla_get_backbone_gw.return`:

Return
------

the (possibly created) backbone gateway or NULL on error

.. _`batadv_bla_update_own_backbone_gw`:

batadv_bla_update_own_backbone_gw
=================================

.. c:function:: void batadv_bla_update_own_backbone_gw(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, unsigned short vid)

    updates the own backbone gw for a VLAN

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the selected primary interface

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_bla_update_own_backbone_gw.description`:

Description
-----------

update or add the own backbone gw to make sure we announce
where we receive other backbone gws

.. _`batadv_bla_answer_request`:

batadv_bla_answer_request
=========================

.. c:function:: void batadv_bla_answer_request(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, unsigned short vid)

    answer a bla request by sending own claims

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        interface where the request came on

    :param unsigned short vid:
        the vid where the request came on

.. _`batadv_bla_answer_request.description`:

Description
-----------

Repeat all of our own claims, and finally send an ANNOUNCE frame
to allow the requester another check if the CRC is correct now.

.. _`batadv_bla_send_request`:

batadv_bla_send_request
=======================

.. c:function:: void batadv_bla_send_request(struct batadv_bla_backbone_gw *backbone_gw)

    send a request to repeat claims

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        the backbone gateway from whom we are out of sync

.. _`batadv_bla_send_request.description`:

Description
-----------

When the crc is wrong, ask the backbone gateway for a full table update.
After the request, it will repeat all of his own claims and finally
send an announcement claim with which we can check again.

.. _`batadv_bla_send_announce`:

batadv_bla_send_announce
========================

.. c:function:: void batadv_bla_send_announce(struct batadv_priv *bat_priv, struct batadv_bla_backbone_gw *backbone_gw)

    Send an announcement frame

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        our backbone gateway which should be announced

.. _`batadv_bla_add_claim`:

batadv_bla_add_claim
====================

.. c:function:: void batadv_bla_add_claim(struct batadv_priv *bat_priv, const u8 *mac, const unsigned short vid, struct batadv_bla_backbone_gw *backbone_gw)

    Adds a claim in the claim hash

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*mac:
        the mac address of the claim

    :param const unsigned short vid:
        the VLAN ID of the frame

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        the backbone gateway which claims it

.. _`batadv_bla_claim_get_backbone_gw`:

batadv_bla_claim_get_backbone_gw
================================

.. c:function:: struct batadv_bla_backbone_gw *batadv_bla_claim_get_backbone_gw(struct batadv_bla_claim *claim)

    Get valid reference for backbone_gw of claim

    :param struct batadv_bla_claim \*claim:
        claim whose backbone_gw should be returned

.. _`batadv_bla_claim_get_backbone_gw.description`:

Description
-----------

Return: valid reference to claim::backbone_gw

.. _`batadv_bla_del_claim`:

batadv_bla_del_claim
====================

.. c:function:: void batadv_bla_del_claim(struct batadv_priv *bat_priv, const u8 *mac, const unsigned short vid)

    delete a claim from the claim hash

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*mac:
        mac address of the claim to be removed

    :param const unsigned short vid:
        VLAN id for the claim to be removed

.. _`batadv_handle_announce`:

batadv_handle_announce
======================

.. c:function:: bool batadv_handle_announce(struct batadv_priv *bat_priv, u8 *an_addr, u8 *backbone_addr, unsigned short vid)

    check for ANNOUNCE frame

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*an_addr:
        announcement mac address (ARP Sender HW address)

    :param u8 \*backbone_addr:
        originator address of the sender (Ethernet source MAC)

    :param unsigned short vid:
        the VLAN ID of the frame

.. _`batadv_handle_announce.return`:

Return
------

true if handled

.. _`batadv_handle_request`:

batadv_handle_request
=====================

.. c:function:: bool batadv_handle_request(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, u8 *backbone_addr, struct ethhdr *ethhdr, unsigned short vid)

    check for REQUEST frame

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the primary hard interface of this batman soft interface

    :param u8 \*backbone_addr:
        backbone address to be requested (ARP sender HW MAC)

    :param struct ethhdr \*ethhdr:
        ethernet header of a packet

    :param unsigned short vid:
        the VLAN ID of the frame

.. _`batadv_handle_request.return`:

Return
------

true if handled

.. _`batadv_handle_unclaim`:

batadv_handle_unclaim
=====================

.. c:function:: bool batadv_handle_unclaim(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, u8 *backbone_addr, u8 *claim_addr, unsigned short vid)

    check for UNCLAIM frame

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the primary hard interface of this batman soft interface

    :param u8 \*backbone_addr:
        originator address of the backbone (Ethernet source)

    :param u8 \*claim_addr:
        Client to be unclaimed (ARP sender HW MAC)

    :param unsigned short vid:
        the VLAN ID of the frame

.. _`batadv_handle_unclaim.return`:

Return
------

true if handled

.. _`batadv_handle_claim`:

batadv_handle_claim
===================

.. c:function:: bool batadv_handle_claim(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, u8 *backbone_addr, u8 *claim_addr, unsigned short vid)

    check for CLAIM frame

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the primary hard interface of this batman soft interface

    :param u8 \*backbone_addr:
        originator address of the backbone (Ethernet Source)

    :param u8 \*claim_addr:
        client mac address to be claimed (ARP sender HW MAC)

    :param unsigned short vid:
        the VLAN ID of the frame

.. _`batadv_handle_claim.return`:

Return
------

true if handled

.. _`batadv_check_claim_group`:

batadv_check_claim_group
========================

.. c:function:: int batadv_check_claim_group(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, u8 *hw_src, u8 *hw_dst, struct ethhdr *ethhdr)

    check for claim group membership

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the primary interface of this batman interface

    :param u8 \*hw_src:
        the Hardware source in the ARP Header

    :param u8 \*hw_dst:
        the Hardware destination in the ARP Header

    :param struct ethhdr \*ethhdr:
        pointer to the Ethernet header of the claim frame

.. _`batadv_check_claim_group.description`:

Description
-----------

checks if it is a claim packet and if its on the same group.
This function also applies the group ID of the sender
if it is in the same mesh.

.. _`batadv_check_claim_group.return`:

Return
------

2  - if it is a claim packet and on the same group
1  - if is a claim packet from another group
0  - if it is not a claim packet

.. _`batadv_bla_process_claim`:

batadv_bla_process_claim
========================

.. c:function:: bool batadv_bla_process_claim(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, struct sk_buff *skb)

    Check if this is a claim frame, and process it

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the primary hard interface of this batman soft interface

    :param struct sk_buff \*skb:
        the frame to be checked

.. _`batadv_bla_process_claim.return`:

Return
------

true if it was a claim frame, otherwise return false to
tell the callee that it can use the frame on its own.

.. _`batadv_bla_purge_backbone_gw`:

batadv_bla_purge_backbone_gw
============================

.. c:function:: void batadv_bla_purge_backbone_gw(struct batadv_priv *bat_priv, int now)

    Remove backbone gateways after a timeout or immediately

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param int now:
        whether the whole hash shall be wiped now

.. _`batadv_bla_purge_backbone_gw.description`:

Description
-----------

Check when we last heard from other nodes, and remove them in case of
a time out, or clean all backbone gws if now is set.

.. _`batadv_bla_purge_claims`:

batadv_bla_purge_claims
=======================

.. c:function:: void batadv_bla_purge_claims(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, int now)

    Remove claims after a timeout or immediately

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the selected primary interface, may be NULL if now is set

    :param int now:
        whether the whole hash shall be wiped now

.. _`batadv_bla_purge_claims.description`:

Description
-----------

Check when we heard last time from our own claims, and remove them in case of
a time out, or clean all claims if now is set

.. _`batadv_bla_update_orig_address`:

batadv_bla_update_orig_address
==============================

.. c:function:: void batadv_bla_update_orig_address(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if, struct batadv_hard_iface *oldif)

    Update the backbone gateways when the own originator address changes

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        the new selected primary_if

    :param struct batadv_hard_iface \*oldif:
        the old primary interface, may be NULL

.. _`batadv_bla_send_loopdetect`:

batadv_bla_send_loopdetect
==========================

.. c:function:: void batadv_bla_send_loopdetect(struct batadv_priv *bat_priv, struct batadv_bla_backbone_gw *backbone_gw)

    send a loopdetect frame

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        the backbone gateway for which a loop should be detected

.. _`batadv_bla_send_loopdetect.description`:

Description
-----------

To detect loops that the bridge loop avoidance can't handle, send a loop
detection packet on the backbone. Unlike other BLA frames, this frame will
be allowed on the mesh by other nodes. If it is received on the mesh, this
indicates that there is a loop.

.. _`batadv_bla_status_update`:

batadv_bla_status_update
========================

.. c:function:: void batadv_bla_status_update(struct net_device *net_dev)

    purge bla interfaces if necessary

    :param struct net_device \*net_dev:
        the soft interface net device

.. _`batadv_bla_periodic_work`:

batadv_bla_periodic_work
========================

.. c:function:: void batadv_bla_periodic_work(struct work_struct *work)

    performs periodic bla work

    :param struct work_struct \*work:
        kernel work struct

.. _`batadv_bla_periodic_work.periodic-work-to-do`:

periodic work to do
-------------------

\* purge structures when they are too old
\* send announcements

.. _`batadv_bla_init`:

batadv_bla_init
===============

.. c:function:: int batadv_bla_init(struct batadv_priv *bat_priv)

    initialize all bla structures

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_bla_init.return`:

Return
------

0 on success, < 0 on error.

.. _`batadv_bla_check_bcast_duplist`:

batadv_bla_check_bcast_duplist
==============================

.. c:function:: bool batadv_bla_check_bcast_duplist(struct batadv_priv *bat_priv, struct sk_buff *skb)

    Check if a frame is in the broadcast dup.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        contains the bcast_packet to be checked

.. _`batadv_bla_check_bcast_duplist.description`:

Description
-----------

check if it is on our broadcast list. Another gateway might
have sent the same packet because it is connected to the same backbone,
so we have to remove this duplicate.

This is performed by checking the CRC, which will tell us
with a good chance that it is the same packet. If it is furthermore
sent by another host, drop it. We allow equal packets from
the same host however as this might be intended.

.. _`batadv_bla_check_bcast_duplist.return`:

Return
------

true if a packet is in the duplicate list, false otherwise.

.. _`batadv_bla_is_backbone_gw_orig`:

batadv_bla_is_backbone_gw_orig
==============================

.. c:function:: bool batadv_bla_is_backbone_gw_orig(struct batadv_priv *bat_priv, u8 *orig, unsigned short vid)

    Check if the originator is a gateway for the VLAN identified by vid.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*orig:
        originator mac address

    :param unsigned short vid:
        VLAN identifier

.. _`batadv_bla_is_backbone_gw_orig.return`:

Return
------

true if orig is a backbone for this vid, false otherwise.

.. _`batadv_bla_is_backbone_gw`:

batadv_bla_is_backbone_gw
=========================

.. c:function:: bool batadv_bla_is_backbone_gw(struct sk_buff *skb, struct batadv_orig_node *orig_node, int hdr_size)

    check if originator is a backbone gw for a VLAN

    :param struct sk_buff \*skb:
        the frame to be checked

    :param struct batadv_orig_node \*orig_node:
        the orig_node of the frame

    :param int hdr_size:
        maximum length of the frame

.. _`batadv_bla_is_backbone_gw.return`:

Return
------

true if the orig_node is also a gateway on the soft interface,
otherwise it returns false.

.. _`batadv_bla_free`:

batadv_bla_free
===============

.. c:function:: void batadv_bla_free(struct batadv_priv *bat_priv)

    free all bla structures

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_bla_free.description`:

Description
-----------

for softinterface free or module unload

.. _`batadv_bla_loopdetect_check`:

batadv_bla_loopdetect_check
===========================

.. c:function:: bool batadv_bla_loopdetect_check(struct batadv_priv *bat_priv, struct sk_buff *skb, struct batadv_hard_iface *primary_if, unsigned short vid)

    check and handle a detected loop

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the packet to check

    :param struct batadv_hard_iface \*primary_if:
        interface where the request came on

    :param unsigned short vid:
        the VLAN ID of the frame

.. _`batadv_bla_loopdetect_check.description`:

Description
-----------

Checks if this packet is a loop detect frame which has been sent by us,
throw an uevent and log the event if that is the case.

.. _`batadv_bla_loopdetect_check.return`:

Return
------

true if it is a loop detect frame which is to be dropped, false
otherwise.

.. _`batadv_bla_rx`:

batadv_bla_rx
=============

.. c:function:: bool batadv_bla_rx(struct batadv_priv *bat_priv, struct sk_buff *skb, unsigned short vid, bool is_bcast)

    check packets coming from the mesh.

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the frame to be checked

    :param unsigned short vid:
        the VLAN ID of the frame

    :param bool is_bcast:
        the packet came in a broadcast packet type.

.. _`batadv_bla_rx.batadv_bla_rx-avoidance-checks-if`:

batadv_bla_rx avoidance checks if
---------------------------------

\* we have to race for a claim
\* if the frame is allowed on the LAN

in these cases, the skb is further handled by this function

.. _`batadv_bla_rx.return`:

Return
------

true if handled, otherwise it returns false and the caller shall
further process the skb.

.. _`batadv_bla_tx`:

batadv_bla_tx
=============

.. c:function:: bool batadv_bla_tx(struct batadv_priv *bat_priv, struct sk_buff *skb, unsigned short vid)

    check packets going into the mesh

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the frame to be checked

    :param unsigned short vid:
        the VLAN ID of the frame

.. _`batadv_bla_tx.batadv_bla_tx-checks-if`:

batadv_bla_tx checks if
-----------------------

\* a claim was received which has to be processed
\* the frame is allowed on the mesh

in these cases, the skb is further handled by this function.

This call might reallocate skb data.

.. _`batadv_bla_tx.return`:

Return
------

true if handled, otherwise it returns false and the caller shall
further process the skb.

.. _`batadv_bla_claim_table_seq_print_text`:

batadv_bla_claim_table_seq_print_text
=====================================

.. c:function:: int batadv_bla_claim_table_seq_print_text(struct seq_file *seq, void *offset)

    print the claim table in a seq file

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_bla_claim_table_seq_print_text.return`:

Return
------

always 0

.. _`batadv_bla_claim_dump_entry`:

batadv_bla_claim_dump_entry
===========================

.. c:function:: int batadv_bla_claim_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hard_iface *primary_if, struct batadv_bla_claim *claim)

    dump one entry of the claim table to a netlink socket

    :param struct sk_buff \*msg:
        buffer for the message

    :param u32 portid:
        netlink port

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_hard_iface \*primary_if:
        primary interface

    :param struct batadv_bla_claim \*claim:
        entry to dump

.. _`batadv_bla_claim_dump_entry.return`:

Return
------

0 or error code.

.. _`batadv_bla_claim_dump_bucket`:

batadv_bla_claim_dump_bucket
============================

.. c:function:: int batadv_bla_claim_dump_bucket(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hard_iface *primary_if, struct hlist_head *head, int *idx_skip)

    dump one bucket of the claim table to a netlink socket

    :param struct sk_buff \*msg:
        buffer for the message

    :param u32 portid:
        netlink port

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_hard_iface \*primary_if:
        primary interface

    :param struct hlist_head \*head:
        bucket to dump

    :param int \*idx_skip:
        How many entries to skip

.. _`batadv_bla_claim_dump_bucket.return`:

Return
------

always 0.

.. _`batadv_bla_claim_dump`:

batadv_bla_claim_dump
=====================

.. c:function:: int batadv_bla_claim_dump(struct sk_buff *msg, struct netlink_callback *cb)

    dump claim table to a netlink socket

    :param struct sk_buff \*msg:
        buffer for the message

    :param struct netlink_callback \*cb:
        callback structure containing arguments

.. _`batadv_bla_claim_dump.return`:

Return
------

message length.

.. _`batadv_bla_backbone_table_seq_print_text`:

batadv_bla_backbone_table_seq_print_text
========================================

.. c:function:: int batadv_bla_backbone_table_seq_print_text(struct seq_file *seq, void *offset)

    print the backbone table in a seq file

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_bla_backbone_table_seq_print_text.return`:

Return
------

always 0

.. _`batadv_bla_backbone_dump_entry`:

batadv_bla_backbone_dump_entry
==============================

.. c:function:: int batadv_bla_backbone_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hard_iface *primary_if, struct batadv_bla_backbone_gw *backbone_gw)

    dump one entry of the backbone table to a netlink socket

    :param struct sk_buff \*msg:
        buffer for the message

    :param u32 portid:
        netlink port

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_hard_iface \*primary_if:
        primary interface

    :param struct batadv_bla_backbone_gw \*backbone_gw:
        entry to dump

.. _`batadv_bla_backbone_dump_entry.return`:

Return
------

0 or error code.

.. _`batadv_bla_backbone_dump_bucket`:

batadv_bla_backbone_dump_bucket
===============================

.. c:function:: int batadv_bla_backbone_dump_bucket(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hard_iface *primary_if, struct hlist_head *head, int *idx_skip)

    dump one bucket of the backbone table to a netlink socket

    :param struct sk_buff \*msg:
        buffer for the message

    :param u32 portid:
        netlink port

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_hard_iface \*primary_if:
        primary interface

    :param struct hlist_head \*head:
        bucket to dump

    :param int \*idx_skip:
        How many entries to skip

.. _`batadv_bla_backbone_dump_bucket.return`:

Return
------

always 0.

.. _`batadv_bla_backbone_dump`:

batadv_bla_backbone_dump
========================

.. c:function:: int batadv_bla_backbone_dump(struct sk_buff *msg, struct netlink_callback *cb)

    dump backbone table to a netlink socket

    :param struct sk_buff \*msg:
        buffer for the message

    :param struct netlink_callback \*cb:
        callback structure containing arguments

.. _`batadv_bla_backbone_dump.return`:

Return
------

message length.

.. _`batadv_bla_check_claim`:

batadv_bla_check_claim
======================

.. c:function:: bool batadv_bla_check_claim(struct batadv_priv *bat_priv, u8 *addr, unsigned short vid)

    check if address is claimed

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 \*addr:
        mac address of which the claim status is checked

    :param unsigned short vid:
        the VLAN ID

.. _`batadv_bla_check_claim.description`:

Description
-----------

addr is checked if this address is claimed by the local device itself.

.. _`batadv_bla_check_claim.return`:

Return
------

true if bla is disabled or the mac is claimed by the device,
false if the device addr is already claimed by another gateway

.. This file was automatic generated / don't edit.

