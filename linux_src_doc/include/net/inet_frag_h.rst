.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/inet_frag.h

.. _`inet_frag_queue`:

struct inet_frag_queue
======================

.. c:type:: struct inet_frag_queue

    fragment queue

.. _`inet_frag_queue.definition`:

Definition
----------

.. code-block:: c

    struct inet_frag_queue {
        struct rhash_head node;
        union {
            struct frag_v4_compare_key v4;
            struct frag_v6_compare_key v6;
        } key;
        struct timer_list timer;
        spinlock_t lock;
        refcount_t refcnt;
        struct sk_buff *fragments;
        struct sk_buff *fragments_tail;
        ktime_t stamp;
        int len;
        int meat;
        __u8 flags;
        u16 max_size;
        struct netns_frags *net;
        struct rcu_head rcu;
    }

.. _`inet_frag_queue.members`:

Members
-------

node
    rhash node

key
    keys identifying this frag.

timer
    queue expiration timer

lock
    spinlock protecting this frag

refcnt
    reference count of the queue

fragments
    received fragments head

fragments_tail
    received fragments tail

stamp
    timestamp of the last received fragment

len
    total length of the original datagram

meat
    length of received fragments so far

flags
    fragment queue flags

max_size
    maximum received fragment size

net
    namespace that this frag belongs to

rcu
    rcu head for freeing deferall

.. This file was automatic generated / don't edit.

