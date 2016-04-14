.. -*- coding: utf-8; mode: rst -*-

=====
can.h
=====

.. _`can_frame`:

struct can_frame
================

.. c:type:: struct can_frame

    basic CAN frame structure



Definition
----------

.. code-block:: c

  struct can_frame {
    canid_t can_id;
    __u8 can_dlc;
    __u8 __pad;
    __u8 __res0;
    __u8 __res1;
    __u8 data[CAN_MAX_DLEN] __attribute__((aligned(8)));
  };



Members
-------

:``can_id``:
    CAN ID of the frame and CAN_\\*_FLAG flags, see canid_t definition

:``can_dlc``:
    frame payload length in byte (0 .. 8) aka data length code
    N.B. the DLC field from ISO 11898-1 Chapter 8.4.2.3 has a 1:1
    mapping of the 'data length code' to the real payload length

:``__pad``:
    padding

:``__res0``:
    reserved / padding

:``__res1``:
    reserved / padding

:``data[CAN_MAX_DLEN] __attribute__((aligned(8)))``:
    CAN frame payload (up to 8 byte)



.. _`canfd_frame`:

struct canfd_frame
==================

.. c:type:: struct canfd_frame

    CAN flexible data rate frame structure



Definition
----------

.. code-block:: c

  struct canfd_frame {
    canid_t can_id;
    __u8 len;
    __u8 flags;
    __u8 __res0;
    __u8 __res1;
    __u8 data[CANFD_MAX_DLEN] __attribute__((aligned(8)));
  };



Members
-------

:``can_id``:
    CAN ID of the frame and CAN_\\*_FLAG flags, see canid_t definition

:``len``:
    frame payload length in byte (0 .. CANFD_MAX_DLEN)

:``flags``:
    additional flags for CAN FD

:``__res0``:
    reserved / padding

:``__res1``:
    reserved / padding

:``data[CANFD_MAX_DLEN] __attribute__((aligned(8)))``:
    CAN FD frame payload (up to CANFD_MAX_DLEN byte)



.. _`sockaddr_can`:

struct sockaddr_can
===================

.. c:type:: struct sockaddr_can

    the sockaddr structure for CAN sockets



Definition
----------

.. code-block:: c

  struct sockaddr_can {
    __kernel_sa_family_t can_family;
    int can_ifindex;
    union can_addr;
  };



Members
-------

:``can_family``:
    address family number AF_CAN.

:``can_ifindex``:
    CAN network interface index.

:``can_addr``:
    protocol specific address information



.. _`can_filter`:

struct can_filter
=================

.. c:type:: struct can_filter

    CAN ID based filter in can_register().



Definition
----------

.. code-block:: c

  struct can_filter {
    canid_t can_id;
    canid_t can_mask;
  };



Members
-------

:``can_id``:
    relevant bits of CAN ID which are not masked out.

:``can_mask``:
    CAN mask (see description)



Description
-----------

Description:
A filter matches, when

<received_can_id> & mask == can_id & mask

The filter can be inverted (CAN_INV_FILTER bit set in can_id) or it can
filter for error message frames (CAN_ERR_FLAG bit set in mask).

