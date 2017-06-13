.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/nilfs2_ondisk.h

.. _`nilfs_inode`:

struct nilfs_inode
==================

.. c:type:: struct nilfs_inode

    structure of an inode on disk

.. _`nilfs_inode.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_inode {
        __le64 i_blocks;
        __le64 i_size;
        __le64 i_ctime;
        __le64 i_mtime;
        __le32 i_ctime_nsec;
        __le32 i_mtime_nsec;
        __le32 i_uid;
        __le32 i_gid;
        __le16 i_mode;
        __le16 i_links_count;
        __le32 i_flags;
        __le64 i_bmap;
    #define i_device_code i_bmap
        __le64 i_xattr;
        __le32 i_generation;
        __le32 i_pad;
    }

.. _`nilfs_inode.members`:

Members
-------

i_blocks
    blocks count

i_size
    size in bytes

i_ctime
    creation time (seconds)

i_mtime
    modification time (seconds)

i_ctime_nsec
    creation time (nano seconds)

i_mtime_nsec
    modification time (nano seconds)

i_uid
    user id

i_gid
    group id

i_mode
    file mode

i_links_count
    links count

i_flags
    file flags

i_bmap
    block mapping

i_xattr
    extended attributes

i_generation
    file generation (for NFS)

i_pad
    padding

.. _`nilfs_super_root`:

struct nilfs_super_root
=======================

.. c:type:: struct nilfs_super_root

    structure of super root

.. _`nilfs_super_root.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_super_root {
        __le32 sr_sum;
        __le16 sr_bytes;
        __le16 sr_flags;
        __le64 sr_nongc_ctime;
        struct nilfs_inode sr_dat;
        struct nilfs_inode sr_cpfile;
        struct nilfs_inode sr_sufile;
    }

.. _`nilfs_super_root.members`:

Members
-------

sr_sum
    check sum

sr_bytes
    byte count of the structure

sr_flags
    flags (reserved)

sr_nongc_ctime
    write time of the last segment not for cleaner operation

sr_dat
    DAT file inode

sr_cpfile
    checkpoint file inode

sr_sufile
    segment usage file inode

.. _`nilfs_super_block`:

struct nilfs_super_block
========================

.. c:type:: struct nilfs_super_block

    structure of super block on disk

.. _`nilfs_super_block.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_super_block {
        __le32 s_rev_level;
        __le16 s_minor_rev_level;
        __le16 s_magic;
        __le16 s_bytes;
        __le16 s_flags;
        __le32 s_crc_seed;
        __le32 s_sum;
        __le32 s_log_block_size;
        __le64 s_nsegments;
        __le64 s_dev_size;
        __le64 s_first_data_block;
        __le32 s_blocks_per_segment;
        __le32 s_r_segments_percentage;
        __le64 s_last_cno;
        __le64 s_last_pseg;
        __le64 s_last_seq;
        __le64 s_free_blocks_count;
        __le64 s_ctime;
        __le64 s_mtime;
        __le64 s_wtime;
        __le16 s_mnt_count;
        __le16 s_max_mnt_count;
        __le16 s_state;
        __le16 s_errors;
        __le64 s_lastcheck;
        __le32 s_checkinterval;
        __le32 s_creator_os;
        __le16 s_def_resuid;
        __le16 s_def_resgid;
        __le32 s_first_ino;
        __le16 s_inode_size;
        __le16 s_dat_entry_size;
        __le16 s_checkpoint_size;
        __le16 s_segment_usage_size;
        __u8 s_uuid;
        char s_volume_name;
        __le32 s_c_interval;
        __le32 s_c_block_max;
        __le64 s_feature_compat;
        __le64 s_feature_compat_ro;
        __le64 s_feature_incompat;
        __u32 s_reserved;
    }

.. _`nilfs_super_block.members`:

Members
-------

s_rev_level
    *undescribed*

s_minor_rev_level
    *undescribed*

s_magic
    *undescribed*

s_bytes
    *undescribed*

s_flags
    *undescribed*

s_crc_seed
    *undescribed*

s_sum
    *undescribed*

s_log_block_size
    *undescribed*

s_nsegments
    *undescribed*

s_dev_size
    *undescribed*

s_first_data_block
    *undescribed*

s_blocks_per_segment
    *undescribed*

s_r_segments_percentage
    *undescribed*

s_last_cno
    *undescribed*

s_last_pseg
    *undescribed*

s_last_seq
    *undescribed*

s_free_blocks_count
    *undescribed*

s_ctime
    *undescribed*

s_mtime
    *undescribed*

s_wtime
    *undescribed*

s_mnt_count
    *undescribed*

s_max_mnt_count
    *undescribed*

s_state
    *undescribed*

s_errors
    *undescribed*

s_lastcheck
    *undescribed*

s_checkinterval
    *undescribed*

s_creator_os
    *undescribed*

s_def_resuid
    *undescribed*

s_def_resgid
    *undescribed*

s_first_ino
    *undescribed*

s_inode_size
    *undescribed*

s_dat_entry_size
    *undescribed*

s_checkpoint_size
    *undescribed*

s_segment_usage_size
    *undescribed*

s_uuid
    *undescribed*

s_volume_name
    *undescribed*

s_c_interval
    *undescribed*

s_c_block_max
    *undescribed*

s_feature_compat
    *undescribed*

s_feature_compat_ro
    *undescribed*

s_feature_incompat
    *undescribed*

s_reserved
    *undescribed*

.. _`nilfs_finfo`:

struct nilfs_finfo
==================

.. c:type:: struct nilfs_finfo

    file information

.. _`nilfs_finfo.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_finfo {
        __le64 fi_ino;
        __le64 fi_cno;
        __le32 fi_nblocks;
        __le32 fi_ndatablk;
    }

