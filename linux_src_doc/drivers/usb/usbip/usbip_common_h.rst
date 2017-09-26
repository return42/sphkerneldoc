.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/usbip/usbip_common.h

.. _`usbip_header_basic`:

struct usbip_header_basic
=========================

.. c:type:: struct usbip_header_basic

    data pertinent to every request

.. _`usbip_header_basic.definition`:

Definition
----------

.. code-block:: c

    struct usbip_header_basic {
        __u32 command;
        __u32 seqnum;
        __u32 devid;
        __u32 direction;
        __u32 ep;
    }

.. _`usbip_header_basic.members`:

Members
-------

command
    the usbip request type

seqnum
    sequential number that identifies requests; incremented per
    connection

devid
    specifies a remote USB device uniquely instead of busnum and devnum;
    in the stub driver, this value is ((busnum << 16) \| devnum)

direction
    direction of the transfer

ep
    endpoint number

.. _`usbip_header_cmd_submit`:

struct usbip_header_cmd_submit
==============================

.. c:type:: struct usbip_header_cmd_submit

    USBIP_CMD_SUBMIT packet header

.. _`usbip_header_cmd_submit.definition`:

Definition
----------

.. code-block:: c

    struct usbip_header_cmd_submit {
        __u32 transfer_flags;
        __s32 transfer_buffer_length;
        __s32 start_frame;
        __s32 number_of_packets;
        __s32 interval;
        unsigned char setup[8];
    }

.. _`usbip_header_cmd_submit.members`:

Members
-------

transfer_flags
    URB flags

transfer_buffer_length
    the data size for (in) or (out) transfer

start_frame
    initial frame for isochronous or interrupt transfers

number_of_packets
    number of isochronous packets

interval
    maximum time for the request on the server-side host controller

setup
    setup data for a control request

.. _`usbip_header_ret_submit`:

struct usbip_header_ret_submit
==============================

.. c:type:: struct usbip_header_ret_submit

    USBIP_RET_SUBMIT packet header

.. _`usbip_header_ret_submit.definition`:

Definition
----------

.. code-block:: c

    struct usbip_header_ret_submit {
        __s32 status;
        __s32 actual_length;
        __s32 start_frame;
        __s32 number_of_packets;
        __s32 error_count;
    }

.. _`usbip_header_ret_submit.members`:

Members
-------

status
    return status of a non-iso request

actual_length
    number of bytes transferred

start_frame
    initial frame for isochronous or interrupt transfers

number_of_packets
    number of isochronous packets

error_count
    number of errors for isochronous transfers

.. _`usbip_header_cmd_unlink`:

struct usbip_header_cmd_unlink
==============================

.. c:type:: struct usbip_header_cmd_unlink

    USBIP_CMD_UNLINK packet header

.. _`usbip_header_cmd_unlink.definition`:

Definition
----------

.. code-block:: c

    struct usbip_header_cmd_unlink {
        __u32 seqnum;
    }

.. _`usbip_header_cmd_unlink.members`:

Members
-------

seqnum
    the URB seqnum to unlink

.. _`usbip_header_ret_unlink`:

struct usbip_header_ret_unlink
==============================

.. c:type:: struct usbip_header_ret_unlink

    USBIP_RET_UNLINK packet header

.. _`usbip_header_ret_unlink.definition`:

Definition
----------

.. code-block:: c

    struct usbip_header_ret_unlink {
        __s32 status;
    }

.. _`usbip_header_ret_unlink.members`:

Members
-------

status
    return status of the request

.. _`usbip_header`:

struct usbip_header
===================

.. c:type:: struct usbip_header

    common header for all usbip packets

.. _`usbip_header.definition`:

Definition
----------

.. code-block:: c

    struct usbip_header {
        struct usbip_header_basic base;
        union {
            struct usbip_header_cmd_submit cmd_submit;
            struct usbip_header_ret_submit ret_submit;
            struct usbip_header_cmd_unlink cmd_unlink;
            struct usbip_header_ret_unlink ret_unlink;
        } u;
    }

.. _`usbip_header.members`:

Members
-------

base
    the basic header

u
    packet type dependent header

.. This file was automatic generated / don't edit.

