.. -*- coding: utf-8; mode: rst -*-

===========
inet_frag.h
===========


.. _`inet_frag_queue`:

struct inet_frag_queue
======================

.. c:type:: inet_frag_queue

    fragment queue


.. _`inet_frag_queue.definition`:

Definition
----------

.. code-block:: c

  struct inet_frag_queue {
    spinlock_t lock;
    struct timer_list timer;
    struct hlist_node list;
    atomic_t refcnt;
    struct sk_buff * fragments;
    struct sk_buff * fragments_tail;
    ktime_t stamp;
    int len;
    int meat;
    __u8 flags;
    u16 max_size;
    struct netns_frags * net;
    struct hlist_node list_evictor;
  };


.. _`inet_frag_queue.members`:

Members
-------

:``lock``:
    spinlock protecting the queue

:``timer``:
    queue expiration timer

:``list``:
    hash bucket list

:``refcnt``:
    reference count of the queue

:``fragments``:
    received fragments head

:``fragments_tail``:
    received fragments tail

:``stamp``:
    timestamp of the last received fragment

:``len``:
    total length of the original datagram

:``meat``:
    length of received fragments so far

:``flags``:
    fragment queue flags

:``max_size``:
    maximum received fragment size

:``net``:
    namespace that this frag belongs to

:``list_evictor``:
    list of queues to forcefully evict (e.g. due to low memory)


