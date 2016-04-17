.. -*- coding: utf-8; mode: rst -*-

===========
nilfs2_fs.h
===========


.. _`nilfs_inode`:

struct nilfs_inode
==================

.. c:type:: nilfs_inode

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
    __le64 i_bmap[NILFS_INODE_BMAP_SIZE];
    #define i_device_code	i_bmap[0]
    __le64 i_xattr;
    __le32 i_generation;
    __le32 i_pad;
  };


.. _`nilfs_inode.members`:

Members
-------

:``i_blocks``:
    blocks count

:``i_size``:
    size in bytes

:``i_ctime``:
    creation time (seconds)

:``i_mtime``:
    modification time (seconds)

:``i_ctime_nsec``:
    creation time (nano seconds)

:``i_mtime_nsec``:
    modification time (nano seconds)

:``i_uid``:
    user id

:``i_gid``:
    group id

:``i_mode``:
    file mode

:``i_links_count``:
    links count

:``i_flags``:
    file flags

:``i_bmap[NILFS_INODE_BMAP_SIZE]``:
    block mapping

:``i_xattr``:
    extended attributes

:``i_generation``:
    file generation (for NFS)

:``i_pad``:
    padding




.. _`nilfs_super_root`:

struct nilfs_super_root
=======================

.. c:type:: nilfs_super_root

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
  };


.. _`nilfs_super_root.members`:

Members
-------

:``sr_sum``:
    check sum

:``sr_bytes``:
    byte count of the structure

:``sr_flags``:
    flags (reserved)

:``sr_nongc_ctime``:
    write time of the last segment not for cleaner operation

:``sr_dat``:
    DAT file inode

:``sr_cpfile``:
    checkpoint file inode

:``sr_sufile``:
    segment usage file inode




.. _`nilfs_super_block`:

struct nilfs_super_block
========================

.. c:type:: nilfs_super_block

    structure of super block on disk


.. _`nilfs_super_block.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_super_block {
  };


.. _`nilfs_super_block.members`:

Members
-------




.. _`nilfs_finfo`:

struct nilfs_finfo
==================

.. c:type:: nilfs_finfo

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
  };


.. _`nilfs_finfo.members`:

Members
-------

:``fi_ino``:
    inode number

:``fi_cno``:
    checkpoint number

:``fi_nblocks``:
    number of blocks (including intermediate blocks)

:``fi_ndatablk``:
    number of file data blocks




.. _`nilfs_binfo_v`:

struct nilfs_binfo_v
====================

.. c:type:: nilfs_binfo_v

    information for the block to which a virtual block number is assigned


.. _`nilfs_binfo_v.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_binfo_v {
    __le64 bi_vblocknr;
    __le64 bi_blkoff;
  };


.. _`nilfs_binfo_v.members`:

Members
-------

:``bi_vblocknr``:
    virtual block number

:``bi_blkoff``:
    block offset




.. _`nilfs_binfo_dat`:

struct nilfs_binfo_dat
======================

.. c:type:: nilfs_binfo_dat

    information for the block which belongs to the DAT file


.. _`nilfs_binfo_dat.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_binfo_dat {
    __le64 bi_blkoff;
    __u8 bi_level;
    __u8 bi_pad[7];
  };


.. _`nilfs_binfo_dat.members`:

Members
-------

:``bi_blkoff``:
    block offset

:``bi_level``:
    level

:``bi_pad[7]``:
    padding




.. _`nilfs_binfo`:

union nilfs_binfo
=================

.. c:type:: nilfs_binfo

    


.. _`nilfs_binfo.definition`:

Definition
----------

.. code-block:: c

  union nilfs_binfo {
    struct nilfs_binfo_v bi_v;
    struct nilfs_binfo_dat bi_dat;
  };


.. _`nilfs_binfo.members`:

Members
-------

:``bi_v``:
    nilfs_binfo_v structure

:``bi_dat``:
    nilfs_binfo_dat structure




.. _`nilfs_segment_summary`:

struct nilfs_segment_summary
============================

.. c:type:: nilfs_segment_summary

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
  };


.. _`nilfs_segment_summary.members`:

Members
-------

:``ss_datasum``:
    checksum of data

:``ss_sumsum``:
    checksum of segment summary

:``ss_magic``:
    magic number

:``ss_bytes``:
    size of this structure in bytes

:``ss_flags``:
    flags

:``ss_seq``:
    sequence number

:``ss_create``:
    creation timestamp

:``ss_next``:
    next segment

:``ss_nblocks``:
    number of blocks

:``ss_nfinfo``:
    number of finfo structures

:``ss_sumbytes``:
    total size of segment summary in bytes

:``ss_pad``:
    padding

:``ss_cno``:
    checkpoint number




.. _`nilfs_btree_node`:

struct nilfs_btree_node
=======================

.. c:type:: nilfs_btree_node

    B-tree node


.. _`nilfs_btree_node.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_btree_node {
    __u8 bn_flags;
    __u8 bn_level;
    __le16 bn_nchildren;
    __le32 bn_pad;
  };


