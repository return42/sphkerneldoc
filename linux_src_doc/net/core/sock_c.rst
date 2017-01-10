.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/sock.c

.. _`sk_ns_capable`:

sk_ns_capable
=============

.. c:function:: bool sk_ns_capable(const struct sock *sk, struct user_namespace *user_ns, int cap)

    General socket capability test

    :param const struct sock \*sk:
        Socket to use a capability on or through

    :param struct user_namespace \*user_ns:
        The user namespace of the capability to use

    :param int cap:
        The capability to use

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

    :param const struct sock \*sk:
        Socket to use a capability on or through

    :param int cap:
        The global capability to use

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

    :param const struct sock \*sk:
        Socket to use a capability on or through

    :param int cap:
        The capability to use

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

    :param struct sock \*sk:
        socket to set it on

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

    :param struct net \*net:
        the applicable net namespace

    :param int family:
        protocol family

    :param gfp_t priority:
        for allocation (%GFP_KERNEL, \ ``GFP_ATOMIC``\ , etc)

    :param struct proto \*prot:
        struct proto associated with this new sock instance

    :param int kern:
        is this to be a kernel socket?

.. _`sk_clone_lock`:

sk_clone_lock
=============

.. c:function:: struct sock *sk_clone_lock(const struct sock *sk, const gfp_t priority)

    clone a socket, and lock its clone

    :param const struct sock \*sk:
        the socket to clone

    :param const gfp_t priority:
        for allocation (%GFP_KERNEL, \ ``GFP_ATOMIC``\ , etc)

.. _`sk_clone_lock.description`:

Description
-----------

Caller must unlock socket even in error path (bh_unlock_sock(newsk))

.. _`skb_page_frag_refill`:

skb_page_frag_refill
====================

.. c:function:: bool skb_page_frag_refill(unsigned int sz, struct page_frag *pfrag, gfp_t gfp)

    check that a page_frag contains enough room

    :param unsigned int sz:
        minimum size of the fragment we want to get

    :param struct page_frag \*pfrag:
        pointer to page_frag

    :param gfp_t gfp:
        priority for memory allocation

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

    :param struct sock \*sk:
        sock to wait on

    :param long \*timeo:
        for how long

    :param const struct sk_buff \*skb:
        last skb seen on sk_receive_queue

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

    :param struct sock \*sk:
        socket

    :param int size:
        memory size to allocate

    :param int amt:
        pages to allocate

    :param int kind:
        allocation type

.. _`__sk_mem_raise_allocated.description`:

Description
-----------

Similar to \__sk_mem_schedule(), but does not update sk_forward_alloc

.. _`__sk_mem_schedule`:

__sk_mem_schedule
=================

.. c:function:: int __sk_mem_schedule(struct sock *sk, int size, int kind)

    increase sk_forward_alloc and memory_allocated

    :param struct sock \*sk:
        socket

    :param int size:
        memory size to allocate

    :param int kind:
        allocation type

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

    :param struct sock \*sk:
        socket

    :param int amount:
        number of quanta

.. _`__sk_mem_reduce_allocated.description`:

Description
-----------

Similar to \__sk_mem_reclaim(), but does not update sk_forward_alloc

.. _`__sk_mem_reclaim`:

__sk_mem_reclaim
================

.. c:function:: void __sk_mem_reclaim(struct sock *sk, int amount)

    reclaim sk_forward_alloc and memory_allocated

    :param struct sock \*sk:
        socket

    :param int amount:
        number of bytes (rounded down to a SK_MEM_QUANTUM multiple)

.. _`lock_sock_fast`:

lock_sock_fast
==============

.. c:function:: bool lock_sock_fast(struct sock *sk)

    fast version of lock_sock

    :param struct sock \*sk:
        socket

.. _`lock_sock_fast.description`:

Description
-----------

This version should be used for very small section, where process wont block
return false if fast path is taken
sk_lock.slock locked, owned = 0, BH disabled
return true if slow path is taken
sk_lock.slock unlocked, owned = 1, BH enabled

.. This file was automatic generated / don't edit.

