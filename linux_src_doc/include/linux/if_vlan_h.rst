.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/if_vlan.h

.. _`vlan_ethhdr`:

struct vlan_ethhdr
==================

.. c:type:: struct vlan_ethhdr

    vlan ethernet header (ethhdr + vlan_hdr)

.. _`vlan_ethhdr.definition`:

Definition
----------

.. code-block:: c

    struct vlan_ethhdr {
        unsigned char h_dest[ETH_ALEN];
        unsigned char h_source[ETH_ALEN];
        __be16 h_vlan_proto;
        __be16 h_vlan_TCI;
        __be16 h_vlan_encapsulated_proto;
    }

.. _`vlan_ethhdr.members`:

Members
-------

h_dest
    destination ethernet address

h_source
    source ethernet address

h_vlan_proto
    ethernet protocol

h_vlan_TCI
    priority and VLAN ID

h_vlan_encapsulated_proto
    packet type ID or len

.. _`vlan_pcpu_stats`:

struct vlan_pcpu_stats
======================

.. c:type:: struct vlan_pcpu_stats

    VLAN percpu rx/tx stats

.. _`vlan_pcpu_stats.definition`:

Definition
----------

.. code-block:: c

    struct vlan_pcpu_stats {
        u64 rx_packets;
        u64 rx_bytes;
        u64 rx_multicast;
        u64 tx_packets;
        u64 tx_bytes;
        struct u64_stats_sync syncp;
        u32 rx_errors;
        u32 tx_dropped;
    }

.. _`vlan_pcpu_stats.members`:

Members
-------

rx_packets
    number of received packets

rx_bytes
    number of received bytes

rx_multicast
    number of received multicast packets

tx_packets
    number of transmitted packets

tx_bytes
    number of transmitted bytes

syncp
    synchronization point for 64bit counters

rx_errors
    number of rx errors

tx_dropped
    number of tx drops

.. _`vlan_priority_tci_mapping`:

struct vlan_priority_tci_mapping
================================

.. c:type:: struct vlan_priority_tci_mapping

    vlan egress priority mappings

.. _`vlan_priority_tci_mapping.definition`:

Definition
----------

.. code-block:: c

    struct vlan_priority_tci_mapping {
        u32 priority;
        u16 vlan_qos;
        struct vlan_priority_tci_mapping *next;
    }

.. _`vlan_priority_tci_mapping.members`:

Members
-------

priority
    skb priority

vlan_qos
    vlan priority: (skb->priority << 13) & 0xE000

next
    pointer to next struct

.. _`vlan_dev_priv`:

struct vlan_dev_priv
====================

.. c:type:: struct vlan_dev_priv

    VLAN private device data

.. _`vlan_dev_priv.definition`:

Definition
----------

.. code-block:: c

    struct vlan_dev_priv {
        unsigned int nr_ingress_mappings;
        u32 ingress_priority_map[8];
        unsigned int nr_egress_mappings;
        struct vlan_priority_tci_mapping  *egress_priority_map[16];
        __be16 vlan_proto;
        u16 vlan_id;
        u16 flags;
        struct net_device *real_dev;
        unsigned char real_dev_addr[ETH_ALEN];
        struct proc_dir_entry *dent;
        struct vlan_pcpu_stats __percpu *vlan_pcpu_stats;
    #ifdef CONFIG_NET_POLL_CONTROLLER
        struct netpoll *netpoll;
    #endif
        unsigned int nest_level;
    }

.. _`vlan_dev_priv.members`:

Members
-------

nr_ingress_mappings
    number of ingress priority mappings

ingress_priority_map
    ingress priority mappings

nr_egress_mappings
    number of egress priority mappings

egress_priority_map
    hash of egress priority mappings

vlan_proto
    VLAN encapsulation protocol

vlan_id
    VLAN identifier

flags
    device flags

real_dev
    underlying netdevice

real_dev_addr
    address of underlying netdevice

dent
    proc dir entry

