.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-sock:

===========
struct sock
===========

*man struct sock(9)*

*4.6.0-rc5*

network layer representation of sockets


Synopsis
========

.. code-block:: c

    struct sock {
      struct sock_common __sk_common;
    #define sk_node         __sk_common.skc_node
    #define sk_nulls_node       __sk_common.skc_nulls_node
    #define sk_refcnt       __sk_common.skc_refcnt
    #define sk_tx_queue_mapping __sk_common.skc_tx_queue_mapping
    #define sk_dontcopy_begin   __sk_common.skc_dontcopy_begin
    #define sk_dontcopy_end     __sk_common.skc_dontcopy_end
    #define sk_hash         __sk_common.skc_hash
    #define sk_portpair     __sk_common.skc_portpair
    #define sk_num          __sk_common.skc_num
    #define sk_dport        __sk_common.skc_dport
    #define sk_addrpair     __sk_common.skc_addrpair
    #define sk_daddr        __sk_common.skc_daddr
    #define sk_rcv_saddr        __sk_common.skc_rcv_saddr
    #define sk_family       __sk_common.skc_family
    #define sk_state        __sk_common.skc_state
    #define sk_reuse        __sk_common.skc_reuse
    #define sk_reuseport        __sk_common.skc_reuseport
    #define sk_ipv6only     __sk_common.skc_ipv6only
    #define sk_net_refcnt       __sk_common.skc_net_refcnt
    #define sk_bound_dev_if     __sk_common.skc_bound_dev_if
    #define sk_bind_node        __sk_common.skc_bind_node
    #define sk_prot         __sk_common.skc_prot
    #define sk_net          __sk_common.skc_net
    #define sk_v6_daddr     __sk_common.skc_v6_daddr
    #define sk_v6_rcv_saddr __sk_common.skc_v6_rcv_saddr
    #define sk_cookie       __sk_common.skc_cookie
    #define sk_incoming_cpu     __sk_common.skc_incoming_cpu
    #define sk_flags        __sk_common.skc_flags
    #define sk_rxhash       __sk_common.skc_rxhash
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


Members
=======

__sk_common
    shared layout with inet_timewait_sock

sk_lock
    synchronizer

sk_receive_queue
    incoming packets

{unnamed_struct}
    anonymous

sk_policy[2]
    flow policy

sk_rx_dst
    receive input route used by early demux

sk_dst_cache
    destination cache

sk_wmem_alloc
    transmit queue bytes committed

sk_omem_alloc
    "o“is”option“or”other"

sk_sndbuf
    size of send buffer in bytes

sk_write_queue
    Packet sending queue

sk_shutdown
    mask of ``SEND_SHUTDOWN`` and/or ``RCV_SHUTDOWN``

sk_no_check_tx
    ``SO_NO_CHECK`` setting, set checksum in TX packets

sk_no_check_rx
    allow zero checksum in RX packets

sk_userlocks
    ``SO_SNDBUF`` and ``SO_RCVBUF`` settings

sk_protocol
    which protocol this socket belongs in this network family

sk_type
    socket type (``SOCK_STREAM``, etc)

sk_wmem_queued
    persistent queue size

sk_allocation
    allocation mode

sk_pacing_rate
    Pacing rate (if supported by transport/packet scheduler)

sk_max_pacing_rate
    Maximum pacing rate (``SO_MAX_PACING_RATE``)

sk_route_caps
    route capabilities (e.g. ``NETIF_F_TSO``)

sk_route_nocaps
    forbidden route capabilities (e.g NETIF_F_GSO_MASK)

sk_gso_type
    GSO type (e.g. ``SKB_GSO_TCPV4``)

sk_gso_max_size
    Maximum GSO segment size to build

sk_gso_max_segs
    Maximum number of GSO segments

sk_rcvlowat
    ``SO_RCVLOWAT`` setting

sk_lingertime
    ``SO_LINGER`` l_linger setting

sk_error_queue
    rarely used

sk_prot_creator
    sk_prot of original sock creator (see ipv6_setsockopt,
    IPV6_ADDRFORM for instance)

sk_callback_lock
    used with the callbacks in the end of this struct

sk_err
    last error

sk_err_soft
    errors that don't cause failure but are the cause of a persistent
    failure not just 'timed out'

sk_ack_backlog
    current listen backlog

sk_max_ack_backlog
    listen backlog set in ``listen``

sk_priority
    ``SO_PRIORITY`` setting

sk_mark
    generic packet mark

sk_peer_pid
    ``struct pid`` for this socket's peer

sk_peer_cred
    ``SO_PEERCRED`` setting

sk_rcvtimeo
    ``SO_RCVTIMEO`` setting

sk_sndtimeo
    ``SO_SNDTIMEO`` setting

sk_timer
    sock cleanup timer

sk_stamp
    time stamp of last packet received

sk_tsflags
    SO_TIMESTAMPING socket options

sk_tskey
    counter to disambiguate concurrent tstamp requests

sk_socket
    Identd and reporting IO signals

sk_user_data
    RPC layer private data

sk_frag
    cached page frag

sk_send_head
    front of stuff to transmit

sk_peek_off
    current peek_offset value

sk_write_pending
    a write to stream socket waits to start

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
    callback to indicate errors (e.g. ``MSG_ERRQUEUE``)

sk_backlog_rcv
    callback to process the backlog

sk_destruct
    called at sock freeing time, i.e. when all refcnt == 0

sk_reuseport_cb
    reuseport group container


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
