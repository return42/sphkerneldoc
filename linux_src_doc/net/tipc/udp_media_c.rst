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
        __be16 udp_port;
        union {unnamed_union};
    }

.. _`udp_media_addr.members`:

Members
-------

proto
    *undescribed*

udp_port
    *undescribed*

{unnamed_union}
    anonymous


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

.. _`parse_options`:

parse_options
=============

.. c:function:: int parse_options(struct nlattr  *attrs[], struct udp_bearer *ub, struct udp_media_addr *local, struct udp_media_addr *remote)

    build local/remote addresses from configuration

    :param struct nlattr  \*attrs:
        netlink config data

    :param struct udp_bearer \*ub:
        UDP bearer instance

    :param struct udp_media_addr \*local:
        local bearer IP address/port

    :param struct udp_media_addr \*remote:
        peer or multicast IP/port

.. _`tipc_udp_enable`:

tipc_udp_enable
===============

.. c:function:: int tipc_udp_enable(struct net *net, struct tipc_bearer *b, struct nlattr  *attrs[])

    callback to create a new udp bearer instance

    :param struct net \*net:
        network namespace

    :param struct tipc_bearer \*b:
        pointer to generic tipc_bearer

    :param struct nlattr  \*attrs:
        netlink bearer configuration

.. _`tipc_udp_enable.description`:

Description
-----------

validate the bearer parameters and initialize the udp bearer
rtnl_lock should be held

.. This file was automatic generated / don't edit.

