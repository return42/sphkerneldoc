.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/logfs/logfs_abi.h

.. _`logfs_segment_header`:

struct logfs_segment_header
===========================

.. c:type:: struct logfs_segment_header

    per-segment header in the ostore

.. _`logfs_segment_header.definition`:

Definition
----------

.. code-block:: c

    struct logfs_segment_header {
        __be32 crc;
        __be16 pad;
        __u8 type;
        __u8 level;
        __be32 segno;
        __be32 ec;
        __be64 gec;
    }

.. _`logfs_segment_header.members`:

Members
-------

crc
    crc32 of header (there is no data)

pad
    unused, must be 0

type
    segment type, see above

level
    GC level for all objects in this segment

segno
    segment number

ec
    erase count for this segment

gec
    global erase count at time of writing

.. _`logfs_disk_super`:

struct logfs_disk_super
=======================

.. c:type:: struct logfs_disk_super

    on-medium superblock

.. _`logfs_disk_super.definition`:

Definition
----------

.. code-block:: c

    struct logfs_disk_super {
        struct logfs_segment_header ds_sh;
        __be64 ds_magic;
        __be32 ds_crc;
        __u8 ds_ifile_levels;
        __u8 ds_iblock_levels;
        __u8 ds_data_levels;
        __u8 ds_segment_shift;
        __u8 ds_block_shift;
        __u8 ds_write_shift;
        __u8 pad0[6];
        __be64 ds_filesystem_size;
        __be32 ds_segment_size;
        __be32 ds_bad_seg_reserve;
        __be64 ds_feature_incompat;
        __be64 ds_feature_ro_compat;
        __be64 ds_feature_compat;
        __be64 ds_feature_flags;
        __be64 ds_root_reserve;
        __be64 ds_speed_reserve;
        __be32 ds_journal_seg[LOGFS_JOURNAL_SEGS];
        __be64 ds_super_ofs[2];
        __be64 pad3[8];
    }

.. _`logfs_disk_super.members`:

Members
-------

ds_sh
    *undescribed*

ds_magic
    magic number, must equal LOGFS_MAGIC

ds_crc
    crc32 of structure starting with the next field

ds_ifile_levels
    maximum number of levels for ifile

ds_iblock_levels
    maximum number of levels for regular files

ds_data_levels
    number of separate levels for data

ds_segment_shift
    log2 of segment size

ds_block_shift
    log2 of block size

ds_write_shift
    log2 of write size

pad0
    reserved, must be 0

ds_filesystem_size
    *undescribed*

ds_segment_size
    *undescribed*

ds_bad_seg_reserve
    number of segments reserved to handle bad blocks

ds_feature_incompat
    incompatible filesystem features

ds_feature_ro_compat
    read-only compatible filesystem features

ds_feature_compat
    compatible filesystem features

ds_feature_flags
    *undescribed*

ds_root_reserve
    bytes reserved for the superuser

ds_speed_reserve
    bytes reserved to speed up GC

ds_journal_seg
    segments used by primary journal

pad3
    reserved, must be 0

.. _`logfs_disk_super.description`:

Description
-----------

Contains only read-only fields.  Read-write fields like the amount of used
space is tracked in the dynamic superblock, which is stored in the journal.

.. _`logfs_object_header`:

struct logfs_object_header
==========================

.. c:type:: struct logfs_object_header

    per-object header in the ostore

.. _`logfs_object_header.definition`:

Definition
----------

.. code-block:: c

    struct logfs_object_header {
        __be32 crc;
        __be16 len;
        __u8 type;
        __u8 compr;
        __be64 ino;
        __be64 bix;
        __be32 data_crc;
    }

.. _`logfs_object_header.members`:

Members
-------

crc
    crc32 of header, excluding data_crc

len
    length of data

type
    object type, see above

compr
    compression type

ino
    inode number

bix
    block index

data_crc
    crc32 of payload

.. _`logfs_disk_inode`:

struct logfs_disk_inode
=======================

