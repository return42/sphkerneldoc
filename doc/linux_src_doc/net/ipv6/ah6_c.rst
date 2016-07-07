.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/ah6.c

.. _`ipv6_rearrange_destopt`:

ipv6_rearrange_destopt
======================

.. c:function:: void ipv6_rearrange_destopt(struct ipv6hdr *iph, struct ipv6_opt_hdr *destopt)

    rearrange IPv6 destination options header

    :param struct ipv6hdr \*iph:
        IPv6 header

    :param struct ipv6_opt_hdr \*destopt:
        destionation options header

.. _`ipv6_rearrange_rthdr`:

ipv6_rearrange_rthdr
====================

.. c:function:: void ipv6_rearrange_rthdr(struct ipv6hdr *iph, struct ipv6_rt_hdr *rthdr)

    rearrange IPv6 routing header

    :param struct ipv6hdr \*iph:
        IPv6 header

    :param struct ipv6_rt_hdr \*rthdr:
        routing header

.. _`ipv6_rearrange_rthdr.description`:

Description
-----------

Rearrange the destination address in \ ``iph``\  and the addresses in \ ``rthdr``\ 
so that they appear in the order they will at the final destination.
See Appendix A2 of RFC 2402 for details.

.. This file was automatic generated / don't edit.

