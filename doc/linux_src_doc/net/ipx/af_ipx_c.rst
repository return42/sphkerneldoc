.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipx/af_ipx.c

.. _`ipxitf_pprop`:

ipxitf_pprop
============

.. c:function:: int ipxitf_pprop(struct ipx_interface *intrfc, struct sk_buff *skb)

    Process packet propagation IPX packet type 0x14, used for NetBIOS broadcasts

    :param struct ipx_interface \*intrfc:
        IPX interface receiving this packet

    :param struct sk_buff \*skb:
        Received packet

.. _`ipxitf_pprop.checks-if-packet-is-valid`:

Checks if packet is valid
-------------------------

if its more than \ ``IPX_MAX_PPROP_HOPS``\  hops or if it
is smaller than a IPX header + the room for \ ``IPX_MAX_PPROP_HOPS``\  hops we drop
it, not even processing it locally, if it has exact \ ``IPX_MAX_PPROP_HOPS``\  we
don't broadcast it, but process it locally. See chapter 5 of Novell's "IPX
RIP and SAP Router Specification", Part Number 107-000029-001.

If it is valid, check if we have pprop broadcasting enabled by the user,
if not, just return zero for local processing.

If it is enabled check the packet and don't broadcast it if we have already
seen this packet.

.. _`ipxitf_pprop.broadcast`:

Broadcast
---------

send it to the interfaces that aren't on the packet visited nets
array, just after the IPX header.

Returns -EINVAL for invalid packets, so that the calling function drops
the packet without local processing. 0 if packet is to be locally processed.

.. This file was automatic generated / don't edit.