.. _`nilfs_btree_node.members`:

Members
-------

:``bn_flags``:
    flags

:``bn_level``:
    level

:``bn_nchildren``:
    number of children

:``bn_pad``:
    padding




.. _`nilfs_palloc_group_desc`:

struct nilfs_palloc_group_desc
==============================

.. c:type:: nilfs_palloc_group_desc

    block group descriptor


.. _`nilfs_palloc_group_desc.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_palloc_group_desc {
    __le32 pg_nfrees;
  };


.. _`nilfs_palloc_group_desc.members`:

Members
-------

:``pg_nfrees``:
    number of free entries in block group




.. _`nilfs_dat_entry`:

struct nilfs_dat_entry
======================

.. c:type:: nilfs_dat_entry

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
  };


.. _`nilfs_dat_entry.members`:

Members
-------

:``de_blocknr``:
    block number

:``de_start``:
    start checkpoint number

:``de_end``:
    end checkpoint number

:``de_rsv``:
    reserved for future use




.. _`nilfs_snapshot_list`:

struct nilfs_snapshot_list
==========================

.. c:type:: nilfs_snapshot_list

    snapshot list


.. _`nilfs_snapshot_list.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_snapshot_list {
    __le64 ssl_next;
    __le64 ssl_prev;
  };


.. _`nilfs_snapshot_list.members`:

Members
-------

:``ssl_next``:
    next checkpoint number on snapshot list

:``ssl_prev``:
    previous checkpoint number on snapshot list




.. _`nilfs_checkpoint`:

struct nilfs_checkpoint
=======================

.. c:type:: nilfs_checkpoint

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
  };


.. _`nilfs_checkpoint.members`:

Members
-------

:``cp_flags``:
    flags

:``cp_checkpoints_count``:
    checkpoints count in a block

:``cp_snapshot_list``:
    snapshot list

:``cp_cno``:
    checkpoint number

:``cp_create``:
    creation timestamp

:``cp_nblk_inc``:
    number of blocks incremented by this checkpoint

:``cp_inodes_count``:
    inodes count

:``cp_blocks_count``:
    blocks count

:``cp_ifile_inode``:
    inode of ifile




.. _`nilfs_cpinfo`:

struct nilfs_cpinfo
===================

.. c:type:: nilfs_cpinfo

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
  };


.. _`nilfs_cpinfo.members`:

Members
-------

:``ci_flags``:
    flags

:``ci_pad``:
    padding

:``ci_cno``:
    checkpoint number

:``ci_create``:
    creation timestamp

:``ci_nblk_inc``:
    number of blocks incremented by this checkpoint

:``ci_inodes_count``:
    inodes count

:``ci_blocks_count``:
    blocks count

:``ci_next``:
    next checkpoint number in snapshot list




.. _`nilfs_cpfile_header`:

struct nilfs_cpfile_header
==========================

.. c:type:: nilfs_cpfile_header

    checkpoint file header


.. _`nilfs_cpfile_header.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_cpfile_header {
    __le64 ch_ncheckpoints;
    __le64 ch_nsnapshots;
    struct nilfs_snapshot_list ch_snapshot_list;
  };


.. _`nilfs_cpfile_header.members`:

Members
-------

:``ch_ncheckpoints``:
    number of checkpoints

:``ch_nsnapshots``:
    number of snapshots

:``ch_snapshot_list``:
    snapshot list




.. _`nilfs_segment_usage`:

struct nilfs_segment_usage
==========================

.. c:type:: nilfs_segment_usage

    segment usage


.. _`nilfs_segment_usage.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_segment_usage {
    __le64 su_lastmod;
    __le32 su_nblocks;
    __le32 su_flags;
  };


.. _`nilfs_segment_usage.members`:

Members
-------

:``su_lastmod``:
    last modified timestamp

:``su_nblocks``:
    number of blocks in segment

:``su_flags``:
    flags




