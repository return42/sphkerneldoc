.. -*- coding: utf-8; mode: rst -*-

=====
net.h
=====

.. _`sock_type`:

enum sock_type
==============

.. c:type:: enum sock_type

    Socket types



Constants
---------

:``SOCK_STREAM``:
    stream (connection) socket

:``SOCK_DGRAM``:
    datagram (conn.less) socket

:``SOCK_RAW``:
    raw socket

:``SOCK_RDM``:
    reliably-delivered message

:``SOCK_SEQPACKET``:
    sequential packet socket

:``SOCK_DCCP``:
    Datagram Congestion Control Protocol socket

:``SOCK_PACKET``:
    linux specific way of getting packets at the dev level.::

                      For writing rarp and other similar things on the user level.


Description
-----------

When adding some new socket type please
grep ARCH_HAS_SOCKET_TYPE include/asm-\* /socket.h, at least MIPS
overrides this enum for binary compat reasons.


.. _`socket`:

struct socket
=============

.. c:type:: struct socket

    general BSD socket



Definition
----------

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
-------

:``state``:
    socket state (\ ``SS_CONNECTED``\ , etc)

:``type``:
    socket type (\ ``SOCK_STREAM``\ , etc)

:``flags``:
    socket flags (\ ``SOCK_NOSPACE``\ , etc)

:``wq``:
    wait queue for several uses

:``file``:
    File back pointer for gc

:``sk``:
    internal networking protocol agnostic socket representation

:``ops``:
    protocol specific socket operations


