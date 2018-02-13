.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/flower/tunnel_conf.c

.. _`nfp_tun_active_tuns`:

struct nfp_tun_active_tuns
==========================

.. c:type:: struct nfp_tun_active_tuns

    periodic message of active tunnels

.. _`nfp_tun_active_tuns.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_active_tuns {
        __be32 seq;
        __be32 count;
        __be32 flags;
        struct route_ip_info {
            __be32 ipv4;
            __be32 egress_port;
            __be32 extra[2];
        } tun_info[];
    }

.. _`nfp_tun_active_tuns.members`:

Members
-------

seq
    sequence number of the message

count
    number of tunnels report in message

flags
    options part of the request

tun_info
    tunnels that have sent traffic in reported period

tun_info.ipv4
    dest IPv4 address of active route

tun_info.egress_port
    port the encapsulated packet egressed

tun_info.extra
    reserved for future use

.. _`nfp_tun_neigh`:

struct nfp_tun_neigh
====================

.. c:type:: struct nfp_tun_neigh

    neighbour/route entry on the NFP

.. _`nfp_tun_neigh.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_neigh {
        __be32 dst_ipv4;
        __be32 src_ipv4;
        u8 dst_addr[ETH_ALEN];
        u8 src_addr[ETH_ALEN];
        __be32 port_id;
    }

.. _`nfp_tun_neigh.members`:

Members
-------

dst_ipv4
    destination IPv4 address

src_ipv4
    source IPv4 address

dst_addr
    destination MAC address

src_addr
    source MAC address

port_id
    NFP port to output packet on - associated with source IPv4

.. _`nfp_tun_req_route_ipv4`:

struct nfp_tun_req_route_ipv4
=============================

.. c:type:: struct nfp_tun_req_route_ipv4

    NFP requests a route/neighbour lookup

.. _`nfp_tun_req_route_ipv4.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_req_route_ipv4 {
        __be32 ingress_port;
        __be32 ipv4_addr;
        __be32 reserved[2];
    }

.. _`nfp_tun_req_route_ipv4.members`:

Members
-------

ingress_port
    ingress port of packet that signalled request

ipv4_addr
    destination ipv4 address for route

reserved
    reserved for future use

.. _`nfp_ipv4_route_entry`:

struct nfp_ipv4_route_entry
===========================

.. c:type:: struct nfp_ipv4_route_entry

    routes that are offloaded to the NFP

.. _`nfp_ipv4_route_entry.definition`:

Definition
----------

.. code-block:: c

    struct nfp_ipv4_route_entry {
        __be32 ipv4_addr;
        struct list_head list;
    }

.. _`nfp_ipv4_route_entry.members`:

Members
-------

ipv4_addr
    destination of route

list
    list pointer

.. _`nfp_tun_ipv4_addr`:

struct nfp_tun_ipv4_addr
========================

.. c:type:: struct nfp_tun_ipv4_addr

    set the IP address list on the NFP

.. _`nfp_tun_ipv4_addr.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_ipv4_addr {
        __be32 count;
        __be32 ipv4_addr[NFP_FL_IPV4_ADDRS_MAX];
    }

.. _`nfp_tun_ipv4_addr.members`:

Members
-------

count
    number of IPs populated in the array

ipv4_addr
    array of IPV4_ADDRS_MAX 32 bit IPv4 addresses

.. _`nfp_ipv4_addr_entry`:

struct nfp_ipv4_addr_entry
==========================

.. c:type:: struct nfp_ipv4_addr_entry

    cached IPv4 addresses

.. _`nfp_ipv4_addr_entry.definition`:

Definition
----------

.. code-block:: c

    struct nfp_ipv4_addr_entry {
        __be32 ipv4_addr;
        int ref_count;
        struct list_head list;
    }

.. _`nfp_ipv4_addr_entry.members`:

Members
-------

ipv4_addr
    IP address

ref_count
    number of rules currently using this IP

list
    list pointer

.. _`nfp_tun_mac_addr`:

struct nfp_tun_mac_addr
=======================

.. c:type:: struct nfp_tun_mac_addr

    configure MAC address of tunnel EP on NFP

.. _`nfp_tun_mac_addr.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_mac_addr {
        __be16 reserved;
        __be16 count;
        struct index_mac_addr {
            __be16 index;
            u8 addr[ETH_ALEN];
        } addresses[];
    }

.. _`nfp_tun_mac_addr.members`:

Members
-------

reserved
    reserved for future use

count
    number of MAC addresses in the message

addresses
    series of MACs to offload

addresses.index
    index of MAC address in the lookup table

addresses.addr
    interface MAC address

.. _`nfp_tun_mac_offload_entry`:

struct nfp_tun_mac_offload_entry
================================

.. c:type:: struct nfp_tun_mac_offload_entry

    list of MACs to offload

.. _`nfp_tun_mac_offload_entry.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_mac_offload_entry {
        __be16 index;
        u8 addr[ETH_ALEN];
        struct list_head list;
    }

.. _`nfp_tun_mac_offload_entry.members`:

Members
-------

index
    index of MAC address for offloading

addr
    interface MAC address

list
    list pointer

.. _`nfp_tun_mac_non_nfp_idx`:

struct nfp_tun_mac_non_nfp_idx
==============================

.. c:type:: struct nfp_tun_mac_non_nfp_idx

    converts non NFP netdev ifindex to 8-bit id

.. _`nfp_tun_mac_non_nfp_idx.definition`:

Definition
----------

.. code-block:: c

    struct nfp_tun_mac_non_nfp_idx {
        int ifindex;
        u8 index;
        struct list_head list;
    }

.. _`nfp_tun_mac_non_nfp_idx.members`:

Members
-------

ifindex
    netdev ifindex of the device

index
    index of netdevs mac on NFP

list
    list pointer

.. This file was automatic generated / don't edit.

