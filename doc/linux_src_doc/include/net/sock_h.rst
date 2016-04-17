.. -*- coding: utf-8; mode: rst -*-

======
sock.h
======


.. _`sock_common`:

struct sock_common
==================

.. c:type:: sock_common

    minimal network layer representation of sockets


.. _`sock_common.definition`:

Definition
----------

.. code-block:: c

  struct sock_common {
    union {unnamed_union};
  };


.. _`sock_common.members`:

Members
-------

:``{unnamed_union}``:
    anonymous




.. _`sock_common.description`:

Description
-----------

This is the minimal network layer representation of sockets, the header
for struct sock and struct inet_timewait_sock.



.. _`sock`:

struct sock
===========

.. c:type:: sock

    network layer representation of sockets


.. _`sock.definition`:

Definition
----------

.. code-block:: c

  struct sock {
    struct sock_common __sk_common;
    #define sk_node			__sk_common.skc_node
    #define sk_nulls_node		__sk_common.skc_nulls_node
    #define sk_refcnt		__sk_common.skc_refcnt
    #define sk_tx_queue_mapping	__sk_common.skc_tx_queue_mapping
    #define sk_dontcopy_begin	__sk_common.skc_dontcopy_begin
    #define sk_dontcopy_end		__sk_common.skc_dontcopy_end
    #define sk_hash			__sk_common.skc_hash
    #define sk_portpair		__sk_common.skc_portpair
    #define sk_num			__sk_common.skc_num
    #define sk_dport		__sk_common.skc_dport
    #define sk_addrpair		__sk_common.skc_addrpair
    #define sk_daddr		__sk_common.skc_daddr
    #define sk_rcv_saddr		__sk_common.skc_rcv_saddr
    #define sk_family		__sk_common.skc_family
    #define sk_state		__sk_common.skc_state
    #define sk_reuse		__sk_common.skc_reuse
    #define sk_reuseport		__sk_common.skc_reuseport
    #define sk_ipv6only		__sk_common.skc_ipv6only
    #define sk_net_refcnt		__sk_common.skc_net_refcnt
    #define sk_bound_dev_if		__sk_common.skc_bound_dev_if
    #define sk_bind_node		__sk_common.skc_bind_node
    #define sk_prot			__sk_common.skc_prot
    #define sk_net			__sk_common.skc_net
    #define sk_v6_daddr		__sk_common.skc_v6_daddr
    #define sk_v6_rcv_saddr	__sk_common.skc_v6_rcv_saddr
    #define sk_cookie		__sk_common.skc_cookie
    #define sk_incoming_cpu		__sk_common.skc_incoming_cpu
    #define sk_flags		__sk_common.skc_flags
    #define sk_rxhash		__sk_common.skc_rxhash
    socket_lock_t sk_lock;
    struct sk_buff_head sk_receive_queue;
    struct {unnamed_struct};
    #ifdef CONFIG_XFRM
    struct xfrm_policy __rcu * sk_policy[2];
    #endif
    struct dst_entry * sk_rx_dst;
    struct dst_entry __rcu * sk_dst_cache;
    atomic_t sk_wmem_alloc;
    atomic_t sk_omem_alloc;
    int sk_sndbuf;
    struct sk_buff_head sk_write_queue;
    unsigned int sk_shutdown:2;
    unsigned int sk_no_check_tx:1;
    unsigned int sk_no_check_rx:1;
    unsigned int sk_userlocks:4;
    unsigned int sk_protocol:8;
    unsigned int sk_type:16;
    #define SK_PROTOCOL_MAX U8_MAX
    int sk_wmem_queued;
    gfp_t sk_allocation;
    u32 sk_pacing_rate;
    u32 sk_max_pacing_rate;
    netdev_features_t sk_route_caps;
    netdev_features_t sk_route_nocaps;
    int sk_gso_type;
    unsigned int sk_gso_max_size;
    u16 sk_gso_max_segs;
    int sk_rcvlowat;
    unsigned long sk_lingertime;
    struct sk_buff_head sk_error_queue;
    struct proto * sk_prot_creator;
    rwlock_t sk_callback_lock;
    int sk_err;
    int sk_err_soft;
    u32 sk_ack_backlog;
    u32 sk_max_ack_backlog;
    __u32 sk_priority;
    __u32 sk_mark;
    struct pid * sk_peer_pid;
    const struct cred * sk_peer_cred;
    long sk_rcvtimeo;
    long sk_sndtimeo;
    struct timer_list sk_timer;
    ktime_t sk_stamp;
    u16 sk_tsflags;
    u32 sk_tskey;
    struct socket * sk_socket;
    void * sk_user_data;
    struct page_frag sk_frag;
    struct sk_buff * sk_send_head;
    __s32 sk_peek_off;
    int sk_write_pending;
    #ifdef CONFIG_SECURITY
    void * sk_security;
    #endif
    struct sock_cgroup_data sk_cgrp_data;
    struct mem_cgroup * sk_memcg;
    void (* sk_state_change) (struct sock *sk);
    void (* sk_data_ready) (struct sock *sk);
    void (* sk_write_space) (struct sock *sk);
    void (* sk_error_report) (struct sock *sk);
    int (* sk_backlog_rcv) (struct sock *sk,struct sk_buff *skb);
    void (* sk_destruct) (struct sock *sk);
    struct sock_reuseport __rcu * sk_reuseport_cb;
  };


