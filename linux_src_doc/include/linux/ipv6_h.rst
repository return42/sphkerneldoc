.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ipv6.h

.. _`ipv6_pinfo`:

struct ipv6_pinfo
=================

.. c:type:: struct ipv6_pinfo

    ipv6 private area

.. _`ipv6_pinfo.definition`:

Definition
----------

.. code-block:: c

    struct ipv6_pinfo {
        struct in6_addr saddr;
        struct in6_pktinfo sticky_pktinfo;
        const struct in6_addr *daddr_cache;
    #ifdef CONFIG_IPV6_SUBTREES
        const struct in6_addr *saddr_cache;
    #endif
        __be32 flow_label;
        __u32 frag_size;
    #if defined__BIG_ENDIAN_BITFIELD
        __s16 hop_limit:9;
        __u16 __unused_1:7;
    #else
        __u16 __unused_1:7;
        __s16 hop_limit:9;
    #endif
    #if defined__BIG_ENDIAN_BITFIELD
        __s16 mcast_hops:9;
        __u16 __unused_2:1:6;
        __u16 mc_loop:1;
    #else
        __u16 mc_loop:1;
        __u16 __unused_2:1:6;
        __s16 mcast_hops:9;
    #endif
        int ucast_oif;
        int mcast_oif;
        union rxopt;
        __u16 recverr:1;
        __u16 sndflow:1:1;
        __u16 repflow:1:1:1;
        __u16 pmtudisc:1:1:1:3;
        __u16 padding:1:1:1:3:1;
        __u16 srcprefs:1:1:1:3:1:3;
        __u16 dontfrag:1:1:1:3:1:3:1;
        __u16 autoflowlabel:1:1:1:3:1:3:1:1;
        __u8 min_hopcount;
        __u8 tclass;
        __be32 rcv_flowinfo;
        __u32 dst_cookie;
        __u32 rx_dst_cookie;
        struct ipv6_mc_socklist __rcu *ipv6_mc_list;
        struct ipv6_ac_socklist *ipv6_ac_list;
        struct ipv6_fl_socklist __rcu *ipv6_fl_list;
        struct ipv6_txoptions __rcu *opt;
        struct sk_buff *pktoptions;
        struct sk_buff *rxpmtu;
        struct inet6_cork cork;
    }

.. _`ipv6_pinfo.members`:

Members
-------

saddr
    *undescribed*

sticky_pktinfo
    *undescribed*

daddr_cache
    *undescribed*

saddr_cache
    *undescribed*

flow_label
    *undescribed*

frag_size
    *undescribed*

hop_limit
    *undescribed*

__unused_1
    *undescribed*

__unused_1
    *undescribed*

hop_limit
    *undescribed*

mcast_hops
    *undescribed*

__unused_2
    *undescribed*

mc_loop
    *undescribed*

mc_loop
    *undescribed*

__unused_2
    *undescribed*

mcast_hops
    *undescribed*

ucast_oif
    *undescribed*

mcast_oif
    *undescribed*

rxopt
    *undescribed*

recverr
    *undescribed*

sndflow
    *undescribed*

repflow
    *undescribed*

pmtudisc
    *undescribed*

padding
    *undescribed*

srcprefs
    *undescribed*

dontfrag
    *undescribed*

autoflowlabel
    *undescribed*

min_hopcount
    *undescribed*

tclass
    *undescribed*

rcv_flowinfo
    *undescribed*

dst_cookie
    *undescribed*

rx_dst_cookie
    *undescribed*

ipv6_mc_list
    *undescribed*

ipv6_ac_list
    *undescribed*

ipv6_fl_list
    *undescribed*

opt
    *undescribed*

pktoptions
    *undescribed*

rxpmtu
    *undescribed*

cork
    *undescribed*

.. _`ipv6_pinfo.description`:

Description
-----------

In the struct sock hierarchy (tcp6_sock, upd6_sock, etc)
this \_must\_ be the last member, so that inet6_sk_generic
is able to calculate its offset from the base struct sock
by using the struct proto->slab_obj_size member. -acme

.. This file was automatic generated / don't edit.

