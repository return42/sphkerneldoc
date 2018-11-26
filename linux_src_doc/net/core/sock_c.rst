.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/sock.c

.. _`sk_ns_capable`:

sk_ns_capable
=============

.. c:function:: bool sk_ns_capable(const struct sock *sk, struct user_namespace *user_ns, int cap)

    General socket capability test

    :param sk:
        Socket to use a capability on or through
    :type sk: const struct sock \*

    :param user_ns:
        The user namespace of the capability to use
    :type user_ns: struct user_namespace \*

    :param cap:
        The capability to use
    :type cap: int

.. _`sk_ns_capable.description`:

Description
-----------

Test to see if the opener of the socket had when the socket was
created and the current process has the capability \ ``cap``\  in the user
namespace \ ``user_ns``\ .

.. _`sk_capable`:

sk_capable
==========

.. c:function:: bool sk_capable(const struct sock *sk, int cap)

    Socket global capability test

    :param sk:
        Socket to use a capability on or through
    :type sk: const struct sock \*

    :param cap:
        The global capability to use
    :type cap: int

.. _`sk_capable.description`:

Description
-----------

Test to see if the opener of the socket had when the socket was
created and the current process has the capability \ ``cap``\  in all user
namespaces.

.. _`sk_net_capable`:

sk_net_capable
==============

.. c:function:: bool sk_net_capable(const struct sock *sk, int cap)

    Network namespace socket capability test

    :param sk:
        Socket to use a capability on or through
    :type sk: const struct sock \*

    :param cap:
        The capability to use
    :type cap: int

.. _`sk_net_capable.description`:

Description
-----------

Test to see if the opener of the socket had when the socket was created
and the current process has the capability \ ``cap``\  over the network namespace
the socket is a member of.

.. _`sk_set_memalloc`:

sk_set_memalloc
===============

.. c:function:: void sk_set_memalloc(struct sock *sk)

    sets \ ``SOCK_MEMALLOC``\ 

    :param sk:
        socket to set it on
    :type sk: struct sock \*

.. _`sk_set_memalloc.description`:

Description
-----------

Set \ ``SOCK_MEMALLOC``\  on a socket for access to emergency reserves.
It's the responsibility of the admin to adjust min_free_kbytes
to meet the requirements

.. _`sk_alloc`:

sk_alloc
========

.. c:function:: struct sock *sk_alloc(struct net *net, int family, gfp_t priority, struct proto *prot, int kern)

    All socket objects are allocated here

    :param net:
        the applicable net namespace
    :type net: struct net \*

    :param family:
        protocol family
    :type family: int

    :param priority:
        for allocation (%GFP_KERNEL, \ ``GFP_ATOMIC``\ , etc)
    :type priority: gfp_t

    :param prot:
        struct proto associated with this new sock instance
    :type prot: struct proto \*

    :param kern:
        is this to be a kernel socket?
    :type kern: int

.. _`sk_clone_lock`:

sk_clone_lock
=============

.. c:function:: struct sock *sk_clone_lock(const struct sock *sk, const gfp_t priority)

    clone a socket, and lock its clone

    :param sk:
        the socket to clone
    :type sk: const struct sock \*

    :param priority:
        for allocation (%GFP_KERNEL, \ ``GFP_ATOMIC``\ , etc)
    :type priority: const gfp_t

.. _`sk_clone_lock.description`:

Description
-----------

     Caller must unlock socket even in error path (bh_unlock_sock(newsk))

.. _`skb_page_frag_refill`:

skb_page_frag_refill
====================

.. c:function:: bool skb_page_frag_refill(unsigned int sz, struct page_frag *pfrag, gfp_t gfp)

    check that a page_frag contains enough room

    :param sz:
        minimum size of the fragment we want to get
    :type sz: unsigned int

    :param pfrag:
        pointer to page_frag
    :type pfrag: struct page_frag \*

    :param gfp:
        priority for memory allocation
    :type gfp: gfp_t

