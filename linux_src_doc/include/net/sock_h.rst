.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/sock.h

.. _`sock_common`:

struct sock_common
==================

.. c:type:: struct sock_common

    minimal network layer representation of sockets

.. _`sock_common.definition`:

Definition
----------

.. code-block:: c

    struct sock_common {
        union {
            __addrpair skc_addrpair;
            struct {
                __be32 skc_daddr;
                __be32 skc_rcv_saddr;
            } ;
        } ;
        union {
            unsigned int skc_hash;
            __u16 skc_u16hashes[2];
        } ;
        union {
            __portpair skc_portpair;
            struct {
                __be16 skc_dport;
                __u16 skc_num;
            } ;
        } ;
        unsigned short skc_family;
        volatile unsigned char skc_state;
        unsigned char skc_reuse:4;
        unsigned char skc_reuseport:1;
        unsigned char skc_ipv6only:1;
        unsigned char skc_net_refcnt:1;
        int skc_bound_dev_if;
        union {
            struct hlist_node skc_bind_node;
            struct hlist_node skc_portaddr_node;
        } ;
        struct proto *skc_prot;
        possible_net_t skc_net;
    #if IS_ENABLED(CONFIG_IPV6)
        struct in6_addr skc_v6_daddr;
        struct in6_addr skc_v6_rcv_saddr;
    #endif
        atomic64_t skc_cookie;
        union {
            unsigned long skc_flags;
            struct sock *skc_listener;
            struct inet_timewait_death_row *skc_tw_dr;
        } ;
        union {
            struct hlist_node skc_node;
            struct hlist_nulls_node skc_nulls_node;
        } ;
        unsigned short skc_tx_queue_mapping;
    #ifdef CONFIG_XPS
        unsigned short skc_rx_queue_mapping;
    #endif
        union {
            int skc_incoming_cpu;
            u32 skc_rcv_wnd;
            u32 skc_tw_rcv_nxt;
        } ;
        refcount_t skc_refcnt;
    }

.. _`sock_common.members`:

Members
-------

{unnamed_union}
    anonymous

skc_addrpair
    *undescribed*

{unnamed_struct}
    anonymous

skc_daddr
    Foreign IPv4 addr

skc_rcv_saddr
    Bound local IPv4 addr

{unnamed_union}
    anonymous

skc_hash
    hash value used with various protocol lookup tables

skc_u16hashes
    two u16 hash values used by UDP lookup tables

{unnamed_union}
    anonymous

skc_portpair
    *undescribed*

{unnamed_struct}
    anonymous

skc_dport
    placeholder for inet_dport/tw_dport

skc_num
    placeholder for inet_num/tw_num

skc_family
    network address family

skc_state
    Connection state

skc_reuse
    \ ``SO_REUSEADDR``\  setting

skc_reuseport
    \ ``SO_REUSEPORT``\  setting

skc_ipv6only
    *undescribed*

skc_net_refcnt
    *undescribed*

skc_bound_dev_if
    bound device index if != 0

{unnamed_union}
    anonymous

skc_bind_node
    bind hash linkage for various protocol lookup tables

skc_portaddr_node
    second hash linkage for UDP/UDP-Lite protocol

skc_prot
    protocol handlers inside a network family

skc_net
    reference to the network namespace of this socket

skc_v6_daddr
    *undescribed*

skc_v6_rcv_saddr
    *undescribed*

skc_cookie
    *undescribed*

{unnamed_union}
    anonymous

skc_flags
    place holder for sk_flags
    \ ``SO_LINGER``\  (l_onoff), \ ``SO_BROADCAST``\ , \ ``SO_KEEPALIVE``\ ,
    \ ``SO_OOBINLINE``\  settings, \ ``SO_TIMESTAMPING``\  settings

skc_listener
    *undescribed*

skc_tw_dr
    *undescribed*

{unnamed_union}
    anonymous

skc_node
    main hash linkage for various protocol lookup tables

skc_nulls_node
    main hash linkage for TCP/UDP/UDP-Lite protocol

skc_tx_queue_mapping
    tx queue number for this connection

skc_rx_queue_mapping
    rx queue number for this connection

{unnamed_union}
    anonymous

skc_incoming_cpu
    record/match cpu processing incoming packets

skc_rcv_wnd
    *undescribed*

skc_tw_rcv_nxt
    *undescribed*

skc_refcnt
    reference count

.. _`sock_common.description`:

