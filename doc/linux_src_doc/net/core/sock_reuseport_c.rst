.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/sock_reuseport.c

.. _`reuseport_add_sock`:

reuseport_add_sock
==================

.. c:function:: int reuseport_add_sock(struct sock *sk, struct sock *sk2)

    Add a socket to the reuseport group of another.

    :param struct sock \*sk:
        New socket to add to the group.

    :param struct sock \*sk2:
        Socket belonging to the existing reuseport group.
        May return ENOMEM and not add socket to group under memory pressure.

.. _`reuseport_select_sock`:

reuseport_select_sock
=====================

.. c:function:: struct sock *reuseport_select_sock(struct sock *sk, u32 hash, struct sk_buff *skb, int hdr_len)

    Select a socket from an SO_REUSEPORT group.

    :param struct sock \*sk:
        First socket in the group.

    :param u32 hash:
        When no BPF filter is available, use this hash to select.

    :param struct sk_buff \*skb:
        skb to run through BPF filter.

    :param int hdr_len:
        BPF filter expects skb data pointer at payload data.  If
        the skb does not yet point at the payload, this parameter represents
        how far the pointer needs to advance to reach the payload.
        Returns a socket that should receive the packet (or NULL on error).

.. This file was automatic generated / don't edit.

