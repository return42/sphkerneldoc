.. -*- coding: utf-8; mode: rst -*-

=============
mcast_snoop.c
=============


.. _`ipv6_mc_check_mld`:

ipv6_mc_check_mld
=================

.. c:function:: int ipv6_mc_check_mld (struct sk_buff *skb, struct sk_buff **skb_trimmed)

    checks whether this is a sane MLD packet

    :param struct sk_buff \*skb:
        the skb to validate

    :param struct sk_buff \*\*skb_trimmed:
        to store an skb pointer trimmed to IPv6 packet tail (optional)



.. _`ipv6_mc_check_mld.description`:

Description
-----------

Checks whether an IPv6 packet is a valid MLD packet. If so sets
skb transport header accordingly and returns zero.

-EINVAL: A broken packet was detected, i.e. it violates some internet
standard

-ENOMSG: IP header validation succeeded but it is not an MLD packet.
-ENOMEM: A memory allocation failure happened.

Optionally, an skb pointer might be provided via skb_trimmed (or set it
to NULL): After parsing an MLD packet successfully it will point to
an skb which has its tail aligned to the IP packet end. This might
either be the originally provided skb or a trimmed, cloned version if
the skb frame had data beyond the IP packet. A cloned skb allows us
to leave the original skb and its full frame unchanged (which might be
desirable for layer 2 frame jugglers).

Caller needs to set the skb network header and free any returned skb if it
differs from the provided skb.