.. _`nilfs_finfo.members`:

Members
-------

fi_ino
    inode number

fi_cno
    checkpoint number

fi_nblocks
    number of blocks (including intermediate blocks)

fi_ndatablk
    number of file data blocks

.. _`nilfs_binfo_v`:

struct nilfs_binfo_v
====================

.. c:type:: struct nilfs_binfo_v

    information on a data block (except DAT)

.. _`nilfs_binfo_v.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_binfo_v {
        __le64 bi_vblocknr;
        __le64 bi_blkoff;
    }

.. _`nilfs_binfo_v.members`:

Members
-------

bi_vblocknr
    virtual block number

bi_blkoff
    block offset

.. _`nilfs_binfo_dat`:

struct nilfs_binfo_dat
======================

.. c:type:: struct nilfs_binfo_dat

    information on a DAT node block

.. _`nilfs_binfo_dat.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_binfo_dat {
        __le64 bi_blkoff;
        __u8 bi_level;
        __u8 bi_pad;
    }

.. _`nilfs_binfo_dat.members`:

Members
-------

bi_blkoff
    block offset

bi_level
    level

bi_pad
    padding

.. _`nilfs_binfo`:

union nilfs_binfo
=================

.. c:type:: struct nilfs_binfo

    block information

.. _`nilfs_binfo.definition`:

Definition
----------

.. code-block:: c

    union nilfs_binfo {
        struct nilfs_binfo_v bi_v;
        struct nilfs_binfo_dat bi_dat;
    }

.. _`nilfs_binfo.members`:

Members
-------

bi_v
    nilfs_binfo_v structure

bi_dat
    nilfs_binfo_dat structure

.. _`nilfs_segment_summary`:

struct nilfs_segment_summary
============================

.. c:type:: struct nilfs_segment_summary

    segment summary header

.. _`nilfs_segment_summary.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_segment_summary {
        __le32 ss_datasum;
        __le32 ss_sumsum;
        __le32 ss_magic;
        __le16 ss_bytes;
        __le16 ss_flags;
        __le64 ss_seq;
        __le64 ss_create;
        __le64 ss_next;
        __le32 ss_nblocks;
        __le32 ss_nfinfo;
        __le32 ss_sumbytes;
        __le32 ss_pad;
        __le64 ss_cno;
    }

.. _`nilfs_segment_summary.members`:

Members
-------

ss_datasum
    checksum of data

ss_sumsum
    checksum of segment summary

ss_magic
    magic number

ss_bytes
    size of this structure in bytes

ss_flags
    flags

ss_seq
    sequence number

ss_create
    creation timestamp

ss_next
    next segment

ss_nblocks
    number of blocks

ss_nfinfo
    number of finfo structures

ss_sumbytes
    total size of segment summary in bytes

ss_pad
    padding

ss_cno
    checkpoint number

.. _`nilfs_btree_node`:

struct nilfs_btree_node
=======================

.. c:type:: struct nilfs_btree_node

    header of B-tree node block

.. _`nilfs_btree_node.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_btree_node {
        __u8 bn_flags;
        __u8 bn_level;
        __le16 bn_nchildren;
        __le32 bn_pad;
    }

.. _`nilfs_btree_node.members`:

Members
-------

bn_flags
    flags

bn_level
    level