Description
-----------

     This is the minimal network layer representation of sockets, the header
     for struct sock and struct inet_timewait_sock.

.. _`sock`:

struct sock
===========

.. c:type:: struct sock

    network layer representation of sockets

.. _`sock.definition`:

Definition
----------

.. code-block:: c

    struct sock {
        struct sock_common __sk_common;
    #define sk_node __sk_common.skc_node
    #define sk_nulls_node __sk_common.skc_nulls_node
    #define sk_refcnt __sk_common.skc_refcnt
    #define sk_tx_queue_mapping __sk_common.skc_tx_queue_mapping
    #ifdef CONFIG_XPS
    #define sk_rx_queue_mapping __sk_common.skc_rx_queue_mapping
    #endif
    #define sk_dontcopy_begin __sk_common.skc_dontcopy_begin
    #define sk_dontcopy_end __sk_common.skc_dontcopy_end
    #define sk_hash __sk_common.skc_hash
    #define sk_portpair __sk_common.skc_portpair
    #define sk_num __sk_common.skc_num
    #define sk_dport __sk_common.skc_dport
    #define sk_addrpair __sk_common.skc_addrpair
    #define sk_daddr __sk_common.skc_daddr
    #define sk_rcv_saddr __sk_common.skc_rcv_saddr
    #define sk_family __sk_common.skc_family
    #define sk_state __sk_common.skc_state
    #define sk_reuse __sk_common.skc_reuse
    #define sk_reuseport __sk_common.skc_reuseport
    #define sk_ipv6only __sk_common.skc_ipv6only
    #define sk_net_refcnt __sk_common.skc_net_refcnt
    #define sk_bound_dev_if __sk_common.skc_bound_dev_if
    #define sk_bind_node __sk_common.skc_bind_node
    #define sk_prot __sk_common.skc_prot
    #define sk_net __sk_common.skc_net
    #define sk_v6_daddr __sk_common.skc_v6_daddr
    #define sk_v6_rcv_saddr __sk_common.skc_v6_rcv_saddr
    #define sk_cookie __sk_common.skc_cookie
    #define sk_incoming_cpu __sk_common.skc_incoming_cpu
    #define sk_flags __sk_common.skc_flags
    #define sk_rxhash __sk_common.skc_rxhash
        socket_lock_t sk_lock;
        atomic_t sk_drops;
        int sk_rcvlowat;
        struct sk_buff_head sk_error_queue;
        struct sk_buff_head sk_receive_queue;
        struct {
            atomic_t rmem_alloc;
            int len;
            struct sk_buff *head;
            struct sk_buff *tail;
        } sk_backlog;
    #define sk_rmem_alloc sk_backlog.rmem_alloc
        int sk_forward_alloc;
    #ifdef CONFIG_NET_RX_BUSY_POLL
        unsigned int sk_ll_usec;
        unsigned int sk_napi_id;
    #endif
        int sk_rcvbuf;
        struct sk_filter __rcu *sk_filter;
        union {
            struct socket_wq __rcu *sk_wq;
            struct socket_wq *sk_wq_raw;
        } ;
    #ifdef CONFIG_XFRM
        struct xfrm_policy __rcu *sk_policy[2];
    #endif
        struct dst_entry *sk_rx_dst;
        struct dst_entry __rcu *sk_dst_cache;
        atomic_t sk_omem_alloc;
        int sk_sndbuf;
        int sk_wmem_queued;
        refcount_t sk_wmem_alloc;
        unsigned long sk_tsq_flags;
        union {
            struct sk_buff *sk_send_head;
            struct rb_root tcp_rtx_queue;
        } ;
        struct sk_buff_head sk_write_queue;
        __s32 sk_peek_off;
        int sk_write_pending;
        __u32 sk_dst_pending_confirm;
        u32 sk_pacing_status;
        long sk_sndtimeo;
        struct timer_list sk_timer;
        __u32 sk_priority;
        __u32 sk_mark;
        unsigned long sk_pacing_rate;
        unsigned long sk_max_pacing_rate;
        struct page_frag sk_frag;
        netdev_features_t sk_route_caps;
        netdev_features_t sk_route_nocaps;
        netdev_features_t sk_route_forced_caps;
        int sk_gso_type;
        unsigned int sk_gso_max_size;
        gfp_t sk_allocation;
        __u32 sk_txhash;
        unsigned int __sk_flags_offset[0];
    #ifdef __BIG_ENDIAN_BITFIELD
    #define SK_FL_PROTO_SHIFT 16
    #define SK_FL_PROTO_MASK 0x00ff0000
    #define SK_FL_TYPE_SHIFT 0
    #define SK_FL_TYPE_MASK 0x0000ffff
    #else
    #define SK_FL_PROTO_SHIFT 8
    #define SK_FL_PROTO_MASK 0x0000ff00
    #define SK_FL_TYPE_SHIFT 16
    #define SK_FL_TYPE_MASK 0xffff0000
    #endif
        unsigned int sk_padding : 1,sk_kern_sock : 1,sk_no_check_tx : 1,sk_no_check_rx : 1,sk_userlocks : 4,sk_protocol : 8, sk_type : 16;
    #define SK_PROTOCOL_MAX U8_MAX
        u16 sk_gso_max_segs;
        u8 sk_pacing_shift;
        unsigned long sk_lingertime;
        struct proto *sk_prot_creator;
        rwlock_t sk_callback_lock;
        int sk_err, sk_err_soft;
        u32 sk_ack_backlog;
        u32 sk_max_ack_backlog;
        kuid_t sk_uid;
        struct pid *sk_peer_pid;
        const struct cred *sk_peer_cred;
        long sk_rcvtimeo;
        ktime_t sk_stamp;
        u16 sk_tsflags;
        u8 sk_shutdown;
        u32 sk_tskey;
        atomic_t sk_zckey;
        u8 sk_clockid;
        u8 sk_txtime_deadline_mode : 1,sk_txtime_report_errors : 1, sk_txtime_unused : 6;
        struct socket *sk_socket;
        void *sk_user_data;
    #ifdef CONFIG_SECURITY
        void *sk_security;
    #endif
        struct sock_cgroup_data sk_cgrp_data;
        struct mem_cgroup *sk_memcg;
        void (*sk_state_change)(struct sock *sk);
        void (*sk_data_ready)(struct sock *sk);
        void (*sk_write_space)(struct sock *sk);
        void (*sk_error_report)(struct sock *sk);
        int (*sk_backlog_rcv)(struct sock *sk, struct sk_buff *skb);
    #ifdef CONFIG_SOCK_VALIDATE_XMIT
        struct sk_buff* (*sk_validate_xmit_skb)(struct sock *sk,struct net_device *dev, struct sk_buff *skb);
    #endif
        void (*sk_destruct)(struct sock *sk);
        struct sock_reuseport __rcu *sk_reuseport_cb;
        struct rcu_head sk_rcu;
    }

