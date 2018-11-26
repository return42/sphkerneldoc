.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/udp.c

.. _`udp_lib_get_port`:

udp_lib_get_port
================

.. c:function:: int udp_lib_get_port(struct sock *sk, unsigned short snum, unsigned int hash2_nulladdr)

    UDP/-Lite port lookup for IPv4 and IPv6

    :param sk:
        socket struct in question
    :type sk: struct sock \*

    :param snum:
        port number to look up
    :type snum: unsigned short

    :param hash2_nulladdr:
        AF-dependent hash value in secondary hash chains,
        with NULL address
    :type hash2_nulladdr: unsigned int

.. _`udp4_hwcsum`:

udp4_hwcsum
===========

.. c:function:: void udp4_hwcsum(struct sk_buff *skb, __be32 src, __be32 dst)

    handle outgoing HW checksumming

    :param skb:
        sk_buff containing the filled-in UDP header
        (checksum field must be zeroed out)
    :type skb: struct sk_buff \*

    :param src:
        source IP address
    :type src: __be32

    :param dst:
        destination IP address
    :type dst: __be32

.. _`first_packet_length`:

first_packet_length
===================

.. c:function:: int first_packet_length(struct sock *sk)

    return length of first packet in receive queue

    :param sk:
        socket
    :type sk: struct sock \*

.. _`first_packet_length.description`:

Description
-----------

Drops all bad checksum frames, until a valid one is found.
Returns the length of found skb, or -1 if none is found.

.. _`udp_poll`:

udp_poll
========

.. c:function:: __poll_t udp_poll(struct file *file, struct socket *sock, poll_table *wait)

    wait for a UDP event. \ ``file``\  - file struct \ ``sock``\  - socket \ ``wait``\  - poll table

    :param file:
        *undescribed*
    :type file: struct file \*

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param wait:
        *undescribed*
    :type wait: poll_table \*

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