.. _`nilfs_sufile_header`:

struct nilfs_sufile_header
==========================

.. c:type:: nilfs_sufile_header

    segment usage file header


.. _`nilfs_sufile_header.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_sufile_header {
    __le64 sh_ncleansegs;
    __le64 sh_ndirtysegs;
    __le64 sh_last_alloc;
  };


.. _`nilfs_sufile_header.members`:

Members
-------

:``sh_ncleansegs``:
    number of clean segments

:``sh_ndirtysegs``:
    number of dirty segments

:``sh_last_alloc``:
    last allocated segment number




.. _`nilfs_cpmode`:

struct nilfs_cpmode
===================

.. c:type:: nilfs_cpmode

    change checkpoint mode structure


.. _`nilfs_cpmode.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_cpmode {
    __u64 cm_cno;
    __u32 cm_mode;
    __u32 cm_pad;
  };


.. _`nilfs_cpmode.members`:

Members
-------

:``cm_cno``:
    checkpoint number

:``cm_mode``:
    mode of checkpoint

:``cm_pad``:
    padding




.. _`nilfs_argv`:

struct nilfs_argv
=================

.. c:type:: nilfs_argv

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
  };


.. _`nilfs_argv.members`:

Members
-------

:``v_base``:
    pointer on data array from userspace

:``v_nmembs``:
    number of members in data array

:``v_size``:
    size of data array in bytes

:``v_flags``:
    flags

:``v_index``:
    start number of target data items




.. _`nilfs_period`:

struct nilfs_period
===================

.. c:type:: nilfs_period

    period of checkpoint numbers


.. _`nilfs_period.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_period {
    __u64 p_start;
    __u64 p_end;
  };


.. _`nilfs_period.members`:

Members
-------

:``p_start``:
    start checkpoint number (inclusive)

:``p_end``:
    end checkpoint number (exclusive)




.. _`nilfs_cpstat`:

struct nilfs_cpstat
===================

.. c:type:: nilfs_cpstat

    checkpoint statistics


.. _`nilfs_cpstat.definition`:

Definition
----------

.. code-block:: c

  struct nilfs_cpstat {
    __u64 cs_cno;
    __u64 cs_ncps;
    __u64 cs_nsss;
  };


.. _`nilfs_cpstat.members`:

Members
-------

:``cs_cno``:
    checkpoint number

:``cs_ncps``:
    number of checkpoints

:``cs_nsss``:
    number of snapshots




.. _`nilfs_sustat`:

struct nilfs_sustat
===================

.. c:type:: nilfs_sustat

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
  };


.. _`nilfs_sustat.members`:

Members
-------

:``ss_nsegs``:
    number of segments

:``ss_ncleansegs``:
    number of clean segments

:``ss_ndirtysegs``:
    number of dirty segments

:``ss_ctime``:
    creation time of the last segment

:``ss_nongc_ctime``:
    creation time of the last segment not for GC

:``ss_prot_seq``:
    least sequence number of segments which must not be reclaimed




.. _`nilfs_vinfo`:

struct nilfs_vinfo
==================

.. c:type:: nilfs_vinfo

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
  };


.. _`nilfs_vinfo.members`:

Members
-------

:``vi_vblocknr``:
    virtual block number

:``vi_start``:
    start checkpoint number (inclusive)

:``vi_end``:
    end checkpoint number (exclusive)

:``vi_blocknr``:
    disk block number




.. _`nilfs_vdesc`:

struct nilfs_vdesc
==================

.. c:type:: nilfs_vdesc

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
  };


.. _`nilfs_vdesc.members`:

Members
-------

:``vd_ino``:
    inode number

:``vd_cno``:
    checkpoint number

:``vd_vblocknr``:
    virtual block number

:``vd_period``:
    period of checkpoint numbers

:``vd_blocknr``:
    disk block number

:``vd_offset``:
    logical block offset inside a file

:``vd_flags``:
    flags (data or node block)

:``vd_pad``:
    padding




.. _`nilfs_bdesc`:

struct nilfs_bdesc
==================

.. c:type:: nilfs_bdesc

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
  };


.. _`nilfs_bdesc.members`:

Members
-------

:``bd_ino``:
    inode number

:``bd_oblocknr``:
    disk block address (for skipping dead blocks)

:``bd_blocknr``:
    disk block address

:``bd_offset``:
    logical block offset inside a file

:``bd_level``:
    level in the b-tree organization

:``bd_pad``:
    padding


