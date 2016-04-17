.. -*- coding: utf-8; mode: rst -*-

============
scif_ioctl.h
============


.. _`scif_port_id`:

struct scif_port_id
===================

.. c:type:: scif_port_id

    SCIF port information


.. _`scif_port_id.definition`:

Definition
----------

.. code-block:: c

  struct scif_port_id {
    __u16 node;
    __u16 port;
  };


.. _`scif_port_id.members`:

Members
-------

:``node``:
    node on which port resides

:``port``:
    local port number




.. _`scifioctl_connect`:

struct scifioctl_connect
========================

.. c:type:: scifioctl_connect

    used for SCIF_CONNECT IOCTL


.. _`scifioctl_connect.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_connect {
    struct scif_port_id self;
    struct scif_port_id peer;
  };


.. _`scifioctl_connect.members`:

Members
-------

:``self``:
    used to read back the assigned port_id

:``peer``:
    destination node and port to connect to




.. _`scifioctl_accept`:

struct scifioctl_accept
=======================

.. c:type:: scifioctl_accept

    used for SCIF_ACCEPTREQ IOCTL


.. _`scifioctl_accept.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_accept {
    __s32 flags;
    struct scif_port_id peer;
    __u64 endpt;
  };


.. _`scifioctl_accept.members`:

Members
-------

:``flags``:
    flags

:``peer``:
    global id of peer endpoint

:``endpt``:
    new connected endpoint descriptor




.. _`scifioctl_msg`:

struct scifioctl_msg
====================

.. c:type:: scifioctl_msg

    used for SCIF_SEND/SCIF_RECV IOCTL


.. _`scifioctl_msg.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_msg {
    __u64 msg;
    __s32 len;
    __s32 flags;
    __s32 out_len;
  };


.. _`scifioctl_msg.members`:

Members
-------

:``msg``:
    message buffer address

:``len``:
    message length

:``flags``:
    flags

:``out_len``:
    number of bytes sent/received




.. _`scifioctl_reg`:

struct scifioctl_reg
====================

.. c:type:: scifioctl_reg

    used for SCIF_REG IOCTL


.. _`scifioctl_reg.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_reg {
    __u64 addr;
    __u64 len;
    __s64 offset;
    __s32 prot;
    __s32 flags;
    __s64 out_offset;
  };


.. _`scifioctl_reg.members`:

Members
-------

:``addr``:
    starting virtual address

:``len``:
    length of range

:``offset``:
    offset of window

:``prot``:
    read/write protection

:``flags``:
    flags

:``out_offset``:
    offset returned




.. _`scifioctl_unreg`:

struct scifioctl_unreg
======================

.. c:type:: scifioctl_unreg

    used for SCIF_UNREG IOCTL


.. _`scifioctl_unreg.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_unreg {
    __s64 offset;
    __u64 len;
  };


.. _`scifioctl_unreg.members`:

Members
-------

:``offset``:
    start of range to unregister

:``len``:
    length of range to unregister




.. _`scifioctl_copy`:

struct scifioctl_copy
=====================

.. c:type:: scifioctl_copy

    used for SCIF DMA copy IOCTLs


.. _`scifioctl_copy.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_copy {
    __s64 loffset;
    __u64 len;
    __s64 roffset;
    __u64 addr;
    __s32 flags;
  };


.. _`scifioctl_copy.members`:

Members
-------

:``loffset``:
    offset in local registered address space to/from
    which to copy

:``len``:
    length of range to copy

:``roffset``:
    offset in remote registered address space to/from
    which to copy

:``addr``:
    user virtual address to/from which to copy

:``flags``:
    flags




.. _`scifioctl_copy.description`:

Description
-----------

This structure is used for SCIF_READFROM, SCIF_WRITETO, SCIF_VREADFROM
and SCIF_VREADFROM IOCTL's.



.. _`scifioctl_fence_mark`:

struct scifioctl_fence_mark
===========================

.. c:type:: scifioctl_fence_mark

    used for SCIF_FENCE_MARK IOCTL


.. _`scifioctl_fence_mark.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_fence_mark {
    __s32 flags;
    __u64 mark;
  };


.. _`scifioctl_fence_mark.members`:

Members
-------

:``flags``:
    flags

:``mark``:
    fence handle which is a pointer to a __s32




.. _`scifioctl_fence_signal`:

struct scifioctl_fence_signal
=============================

.. c:type:: scifioctl_fence_signal

    used for SCIF_FENCE_SIGNAL IOCTL


.. _`scifioctl_fence_signal.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_fence_signal {
    __s64 loff;
    __u64 lval;
    __s64 roff;
    __u64 rval;
    __s32 flags;
  };


.. _`scifioctl_fence_signal.members`:

Members
-------

:``loff``:
    local offset

:``lval``:
    value to write to loffset

:``roff``:
    remote offset

:``rval``:
    value to write to roffset

:``flags``:
    flags




.. _`scifioctl_node_ids`:

struct scifioctl_node_ids
=========================

.. c:type:: scifioctl_node_ids

    used for SCIF_GET_NODEIDS IOCTL


.. _`scifioctl_node_ids.definition`:

Definition
----------

.. code-block:: c

  struct scifioctl_node_ids {
    __u64 nodes;
    __u64 self;
    __s32 len;
  };


.. _`scifioctl_node_ids.members`:

Members
-------

:``nodes``:
    pointer to an array of node_ids

:``self``:
    ID of the current node

:``len``:
    length of array


