
.. _API-struct-sock-common:

==================
struct sock_common
==================

*man struct sock_common(9)*

*4.6.0-rc1*

minimal network layer representation of sockets


Synopsis
========

.. code-block:: c

    struct sock_common {
      union {unnamed_union};
    };


Members
=======

{unnamed_union}
    anonymous


Description
===========

This is the minimal network layer representation of sockets, the header for struct sock and struct inet_timewait_sock.
