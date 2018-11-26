.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/mtd/ubi-user.h

.. _`ubi_attach_req`:

struct ubi_attach_req
=====================

.. c:type:: struct ubi_attach_req

    attach MTD device request.

.. _`ubi_attach_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_attach_req {
        __s32 ubi_num;
        __s32 mtd_num;
        __s32 vid_hdr_offset;
        __s16 max_beb_per1024;
        __s8 padding[10];
    }

.. _`ubi_attach_req.members`:

Members
-------

ubi_num
    UBI device number to create

mtd_num
    MTD device number to attach

vid_hdr_offset
    VID header offset (use defaults if \ ``0``\ )

max_beb_per1024
    maximum expected number of bad PEB per 1024 PEBs

padding
    reserved for future, not used, has to be zeroed

.. _`ubi_attach_req.description`:

Description
-----------

This data structure is used to specify MTD device UBI has to attach and the
parameters it has to use. The number which should be assigned to the new UBI
device is passed in \ ``ubi_num``\ . UBI may automatically assign the number if
\ ``UBI_DEV_NUM_AUTO``\  is passed. In this case, the device number is returned in
\ ``ubi_num``\ .

Most applications should pass \ ``0``\  in \ ``vid_hdr_offset``\  to make UBI use default
offset of the VID header within physical eraseblocks. The default offset is
the next min. I/O unit after the EC header. For example, it will be offset
512 in case of a 512 bytes page NAND flash with no sub-page support. Or
it will be 512 in case of a 2KiB page NAND flash with 4 512-byte sub-pages.

But in rare cases, if this optimizes things, the VID header may be placed to
a different offset. For example, the boot-loader might do things faster if
the VID header sits at the end of the first 2KiB NAND page with 4 sub-pages.
As the boot-loader would not normally need to read EC headers (unless it
needs UBI in RW mode), it might be faster to calculate ECC. This is weird
example, but it real-life example. So, in this example, \ ``vid_hdr_offer``\  would
be 2KiB-64 bytes = 1984. Note, that this position is not even 512-bytes
aligned, which is OK, as UBI is clever enough to realize this is 4th
sub-page of the first page and add needed padding.

The \ ``max_beb_per1024``\  is the maximum amount of bad PEBs UBI expects on the
UBI device per 1024 eraseblocks.  This value is often given in an other form
in the NAND datasheet (min NVB i.e. minimal number of valid blocks). The

.. _`ubi_attach_req.maximum-expected-bad-eraseblocks-per-1024-is-then`:

maximum expected bad eraseblocks per 1024 is then
-------------------------------------------------

1024 \* (1 - MinNVB / MaxNVB)
Which gives 20 for most NAND devices.  This limit is used in order to derive
amount of eraseblock UBI reserves for handling new bad blocks. If the device
has more bad eraseblocks than this limit, UBI does not reserve any physical
eraseblocks for new bad eraseblocks, but attempts to use available
eraseblocks (if any). The accepted range is 0-768. If 0 is given, the
default kernel value of \ ``CONFIG_MTD_UBI_BEB_LIMIT``\  will be used.

.. _`ubi_mkvol_req`:

struct ubi_mkvol_req
====================

.. c:type:: struct ubi_mkvol_req

    volume description data structure used in volume creation requests.

.. _`ubi_mkvol_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_mkvol_req {
        __s32 vol_id;
        __s32 alignment;
        __s64 bytes;
        __s8 vol_type;
        __u8 flags;
        __s16 name_len;
        __s8 padding2[4];
        char name[UBI_MAX_VOLUME_NAME + 1];
    }

.. _`ubi_mkvol_req.members`:

Members
-------

vol_id
    volume number

alignment
    volume alignment

bytes
    volume size in bytes

vol_type
    volume type (%UBI_DYNAMIC_VOLUME or \ ``UBI_STATIC_VOLUME``\ )

flags
    volume flags (%UBI_VOL_SKIP_CRC_CHECK_FLG)

name_len
    volume name length

padding2
    reserved for future, not used, has to be zeroed

name
    volume name

.. _`ubi_mkvol_req.description`:

Description
-----------

This structure is used by user-space programs when creating new volumes. The
\ ``used_bytes``\  field is only necessary when creating static volumes.

The \ ``alignment``\  field specifies the required alignment of the volume logical
eraseblock. This means, that the size of logical eraseblocks will be aligned
to this number, i.e.,
(UBI device logical eraseblock size) mod (@alignment) = 0.

To put it differently, the logical eraseblock of this volume may be slightly
shortened in order to make it properly aligned. The alignment has to be
multiple of the flash minimal input/output unit, or \ ``1``\  to utilize the entire
available space of logical eraseblocks.

The \ ``alignment``\  field may be useful, for example, when one wants to maintain
a block device on top of an UBI volume. In this case, it is desirable to fit
an integer number of blocks in logical eraseblocks of this UBI volume. With
alignment it is possible to update this volume using plane UBI volume image
BLOBs, without caring about how to properly align them.

.. _`ubi_rsvol_req`:

struct ubi_rsvol_req
====================

.. c:type:: struct ubi_rsvol_req

    a data structure used in volume re-size requests.

