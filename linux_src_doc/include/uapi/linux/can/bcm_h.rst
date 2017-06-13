.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/can/bcm.h

.. _`bcm_msg_head`:

struct bcm_msg_head
===================

.. c:type:: struct bcm_msg_head

    head of messages to/from the broadcast manager

.. _`bcm_msg_head.definition`:

Definition
----------

.. code-block:: c

    struct bcm_msg_head {
        __u32 opcode;
        __u32 flags;
        __u32 count;
        struct bcm_timeval ival1;
        struct bcm_timeval ival2;
        canid_t can_id;
        __u32 nframes;
        struct can_frame frames;
    }

.. _`bcm_msg_head.members`:

Members
-------

opcode
    opcode, see enum below.

flags
    special flags, see below.

count
    number of frames to send before changing interval.

ival1
    interval for the first \ ``count``\  frames.

ival2
    interval for the following frames.

can_id
    CAN ID of frames to be sent or received.

nframes
    number of frames appended to the message head.

frames
    array of CAN frames.

.. This file was automatic generated / don't edit.