.. _`sock.members`:

Members
-------

:``__sk_common``:
    shared layout with inet_timewait_sock

:``sk_lock``:
    synchronizer

:``sk_receive_queue``:
    incoming packets

:``{unnamed_struct}``:
    anonymous

:``sk_policy[2]``:
    flow policy

:``sk_rx_dst``:
    receive input route used by early demux

:``sk_dst_cache``:
    destination cache

:``sk_wmem_alloc``:
    transmit queue bytes committed

:``sk_omem_alloc``:
    "o" is "option" or "other"

:``sk_sndbuf``:
    size of send buffer in bytes

:``sk_write_queue``:
    Packet sending queue

:``sk_shutdown``:
    mask of ``SEND_SHUTDOWN`` and/or ``RCV_SHUTDOWN``

:``sk_no_check_tx``:
    ``SO_NO_CHECK`` setting, set checksum in TX packets

:``sk_no_check_rx``:
    allow zero checksum in RX packets

:``sk_userlocks``:
    ``SO_SNDBUF`` and ``SO_RCVBUF`` settings

:``sk_protocol``:
    which protocol this socket belongs in this network family

:``sk_type``:
    socket type (\ ``SOCK_STREAM``\ , etc)

:``sk_wmem_queued``:
    persistent queue size

:``sk_allocation``:
    allocation mode

:``sk_pacing_rate``:
    Pacing rate (if supported by transport/packet scheduler)

:``sk_max_pacing_rate``:
    Maximum pacing rate (\ ``SO_MAX_PACING_RATE``\ )

:``sk_route_caps``:
    route capabilities (e.g. ``NETIF_F_TSO``\ )

:``sk_route_nocaps``:
    forbidden route capabilities (e.g NETIF_F_GSO_MASK)

:``sk_gso_type``:
    GSO type (e.g. ``SKB_GSO_TCPV4``\ )

:``sk_gso_max_size``:
    Maximum GSO segment size to build

:``sk_gso_max_segs``:
    Maximum number of GSO segments

:``sk_rcvlowat``:
    ``SO_RCVLOWAT`` setting

:``sk_lingertime``:
    ``SO_LINGER`` l_linger setting

:``sk_error_queue``:
    rarely used

:``sk_prot_creator``:
    sk_prot of original sock creator (see ipv6_setsockopt,
    IPV6_ADDRFORM for instance)

:``sk_callback_lock``:
    used with the callbacks in the end of this struct

:``sk_err``:
    last error

:``sk_err_soft``:
    errors that don't cause failure but are the cause of a
    persistent failure not just 'timed out'

