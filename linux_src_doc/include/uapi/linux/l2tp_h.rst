.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/l2tp.h

.. _`sockaddr_l2tpip6`:

struct sockaddr_l2tpip6
=======================

.. c:type:: struct sockaddr_l2tpip6

    the sockaddr structure for L2TP-over-IPv6 sockets

.. _`sockaddr_l2tpip6.definition`:

Definition
----------

.. code-block:: c

    struct sockaddr_l2tpip6 {
        __kernel_sa_family_t l2tp_family;
        __be16 l2tp_unused;
        __be32 l2tp_flowinfo;
        struct in6_addr l2tp_addr;
        __u32 l2tp_scope_id;
        __u32 l2tp_conn_id;
    }

.. _`sockaddr_l2tpip6.members`:

Members
-------

l2tp_family
    address family number AF_L2TPIP.

l2tp_unused
    *undescribed*

l2tp_flowinfo
    *undescribed*

l2tp_addr
    protocol specific address information

l2tp_scope_id
    *undescribed*

l2tp_conn_id
    connection id of tunnel

.. This file was automatic generated / don't edit.