.. _`skb_page_frag_refill.note`:

Note
----

While this allocator tries to use high order pages, there is
no guarantee that allocations succeed. Therefore, \ ``sz``\  MUST be
less or equal than PAGE_SIZE.

.. _`sk_wait_data`:

sk_wait_data
============

.. c:function:: int sk_wait_data(struct sock *sk, long *timeo, const struct sk_buff *skb)

    wait for data to arrive at sk_receive_queue

    :param sk:
        sock to wait on
    :type sk: struct sock \*

    :param timeo:
        for how long
    :type timeo: long \*

    :param skb:
        last skb seen on sk_receive_queue
    :type skb: const struct sk_buff \*

.. _`sk_wait_data.description`:

Description
-----------

Now socket state including sk->sk_err is changed only under lock,
hence we may omit checks after joining wait queue.
We check receive queue before \ :c:func:`schedule`\  only as optimization;
it is very likely that \ :c:func:`release_sock`\  added new data.

.. _`__sk_mem_raise_allocated`:

__sk_mem_raise_allocated
========================

.. c:function:: int __sk_mem_raise_allocated(struct sock *sk, int size, int amt, int kind)

    increase memory_allocated

    :param sk:
        socket
    :type sk: struct sock \*

    :param size:
        memory size to allocate
    :type size: int

    :param amt:
        pages to allocate
    :type amt: int

    :param kind:
        allocation type
    :type kind: int

.. _`__sk_mem_raise_allocated.description`:

Description
-----------

     Similar to \ :c:func:`__sk_mem_schedule`\ , but does not update sk_forward_alloc

.. _`__sk_mem_schedule`:

__sk_mem_schedule
=================

.. c:function:: int __sk_mem_schedule(struct sock *sk, int size, int kind)

    increase sk_forward_alloc and memory_allocated

    :param sk:
        socket
    :type sk: struct sock \*

    :param size:
        memory size to allocate
    :type size: int

    :param kind:
        allocation type
    :type kind: int

.. _`__sk_mem_schedule.description`:

Description
-----------

     If kind is SK_MEM_SEND, it means wmem allocation. Otherwise it means
     rmem allocation. This function assumes that protocols which have
     memory_pressure use sk_wmem_queued as write buffer accounting.

.. _`__sk_mem_reduce_allocated`:

__sk_mem_reduce_allocated
=========================

.. c:function:: void __sk_mem_reduce_allocated(struct sock *sk, int amount)

    reclaim memory_allocated

    :param sk:
        socket
    :type sk: struct sock \*

    :param amount:
        number of quanta
    :type amount: int

.. _`__sk_mem_reduce_allocated.description`:

Description
-----------

     Similar to \ :c:func:`__sk_mem_reclaim`\ , but does not update sk_forward_alloc

.. _`__sk_mem_reclaim`:

__sk_mem_reclaim
================

.. c:function:: void __sk_mem_reclaim(struct sock *sk, int amount)

    reclaim sk_forward_alloc and memory_allocated

    :param sk:
        socket
    :type sk: struct sock \*

    :param amount:
        number of bytes (rounded down to a SK_MEM_QUANTUM multiple)
    :type amount: int

.. _`lock_sock_fast`:

lock_sock_fast
==============

.. c:function:: bool lock_sock_fast(struct sock *sk)

    fast version of lock_sock

    :param sk:
        socket
    :type sk: struct sock \*

.. _`lock_sock_fast.description`:

Description
-----------

This version should be used for very small section, where process wont block

.. _`lock_sock_fast.return-false-if-fast-path-is-taken`:

return false if fast path is taken
----------------------------------


  sk_lock.slock locked, owned = 0, BH disabled

.. _`lock_sock_fast.return-true-if-slow-path-is-taken`:

return true if slow path is taken
---------------------------------


  sk_lock.slock unlocked, owned = 1, BH enabled

.. This file was automatic generated / don't edit.

