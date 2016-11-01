.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/udp.c

.. _`udp_lib_get_port`:

udp_lib_get_port
================

.. c:function:: int udp_lib_get_port(struct sock *sk, unsigned short snum, int (*saddr_comp)(const struct sock *sk1, const struct sock *sk2, bool match_wildcard), unsigned int hash2_nulladdr)

    UDP/-Lite port lookup for IPv4 and IPv6

    :param struct sock \*sk:
        socket struct in question

    :param unsigned short snum:
        port number to look up

    :param int (\*saddr_comp)(const struct sock \*sk1, const struct sock \*sk2, bool match_wildcard):
        AF-dependent comparison of bound local IP addresses

    :param unsigned int hash2_nulladdr:
        AF-dependent hash value in secondary hash chains,
        with NULL address

.. _`udp4_hwcsum`:

udp4_hwcsum
===========

.. c:function:: void udp4_hwcsum(struct sk_buff *skb, __be32 src, __be32 dst)

    handle outgoing HW checksumming

    :param struct sk_buff \*skb:
        sk_buff containing the filled-in UDP header
        (checksum field must be zeroed out)

    :param __be32 src:
        source IP address

    :param __be32 dst:
        destination IP address

.. _`first_packet_length`:

first_packet_length
===================

.. c:function:: int first_packet_length(struct sock *sk)

    return length of first packet in receive queue

    :param struct sock \*sk:
        socket

.. _`first_packet_length.description`:

Description
-----------

Drops all bad checksum frames, until a valid one is found.
Returns the length of found skb, or -1 if none is found.

.. _`udp_poll`:

udp_poll
========

.. c:function:: unsigned int udp_poll(struct file *file, struct socket *sock, poll_table *wait)

    wait for a UDP event. \ ``file``\  - file struct \ ``sock``\  - socket \ ``wait``\  - poll table

    :param struct file \*file:
        *undescribed*

    :param struct socket \*sock:
        *undescribed*

    :param poll_table \*wait:
        *undescribed*

.. _`udp_poll.description`:

Description
-----------

This is same as datagram poll, except for the special case of
blocking sockets. If application is using a blocking fd
and a packet with checksum error is in the queue;
then it could get return from select indicating data available
but then block when reading it. Add special case code
to work around these arguably broken applications.

.. This file was automatic generated / don't edit.

