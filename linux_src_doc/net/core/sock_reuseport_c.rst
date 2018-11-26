.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/sock_reuseport.c

.. _`reuseport_add_sock`:

reuseport_add_sock
==================

.. c:function:: int reuseport_add_sock(struct sock *sk, struct sock *sk2, bool bind_inany)

    Add a socket to the reuseport group of another.

    :param sk:
        New socket to add to the group.
    :type sk: struct sock \*

    :param sk2:
        Socket belonging to the existing reuseport group.
        May return ENOMEM and not add socket to group under memory pressure.
    :type sk2: struct sock \*

    :param bind_inany:
        *undescribed*
    :type bind_inany: bool

.. _`reuseport_select_sock`:

reuseport_select_sock
=====================

.. c:function:: struct sock *reuseport_select_sock(struct sock *sk, u32 hash, struct sk_buff *skb, int hdr_len)

    Select a socket from an SO_REUSEPORT group.

    :param sk:
        First socket in the group.
    :type sk: struct sock \*

    :param hash:
        When no BPF filter is available, use this hash to select.
    :type hash: u32

    :param skb:
        skb to run through BPF filter.
    :type skb: struct sk_buff \*

    :param hdr_len:
        BPF filter expects skb data pointer at payload data.  If
        the skb does not yet point at the payload, this parameter represents
        how far the pointer needs to advance to reach the payload.
        Returns a socket that should receive the packet (or NULL on error).
    :type hdr_len: int

.. This file was automatic generated / don't edit.