.. _`sock.members`:

Members
-------

__sk_common
    shared layout with inet_timewait_sock

sk_lock
    synchronizer

sk_drops
    raw/udp drops counter

sk_rcvlowat
    \ ``SO_RCVLOWAT``\  setting

sk_error_queue
    rarely used

sk_receive_queue
    incoming packets

sk_backlog
    always used with the per-socket spinlock held

sk_forward_alloc
    space allocated forward

sk_ll_usec
    usecs to busypoll when there is no data

sk_napi_id
    id of the last napi context to receive data for sk

sk_rcvbuf
    size of receive buffer in bytes

sk_filter
    socket filtering instructions

{unnamed_union}
    anonymous

sk_wq
    sock wait queue and async head

sk_wq_raw
    *undescribed*

sk_policy
    flow policy

sk_rx_dst
    receive input route used by early demux

sk_dst_cache
    destination cache

sk_omem_alloc
    "o" is "option" or "other"

sk_sndbuf
    size of send buffer in bytes

sk_wmem_queued
    persistent queue size

sk_wmem_alloc
    transmit queue bytes committed

sk_tsq_flags
    TCP Small Queues flags

{unnamed_union}
    anonymous

sk_send_head
    front of stuff to transmit

tcp_rtx_queue
    *undescribed*

sk_write_queue
    Packet sending queue

sk_peek_off
    current peek_offset value

sk_write_pending
    a write to stream socket waits to start

sk_dst_pending_confirm
    need to confirm neighbour

sk_pacing_status
    Pacing status (requested, handled by sch_fq)

sk_sndtimeo
    \ ``SO_SNDTIMEO``\  setting

sk_timer
    sock cleanup timer

sk_priority
    \ ``SO_PRIORITY``\  setting

sk_mark
    generic packet mark

sk_pacing_rate
    Pacing rate (if supported by transport/packet scheduler)

sk_max_pacing_rate
    Maximum pacing rate (%SO_MAX_PACING_RATE)

sk_frag
    cached page frag

