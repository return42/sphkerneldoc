.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/segbuf.h

.. _`nilfs_segsum_info`:

struct nilfs_segsum_info
========================

.. c:type:: struct nilfs_segsum_info

    On-memory segment summary

.. _`nilfs_segsum_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_segsum_info {
        unsigned int flags;
        unsigned long nfinfo;
        unsigned long nblocks;
        unsigned long nsumblk;
        unsigned long sumbytes;
        unsigned long nfileblk;
        u64 seg_seq;
        __u64 cno;
        time64_t ctime;
        sector_t next;
    }

.. _`nilfs_segsum_info.members`:

Members
-------

flags
    Flags

nfinfo
    Number of file information structures

nblocks
    Number of blocks included in the partial segment

nsumblk
    Number of summary blocks

sumbytes
    Byte count of segment summary

nfileblk
    Total number of file blocks

seg_seq
    Segment sequence number

cno
    Checkpoint number

ctime
    Creation time

next
    Block number of the next full segment

.. _`nilfs_segment_buffer`:

struct nilfs_segment_buffer
===========================

.. c:type:: struct nilfs_segment_buffer

    Segment buffer

.. _`nilfs_segment_buffer.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_segment_buffer {
        struct super_block *sb_super;
        struct list_head sb_list;
        struct nilfs_segsum_info sb_sum;
        __u64 sb_segnum;
        __u64 sb_nextnum;
        sector_t sb_fseg_start, sb_fseg_end;
        sector_t sb_pseg_start;
        unsigned int sb_rest_blocks;
        struct list_head sb_segsum_buffers;
        struct list_head sb_payload_buffers;
        struct buffer_head *sb_super_root;
        int sb_nbio;
        atomic_t sb_err;
        struct completion sb_bio_event;
    }

.. _`nilfs_segment_buffer.members`:

Members
-------

sb_super
    back pointer to a superblock struct

sb_list
    List head to chain this structure

sb_sum
    On-memory segment summary

sb_segnum
    Index number of the full segment

sb_nextnum
    Index number of the next full segment

sb_fseg_start
    Start block number of the full segment

sb_fseg_end
    End block number of the full segment

sb_pseg_start
    Disk block number of partial segment

sb_rest_blocks
    Number of residual blocks in the current segment

sb_segsum_buffers
    List of buffers for segment summaries

sb_payload_buffers
    List of buffers for segment payload

sb_super_root
    Pointer to buffer storing a super root block (if exists)

sb_nbio
    Number of flying bio requests

sb_err
    I/O error status

sb_bio_event
    Completion event of log writing

.. This file was automatic generated / don't edit.

