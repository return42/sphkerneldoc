.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/ubi-media.h

.. _`ubi_ec_hdr`:

struct ubi_ec_hdr
=================

.. c:type:: struct ubi_ec_hdr

    UBI erase counter header.

.. _`ubi_ec_hdr.definition`:

Definition
----------

.. code-block:: c

    struct ubi_ec_hdr {
        __be32 magic;
        __u8 version;
        __u8 padding1[3];
        __be64 ec;
        __be32 vid_hdr_offset;
        __be32 data_offset;
        __be32 image_seq;
        __u8 padding2[32];
        __be32 hdr_crc;
    }

.. _`ubi_ec_hdr.members`:

Members
-------

magic
    erase counter header magic number (%UBI_EC_HDR_MAGIC)

version
    version of UBI implementation which is supposed to accept this
    UBI image

padding1
    reserved for future, zeroes

ec
    the erase counter

vid_hdr_offset
    where the VID header starts

data_offset
    where the user data start

image_seq
    image sequence number

padding2
    reserved for future, zeroes

hdr_crc
    erase counter header CRC checksum

.. _`ubi_ec_hdr.description`:

Description
-----------

The erase counter header takes 64 bytes and has a plenty of unused space for
future usage. The unused fields are zeroed. The \ ``version``\  field is used to
indicate the version of UBI implementation which is supposed to be able to
work with this UBI image. If \ ``version``\  is greater than the current UBI
version, the image is rejected. This may be useful in future if something
is changed radically. This field is duplicated in the volume identifier
header.

The \ ``vid_hdr_offset``\  and \ ``data_offset``\  fields contain the offset of the the
volume identifier header and user data, relative to the beginning of the
physical eraseblock. These values have to be the same for all physical
eraseblocks.

The \ ``image_seq``\  field is used to validate a UBI image that has been prepared
for a UBI device. The \ ``image_seq``\  value can be any value, but it must be the
same on all eraseblocks. UBI will ensure that all new erase counter headers
also contain this value, and will check the value when attaching the flash.
One way to make use of \ ``image_seq``\  is to increase its value by one every time
an image is flashed over an existing image, then, if the flashing does not
complete, UBI will detect the error when attaching the media.

.. _`ubi_vid_hdr`:

struct ubi_vid_hdr
==================

.. c:type:: struct ubi_vid_hdr

    on-flash UBI volume identifier header.

.. _`ubi_vid_hdr.definition`:

Definition
----------

.. code-block:: c

    struct ubi_vid_hdr {
        __be32 magic;
        __u8 version;
        __u8 vol_type;
        __u8 copy_flag;
        __u8 compat;
        __be32 vol_id;
        __be32 lnum;
        __u8 padding1[4];
        __be32 data_size;
        __be32 used_ebs;
        __be32 data_pad;
        __be32 data_crc;
        __u8 padding2[4];
        __be64 sqnum;
        __u8 padding3[12];
        __be32 hdr_crc;
    }

.. _`ubi_vid_hdr.members`:

Members
-------

magic
    volume identifier header magic number (%UBI_VID_HDR_MAGIC)

version
    UBI implementation version which is supposed to accept this UBI
    image (%UBI_VERSION)

vol_type
    volume type (%UBI_VID_DYNAMIC or \ ``UBI_VID_STATIC``\ )

copy_flag
    if this logical eraseblock was copied from another physical
    eraseblock (for wear-leveling reasons)

compat
    compatibility of this volume (%0, \ ``UBI_COMPAT_DELETE``\ ,
    \ ``UBI_COMPAT_IGNORE``\ , \ ``UBI_COMPAT_PRESERVE``\ , or \ ``UBI_COMPAT_REJECT``\ )

vol_id
    ID of this volume

lnum
    logical eraseblock number

padding1
    reserved for future, zeroes

data_size
    how many bytes of data this logical eraseblock contains

used_ebs
    total number of used logical eraseblocks in this volume

data_pad
    how many bytes at the end of this physical eraseblock are not
    used

data_crc
    CRC checksum of the data stored in this logical eraseblock

padding2
    reserved for future, zeroes

sqnum
    sequence number

padding3
    reserved for future, zeroes