sk_route_caps
    route capabilities (e.g. \ ``NETIF_F_TSO``\ )

sk_route_nocaps
    forbidden route capabilities (e.g NETIF_F_GSO_MASK)

sk_route_forced_caps
    *undescribed*

sk_gso_type
    GSO type (e.g. \ ``SKB_GSO_TCPV4``\ )

sk_gso_max_size
    Maximum GSO segment size to build

sk_allocation
    allocation mode

sk_txhash
    computed flow hash for use on transmit

__sk_flags_offset
    empty field used to determine location of bitfield

sk_padding
    unused element for alignment

sk_kern_sock
    True if sock is using kernel lock classes

sk_no_check_tx
    \ ``SO_NO_CHECK``\  setting, set checksum in TX packets

sk_no_check_rx
    allow zero checksum in RX packets

sk_userlocks
    \ ``SO_SNDBUF``\  and \ ``SO_RCVBUF``\  settings

sk_protocol
    which protocol this socket belongs in this network family

sk_type
    socket type (%SOCK_STREAM, etc)

sk_gso_max_segs
    Maximum number of GSO segments

sk_pacing_shift
    scaling factor for TCP Small Queues

sk_lingertime
    \ ``SO_LINGER``\  l_linger setting

sk_prot_creator
    sk_prot of original sock creator (see ipv6_setsockopt,
    IPV6_ADDRFORM for instance)

sk_callback_lock
    used with the callbacks in the end of this struct

sk_err
    last error

sk_err_soft
    errors that don't cause failure but are the cause of a
    persistent failure not just 'timed out'

sk_ack_backlog
    current listen backlog

sk_max_ack_backlog
    listen backlog set in \ :c:func:`listen`\ 

sk_uid
    user id of owner

sk_peer_pid
    \ :c:type:`struct pid <pid>`\  for this socket's peer

sk_peer_cred
    \ ``SO_PEERCRED``\  setting

sk_rcvtimeo
    \ ``SO_RCVTIMEO``\  setting

sk_stamp
    time stamp of last packet received

sk_tsflags
    SO_TIMESTAMPING socket options

sk_shutdown
    mask of \ ``SEND_SHUTDOWN``\  and/or \ ``RCV_SHUTDOWN``\ 

sk_tskey
    counter to disambiguate concurrent tstamp requests

sk_zckey
    counter to order MSG_ZEROCOPY notifications

sk_clockid
    clockid used by time-based scheduling (SO_TXTIME)

sk_txtime_deadline_mode
    set deadline mode for SO_TXTIME

sk_txtime_report_errors
    *undescribed*

sk_txtime_unused
    unused txtime flags

sk_socket
    Identd and reporting IO signals

sk_user_data
    RPC layer private data

sk_security
    used by security modules

sk_cgrp_data
    cgroup data for this cgroup

sk_memcg
    this socket's memory cgroup association

sk_state_change
    callback to indicate change in the state of the sock

sk_data_ready
    callback to indicate there is data to be processed

sk_write_space
    callback to indicate there is bf sending space available

sk_error_report
    callback to indicate errors (e.g. \ ``MSG_ERRQUEUE``\ )

sk_backlog_rcv
    callback to process the backlog

sk_validate_xmit_skb
    *undescribed*

sk_destruct
    called at sock freeing time, i.e. when all refcnt == 0

sk_reuseport_cb
    reuseport group container

sk_rcu
    used during RCU grace period

.. _`sk_for_each_entry_offset_rcu`:

sk_for_each_entry_offset_rcu
============================

.. c:function::  sk_for_each_entry_offset_rcu( tpos,  pos,  head,  offset)

    iterate over a list at a given struct offset

    :param tpos:
        the type * to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct hlist_node <hlist_node>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param offset:
        offset of hlist_node within the struct.
    :type offset: 

.. _`unlock_sock_fast`:

unlock_sock_fast
================

.. c:function:: void unlock_sock_fast(struct sock *sk, bool slow)

    complement of lock_sock_fast

    :param sk:
        socket
    :type sk: struct sock \*

    :param slow:
        slow mode
    :type slow: bool

.. _`unlock_sock_fast.description`:

Description
-----------

fast unlock socket for user context.
If slow mode is on, we call regular \ :c:func:`release_sock`\ 

.. _`sk_wmem_alloc_get`:

sk_wmem_alloc_get
=================

.. c:function:: int sk_wmem_alloc_get(const struct sock *sk)

    returns write allocations

    :param sk:
        socket
    :type sk: const struct sock \*