.. _`ubi_rsvol_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_rsvol_req {
        __s64 bytes;
        __s32 vol_id;
    }

.. _`ubi_rsvol_req.members`:

Members
-------

bytes
    new size of the volume in bytes

vol_id
    ID of the volume to re-size

.. _`ubi_rsvol_req.description`:

Description
-----------

Re-sizing is possible for both dynamic and static volumes. But while dynamic
volumes may be re-sized arbitrarily, static volumes cannot be made to be
smaller than the number of bytes they bear. To arbitrarily shrink a static
volume, it must be wiped out first (by means of volume update operation with
zero number of bytes).

.. _`ubi_rnvol_req`:

struct ubi_rnvol_req
====================

.. c:type:: struct ubi_rnvol_req

    volumes re-name request.

.. _`ubi_rnvol_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_rnvol_req {
        __s32 count;
        __s8 padding1[12];
        struct {
            __s32 vol_id;
            __s16 name_len;
            __s8 padding2[2];
            char name[UBI_MAX_VOLUME_NAME + 1];
        } ents[UBI_MAX_RNVOL];
    }

.. _`ubi_rnvol_req.members`:

Members
-------

count
    count of volumes to re-name

padding1
    reserved for future, not used, has to be zeroed

ents
    *undescribed*

.. _`ubi_rnvol_req.description`:

Description
-----------

UBI allows to re-name up to \ ``32``\  volumes at one go. The count of volumes to
re-name is specified in the \ ``count``\  field. The ID of the volumes to re-name
and the new names are specified in the \ ``vol_id``\  and \ ``name``\  fields.

The UBI volume re-name operation is atomic, which means that should power cut
happen, the volumes will have either old name or new name. So the possible
use-cases of this command is atomic upgrade. Indeed, to upgrade, say, volumes
A and B one may create temporary volumes \ ``A1``\  and \ ``B1``\  with the new contents,
then atomically re-name A1->A and B1->B, in which case old \ ``A``\  and \ ``B``\  will
be removed.

If it is not desirable to remove old A and B, the re-name request has to

.. _`ubi_rnvol_req.contain-4-entries`:

contain 4 entries
-----------------

A1->A, A->A1, B1->B, B->B1, in which case old A1 and B1
become A and B, and old A and B will become A1 and B1.

.. _`ubi_rnvol_req.it-is-also-ok-to-request`:

It is also OK to request
------------------------

A1->A, A1->X, B1->B, B->Y, in which case old A1
and B1 become A and B, and old A and B become X and Y.

In other words, in case of re-naming into an existing volume name, the
existing volume is removed, unless it is re-named as well at the same
re-name request.

.. _`ubi_leb_change_req`:

struct ubi_leb_change_req
=========================

.. c:type:: struct ubi_leb_change_req

    a data structure used in atomic LEB change requests.

.. _`ubi_leb_change_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_leb_change_req {
        __s32 lnum;
        __s32 bytes;
        __s8 dtype;
        __s8 padding[7];
    }

.. _`ubi_leb_change_req.members`:

Members
-------

lnum
    logical eraseblock number to change

bytes
    how many bytes will be written to the logical eraseblock

dtype
    pass "3" for better compatibility with old kernels

padding
    reserved for future, not used, has to be zeroed

.. _`ubi_leb_change_req.description`:

Description
-----------

The \ ``dtype``\  field used to inform UBI about what kind of data will be written

.. _`ubi_leb_change_req.to-the-leb`:

to the LEB
----------

long term (value 1), short term (value 2), unknown (value 3).
UBI tried to pick a PEB with lower erase counter for short term data and a
PEB with higher erase counter for long term data. But this was not really
used because users usually do not know this and could easily mislead UBI. We
removed this feature in May 2012. UBI currently just ignores the \ ``dtype``\ 
field. But for better compatibility with older kernels it is recommended to
set \ ``dtype``\  to 3 (unknown).

.. _`ubi_map_req`:

struct ubi_map_req
==================

.. c:type:: struct ubi_map_req

    a data structure used in map LEB requests.

.. _`ubi_map_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_map_req {
        __s32 lnum;
        __s8 dtype;
        __s8 padding[3];
    }

.. _`ubi_map_req.members`:

Members
-------

lnum
    logical eraseblock number to unmap

dtype
    pass "3" for better compatibility with old kernels

padding
    reserved for future, not used, has to be zeroed

.. _`ubi_set_vol_prop_req`:

struct ubi_set_vol_prop_req
===========================

.. c:type:: struct ubi_set_vol_prop_req

    a data structure used to set an UBI volume property.

.. _`ubi_set_vol_prop_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_set_vol_prop_req {
        __u8 property;
        __u8 padding[7];
        __u64 value;
    }

.. _`ubi_set_vol_prop_req.members`:

Members
-------

property
    property to set (%UBI_VOL_PROP_DIRECT_WRITE)

padding
    reserved for future, not used, has to be zeroed

value
    value to set

.. _`ubi_blkcreate_req`:

struct ubi_blkcreate_req
========================

.. c:type:: struct ubi_blkcreate_req

    a data structure used in block creation requests.

.. _`ubi_blkcreate_req.definition`:

Definition
----------

.. code-block:: c

    struct ubi_blkcreate_req {
        __s8 padding[128];
    }

.. _`ubi_blkcreate_req.members`:

Members
-------

padding
    reserved for future, not used, has to be zeroed

.. This file was automatic generated / don't edit.

