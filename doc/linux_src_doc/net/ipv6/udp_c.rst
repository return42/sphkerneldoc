.. -*- coding: utf-8; mode: rst -*-

=====
udp.c
=====


.. _`udp6_hwcsum_outgoing`:

udp6_hwcsum_outgoing
====================

.. c:function:: void udp6_hwcsum_outgoing (struct sock *sk, struct sk_buff *skb, const struct in6_addr *saddr, const struct in6_addr *daddr, int len)

    handle outgoing HW checksumming

    :param struct sock \*sk:
        socket we are sending on

    :param struct sk_buff \*skb:
        sk_buff containing the filled-in UDP header
        (checksum field must be zeroed out)

    :param const struct in6_addr \*saddr:

        *undescribed*

    :param const struct in6_addr \*daddr:

        *undescribed*

    :param int len:

        *undescribed*