vlan_pcpu_stats
    ptr to percpu rx stats

netpoll
    *undescribed*

nest_level
    *undescribed*

.. _`eth_type_vlan`:

eth_type_vlan
=============

.. c:function:: bool eth_type_vlan(__be16 ethertype)

    check for valid vlan ether type.

    :param __be16 ethertype:
        ether type to check

.. _`eth_type_vlan.description`:

Description
-----------

Returns true if the ether type is a vlan ether type.

.. _`__vlan_insert_tag`:

__vlan_insert_tag
=================

.. c:function:: int __vlan_insert_tag(struct sk_buff *skb, __be16 vlan_proto, u16 vlan_tci)

    regular VLAN tag inserting

    :param struct sk_buff \*skb:
        skbuff to tag

    :param __be16 vlan_proto:
        VLAN encapsulation protocol

    :param u16 vlan_tci:
        VLAN TCI to insert

.. _`__vlan_insert_tag.description`:

Description
-----------

Inserts the VLAN tag into \ ``skb``\  as part of the payload
Returns error if skb_cow_head failes.

Does not change skb->protocol so this function can be used during receive.

.. _`vlan_insert_tag`:

vlan_insert_tag
===============

.. c:function:: struct sk_buff *vlan_insert_tag(struct sk_buff *skb, __be16 vlan_proto, u16 vlan_tci)

    regular VLAN tag inserting

    :param struct sk_buff \*skb:
        skbuff to tag

    :param __be16 vlan_proto:
        VLAN encapsulation protocol

    :param u16 vlan_tci:
        VLAN TCI to insert

.. _`vlan_insert_tag.description`:

Description
-----------

Inserts the VLAN tag into \ ``skb``\  as part of the payload
Returns a VLAN tagged skb. If a new skb is created, \ ``skb``\  is freed.

Following the \ :c:func:`skb_unshare`\  example, in case of error, the calling function
doesn't have to worry about freeing the original skb.

Does not change skb->protocol so this function can be used during receive.

.. _`vlan_insert_tag_set_proto`:

vlan_insert_tag_set_proto
=========================

.. c:function:: struct sk_buff *vlan_insert_tag_set_proto(struct sk_buff *skb, __be16 vlan_proto, u16 vlan_tci)

    regular VLAN tag inserting

    :param struct sk_buff \*skb:
        skbuff to tag

    :param __be16 vlan_proto:
        VLAN encapsulation protocol

    :param u16 vlan_tci:
        VLAN TCI to insert

.. _`vlan_insert_tag_set_proto.description`:

Description
-----------

Inserts the VLAN tag into \ ``skb``\  as part of the payload
Returns a VLAN tagged skb. If a new skb is created, \ ``skb``\  is freed.

Following the \ :c:func:`skb_unshare`\  example, in case of error, the calling function
doesn't have to worry about freeing the original skb.

.. _`__vlan_hwaccel_put_tag`:

__vlan_hwaccel_put_tag
======================

.. c:function:: void __vlan_hwaccel_put_tag(struct sk_buff *skb, __be16 vlan_proto, u16 vlan_tci)

    hardware accelerated VLAN inserting

    :param struct sk_buff \*skb:
        skbuff to tag

    :param __be16 vlan_proto:
        VLAN encapsulation protocol

    :param u16 vlan_tci:
        VLAN TCI to insert

.. _`__vlan_hwaccel_put_tag.description`:

Description
-----------

Puts the VLAN TCI in \ ``skb``\ ->vlan_tci and lets the device do the rest

.. _`__vlan_get_tag`:

__vlan_get_tag
==============

.. c:function:: int __vlan_get_tag(const struct sk_buff *skb, u16 *vlan_tci)

    get the VLAN ID that is part of the payload

    :param const struct sk_buff \*skb:
        skbuff to query

    :param u16 \*vlan_tci:
        buffer to store value

.. _`__vlan_get_tag.description`:

Description
-----------

Returns error if the skb is not of VLAN type