:``sk_ack_backlog``:
    current listen backlog

:``sk_max_ack_backlog``:
    listen backlog set in :c:func:`listen`

:``sk_priority``:
    ``SO_PRIORITY`` setting

:``sk_mark``:
    generic packet mark

:``sk_peer_pid``:
    :c:type:`struct pid <pid>` for this socket's peer

:``sk_peer_cred``:
    ``SO_PEERCRED`` setting

:``sk_rcvtimeo``:
    ``SO_RCVTIMEO`` setting

:``sk_sndtimeo``:
    ``SO_SNDTIMEO`` setting

:``sk_timer``:
    sock cleanup timer

:``sk_stamp``:
    time stamp of last packet received

:``sk_tsflags``:
    SO_TIMESTAMPING socket options

:``sk_tskey``:
    counter to disambiguate concurrent tstamp requests

:``sk_socket``:
    Identd and reporting IO signals

:``sk_user_data``:
    RPC layer private data

:``sk_frag``:
    cached page frag

:``sk_send_head``:
    front of stuff to transmit

:``sk_peek_off``:
    current peek_offset value

:``sk_write_pending``:
    a write to stream socket waits to start

:``sk_security``:
    used by security modules

:``sk_cgrp_data``:
    cgroup data for this cgroup

:``sk_memcg``:
    this socket's memory cgroup association

:``sk_state_change``:
    callback to indicate change in the state of the sock

:``sk_data_ready``:
    callback to indicate there is data to be processed

:``sk_write_space``:
    callback to indicate there is bf sending space available

:``sk_error_report``:
    callback to indicate errors (e.g. ``MSG_ERRQUEUE``\ )

:``sk_backlog_rcv``:
    callback to process the backlog

:``sk_destruct``:
    called at sock freeing time, i.e. when all refcnt == 0

:``sk_reuseport_cb``:
    reuseport group container




.. _`sk_nulls_for_each_entry_offset`:

sk_nulls_for_each_entry_offset
==============================

.. c:function:: sk_nulls_for_each_entry_offset ( tpos,  pos,  head,  offset)

    iterate over a list at a given struct offset

    :param tpos:
        the type * to use as a loop cursor.

    :param pos:
        the :c:type:`struct hlist_node <hlist_node>` to use as a loop cursor.

    :param head:
        the head for your list.

    :param offset:
        offset of hlist_node within the struct.



.. _`unlock_sock_fast`:

unlock_sock_fast
================

.. c:function:: void unlock_sock_fast (struct sock *sk, bool slow)

    complement of lock_sock_fast

    :param struct sock \*sk:
        socket

    :param bool slow:
        slow mode



.. _`unlock_sock_fast.description`:

Description
-----------

fast unlock socket for user context.
If slow mode is on, we call regular :c:func:`release_sock`



.. _`sk_wmem_alloc_get`:

sk_wmem_alloc_get
=================

.. c:function:: int sk_wmem_alloc_get (const struct sock *sk)

    returns write allocations

    :param const struct sock \*sk:
        socket



.. _`sk_wmem_alloc_get.description`:

Description
-----------

Returns sk_wmem_alloc minus initial offset of one



.. _`sk_rmem_alloc_get`:

sk_rmem_alloc_get
=================

.. c:function:: int sk_rmem_alloc_get (const struct sock *sk)

    returns read allocations

    :param const struct sock \*sk:
        socket



.. _`sk_rmem_alloc_get.description`:

Description
-----------

Returns sk_rmem_alloc



.. _`sk_has_allocations`:

sk_has_allocations
==================

.. c:function:: bool sk_has_allocations (const struct sock *sk)

    check if allocations are outstanding

    :param const struct sock \*sk:
        socket



.. _`sk_has_allocations.description`:

Description
-----------

Returns true if socket has write or read allocations



.. _`skwq_has_sleeper`:

skwq_has_sleeper
================

