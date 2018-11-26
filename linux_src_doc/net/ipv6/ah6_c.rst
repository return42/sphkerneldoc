.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/ah6.c

.. _`ipv6_rearrange_destopt`:

ipv6_rearrange_destopt
======================

.. c:function:: void ipv6_rearrange_destopt(struct ipv6hdr *iph, struct ipv6_opt_hdr *destopt)

    rearrange IPv6 destination options header

    :param iph:
        IPv6 header
    :type iph: struct ipv6hdr \*

    :param destopt:
        destionation options header
    :type destopt: struct ipv6_opt_hdr \*

.. _`ipv6_rearrange_rthdr`:

ipv6_rearrange_rthdr
====================

.. c:function:: void ipv6_rearrange_rthdr(struct ipv6hdr *iph, struct ipv6_rt_hdr *rthdr)

    rearrange IPv6 routing header

    :param iph:
        IPv6 header
    :type iph: struct ipv6hdr \*

    :param rthdr:
        routing header
    :type rthdr: struct ipv6_rt_hdr \*

.. _`ipv6_rearrange_rthdr.description`:

Description
-----------

Rearrange the destination address in \ ``iph``\  and the addresses in \ ``rthdr``\ 
so that they appear in the order they will at the final destination.
See Appendix A2 of RFC 2402 for details.

.. This file was automatic generated / don't edit.

