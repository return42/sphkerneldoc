.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/ip6_gre.c

.. _`ip6gre_tnl_addr_conflict`:

ip6gre_tnl_addr_conflict
========================

.. c:function:: bool ip6gre_tnl_addr_conflict(const struct ip6_tnl *t, const struct ipv6hdr *hdr)

    compare packet addresses to tunnel's own

    :param t:
        the outgoing tunnel device
    :type t: const struct ip6_tnl \*

    :param hdr:
        IPv6 header from the incoming packet
    :type hdr: const struct ipv6hdr \*

.. _`ip6gre_tnl_addr_conflict.description`:

Description
-----------

Avoid trivial tunneling loop by checking that tunnel exit-point
doesn't match source of incoming packet.

.. _`ip6gre_tnl_addr_conflict.return`:

Return
------

1 if conflict,
0 else

.. This file was automatic generated / don't edit.

