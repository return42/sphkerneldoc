.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/nilfs2_api.h

.. _`nilfs_cpinfo`:

struct nilfs_cpinfo
===================

.. c:type:: struct nilfs_cpinfo

    checkpoint information

.. _`nilfs_cpinfo.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_cpinfo {
        __u32 ci_flags;
        __u32 ci_pad;
        __u64 ci_cno;
        __u64 ci_create;
        __u64 ci_nblk_inc;
        __u64 ci_inodes_count;
        __u64 ci_blocks_count;
        __u64 ci_next;
    }

.. _`nilfs_cpinfo.members`:

Members
-------

ci_flags
    flags

ci_pad
    padding

ci_cno
    checkpoint number

ci_create
    creation timestamp

ci_nblk_inc
    number of blocks incremented by this checkpoint

ci_inodes_count
    inodes count

ci_blocks_count
    blocks count

ci_next
    next checkpoint number in snapshot list

.. _`nilfs_cpmode`:

struct nilfs_cpmode
===================

.. c:type:: struct nilfs_cpmode

    change checkpoint mode structure

.. _`nilfs_cpmode.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_cpmode {
        __u64 cm_cno;
        __u32 cm_mode;
        __u32 cm_pad;
    }

.. _`nilfs_cpmode.members`:

Members
-------

cm_cno
    checkpoint number

cm_mode
    mode of checkpoint

cm_pad
    padding

.. _`nilfs_argv`:

struct nilfs_argv
=================

.. c:type:: struct nilfs_argv

    argument vector

.. _`nilfs_argv.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_argv {
        __u64 v_base;
        __u32 v_nmembs;
        __u16 v_size;
        __u16 v_flags;
        __u64 v_index;
    }

.. _`nilfs_argv.members`:

Members
-------

v_base
    pointer on data array from userspace

v_nmembs
    number of members in data array

v_size
    size of data array in bytes

v_flags
    flags

v_index
    start number of target data items

.. _`nilfs_period`:

struct nilfs_period
===================

.. c:type:: struct nilfs_period

    period of checkpoint numbers

.. _`nilfs_period.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_period {
        __u64 p_start;
        __u64 p_end;
    }

.. _`nilfs_period.members`:

Members
-------

p_start
    start checkpoint number (inclusive)

p_end
    end checkpoint number (exclusive)

.. _`nilfs_cpstat`:

struct nilfs_cpstat
===================

.. c:type:: struct nilfs_cpstat

    checkpoint statistics

.. _`nilfs_cpstat.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_cpstat {
        __u64 cs_cno;
        __u64 cs_ncps;
        __u64 cs_nsss;
    }

.. _`nilfs_cpstat.members`:

Members
-------

cs_cno
    checkpoint number

cs_ncps
    number of checkpoints

cs_nsss
    number of snapshots

.. _`nilfs_sustat`:

struct nilfs_sustat
===================

.. c:type:: struct nilfs_sustat

    segment usage statistics

.. _`nilfs_sustat.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_sustat {
        __u64 ss_nsegs;
        __u64 ss_ncleansegs;
        __u64 ss_ndirtysegs;
        __u64 ss_ctime;
        __u64 ss_nongc_ctime;
        __u64 ss_prot_seq;
    }

.. _`nilfs_sustat.members`:

Members
-------

ss_nsegs
    number of segments

ss_ncleansegs
    number of clean segments

ss_ndirtysegs
    number of dirty segments

ss_ctime
    creation time of the last segment

ss_nongc_ctime
    creation time of the last segment not for GC

ss_prot_seq
    least sequence number of segments which must not be reclaimed

.. _`nilfs_vinfo`:

struct nilfs_vinfo
==================

.. c:type:: struct nilfs_vinfo

    virtual block number information

.. _`nilfs_vinfo.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_vinfo {
        __u64 vi_vblocknr;
        __u64 vi_start;
        __u64 vi_end;
        __u64 vi_blocknr;
    }

.. _`nilfs_vinfo.members`:

Members
-------

vi_vblocknr
    virtual block number

vi_start
    start checkpoint number (inclusive)

vi_end
    end checkpoint number (exclusive)

vi_blocknr
    disk block number

.. _`nilfs_vdesc`:

struct nilfs_vdesc
==================

.. c:type:: struct nilfs_vdesc

    descriptor of virtual block number

.. _`nilfs_vdesc.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_vdesc {
        __u64 vd_ino;
        __u64 vd_cno;
        __u64 vd_vblocknr;
        struct nilfs_period vd_period;
        __u64 vd_blocknr;
        __u64 vd_offset;
        __u32 vd_flags;
        __u32 vd_pad;
    }

.. _`nilfs_vdesc.members`:

Members
-------

vd_ino
    inode number

vd_cno
    checkpoint number

vd_vblocknr
    virtual block number

vd_period
    period of checkpoint numbers

vd_blocknr
    disk block number

vd_offset
    logical block offset inside a file

vd_flags
    flags (data or node block)

vd_pad
    padding

.. _`nilfs_bdesc`:

struct nilfs_bdesc
==================

.. c:type:: struct nilfs_bdesc

    descriptor of disk block number

.. _`nilfs_bdesc.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_bdesc {
        __u64 bd_ino;
        __u64 bd_oblocknr;
        __u64 bd_blocknr;
        __u64 bd_offset;
        __u32 bd_level;
        __u32 bd_pad;
    }

.. _`nilfs_bdesc.members`:

Members
-------

bd_ino
    inode number

bd_oblocknr
    disk block address (for skipping dead blocks)

bd_blocknr
    disk block address

bd_offset
    logical block offset inside a file

bd_level
    level in the b-tree organization

bd_pad
    padding

.. This file was automatic generated / don't edit.

