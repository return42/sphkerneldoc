.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00dump.h

.. _`introduction`:

Introduction
============

This header is intended to be exported to userspace,
to make the structures and enumerations available to userspace
applications. This means that all data types should be exportable.

When rt2x00 is compiled with debugfs support enabled,
it is possible to capture all data coming in and out of the device
by reading the frame dump file. This file can have only a single reader.
The following frames will be reported:
- All incoming frames (rx)
- All outgoing frames (tx, including beacon and atim)
- All completed frames (txdone including atim)

The data is send to the file using the following format:

[rt2x00dump header][hardware descriptor][ieee802.11 frame]

rt2x00dump header: The description of the dumped frame, as well as
additional information useful for debugging. See \ :c:type:`struct rt2x00dump_hdr <rt2x00dump_hdr>`\ .
hardware descriptor: Descriptor that was used to receive or transmit
the frame.
ieee802.11 frame: The actual frame that was received or transmitted.

.. _`rt2x00_dump_type`:

enum rt2x00_dump_type
=====================

.. c:type:: enum rt2x00_dump_type

    Frame type

.. _`rt2x00_dump_type.definition`:

Definition
----------

.. code-block:: c

    enum rt2x00_dump_type {
        DUMP_FRAME_RXDONE,
        DUMP_FRAME_TX,
        DUMP_FRAME_TXDONE,
        DUMP_FRAME_BEACON
    };

.. _`rt2x00_dump_type.constants`:

Constants
---------

DUMP_FRAME_RXDONE
    This frame has been received by the hardware.

DUMP_FRAME_TX
    This frame is queued for transmission to the hardware.

DUMP_FRAME_TXDONE
    This frame indicates the device has handled
    the tx event which has either succeeded or failed. A frame
    with this type should also have been reported with as a
    \ ``DUMP_FRAME_TX``\  frame.

DUMP_FRAME_BEACON
    This beacon frame is queued for transmission to the
    hardware.

.. _`rt2x00_dump_type.description`:

Description
-----------

These values are used for the \ ``type``\  member of \ :c:type:`struct rt2x00dump_hdr <rt2x00dump_hdr>`\ .

.. _`rt2x00dump_hdr`:

struct rt2x00dump_hdr
=====================

.. c:type:: struct rt2x00dump_hdr

    Dump frame header

.. _`rt2x00dump_hdr.definition`:

Definition
----------

.. code-block:: c

    struct rt2x00dump_hdr {
        __le32 version;
    #define DUMP_HEADER_VERSION 3
        __le32 header_length;
        __le32 desc_length;
        __le32 data_length;
        __le16 chip_rt;
        __le16 chip_rf;
        __le16 chip_rev;
        __le16 type;
        __u8 queue_index;
        __u8 entry_index;
        __le32 timestamp_sec;
        __le32 timestamp_usec;
    }

.. _`rt2x00dump_hdr.members`:

Members
-------

version
    Header version should always be set to \ ``DUMP_HEADER_VERSION``\ .
    This field must be checked by userspace to determine if it can
    handle this frame.

header_length
    The length of the \ :c:type:`struct rt2x00dump_hdr <rt2x00dump_hdr>`\  structure. This is
    used for compatibility reasons so userspace can easily determine
    the location of the next field in the dump.

desc_length
    The length of the device descriptor.

data_length
    The length of the frame data (including the ieee802.11 header.

chip_rt
    RT chipset

chip_rf
    RF chipset

chip_rev
    Chipset revision

type
    The frame type (&rt2x00_dump_type)

queue_index
    The index number of the data queue.

entry_index
    The index number of the entry inside the data queue.

timestamp_sec
    Timestamp - seconds

timestamp_usec
    Timestamp - microseconds

.. _`rt2x00dump_hdr.description`:

Description
-----------

Each frame dumped to the debugfs file starts with this header
attached. This header contains the description of the actual
frame which was dumped.

New fields inside the structure must be appended to the end of
the structure. This way userspace tools compiled for earlier
header versions can still correctly handle the frame dump
(although they will not handle all data passed to them in the dump).

.. This file was automatic generated / don't edit.