bn_nchildren
    number of children

bn_pad
    padding

.. _`nilfs_direct_node`:

struct nilfs_direct_node
========================

.. c:type:: struct nilfs_direct_node

    header of built-in bmap array

.. _`nilfs_direct_node.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_direct_node {
        __u8 dn_flags;
        __u8 pad;
    }

.. _`nilfs_direct_node.members`:

Members
-------

dn_flags
    flags

pad
    *undescribed*

.. _`nilfs_palloc_group_desc`:

struct nilfs_palloc_group_desc
==============================

.. c:type:: struct nilfs_palloc_group_desc

    block group descriptor

.. _`nilfs_palloc_group_desc.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_palloc_group_desc {
        __le32 pg_nfrees;
    }

.. _`nilfs_palloc_group_desc.members`:

Members
-------

pg_nfrees
    number of free entries in block group

.. _`nilfs_dat_entry`:

struct nilfs_dat_entry
======================

.. c:type:: struct nilfs_dat_entry

    disk address translation entry

.. _`nilfs_dat_entry.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_dat_entry {
        __le64 de_blocknr;
        __le64 de_start;
        __le64 de_end;
        __le64 de_rsv;
    }

.. _`nilfs_dat_entry.members`:

Members
-------

de_blocknr
    block number

de_start
    start checkpoint number

de_end
    end checkpoint number

de_rsv
    reserved for future use

.. _`nilfs_snapshot_list`:

struct nilfs_snapshot_list
==========================

.. c:type:: struct nilfs_snapshot_list

    snapshot list

.. _`nilfs_snapshot_list.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_snapshot_list {
        __le64 ssl_next;
        __le64 ssl_prev;
    }

.. _`nilfs_snapshot_list.members`:

Members
-------

ssl_next
    next checkpoint number on snapshot list

ssl_prev
    previous checkpoint number on snapshot list

.. _`nilfs_checkpoint`:

struct nilfs_checkpoint
=======================

.. c:type:: struct nilfs_checkpoint

    checkpoint structure

.. _`nilfs_checkpoint.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_checkpoint {
        __le32 cp_flags;
        __le32 cp_checkpoints_count;
        struct nilfs_snapshot_list cp_snapshot_list;
        __le64 cp_cno;
        __le64 cp_create;
        __le64 cp_nblk_inc;
        __le64 cp_inodes_count;
        __le64 cp_blocks_count;
        struct nilfs_inode cp_ifile_inode;
    }

.. _`nilfs_checkpoint.members`:

Members
-------

cp_flags
    flags

cp_checkpoints_count
    checkpoints count in a block

cp_snapshot_list
    snapshot list

cp_cno
    checkpoint number

cp_create
    creation timestamp

cp_nblk_inc
    number of blocks incremented by this checkpoint

cp_inodes_count
    inodes count

cp_blocks_count
    blocks count

cp_ifile_inode
    inode of ifile

.. _`nilfs_cpfile_header`:

struct nilfs_cpfile_header
==========================

.. c:type:: struct nilfs_cpfile_header

    checkpoint file header

.. _`nilfs_cpfile_header.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_cpfile_header {
        __le64 ch_ncheckpoints;
        __le64 ch_nsnapshots;
        struct nilfs_snapshot_list ch_snapshot_list;
    }

.. _`nilfs_cpfile_header.members`:

Members
-------

ch_ncheckpoints
    number of checkpoints

ch_nsnapshots
    number of snapshots

ch_snapshot_list
    snapshot list

.. _`nilfs_segment_usage`:

struct nilfs_segment_usage
==========================

.. c:type:: struct nilfs_segment_usage

    segment usage

.. _`nilfs_segment_usage.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_segment_usage {
        __le64 su_lastmod;
        __le32 su_nblocks;
        __le32 su_flags;
    }

.. _`nilfs_segment_usage.members`:

Members
-------

su_lastmod
    last modified timestamp

su_nblocks
    number of blocks in segment

su_flags
    flags

.. _`nilfs_sufile_header`:

struct nilfs_sufile_header
==========================

.. c:type:: struct nilfs_sufile_header

    segment usage file header

.. _`nilfs_sufile_header.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_sufile_header {
        __le64 sh_ncleansegs;
        __le64 sh_ndirtysegs;
        __le64 sh_last_alloc;
    }

.. _`nilfs_sufile_header.members`:

Members
-------

sh_ncleansegs
    number of clean segments

sh_ndirtysegs
    number of dirty segments

sh_last_alloc
    last allocated segment number

.. This file was automatic generated / don't edit.