.. _`__vlan_hwaccel_get_tag`:

__vlan_hwaccel_get_tag
======================

.. c:function:: int __vlan_hwaccel_get_tag(const struct sk_buff *skb, u16 *vlan_tci)

    get the VLAN ID that is in \ ``skb``\ ->cb[]

    :param const struct sk_buff \*skb:
        skbuff to query

    :param u16 \*vlan_tci:
        buffer to store value

.. _`__vlan_hwaccel_get_tag.description`:

Description
-----------

Returns error if \ ``skb``\ ->vlan_tci is not set correctly

.. _`vlan_get_tag`:

vlan_get_tag
============

.. c:function:: int vlan_get_tag(const struct sk_buff *skb, u16 *vlan_tci)

    get the VLAN ID from the skb

    :param const struct sk_buff \*skb:
        skbuff to query

    :param u16 \*vlan_tci:
        buffer to store value

.. _`vlan_get_tag.description`:

Description
-----------

Returns error if the skb is not VLAN tagged

.. _`__vlan_get_protocol`:

__vlan_get_protocol
===================

.. c:function:: __be16 __vlan_get_protocol(struct sk_buff *skb, __be16 type, int *depth)

    get protocol EtherType.

    :param struct sk_buff \*skb:
        skbuff to query

    :param __be16 type:
        first vlan protocol

    :param int \*depth:
        buffer to store length of eth and vlan tags in bytes

.. _`__vlan_get_protocol.description`:

Description
-----------

Returns the EtherType of the packet, regardless of whether it is
vlan encapsulated (normal or hardware accelerated) or not.

.. _`vlan_get_protocol`:

vlan_get_protocol
=================

.. c:function:: __be16 vlan_get_protocol(struct sk_buff *skb)

    get protocol EtherType.

    :param struct sk_buff \*skb:
        skbuff to query

.. _`vlan_get_protocol.description`:

Description
-----------

Returns the EtherType of the packet, regardless of whether it is
vlan encapsulated (normal or hardware accelerated) or not.

.. _`skb_vlan_tagged`:

skb_vlan_tagged
===============

.. c:function:: bool skb_vlan_tagged(const struct sk_buff *skb)

    check if skb is vlan tagged.

    :param const struct sk_buff \*skb:
        skbuff to query

.. _`skb_vlan_tagged.description`:

Description
-----------

Returns true if the skb is tagged, regardless of whether it is hardware
accelerated or not.

.. _`skb_vlan_tagged_multi`:

skb_vlan_tagged_multi
=====================

.. c:function:: bool skb_vlan_tagged_multi(const struct sk_buff *skb)

    check if skb is vlan tagged with multiple headers.

    :param const struct sk_buff \*skb:
        skbuff to query

.. _`skb_vlan_tagged_multi.description`:

Description
-----------

Returns true if the skb is tagged with multiple vlan headers, regardless
of whether it is hardware accelerated or not.

.. _`vlan_features_check`:

vlan_features_check
===================

.. c:function:: netdev_features_t vlan_features_check(const struct sk_buff *skb, netdev_features_t features)

    drop unsafe features for skb with multiple tags.

    :param const struct sk_buff \*skb:
        skbuff to query

    :param netdev_features_t features:
        features to be checked

.. _`vlan_features_check.description`:

Description
-----------

Returns features without unsafe ones if the skb has multiple tags.

.. _`compare_vlan_header`:

compare_vlan_header
===================

.. c:function:: unsigned long compare_vlan_header(const struct vlan_hdr *h1, const struct vlan_hdr *h2)

    Compare two vlan headers

    :param const struct vlan_hdr \*h1:
        Pointer to vlan header

    :param const struct vlan_hdr \*h2:
        Pointer to vlan header

.. _`compare_vlan_header.description`:

Description
-----------

Compare two vlan headers, returns 0 if equal.

Please note that alignment of h1 & h2 are only guaranteed to be 16 bits.

.. This file was automatic generated / don't edit.