hdr_crc
    volume identifier header CRC checksum

.. _`ubi_vid_hdr.description`:

Description
-----------

The \ ``sqnum``\  is the value of the global sequence counter at the time when this
VID header was created. The global sequence counter is incremented each time
UBI writes a new VID header to the flash, i.e. when it maps a logical
eraseblock to a new physical eraseblock. The global sequence counter is an
unsigned 64-bit integer and we assume it never overflows. The \ ``sqnum``\ 
(sequence number) is used to distinguish between older and newer versions of
logical eraseblocks.

There are 2 situations when there may be more than one physical eraseblock
corresponding to the same logical eraseblock, i.e., having the same \ ``vol_id``\ 
and \ ``lnum``\  values in the volume identifier header. Suppose we have a logical
eraseblock L and it is mapped to the physical eraseblock P.

1. Because UBI may erase physical eraseblocks asynchronously, the following

.. _`ubi_vid_hdr.situation-is-possible`:

situation is possible
---------------------

L is asynchronously erased, so P is scheduled for
erasure, then L is written to,i.e. mapped to another physical eraseblock P1,
so P1 is written to, then an unclean reboot happens. Result - there are 2
physical eraseblocks P and P1 corresponding to the same logical eraseblock
L. But P1 has greater sequence number, so UBI picks P1 when it attaches the
flash.

2. From time to time UBI moves logical eraseblocks to other physical
eraseblocks for wear-leveling reasons. If, for example, UBI moves L from P
to P1, and an unclean reboot happens before P is physically erased, there
are two physical eraseblocks P and P1 corresponding to L and UBI has to
select one of them when the flash is attached. The \ ``sqnum``\  field says which
PEB is the original (obviously P will have lower \ ``sqnum``\ ) and the copy. But
it is not enough to select the physical eraseblock with the higher sequence
number, because the unclean reboot could have happen in the middle of the
copying process, so the data in P is corrupted. It is also not enough to
just select the physical eraseblock with lower sequence number, because the
data there may be old (consider a case if more data was added to P1 after
the copying). Moreover, the unclean reboot may happen when the erasure of P
was just started, so it result in unstable P, which is "mostly" OK, but
still has unstable bits.

UBI uses the \ ``copy_flag``\  field to indicate that this logical eraseblock is a
copy. UBI also calculates data CRC when the data is moved and stores it at
the \ ``data_crc``\  field of the copy (P1). So when UBI needs to pick one physical
eraseblock of two (P or P1), the \ ``copy_flag``\  of the newer one (P1) is
examined. If it is cleared, the situation is simple and the newer one is
picked. If it is set, the data CRC of the copy (P1) is examined. If the CRC
checksum is correct, this physical eraseblock is selected (P1). Otherwise
the older one (P) is selected.

.. _`ubi_vid_hdr.there-are-2-sorts-of-volumes-in-ubi`:

There are 2 sorts of volumes in UBI
-----------------------------------

user volumes and internal volumes.
Internal volumes are not seen from outside and are used for various internal
UBI purposes. In this implementation there is only one internal volume - the
layout volume. Internal volumes are the main mechanism of UBI extensions.
For example, in future one may introduce a journal internal volume. Internal
volumes have their own reserved range of IDs.

The \ ``compat``\  field is only used for internal volumes and contains the "degree
of their compatibility". It is always zero for user volumes. This field
provides a mechanism to introduce UBI extensions and to be still compatible
with older UBI binaries. For example, if someone introduced a journal in
future, he would probably use \ ``UBI_COMPAT_DELETE``\  compatibility for the
journal volume.  And in this case, older UBI binaries, which know nothing
about the journal volume, would just delete this volume and work perfectly
fine. This is similar to what Ext2fs does when it is fed by an Ext3fs image
- it just ignores the Ext3fs journal.

The \ ``data_crc``\  field contains the CRC checksum of the contents of the logical
eraseblock if this is a static volume. In case of dynamic volumes, it does
not contain the CRC checksum as a rule. The only exception is when the
data of the physical eraseblock was moved by the wear-leveling sub-system,
then the wear-leveling sub-system calculates the data CRC and stores it in
the \ ``data_crc``\  field. And of course, the \ ``copy_flag``\  is \ ``in``\  this case.