.. _`sk_wmem_alloc_get.description`:

Description
-----------

Returns sk_wmem_alloc minus initial offset of one

.. _`sk_rmem_alloc_get`:

sk_rmem_alloc_get
=================

.. c:function:: int sk_rmem_alloc_get(const struct sock *sk)

    returns read allocations

    :param sk:
        socket
    :type sk: const struct sock \*

.. _`sk_rmem_alloc_get.description`:

Description
-----------

Returns sk_rmem_alloc

.. _`sk_has_allocations`:

sk_has_allocations
==================

.. c:function:: bool sk_has_allocations(const struct sock *sk)

    check if allocations are outstanding

    :param sk:
        socket
    :type sk: const struct sock \*

.. _`sk_has_allocations.description`:

Description
-----------

Returns true if socket has write or read allocations

.. _`skwq_has_sleeper`:

skwq_has_sleeper
================

.. c:function:: bool skwq_has_sleeper(struct socket_wq *wq)

    check if there are any waiting processes

    :param wq:
        struct socket_wq
    :type wq: struct socket_wq \*

.. _`skwq_has_sleeper.description`:

Description
-----------

Returns true if socket_wq has waiting processes

The purpose of the skwq_has_sleeper and sock_poll_wait is to wrap the memory
barrier call. They were added due to the race found within the tcp code.

Consider following tcp code paths::

  CPU1                CPU2
  sys_select          receive packet
  ...                 ...
  __add_wait_queue    update tp->rcv_nxt
  ...                 ...
  tp->rcv_nxt check   sock_def_readable
  ...                 {
  schedule               rcu_read_lock();
                         wq = rcu_dereference(sk->sk_wq);
                         if (wq && waitqueue_active(&wq->wait))
                             wake_up_interruptible(&wq->wait)
                         ...
                      }

The race for tcp fires when the __add_wait_queue changes done by CPU1 stay
in its cache, and so does the tp->rcv_nxt update on CPU2 side.  The CPU1
could then endup calling schedule and sleep forever if there are no more
data on the socket.

.. _`sock_poll_wait`:

sock_poll_wait
==============

.. c:function:: void sock_poll_wait(struct file *filp, struct socket *sock, poll_table *p)

    place memory barrier behind the poll_wait call.

    :param filp:
        file
    :type filp: struct file \*

    :param sock:
        socket to wait on
    :type sock: struct socket \*

    :param p:
        poll_table
    :type p: poll_table \*

.. _`sock_poll_wait.description`:

Description
-----------

See the comments in the wq_has_sleeper function.

Do not derive sock from filp->private_data here. An SMC socket establishes
an internal TCP socket that is used in the fallback case. All socket
operations on the SMC socket are then forwarded to the TCP socket. In case of
poll, the filp->private_data pointer references the SMC socket because the
TCP socket has no file assigned.

.. _`sk_page_frag`:

sk_page_frag
============

.. c:function:: struct page_frag *sk_page_frag(struct sock *sk)

    return an appropriate page_frag

    :param sk:
        socket
    :type sk: struct sock \*

.. _`sk_page_frag.description`:

Description
-----------

If socket allocation mode allows current thread to sleep, it means its
safe to use the per task page_frag instead of the per socket one.

.. _`sock_tx_timestamp`:

sock_tx_timestamp
=================

.. c:function:: void sock_tx_timestamp(const struct sock *sk, __u16 tsflags, __u8 *tx_flags)

    checks whether the outgoing packet is to be time stamped

    :param sk:
        socket sending this packet
    :type sk: const struct sock \*

    :param tsflags:
        timestamping flags to use
    :type tsflags: __u16

    :param tx_flags:
        completed with instructions for time stamping
    :type tx_flags: __u8 \*

.. _`sock_tx_timestamp.note`:

Note
----

callers should take care of initial ``*tx_flags`` value (usually 0)

.. _`sk_eat_skb`:

sk_eat_skb
==========

.. c:function:: void sk_eat_skb(struct sock *sk, struct sk_buff *skb)

    Release a skb if it is no longer needed

    :param sk:
        socket to eat this skb from
    :type sk: struct sock \*

    :param skb:
        socket buffer to eat
    :type skb: struct sk_buff \*

.. _`sk_eat_skb.description`:

Description
-----------

This routine must be called with interrupts disabled or with the socket
locked so that the sk_buff queue operation is ok.

.. This file was automatic generated / don't edit.

