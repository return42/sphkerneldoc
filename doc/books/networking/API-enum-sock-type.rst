.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-sock-type:

==============
enum sock_type
==============

*man enum sock_type(9)*

*4.6.0-rc5*

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
    linux specific way of getting packets at the dev level. For writing
    rarp and other similar things on the user level.


Description
===========

When adding some new socket type please grep ARCH_HAS_SOCKET_TYPE
include/asm-* /socket.h, at least MIPS overrides this enum for binary
compat reasons.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
