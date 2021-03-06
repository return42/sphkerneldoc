.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/udp.h

.. _`udp_skb_cb`:

struct udp_skb_cb
=================

.. c:type:: struct udp_skb_cb

    UDP(-Lite) private variables

.. _`udp_skb_cb.definition`:

Definition
----------

.. code-block:: c

    struct udp_skb_cb {
        union {
            struct inet_skb_parm h4;
    #if IS_ENABLED(CONFIG_IPV6)
            struct inet6_skb_parm h6;
    #endif
        } header;
        __u16 cscov;
        __u8 partial_cov;
    }

.. _`udp_skb_cb.members`:

Members
-------

header
    private variables used by IPv4/IPv6

cscov
    checksum coverage length (UDP-Lite only)

partial_cov
    if set indicates partial csum coverage

.. _`udp_hslot`:

struct udp_hslot
================

.. c:type:: struct udp_hslot

    UDP hash slot

.. _`udp_hslot.definition`:

Definition
----------

.. code-block:: c

    struct udp_hslot {
        struct hlist_head head;
        int count;
        spinlock_t lock;
    }

.. _`udp_hslot.members`:

Members
-------

head
    head of list of sockets

count
    number of sockets in 'head' list

lock
    spinlock protecting changes to head/count

.. _`udp_table`:

struct udp_table
================

.. c:type:: struct udp_table

    UDP table

.. _`udp_table.definition`:

Definition
----------

.. code-block:: c

    struct udp_table {
        struct udp_hslot *hash;
        struct udp_hslot *hash2;
        unsigned int mask;
        unsigned int log;
    }

.. _`udp_table.members`:

Members
-------

hash
    hash table, sockets are hashed on (local port)

hash2
    hash table, sockets are hashed on (local port, local address)

mask
    number of slots in hash tables, minus 1

log
    log2(number of slots in hash table)

.. _`udp_csum_outgoing`:

udp_csum_outgoing
=================

.. c:function:: __wsum udp_csum_outgoing(struct sock *sk, struct sk_buff *skb)

    compute UDPv4/v6 checksum over fragments

    :param sk:
        socket we are writing to
    :type sk: struct sock \*

    :param skb:
        sk_buff containing the filled-in UDP header
        (checksum field must be zeroed out)
    :type skb: struct sk_buff \*

.. This file was automatic generated / don't edit.

