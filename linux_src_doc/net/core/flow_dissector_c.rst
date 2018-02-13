.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/flow_dissector.c

.. _`skb_flow_get_be16`:

skb_flow_get_be16
=================

.. c:function:: __be16 skb_flow_get_be16(const struct sk_buff *skb, int poff, void *data, int hlen)

    extract be16 entity

    :param const struct sk_buff \*skb:
        sk_buff to extract from

    :param int poff:
        offset to extract at

    :param void \*data:
        raw buffer pointer to the packet

    :param int hlen:
        packet header length

.. _`skb_flow_get_be16.description`:

Description
-----------

The function will try to retrieve a be32 entity at
offset poff

.. _`__skb_flow_get_ports`:

__skb_flow_get_ports
====================

.. c:function:: __be32 __skb_flow_get_ports(const struct sk_buff *skb, int thoff, u8 ip_proto, void *data, int hlen)

    extract the upper layer ports and return them

    :param const struct sk_buff \*skb:
        sk_buff to extract the ports from

    :param int thoff:
        transport header offset

    :param u8 ip_proto:
        protocol for which to get port offset

    :param void \*data:
        raw buffer pointer to the packet, if NULL use skb->data

    :param int hlen:
        packet header length, if \ ``data``\  is NULL use skb_headlen(skb)

.. _`__skb_flow_get_ports.description`:

Description
-----------

The function will try to retrieve the ports at offset thoff + poff where poff
is the protocol port offset returned from proto_ports_offset

.. _`__skb_flow_dissect_batadv`:

__skb_flow_dissect_batadv
=========================

.. c:function:: enum flow_dissect_ret __skb_flow_dissect_batadv(const struct sk_buff *skb, struct flow_dissector_key_control *key_control, void *data, __be16 *p_proto, int *p_nhoff, int hlen, unsigned int flags)

    dissect batman-adv header

    :param const struct sk_buff \*skb:
        sk_buff to with the batman-adv header

    :param struct flow_dissector_key_control \*key_control:
        flow dissectors control key

    :param void \*data:
        raw buffer pointer to the packet, if NULL use skb->data

    :param __be16 \*p_proto:
        pointer used to update the protocol to process next

    :param int \*p_nhoff:
        pointer used to update inner network header offset

    :param int hlen:
        packet header length

    :param unsigned int flags:
        any combination of FLOW_DISSECTOR_F\_\*

.. _`__skb_flow_dissect_batadv.description`:

Description
-----------

ETH_P_BATMAN packets are tried to be dissected. Only
\ :c:type:`struct batadv_unicast <batadv_unicast>`\  packets are actually processed because they contain an
inner ethernet header and are usually followed by actual network header. This
allows the flow dissector to continue processing the packet.

.. _`__skb_flow_dissect_batadv.return`:

Return
------

FLOW_DISSECT_RET_PROTO_AGAIN when \ :c:type:`struct batadv_unicast <batadv_unicast>`\  was found,
FLOW_DISSECT_RET_OUT_GOOD when dissector should stop after encapsulation,
otherwise FLOW_DISSECT_RET_OUT_BAD

.. _`__skb_flow_dissect`:

__skb_flow_dissect
==================

.. c:function:: bool __skb_flow_dissect(const struct sk_buff *skb, struct flow_dissector *flow_dissector, void *target_container, void *data, __be16 proto, int nhoff, int hlen, unsigned int flags)

    extract the flow_keys struct and return it

    :param const struct sk_buff \*skb:
        sk_buff to extract the flow from, can be NULL if the rest are specified

    :param struct flow_dissector \*flow_dissector:
        list of keys to dissect

    :param void \*target_container:
        target structure to put dissected values into

    :param void \*data:
        raw buffer pointer to the packet, if NULL use skb->data

    :param __be16 proto:
        protocol for which to get the flow, if \ ``data``\  is NULL use skb->protocol

    :param int nhoff:
        network header offset, if \ ``data``\  is NULL use skb_network_offset(skb)

    :param int hlen:
        packet header length, if \ ``data``\  is NULL use skb_headlen(skb)

    :param unsigned int flags:
        *undescribed*

.. _`__skb_flow_dissect.description`:

Description
-----------

The function will try to retrieve individual keys into target specified
by flow_dissector from either the skbuff or a raw buffer specified by the
rest parameters.

Caller must take care of zeroing target container memory.

.. _`__skb_get_hash`:

__skb_get_hash
==============

.. c:function:: void __skb_get_hash(struct sk_buff *skb)

    calculate a flow hash

    :param struct sk_buff \*skb:
        sk_buff to calculate flow hash from

.. _`__skb_get_hash.description`:

Description
-----------

This function calculates a flow hash based on src/dst addresses
and src/dst port numbers.  Sets hash in skb to non-zero hash value
on success, zero indicates no valid hash.  Also, sets l4_hash in skb
if hash is a canonical 4-tuple hash over transport ports.

.. _`skb_get_poff`:

skb_get_poff
============

.. c:function:: u32 skb_get_poff(const struct sk_buff *skb)

    get the offset to the payload

    :param const struct sk_buff \*skb:
        sk_buff to get the payload offset from

.. _`skb_get_poff.description`:

Description
-----------

The function will get the offset to the payload as far as it could
be dissected.  The main user is currently BPF, so that we can dynamically
truncate packets without needing to push actual payload to the user
space and can analyze headers only, instead.

.. This file was automatic generated / don't edit.

