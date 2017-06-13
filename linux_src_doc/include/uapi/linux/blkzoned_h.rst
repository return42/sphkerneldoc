.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/blkzoned.h

.. _`blk_zone_type`:

enum blk_zone_type
==================

.. c:type:: enum blk_zone_type

    Types of zones allowed in a zoned device.

.. _`blk_zone_type.definition`:

Definition
----------

.. code-block:: c

    enum blk_zone_type {
        BLK_ZONE_TYPE_CONVENTIONAL,
        BLK_ZONE_TYPE_SEQWRITE_REQ,
        BLK_ZONE_TYPE_SEQWRITE_PREF
    };

.. _`blk_zone_type.constants`:

Constants
---------

BLK_ZONE_TYPE_CONVENTIONAL
    The zone has no write pointer and can be writen
    randomly. Zone reset has no effect on the zone.

BLK_ZONE_TYPE_SEQWRITE_REQ
    The zone must be written sequentially

BLK_ZONE_TYPE_SEQWRITE_PREF
    The zone can be written non-sequentially

.. _`blk_zone_type.description`:

Description
-----------

Any other value not defined is reserved and must be considered as invalid.

.. _`blk_zone_cond`:

enum blk_zone_cond
==================

.. c:type:: enum blk_zone_cond

    Condition [state] of a zone in a zoned device.

.. _`blk_zone_cond.definition`:

Definition
----------

.. code-block:: c

    enum blk_zone_cond {
        BLK_ZONE_COND_NOT_WP,
        BLK_ZONE_COND_EMPTY,
        BLK_ZONE_COND_IMP_OPEN,
        BLK_ZONE_COND_EXP_OPEN,
        BLK_ZONE_COND_CLOSED,
        BLK_ZONE_COND_READONLY,
        BLK_ZONE_COND_FULL,
        BLK_ZONE_COND_OFFLINE
    };

.. _`blk_zone_cond.constants`:

Constants
---------

BLK_ZONE_COND_NOT_WP
    The zone has no write pointer, it is conventional.

BLK_ZONE_COND_EMPTY
    The zone is empty.

BLK_ZONE_COND_IMP_OPEN
    The zone is open, but not explicitly opened.

BLK_ZONE_COND_EXP_OPEN
    The zones was explicitly opened by an
    OPEN ZONE command.

BLK_ZONE_COND_CLOSED
    The zone was [explicitly] closed after writing.

BLK_ZONE_COND_READONLY
    The zone is read-only.

BLK_ZONE_COND_FULL
    The zone is marked as full, possibly by a zone
    FINISH ZONE command.

BLK_ZONE_COND_OFFLINE
    The zone is offline (sectors cannot be read/written).

.. _`blk_zone_cond.description`:

Description
-----------

The Zone Condition state machine in the ZBC/ZAC standards maps the above

.. _`blk_zone_cond.deinitions-as`:

deinitions as
-------------

- ZC1: Empty         \| BLK_ZONE_EMPTY
- ZC2: Implicit Open \| BLK_ZONE_COND_IMP_OPEN
- ZC3: Explicit Open \| BLK_ZONE_COND_EXP_OPEN
- ZC4: Closed        \| BLK_ZONE_CLOSED
- ZC5: Full          \| BLK_ZONE_FULL
- ZC6: Read Only     \| BLK_ZONE_READONLY
- ZC7: Offline       \| BLK_ZONE_OFFLINE

Conditions 0x5 to 0xC are reserved by the current ZBC/ZAC spec and should
be considered invalid.

.. _`blk_zone`:

struct blk_zone
===============

.. c:type:: struct blk_zone

    Zone descriptor for BLKREPORTZONE ioctl.

.. _`blk_zone.definition`:

Definition
----------

.. code-block:: c

    struct blk_zone {
        __u64 start;
        __u64 len;
        __u64 wp;
        __u8 type;
        __u8 cond;
        __u8 non_seq;
        __u8 reset;
        __u8 reserved;
    }

.. _`blk_zone.members`:

Members
-------

start
    Zone start in 512 B sector units

len
    Zone length in 512 B sector units

wp
    Zone write pointer location in 512 B sector units

type
    see enum blk_zone_type for possible values

cond
    see enum blk_zone_cond for possible values

non_seq
    Flag indicating that the zone is using non-sequential resources
    (for host-aware zoned block devices only).

reset
    Flag indicating that a zone reset is recommended.

reserved
    Padding to 64 B to match the ZBC/ZAC defined zone descriptor size.

.. _`blk_zone.description`:

Description
-----------

start, len and wp use the regular 512 B sector unit, regardless of the
device logical block size. The overall structure size is 64 B to match the
ZBC/ZAC defined zone descriptor and allow support for future additional
zone information.

.. _`blk_zone_report`:

struct blk_zone_report
======================

.. c:type:: struct blk_zone_report

    BLKREPORTZONE ioctl request/reply

.. _`blk_zone_report.definition`:

Definition
----------

.. code-block:: c

    struct blk_zone_report {
        __u64 sector;
        __u32 nr_zones;
        __u8 reserved;
        struct blk_zone zones;
    }

.. _`blk_zone_report.members`:

Members
-------

sector
    starting sector of report

nr_zones
    IN maximum / OUT actual

reserved
    padding to 16 byte alignment

zones
    Space to hold \ ``nr_zones``\  \ ``zones``\  entries on reply.

.. _`blk_zone_report.description`:

Description
-----------

The array of at most \ ``nr_zones``\  must follow this structure in memory.

.. _`blk_zone_range`:

struct blk_zone_range
=====================

.. c:type:: struct blk_zone_range

    BLKRESETZONE ioctl request

.. _`blk_zone_range.definition`:

Definition
----------

.. code-block:: c

    struct blk_zone_range {
        __u64 sector;
        __u64 nr_sectors;
    }

.. _`blk_zone_range.members`:

Members
-------

sector
    starting sector of the first zone to issue reset write pointer

nr_sectors
    Total number of sectors of 1 or more zones to reset

.. _`blkreportzone`:

BLKREPORTZONE
=============

.. c:function::  BLKREPORTZONE()

.. This file was automatic generated / don't edit.

