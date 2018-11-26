.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/udp.c

.. _`udp6_hwcsum_outgoing`:

udp6_hwcsum_outgoing
====================

.. c:function:: void udp6_hwcsum_outgoing(struct sock *sk, struct sk_buff *skb, const struct in6_addr *saddr, const struct in6_addr *daddr, int len)

    handle outgoing HW checksumming

    :param sk:
        socket we are sending on
    :type sk: struct sock \*

    :param skb:
        sk_buff containing the filled-in UDP header
        (checksum field must be zeroed out)
    :type skb: struct sk_buff \*

    :param saddr:
        *undescribed*
    :type saddr: const struct in6_addr \*

    :param daddr:
        *undescribed*
    :type daddr: const struct in6_addr \*

    :param len:
        *undescribed*
    :type len: int

.. This file was automatic generated / don't edit.