.. c:type:: struct logfs_disk_inode

    on-medium inode

.. _`logfs_disk_inode.definition`:

Definition
----------

.. code-block:: c

    struct logfs_disk_inode {
        __be16 di_mode;
        __u8 di_height;
        __u8 di_pad;
        __be32 di_flags;
        __be32 di_uid;
        __be32 di_gid;
        __be64 di_ctime;
        __be64 di_mtime;
        __be64 di_atime;
        __be32 di_refcount;
        __be32 di_generation;
        __be64 di_used_bytes;
        __be64 di_size;
        __be64 di_data[LOGFS_EMBEDDED_FIELDS];
    }

.. _`logfs_disk_inode.members`:

Members
-------

di_mode
    file mode

di_height
    *undescribed*

di_pad
    reserved, must be 0

di_flags
    inode flags, see above

di_uid
    user id

di_gid
    group id

di_ctime
    change time

di_mtime
    modify time

di_atime
    *undescribed*

di_refcount
    reference count (aka nlink or link count)

di_generation
    inode generation, for nfs

di_used_bytes
    number of bytes used

di_size
    file size

di_data
    data pointers

.. _`logfs_segment_entry`:

struct logfs_segment_entry
==========================

.. c:type:: struct logfs_segment_entry

    segment file entry

.. _`logfs_segment_entry.definition`:

Definition
----------

.. code-block:: c

    struct logfs_segment_entry {
        __be32 ec_level;
        __be32 valid;
    }

.. _`logfs_segment_entry.members`:

Members
-------

ec_level
    erase count and level

valid
    number of valid bytes

.. _`logfs_segment_entry.description`:

Description
-----------

Segment file contains one entry for every segment.  ec_level contains the
erasecount in the upper 28 bits and the level in the lower 4 bits.  An
ec_level of BADSEG (-1) identifies bad segments.  valid contains the number
of valid bytes or RESERVED (-1 again) if the segment is used for either the
superblock or the journal, or when the segment is bad.

.. _`logfs_journal_header`:

struct logfs_journal_header
===========================

.. c:type:: struct logfs_journal_header

    header for journal entries (JEs)

.. _`logfs_journal_header.definition`:

Definition
----------

.. code-block:: c

    struct logfs_journal_header {
        __be32 h_crc;
        __be16 h_len;
        __be16 h_datalen;
        __be16 h_type;
        __u8 h_compr;
        __u8 h_pad[5];
    }

.. _`logfs_journal_header.members`:

Members
-------

h_crc
    crc32 of journal entry

h_len
    length of compressed journal entry,
    not including header

h_datalen
    length of uncompressed data

h_type
    JE type

h_compr
    compression type

h_pad
    reserved

.. _`logfs_je_area`:

struct logfs_je_area
====================

.. c:type:: struct logfs_je_area

    wbuf header

.. _`logfs_je_area.definition`:

Definition
----------

.. code-block:: c

    struct logfs_je_area {
        __be32 segno;
        __be32 used_bytes;
        __u8 gc_level;
        __u8 vim;
    }

.. _`logfs_je_area.members`:

Members
-------

segno
    segment number of area

used_bytes
    number of bytes already used

gc_level
    GC level

vim
    life expectancy of data

.. _`logfs_je_area.description`:

Description
-----------

"Areas" are segments currently being used for writing.  There is at least
one area per GC level.  Several may be used to separate long-living from
short-living data.  If an area with unknown vim is encountered, it can
simply be closed.
The write buffer immediately follow this header.

.. _`logfs_je_dynsb`:

struct logfs_je_dynsb
=====================

.. c:type:: struct logfs_je_dynsb

    dynamic superblock

.. _`logfs_je_dynsb.definition`:

Definition
----------

.. code-block:: c

    struct logfs_je_dynsb {
        __be64 ds_gec;
        __be64 ds_sweeper;
        __be64 ds_rename_dir;
        __be64 ds_rename_pos;
        __be64 ds_victim_ino;
        __be64 ds_victim_parent;
        __be64 ds_used_bytes;
        __be32 ds_generation;
        __be32 pad;
    }

