.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/flow_dissector.h

.. _`flow_dissector_key_control`:

struct flow_dissector_key_control
=================================

.. c:type:: struct flow_dissector_key_control


.. _`flow_dissector_key_control.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_control {
        u16 thoff;
        u16 addr_type;
        u32 flags;
    }

.. _`flow_dissector_key_control.members`:

Members
-------

thoff
    Transport header offset

addr_type
    *undescribed*

flags
    *undescribed*

.. _`flow_dissector_key_basic`:

struct flow_dissector_key_basic
===============================

.. c:type:: struct flow_dissector_key_basic


.. _`flow_dissector_key_basic.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_basic {
        __be16 n_proto;
        u8 ip_proto;
        u8 padding;
    }

.. _`flow_dissector_key_basic.members`:

Members
-------

n_proto
    Network header protocol (eg. IPv4/IPv6)

ip_proto
    Transport header protocol (eg. TCP/UDP)

padding
    *undescribed*

.. _`flow_dissector_key_enc_opts`:

struct flow_dissector_key_enc_opts
==================================

.. c:type:: struct flow_dissector_key_enc_opts


.. _`flow_dissector_key_enc_opts.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_enc_opts {
        u8 data[FLOW_DIS_TUN_OPTS_MAX];
        u8 len;
        __be16 dst_opt_type;
    }

.. _`flow_dissector_key_enc_opts.members`:

Members
-------

data
    tunnel option data

len
    length of tunnel option data

dst_opt_type
    tunnel option type

.. _`flow_dissector_key_ipv4_addrs`:

struct flow_dissector_key_ipv4_addrs
====================================

.. c:type:: struct flow_dissector_key_ipv4_addrs


.. _`flow_dissector_key_ipv4_addrs.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_ipv4_addrs {
        __be32 src;
        __be32 dst;
    }

.. _`flow_dissector_key_ipv4_addrs.members`:

Members
-------

src
    source ip address

dst
    destination ip address

.. _`flow_dissector_key_ipv6_addrs`:

struct flow_dissector_key_ipv6_addrs
====================================

.. c:type:: struct flow_dissector_key_ipv6_addrs


.. _`flow_dissector_key_ipv6_addrs.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_ipv6_addrs {
        struct in6_addr src;
        struct in6_addr dst;
    }

.. _`flow_dissector_key_ipv6_addrs.members`:

Members
-------

src
    source ip address

dst
    destination ip address

.. _`flow_dissector_key_tipc`:

struct flow_dissector_key_tipc
==============================

.. c:type:: struct flow_dissector_key_tipc


.. _`flow_dissector_key_tipc.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_tipc {
        __be32 key;
    }

.. _`flow_dissector_key_tipc.members`:

Members
-------

key
    source node address combined with selector

.. _`flow_dissector_key_addrs`:

struct flow_dissector_key_addrs
===============================

.. c:type:: struct flow_dissector_key_addrs


.. _`flow_dissector_key_addrs.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_addrs {
        union {
            struct flow_dissector_key_ipv4_addrs v4addrs;
            struct flow_dissector_key_ipv6_addrs v6addrs;
            struct flow_dissector_key_tipc tipckey;
        } ;
    }

.. _`flow_dissector_key_addrs.members`:

Members
-------

{unnamed_union}
    anonymous

v4addrs
    IPv4 addresses

v6addrs
    IPv6 addresses

tipckey
    *undescribed*

.. _`flow_dissector_key_eth_addrs`:

struct flow_dissector_key_eth_addrs
===================================

.. c:type:: struct flow_dissector_key_eth_addrs


.. _`flow_dissector_key_eth_addrs.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_eth_addrs {
        unsigned char dst[ETH_ALEN];
        unsigned char src[ETH_ALEN];
    }

.. _`flow_dissector_key_eth_addrs.members`:

Members
-------

dst
    destination Ethernet address

src
    source Ethernet address

.. _`flow_dissector_key_tcp`:

struct flow_dissector_key_tcp
=============================

.. c:type:: struct flow_dissector_key_tcp


.. _`flow_dissector_key_tcp.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_tcp {
        __be16 flags;
    }

.. _`flow_dissector_key_tcp.members`:

Members
-------

flags
    flags

.. _`flow_dissector_key_ip`:

struct flow_dissector_key_ip
============================

.. c:type:: struct flow_dissector_key_ip


.. _`flow_dissector_key_ip.definition`:

Definition
----------

.. code-block:: c

    struct flow_dissector_key_ip {
        __u8 tos;
        __u8 ttl;
    }

.. _`flow_dissector_key_ip.members`:

Members
-------

tos
    tos

ttl
    ttl

.. This file was automatic generated / don't edit.

