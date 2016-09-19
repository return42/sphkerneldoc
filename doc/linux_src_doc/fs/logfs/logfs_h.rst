.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/logfs/logfs.h

.. _`logfs_area`:

struct logfs_area
=================

.. c:type:: struct logfs_area

    area management information

.. _`logfs_area.definition`:

Definition
----------

.. code-block:: c

    struct logfs_area {
        struct super_block *a_sb;
        int a_is_open;
        u32 a_segno;
        u32 a_written_bytes;
        u32 a_used_bytes;
        const struct logfs_area_ops *a_ops;
        u32 a_erase_count;
        gc_level_t a_level;
    }

.. _`logfs_area.members`:

Members
-------

a_sb
    the superblock this area belongs to

a_is_open
    1 if the area is currently open, else 0

a_segno
    segment number of area

a_written_bytes
    number of bytes already written back

a_used_bytes
    number of used bytes

a_ops
    area operations (either journal or ostore)

a_erase_count
    erase count

a_level
    GC level

.. _`logfs_area_ops`:

struct logfs_area_ops
=====================

.. c:type:: struct logfs_area_ops

    area operations

.. _`logfs_area_ops.definition`:

Definition
----------

.. code-block:: c

    struct logfs_area_ops {
        void (*get_free_segment)(struct logfs_area *area);
        void (*get_erase_count)(struct logfs_area *area);
        int (*erase_segment)(struct logfs_area *area);
    }

.. _`logfs_area_ops.members`:

Members
-------

get_free_segment
    fill area->ofs with the offset of a free segment

get_erase_count
    fill area->erase_count (needs area->ofs)

erase_segment
    erase and setup segment

.. _`logfs_device_ops`:

struct logfs_device_ops
=======================

.. c:type:: struct logfs_device_ops

    device access operations

.. _`logfs_device_ops.definition`:

Definition
----------

.. code-block:: c

    struct logfs_device_ops {
        struct page *(*find_first_sb)(struct super_block *sb, u64 *ofs);
        struct page *(*find_last_sb)(struct super_block *sb, u64 *ofs);
        int (*write_sb)(struct super_block *sb, struct page *page);
        int (*readpage)(void *_sb, struct page *page);
        void (*writeseg)(struct super_block *sb, u64 ofs, size_t len);
        int (*erase)(struct super_block *sb, loff_t ofs, size_t len,int ensure_write);
        int (*can_write_buf)(struct super_block *sb, u64 ofs);
        void (*sync)(struct super_block *sb);
        void (*put_device)(struct logfs_super *s);
    }

.. _`logfs_device_ops.members`:

Members
-------

find_first_sb
    *undescribed*

find_last_sb
    *undescribed*

write_sb
    *undescribed*

readpage
    read one page (mm page)

writeseg
    write one segment.  may be a partial segment

erase
    erase part of the device

can_write_buf
    decide whether wbuf can be written to ofs

sync
    *undescribed*

put_device
    *undescribed*

.. _`candidate_list`:

struct candidate_list
=====================

.. c:type:: struct candidate_list

    list of similar candidates

.. _`candidate_list.definition`:

Definition
----------

.. code-block:: c

    struct candidate_list {
        struct rb_root rb_tree;
        int count;
        int maxcount;
        int sort_by_ec;
    }

.. _`candidate_list.members`:

Members
-------

rb_tree
    *undescribed*

count
    *undescribed*

maxcount
    *undescribed*

sort_by_ec
    *undescribed*

.. _`gc_candidate`:

struct gc_candidate
===================

.. c:type:: struct gc_candidate

    "candidate" segment to be garbage collected next

.. _`gc_candidate.definition`:

Definition
----------

.. code-block:: c

    struct gc_candidate {
        struct rb_node rb_node;
        struct candidate_list *list;
        u32 segno;
        u32 valid;
        u32 erase_count;
        u8 dist;
    }

