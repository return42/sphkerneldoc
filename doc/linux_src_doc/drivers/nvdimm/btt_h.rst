.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/btt.h

.. _`arena_info`:

struct arena_info
=================

.. c:type:: struct arena_info

    handle for an arena

.. _`arena_info.definition`:

Definition
----------

.. code-block:: c

    struct arena_info {
        u64 size;
        u64 external_lba_start;
        u32 internal_nlba;
        u32 internal_lbasize;
        u32 external_nlba;
        u32 external_lbasize;
        u32 nfree;
        u16 version_major;
        u16 version_minor;
        u64 nextoff;
        u64 infooff;
        u64 dataoff;
        u64 mapoff;
        u64 logoff;
        u64 info2off;
        struct free_entry *freelist;
        u32 *rtt;
        struct aligned_lock *map_locks;
        struct nd_btt *nd_btt;
        struct list_head list;
        struct dentry *debugfs_dir;
        u32 flags;
    }

.. _`arena_info.members`:

Members
-------

size
    Size in bytes this arena occupies on the raw device.
    This includes arena metadata.

external_lba_start
    The first external LBA in this arena.

internal_nlba
    Number of internal blocks available in the arena
    including nfree reserved blocks

internal_lbasize
    Internal and external lba sizes may be different as
    we can round up 'odd' external lbasizes such as 520B
    to be aligned.

external_nlba
    Number of blocks contributed by the arena to the number
    reported to upper layers. (internal_nlba - nfree)

external_lbasize
    LBA size as exposed to upper layers.

nfree
    A reserve number of 'free' blocks that is used to
    handle incoming writes.

version_major
    Metadata layout version major.

version_minor
    Metadata layout version minor.

nextoff
    Offset in bytes to the start of the next arena.

infooff
    Offset in bytes to the info block of this arena.

dataoff
    Offset in bytes to the data area of this arena.

mapoff
    Offset in bytes to the map area of this arena.

logoff
    Offset in bytes to the log area of this arena.

info2off
    Offset in bytes to the backup info block of this arena.

freelist
    Pointer to in-memory list of free blocks

rtt
    Pointer to in-memory "Read Tracking Table"

map_locks
    Spinlocks protecting concurrent map writes

nd_btt
    Pointer to parent nd_btt structure.

list
    List head for list of arenas

debugfs_dir
    Debugfs dentry

flags
    Arena flags - may signify error states.

.. _`arena_info.description`:

Description
-----------

arena_info is a per-arena handle. Once an arena is narrowed down for an
IO, this struct is passed around for the duration of the IO.

.. _`btt`:

struct btt
==========

.. c:type:: struct btt

    handle for a BTT instance

.. _`btt.definition`:

Definition
----------

.. code-block:: c

    struct btt {
        struct gendisk *btt_disk;
        struct request_queue *btt_queue;
        struct list_head arena_list;
        struct dentry *debugfs_dir;
        struct nd_btt *nd_btt;
        u64 nlba;
        unsigned long long rawsize;
        u32 lbasize;
        u32 sector_size;
        struct nd_region *nd_region;
        struct mutex init_lock;
        int init_state;
        int num_arenas;
    }

.. _`btt.members`:

Members
-------

btt_disk
    Pointer to the gendisk for BTT device

btt_queue
    Pointer to the request queue for the BTT device

arena_list
    Head of the list of arenas

debugfs_dir
    Debugfs dentry

nd_btt
    Parent nd_btt struct

nlba
    Number of logical blocks exposed to the upper layers
    after removing the amount of space needed by metadata

rawsize
    Total size in bytes of the available backing device

lbasize
    LBA size as requested and presented to upper layers.
    This is sector_size + size of any metadata.

sector_size
    The Linux sector size - 512 or 4096

nd_region
    *undescribed*

init_lock
    Mutex used for the BTT initialization

init_state
    Flag describing the initialization state for the BTT

num_arenas
    Number of arenas in the BTT instance

.. This file was automatic generated / don't edit.