.. c:function:: bool skwq_has_sleeper (struct socket_wq *wq)

    check if there are any waiting processes

    :param struct socket_wq \*wq:
        struct socket_wq



.. _`skwq_has_sleeper.description`:

Description
-----------

Returns true if socket_wq has waiting processes

The purpose of the skwq_has_sleeper and sock_poll_wait is to wrap the memory
barrier call. They were added due to the race found within the tcp code.



.. _`skwq_has_sleeper.consider-following-tcp-code-paths`:

Consider following tcp code paths
---------------------------------


CPU1                  CPU2

sys_select            receive packet
...                 ...
__add_wait_queue    update tp->rcv_nxt
...                 ...
tp->rcv_nxt check   sock_def_readable
...                 {
schedule               :c:func:`rcu_read_lock`;
wq = rcu_dereference(sk->sk_wq);
if (wq && waitqueue_active(:c:type:`struct wq <wq>`->wait))
wake_up_interruptible(:c:type:`struct wq <wq>`->wait)
...
}

The race for tcp fires when the __add_wait_queue changes done by CPU1 stay
in its cache, and so does the tp->rcv_nxt update on CPU2 side.  The CPU1
could then endup calling schedule and sleep forever if there are no more
data on the socket.



.. _`sock_poll_wait`:

sock_poll_wait
==============

.. c:function:: void sock_poll_wait (struct file *filp, wait_queue_head_t *wait_address, poll_table *p)

    place memory barrier behind the poll_wait call.

    :param struct file \*filp:
        file

    :param wait_queue_head_t \*wait_address:
        socket wait queue

    :param poll_table \*p:
        poll_table



.. _`sock_poll_wait.description`:

Description
-----------

See the comments in the wq_has_sleeper function.



.. _`sk_page_frag`:

sk_page_frag
============

.. c:function:: struct page_frag *sk_page_frag (struct sock *sk)

    return an appropriate page_frag

    :param struct sock \*sk:
        socket



.. _`sk_page_frag.description`:

Description
-----------

If socket allocation mode allows current thread to sleep, it means its
safe to use the per task page_frag instead of the per socket one.



.. _`sock_tx_timestamp`:

sock_tx_timestamp
=================

.. c:function:: void sock_tx_timestamp (const struct sock *sk, __u8 *tx_flags)

    checks whether the outgoing packet is to be time stamped

    :param const struct sock \*sk:
        socket sending this packet

    :param __u8 \*tx_flags:
        completed with instructions for time stamping



.. _`sock_tx_timestamp.note`:

Note 
-----

callers should take care of initial \*tx_flags value (usually 0)



.. _`sk_eat_skb`:

sk_eat_skb
==========

.. c:function:: void sk_eat_skb (struct sock *sk, struct sk_buff *skb)

    Release a skb if it is no longer needed

    :param struct sock \*sk:
        socket to eat this skb from

    :param struct sk_buff \*skb:
        socket buffer to eat



.. _`sk_eat_skb.description`:

Description
-----------

This routine must be called with interrupts disabled or with the socket
locked so that the sk_buff queue operation is ok.



.. _`sk_state_load`:

sk_state_load
=============

.. c:function:: int sk_state_load (const struct sock *sk)

    read sk->sk_state for lockless contexts

    :param const struct sock \*sk:
        socket pointer



.. _`sk_state_load.description`:

Description
-----------

Paired with :c:func:`sk_state_store`. Used in places we do not hold socket lock :
:c:func:`tcp_diag_get_info`, :c:func:`tcp_get_info`, :c:func:`tcp_poll`, :c:func:`get_tcp4_sock` ...



.. _`sk_state_store`:

sk_state_store
==============

.. c:function:: void sk_state_store (struct sock *sk, int newstate)

    update sk->sk_state

    :param struct sock \*sk:
        socket pointer

    :param int newstate:
        new state



.. _`sk_state_store.description`:

Description
-----------

Paired with :c:func:`sk_state_load`. Should be used in contexts where
state change might impact lockless readers.