The \ ``data_size``\  field is used only for static volumes because UBI has to know
how many bytes of data are stored in this eraseblock. For dynamic volumes,
this field usually contains zero. The only exception is when the data of the
physical eraseblock was moved to another physical eraseblock for
wear-leveling reasons. In this case, UBI calculates CRC checksum of the
contents and uses both \ ``data_crc``\  and \ ``data_size``\  fields. In this case, the
\ ``data_size``\  field contains data size.

The \ ``used_ebs``\  field is used only for static volumes and indicates how many
eraseblocks the data of the volume takes. For dynamic volumes this field is
not used and always contains zero.

The \ ``data_pad``\  is calculated when volumes are created using the alignment
parameter. So, effectively, the \ ``data_pad``\  field reduces the size of logical
eraseblocks of this volume. This is very handy when one uses block-oriented
software (say, cramfs) on top of the UBI volume.

.. _`ubi_vtbl_record`:

struct ubi_vtbl_record
======================

.. c:type:: struct ubi_vtbl_record

    a record in the volume table.

.. _`ubi_vtbl_record.definition`:

Definition
----------

.. code-block:: c

    struct ubi_vtbl_record {
        __be32 reserved_pebs;
        __be32 alignment;
        __be32 data_pad;
        __u8 vol_type;
        __u8 upd_marker;
        __be16 name_len;
        __u8 name[UBI_VOL_NAME_MAX+1];
        __u8 flags;
        __u8 padding[23];
        __be32 crc;
    }

.. _`ubi_vtbl_record.members`:

Members
-------

reserved_pebs
    how many physical eraseblocks are reserved for this volume

alignment
    volume alignment

data_pad
    how many bytes are unused at the end of the each physical
    eraseblock to satisfy the requested alignment

vol_type
    volume type (%UBI_DYNAMIC_VOLUME or \ ``UBI_STATIC_VOLUME``\ )

upd_marker
    if volume update was started but not finished

name_len
    volume name length

name
    the volume name

flags
    volume flags (%UBI_VTBL_AUTORESIZE_FLG)

padding
    reserved, zeroes

crc
    a CRC32 checksum of the record

.. _`ubi_vtbl_record.description`:

Description
-----------

The volume table records are stored in the volume table, which is stored in
the layout volume. The layout volume consists of 2 logical eraseblock, each
of which contains a copy of the volume table (i.e., the volume table is
duplicated). The volume table is an array of \ :c:type:`struct ubi_vtbl_record <ubi_vtbl_record>`\ 
objects indexed by the volume ID.

If the size of the logical eraseblock is large enough to fit
\ ``UBI_MAX_VOLUMES``\  records, the volume table contains \ ``UBI_MAX_VOLUMES``\ 
records. Otherwise, it contains as many records as it can fit (i.e., size of
logical eraseblock divided by sizeof(struct ubi_vtbl_record)).

The \ ``upd_marker``\  flag is used to implement volume update. It is set to \ ``1``\ 
before update and set to \ ``0``\  after the update. So if the update operation was
interrupted, UBI knows that the volume is corrupted.

The \ ``alignment``\  field is specified when the volume is created and cannot be
later changed. It may be useful, for example, when a block-oriented file
system works on top of UBI. The \ ``data_pad``\  field is calculated using the
logical eraseblock size and \ ``alignment``\ . The alignment must be multiple to the
minimal flash I/O unit. If \ ``alignment``\  is 1, all the available space of
the physical eraseblocks is used.

Empty records contain all zeroes and the CRC checksum of those zeroes.

.. _`ubi_fm_sb`:

struct ubi_fm_sb
================

.. c:type:: struct ubi_fm_sb

    UBI fastmap super block

