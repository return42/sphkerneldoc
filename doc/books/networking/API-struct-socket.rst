
.. _API-struct-socket:

=============
struct socket
=============

*man struct socket(9)*

*4.6.0-rc1*

general BSD socket


Synopsis
========

.. code-block:: c

    struct socket {
      socket_state state;
      short type;
      unsigned long flags;
      struct socket_wq __rcu * wq;
      struct file * file;
      struct sock * sk;
      const struct proto_ops * ops;
    };


Members
=======

state
    socket state (``SS_CONNECTED``, etc)

type
    socket type (``SOCK_STREAM``, etc)

flags
    socket flags (``SOCK_NOSPACE``, etc)

wq
    wait queue for several uses

file
    File back pointer for gc

sk
    internal networking protocol agnostic socket representation

ops
    protocol specific socket operations
