.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/em28xx/em28xx.h

.. _`em28xx_usb_bufs`:

struct em28xx_usb_bufs
======================

.. c:type:: struct em28xx_usb_bufs

    Contains URB-related buffer data

.. _`em28xx_usb_bufs.definition`:

Definition
----------

.. code-block:: c

    struct em28xx_usb_bufs {
        int max_pkt_size;
        int num_packets;
        int num_bufs;
        struct urb **urb;
        char **buf;
    }

.. _`em28xx_usb_bufs.members`:

Members
-------

max_pkt_size
    max packet size of isoc transaction

num_packets
    number of packets in each buffer

num_bufs
    number of allocated urb

urb
    urb for isoc/bulk transfers

buf
    transfer buffers for isoc/bulk transfer

.. _`em28xx_usb_ctl`:

struct em28xx_usb_ctl
=====================

.. c:type:: struct em28xx_usb_ctl

    Contains URB-related buffer data

.. _`em28xx_usb_ctl.definition`:

Definition
----------

.. code-block:: c

    struct em28xx_usb_ctl {
        struct em28xx_usb_bufs analog_bufs;
        struct em28xx_usb_bufs digital_bufs;
        struct em28xx_buffer *vid_buf;
        struct em28xx_buffer *vbi_buf;
        int (*urb_data_copy)(struct em28xx *dev, struct urb *urb);
    }

.. _`em28xx_usb_ctl.members`:

Members
-------

analog_bufs
    isoc/bulk transfer buffers for analog mode

digital_bufs
    isoc/bulk transfer buffers for digital mode

vid_buf
    Stores already requested video buffers

vbi_buf
    Stores already requested VBI buffers

urb_data_copy
    copy data from URB

.. _`em28xx_fmt`:

struct em28xx_fmt
=================

.. c:type:: struct em28xx_fmt

    Struct to enumberate video formats

.. _`em28xx_fmt.definition`:

Definition
----------

.. code-block:: c

    struct em28xx_fmt {
        char *name;
        u32 fourcc;
        int depth;
        int reg;
    }

.. _`em28xx_fmt.members`:

Members
-------

name
    Name for the video standard

fourcc
    v4l2 format id

depth
    mean number of bits to represent a pixel

reg
    em28xx register value to set it

.. _`em28xx_buffer`:

struct em28xx_buffer
====================

.. c:type:: struct em28xx_buffer

    buffer for storing one video frame

.. _`em28xx_buffer.definition`:

Definition
----------

.. code-block:: c

    struct em28xx_buffer {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        void *mem;
        unsigned int length;
        int top_field;
        unsigned int pos;
        char *vb_buf;
    }

.. _`em28xx_buffer.members`:

Members
-------

vb
    common v4l buffer stuff

list
    List to associate it with the other buffers

mem
    pointer to the buffer, as returned by \ :c:func:`vb2_plane_vaddr`\ 

length
    length of the buffer, as returned by \ :c:func:`vb2_plane_size`\ 

top_field
    If non-zero, indicate that the buffer is the top field

pos
    Indicate the next position of the buffer to be filled.

vb_buf
    pointer to vmalloc memory address in vb

.. _`em28xx_buffer.description`:

Description
-----------

.. note::

in interlaced mode, \ ``pos``\  is reset to zero at the start of each new
field (not frame !)

.. This file was automatic generated / don't edit.

