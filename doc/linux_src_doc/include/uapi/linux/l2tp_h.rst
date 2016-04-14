.. -*- coding: utf-8; mode: rst -*-

======
l2tp.h
======

.. _`sockaddr_l2tpip6`:

struct sockaddr_l2tpip6
=======================

.. c:type:: struct sockaddr_l2tpip6

    the sockaddr structure for L2TP-over-IPv6 sockets



Definition
----------

.. code-block:: c

  struct sockaddr_l2tpip6 {
    __kernel_sa_family_t l2tp_family;
    struct in6_addr l2tp_addr;
    __u32 l2tp_conn_id;
  };



Members
-------

:``l2tp_family``:
    address family number AF_L2TPIP.

:``l2tp_addr``:
    protocol specific address information

:``l2tp_conn_id``:
    connection id of tunnel


