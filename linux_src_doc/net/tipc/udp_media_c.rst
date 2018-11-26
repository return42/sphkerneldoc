.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/udp_media.c

.. _`udp_media_addr`:

struct udp_media_addr
=====================

.. c:type:: struct udp_media_addr

    IP/UDP addressing information

.. _`udp_media_addr.definition`:

Definition
----------

.. code-block:: c

    struct udp_media_addr {
        __be16 proto;
        __be16 port;
        union {
            struct in_addr ipv4;
            struct in6_addr ipv6;
        } ;
    }

.. _`udp_media_addr.members`:

Members
-------

proto
    *undescribed*

port
    *undescribed*

{unnamed_union}
    anonymous

ipv4
    *undescribed*

ipv6
    *undescribed*

.. _`udp_media_addr.description`:

Description
-----------

This is the bearer level originating address used in neighbor discovery
messages, and all fields should be in network byte order

.. _`udp_bearer`:

struct udp_bearer
=================

.. c:type:: struct udp_bearer

    ip/udp bearer data structure

.. _`udp_bearer.definition`:

Definition
----------

.. code-block:: c

    struct udp_bearer {
        struct tipc_bearer __rcu *bearer;
        struct socket *ubsock;
        u32 ifindex;
        struct work_struct work;
        struct udp_replicast rcast;
    }

.. _`udp_bearer.members`:

Members
-------

bearer
    associated generic tipc bearer

ubsock
    bearer associated socket

ifindex
    local address scope

work
    used to schedule deferred work on a bearer

rcast
    *undescribed*

.. _`tipc_parse_udp_addr`:

tipc_parse_udp_addr
===================

.. c:function:: int tipc_parse_udp_addr(struct nlattr *nla, struct udp_media_addr *addr, u32 *scope_id)

    build udp media address from netlink data

    :param nla:
        *undescribed*
    :type nla: struct nlattr \*

    :param addr:
        tipc media address to fill with address, port and protocol type
    :type addr: struct udp_media_addr \*

    :param scope_id:
        IPv6 scope id pointer, not NULL indicates it's required
    :type scope_id: u32 \*

.. _`tipc_udp_enable`:

tipc_udp_enable
===============

.. c:function:: int tipc_udp_enable(struct net *net, struct tipc_bearer *b, struct nlattr  *attrs)

    callback to create a new udp bearer instance

    :param net:
        network namespace
    :type net: struct net \*

    :param b:
        pointer to generic tipc_bearer
    :type b: struct tipc_bearer \*

    :param attrs:
        netlink bearer configuration
    :type attrs: struct nlattr  \*

.. _`tipc_udp_enable.description`:

Description
-----------

validate the bearer parameters and initialize the udp bearer
rtnl_lock should be held

.. This file was automatic generated / don't edit.

