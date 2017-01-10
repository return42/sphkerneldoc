.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/flow.c

.. _`parse_vlan_tag`:

parse_vlan_tag
==============

.. c:function:: int parse_vlan_tag(struct sk_buff *skb, struct vlan_head *key_vh)

    Returns ERROR on memory error. Returns 0 if it encounters a non-vlan or incomplete packet. Returns 1 after successfully parsing vlan tag.

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct vlan_head \*key_vh:
        *undescribed*

.. _`key_extract`:

key_extract
===========

.. c:function:: int key_extract(struct sk_buff *skb, struct sw_flow_key *key)

    extracts a flow key from an Ethernet frame.

    :param struct sk_buff \*skb:
        sk_buff that contains the frame, with skb->data pointing to the
        Ethernet header

    :param struct sw_flow_key \*key:
        output flow key

.. _`key_extract.description`:

Description
-----------

The caller must ensure that skb->len >= ETH_HLEN.

Returns 0 if successful, otherwise a negative errno value.

Initializes \ ``skb``\  header fields as follows:

- skb->mac_header: the L2 header.

- skb->network_header: just past the L2 header, or just past the
VLAN header, to the first byte of the L2 payload.

- skb->transport_header: If key->eth.type is ETH_P_IP or ETH_P_IPV6
on output, then just past the IP header, if one is present and
of a correct length, otherwise the same as skb->network_header.
For other key->eth.type values it is left untouched.

- skb->protocol: the type of the data starting at skb->network_header.
Equals to key->eth.type.

.. This file was automatic generated / don't edit.

