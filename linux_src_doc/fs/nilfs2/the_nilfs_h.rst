.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/the_nilfs.h

.. _`the_nilfs`:

struct the_nilfs
================

.. c:type:: struct the_nilfs

    struct to supervise multiple nilfs mount points

.. _`the_nilfs.definition`:

Definition
----------

.. code-block:: c

    struct the_nilfs {
        unsigned long ns_flags;
        int ns_flushed_device;
        struct super_block *ns_sb;
        struct block_device *ns_bdev;
        struct rw_semaphore ns_sem;
        struct mutex ns_snapshot_mount_mutex;
        struct buffer_head  *ns_sbh;
        struct nilfs_super_block  *ns_sbp;
        time_t ns_sbwtime;
        unsigned int ns_sbwcount;
        unsigned int ns_sbsize;
        unsigned int ns_mount_state;
        unsigned int ns_sb_update_freq;
        u64 ns_seg_seq;
        __u64 ns_segnum;
        __u64 ns_nextnum;
        unsigned long ns_pseg_offset;
        __u64 ns_cno;
        time_t ns_ctime;
        time_t ns_nongc_ctime;
        atomic_t ns_ndirtyblks;
        spinlock_t ns_last_segment_lock;
        sector_t ns_last_pseg;
        u64 ns_last_seq;
        __u64 ns_last_cno;
        u64 ns_prot_seq;
        u64 ns_prev_seq;
        struct nilfs_sc_info *ns_writer;
        struct rw_semaphore ns_segctor_sem;
        struct inode *ns_dat;
        struct inode *ns_cpfile;
        struct inode *ns_sufile;
        struct rb_root ns_cptree;
        spinlock_t ns_cptree_lock;
        struct list_head ns_dirty_files;
        spinlock_t ns_inode_lock;
        struct list_head ns_gc_inodes;
        u32 ns_next_generation;
        spinlock_t ns_next_gen_lock;
        unsigned long ns_mount_opt;
        uid_t ns_resuid;
        gid_t ns_resgid;
        unsigned long ns_interval;
        unsigned long ns_watermark;
        unsigned int ns_blocksize_bits;
        unsigned int ns_blocksize;
        unsigned long ns_nsegments;
        unsigned long ns_blocks_per_segment;
        unsigned long ns_r_segments_percentage;
        unsigned long ns_nrsvsegs;
        unsigned long ns_first_data_block;
        int ns_inode_size;
        int ns_first_ino;
        u32 ns_crc_seed;
        struct kobject ns_dev_kobj;
        struct completion ns_dev_kobj_unregister;
        struct nilfs_sysfs_dev_subgroups *ns_dev_subgroups;
    }

.. _`the_nilfs.members`:

Members
-------

ns_flags
    flags

ns_flushed_device
    flag indicating if all volatile data was flushed

ns_sb
    back pointer to super block instance

ns_bdev
    block device

ns_sem
    semaphore for shared states

ns_snapshot_mount_mutex
    mutex to protect snapshot mounts

ns_sbh
    buffer heads of on-disk super blocks

ns_sbp
    pointers to super block data

ns_sbwtime
    previous write time of super block

ns_sbwcount
    write count of super block

ns_sbsize
    size of valid data in super block

ns_mount_state
    file system state

ns_sb_update_freq
    interval of periodical update of superblocks (in seconds)

ns_seg_seq
    segment sequence counter

ns_segnum
    index number of the latest full segment.

ns_nextnum
    index number of the full segment index to be used next

ns_pseg_offset
    offset of next partial segment in the current full segment

ns_cno
    next checkpoint number

ns_ctime
    write time of the last segment

ns_nongc_ctime
    write time of the last segment not for cleaner operation

ns_ndirtyblks
    Number of dirty data blocks

ns_last_segment_lock
    lock protecting fields for the latest segment

ns_last_pseg
    start block number of the latest segment

ns_last_seq
    sequence value of the latest segment

ns_last_cno
    checkpoint number of the latest segment

ns_prot_seq
    least sequence number of segments which must not be reclaimed

ns_prev_seq
    base sequence number used to decide if advance log cursor

ns_writer
    log writer

ns_segctor_sem
    semaphore protecting log write

ns_dat
    DAT file inode

ns_cpfile
    checkpoint file inode

ns_sufile
    segusage file inode

ns_cptree
    rb-tree of all mounted checkpoints (nilfs_root)

ns_cptree_lock
    lock protecting \ ``ns_cptree``\ 

ns_dirty_files
    list of dirty files

ns_inode_lock
    lock protecting \ ``ns_dirty_files``\ 

ns_gc_inodes
    dummy inodes to keep live blocks

ns_next_generation
    next generation number for inodes

ns_next_gen_lock
    lock protecting \ ``ns_next_generation``\ 

ns_mount_opt
    mount options

ns_resuid
    uid for reserved blocks

ns_resgid
    gid for reserved blocks

ns_interval
    checkpoint creation interval

ns_watermark
    watermark for the number of dirty buffers

ns_blocksize_bits
    bit length of block size

ns_blocksize
    block size

ns_nsegments
    number of segments in filesystem

ns_blocks_per_segment
    number of blocks per segment

ns_r_segments_percentage
    reserved segments percentage

ns_nrsvsegs
    number of reserved segments

ns_first_data_block
    block number of first data block

ns_inode_size
    size of on-disk inode

ns_first_ino
    first not-special inode number

ns_crc_seed
    seed value of CRC32 calculation

ns_dev_kobj
    /sys/fs/<nilfs>/<device>

ns_dev_kobj_unregister
    completion state

ns_dev_subgroups
    <device> subgroups pointer

.. _`nilfs_root`:

struct nilfs_root
=================

.. c:type:: struct nilfs_root

    nilfs root object

.. _`nilfs_root.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_root {
        __u64 cno;
        struct rb_node rb_node;
        atomic_t count;
        struct the_nilfs *nilfs;
        struct inode *ifile;
        atomic64_t inodes_count;
        atomic64_t blocks_count;
        struct kobject snapshot_kobj;
        struct completion snapshot_kobj_unregister;
    }

.. _`nilfs_root.members`:

Members
-------

cno
    checkpoint number

rb_node
    red-black tree node

count
    refcount of this structure

nilfs
    nilfs object

ifile
    inode file

inodes_count
    number of inodes

blocks_count
    number of blocks

snapshot_kobj
    /sys/fs/<nilfs>/<device>/mounted_snapshots/<snapshot>

snapshot_kobj_unregister
    completion state for kernel object

.. This file was automatic generated / don't edit.