.. _`logfs_je_dynsb.members`:

Members
-------

ds_gec
    global erase count

ds_sweeper
    current position of GC "sweeper"

ds_rename_dir
    source directory ino (see dir.c documentation)

ds_rename_pos
    position of source dd (see dir.c documentation)

ds_victim_ino
    parent inode of victim (see dir.c)

ds_victim_parent
    *undescribed*

ds_used_bytes
    number of used bytes

ds_generation
    *undescribed*

pad
    *undescribed*

.. _`logfs_je_anchor`:

struct logfs_je_anchor
======================

.. c:type:: struct logfs_je_anchor

    anchor of filesystem tree, aka master inode

.. _`logfs_je_anchor.definition`:

Definition
----------

.. code-block:: c

    struct logfs_je_anchor {
        __be64 da_size;
        __be64 da_last_ino;
        __be64 da_used_bytes;
        u8 da_height;
        u8 pad[7];
        __be64 da_data[LOGFS_EMBEDDED_FIELDS];
    }

.. _`logfs_je_anchor.members`:

Members
-------

da_size
    size of inode file

da_last_ino
    last created inode

da_used_bytes
    number of bytes used

da_height
    *undescribed*

da_data
    data pointers

.. _`logfs_je_spillout`:

struct logfs_je_spillout
========================

.. c:type:: struct logfs_je_spillout

    spillout entry (from 1st to 2nd journal)

.. _`logfs_je_spillout.definition`:

Definition
----------

.. code-block:: c

    struct logfs_je_spillout {
        __be64 so_segment[0];
    }

.. _`logfs_je_spillout.members`:

Members
-------

so_segment
    segments used for 2nd journal

.. _`logfs_je_spillout.description`:

Description
-----------

Length of the array is given by h_len field in the header.

.. _`logfs_je_journal_ec`:

struct logfs_je_journal_ec
==========================

.. c:type:: struct logfs_je_journal_ec

    erase counts for all journal segments

.. _`logfs_je_journal_ec.definition`:

Definition
----------

.. code-block:: c

    struct logfs_je_journal_ec {
        __be32 ec[0];
    }

.. _`logfs_je_journal_ec.members`:

Members
-------

ec
    erase count

.. _`logfs_je_journal_ec.description`:

Description
-----------

Length of the array is given by h_len field in the header.

.. _`logfs_je_free_segments`:

struct logfs_je_free_segments
=============================

.. c:type:: struct logfs_je_free_segments

    list of free segmetns with erase count

.. _`logfs_je_free_segments.definition`:

Definition
----------

.. code-block:: c

    struct logfs_je_free_segments {
        __be32 segno;
        __be32 ec;
    }

.. _`logfs_je_free_segments.members`:

Members
-------

segno
    *undescribed*

ec
    *undescribed*

.. _`logfs_seg_alias`:

struct logfs_seg_alias
======================

.. c:type:: struct logfs_seg_alias

    list of segment aliases

.. _`logfs_seg_alias.definition`:

Definition
----------

.. code-block:: c

    struct logfs_seg_alias {
        __be32 old_segno;
        __be32 new_segno;
    }

.. _`logfs_seg_alias.members`:

Members
-------

old_segno
    *undescribed*

new_segno
    *undescribed*

.. _`logfs_obj_alias`:

struct logfs_obj_alias
======================

.. c:type:: struct logfs_obj_alias

    list of object aliases

.. _`logfs_obj_alias.definition`:

Definition
----------

.. code-block:: c

    struct logfs_obj_alias {
        __be64 ino;
        __be64 bix;
        __be64 val;
        u8 level;
        u8 pad[5];
        __be16 child_no;
    }

.. _`logfs_obj_alias.members`:

Members
-------

ino
    *undescribed*

bix
    *undescribed*

val
    *undescribed*

level
    *undescribed*

child_no
    *undescribed*

.. This file was automatic generated / don't edit.