.. _`ubi_fm_sb.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_sb {
        __be32 magic;
        __u8 version;
        __u8 padding1[3];
        __be32 data_crc;
        __be32 used_blocks;
        __be32 block_loc[UBI_FM_MAX_BLOCKS];
        __be32 block_ec[UBI_FM_MAX_BLOCKS];
        __be64 sqnum;
        __u8 padding2[32];
    }

.. _`ubi_fm_sb.members`:

Members
-------

magic
    fastmap super block magic number (%UBI_FM_SB_MAGIC)

version
    format version of this fastmap

padding1
    *undescribed*

data_crc
    CRC over the fastmap data

used_blocks
    number of PEBs used by this fastmap

block_loc
    an array containing the location of all PEBs of the fastmap

block_ec
    the erase counter of each used PEB

sqnum
    highest sequence number value at the time while taking the fastmap

padding2
    *undescribed*

.. _`ubi_fm_hdr`:

struct ubi_fm_hdr
=================

.. c:type:: struct ubi_fm_hdr

    header of the fastmap data set

.. _`ubi_fm_hdr.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_hdr {
        __be32 magic;
        __be32 free_peb_count;
        __be32 used_peb_count;
        __be32 scrub_peb_count;
        __be32 bad_peb_count;
        __be32 erase_peb_count;
        __be32 vol_count;
        __u8 padding[4];
    }

.. _`ubi_fm_hdr.members`:

Members
-------

magic
    fastmap header magic number (%UBI_FM_HDR_MAGIC)

free_peb_count
    number of free PEBs known by this fastmap

used_peb_count
    number of used PEBs known by this fastmap

scrub_peb_count
    number of to be scrubbed PEBs known by this fastmap

bad_peb_count
    number of bad PEBs known by this fastmap

erase_peb_count
    number of bad PEBs which have to be erased

vol_count
    number of UBI volumes known by this fastmap

padding
    *undescribed*

.. _`ubi_fm_scan_pool`:

struct ubi_fm_scan_pool
=======================

.. c:type:: struct ubi_fm_scan_pool

    Fastmap pool PEBs to be scanned while attaching

.. _`ubi_fm_scan_pool.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_scan_pool {
        __be32 magic;
        __be16 size;
        __be16 max_size;
        __be32 pebs[UBI_FM_MAX_POOL_SIZE];
        __be32 padding[4];
    }

.. _`ubi_fm_scan_pool.members`:

Members
-------

magic
    pool magic numer (%UBI_FM_POOL_MAGIC)

size
    current pool size

max_size
    maximal pool size

pebs
    an array containing the location of all PEBs in this pool

padding
    *undescribed*

.. _`ubi_fm_ec`:

struct ubi_fm_ec
================

.. c:type:: struct ubi_fm_ec

    stores the erase counter of a PEB

.. _`ubi_fm_ec.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_ec {
        __be32 pnum;
        __be32 ec;
    }

.. _`ubi_fm_ec.members`:

Members
-------

pnum
    PEB number

ec
    ec of this PEB

.. _`ubi_fm_volhdr`:

struct ubi_fm_volhdr
====================

.. c:type:: struct ubi_fm_volhdr

    Fastmap volume header it identifies the start of an eba table

.. _`ubi_fm_volhdr.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_volhdr {
        __be32 magic;
        __be32 vol_id;
        __u8 vol_type;
        __u8 padding1[3];
        __be32 data_pad;
        __be32 used_ebs;
        __be32 last_eb_bytes;
        __u8 padding2[8];
    }

.. _`ubi_fm_volhdr.members`:

Members
-------

magic
    Fastmap volume header magic number (%UBI_FM_VHDR_MAGIC)

vol_id
    volume id of the fastmapped volume

vol_type
    type of the fastmapped volume

padding1
    *undescribed*

data_pad
    data_pad value of the fastmapped volume

used_ebs
    number of used LEBs within this volume

last_eb_bytes
    number of bytes used in the last LEB

padding2
    *undescribed*

.. _`ubi_fm_eba`:

struct ubi_fm_eba
=================

.. c:type:: struct ubi_fm_eba

    denotes an association between a PEB and LEB

.. _`ubi_fm_eba.definition`:

Definition
----------

.. code-block:: c

    struct ubi_fm_eba {
        __be32 magic;
        __be32 reserved_pebs;
        __be32 pnum[0];
    }

.. _`ubi_fm_eba.members`:

Members
-------

magic
    EBA table magic number

reserved_pebs
    number of table entries

pnum
    PEB number of LEB (LEB is the index)

.. This file was automatic generated / don't edit.