.. _`gc_candidate.members`:

Members
-------

rb_node
    *undescribed*

list
    list (either free of low)

segno
    segment number

valid
    number of valid bytes

erase_count
    erase count of segment

dist
    distance from tree root

.. _`gc_candidate.description`:

Description
-----------

Candidates can be on two lists.  The free list contains electees rather
than candidates - segments that no longer contain any valid data.  The
low list contains candidates to be picked for GC.  It should be kept
short.  It is not required to always pick a perfect candidate.  In the
worst case GC will have to move more data than absolutely necessary.

.. _`logfs_journal_entry`:

struct logfs_journal_entry
==========================

.. c:type:: struct logfs_journal_entry

    temporary structure used during journal scan

.. _`logfs_journal_entry.definition`:

Definition
----------

.. code-block:: c

    struct logfs_journal_entry {
        int used;
        s16 version;
        u16 len;
        u16 datalen;
        u64 offset;
    }

.. _`logfs_journal_entry.members`:

Members
-------

used
    *undescribed*

version
    normalized version

len
    length

datalen
    *undescribed*

offset
    offset

.. _`logfs_transaction`:

struct logfs_transaction
========================

.. c:type:: struct logfs_transaction

    essential fields to support atomic dirops

.. _`logfs_transaction.definition`:

Definition
----------

.. code-block:: c

    struct logfs_transaction {
        enum transaction_state state;
        u64 ino;
        u64 dir;
        u64 pos;
    }

.. _`logfs_transaction.members`:

Members
-------

state
    *undescribed*

ino
    target inode

dir
    inode of directory containing dentry

pos
    pos of dentry in directory

.. _`logfs_shadow`:

struct logfs_shadow
===================

.. c:type:: struct logfs_shadow

    old block in the shadow of a not-yet-committed new one

.. _`logfs_shadow.definition`:

Definition
----------

.. code-block:: c

    struct logfs_shadow {
        u64 old_ofs;
        u64 new_ofs;
        u64 ino;
        u64 bix;
        int old_len;
        int new_len;
        gc_level_t gc_level;
    }

.. _`logfs_shadow.members`:

Members
-------

old_ofs
    offset of old block on medium

new_ofs
    offset of new block on medium

ino
    inode number

bix
    block index

old_len
    size of old block, including header

new_len
    size of new block, including header

gc_level
    *undescribed*

.. _`shadow_tree`:

struct shadow_tree
==================

.. c:type:: struct shadow_tree


.. _`shadow_tree.definition`:

Definition
----------

.. code-block:: c

    struct shadow_tree {
        struct btree_head64 new;
        struct btree_head64 old;
        struct btree_head32 segment_map;
        int no_shadowed_segments;
    }

.. _`shadow_tree.members`:

Members
-------

new
    shadows where old_ofs==0, indexed by new_ofs

old
    shadows where old_ofs!=0, indexed by old_ofs

segment_map
    bitfield of segments containing shadows

no_shadowed_segments
    *undescribed*

.. _`logfs_inode`:

struct logfs_inode
==================

.. c:type:: struct logfs_inode

    in-memory inode

.. _`logfs_inode.definition`:

Definition
----------

.. code-block:: c

    struct logfs_inode {
        struct inode vfs_inode;
        u64 li_data[LOGFS_EMBEDDED_FIELDS];
        u64 li_used_bytes;
        struct list_head li_freeing_list;
        struct logfs_block *li_block;
        u32 li_flags;
        u8 li_height;
        int li_refcount;
    }

.. _`logfs_inode.members`:

Members
-------

vfs_inode
    struct inode

li_data
    data pointers

li_used_bytes
    number of used bytes

li_freeing_list
    used to track inodes currently being freed

li_block
    *undescribed*

li_flags
    inode flags

li_height
    *undescribed*

li_refcount
    number of internal (GC-induced) references

.. This file was automatic generated / don't edit.

