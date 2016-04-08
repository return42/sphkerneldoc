
.. _API-enum-sock-type:

==============
enum sock_type
==============

*man enum sock_type(9)*

*4.6.0-rc1*

Socket types


Synopsis
========

.. code-block:: c

    enum sock_type {
      SOCK_STREAM,
      SOCK_DGRAM,
      SOCK_RAW,
      SOCK_RDM,
      SOCK_SEQPACKET,
      SOCK_DCCP,
      SOCK_PACKET
    };


Constants
=========

SOCK_STREAM
    stream (connection) socket

SOCK_DGRAM
    datagram (conn.less) socket

SOCK_RAW
    raw socket

SOCK_RDM
    reliably-delivered message

SOCK_SEQPACKET
    sequential packet socket

SOCK_DCCP
    Datagram Congestion Control Protocol socket

SOCK_PACKET
    linux specific way of getting packets at the dev level. For writing rarp and other similar things on the user level.


Description
===========

When adding some new socket type please grep ARCH_HAS_SOCKET_TYPE include/asm-⋆ /socket.h, at least MIPS overrides this enum for binary compat reasons.
