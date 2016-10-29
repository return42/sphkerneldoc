.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/flow.c

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

Initializes \ ``skb``\  header pointers as follows:

- skb->mac_header: the Ethernet header.

- skb->network_header: just past the Ethernet header, or just past the
VLAN header, to the first byte of the Ethernet payload.

- skb->transport_header: If key->eth.type is ETH_P_IP or ETH_P_IPV6
on output, then just past the IP header, if one is present and
of a correct length, otherwise the same as skb->network_header.
For other key->eth.type values it is left untouched.

.. This file was automatic generated / don't edit.
