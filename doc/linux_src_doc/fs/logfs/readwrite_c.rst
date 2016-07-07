.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/logfs/readwrite.c

.. _`arch_shift`:

ARCH_SHIFT
==========

.. c:function::  ARCH_SHIFT()

    pages, upper half to indirect blocks.  If the high bit (INDIRECT_BIT) is set, the actual block index (bix) and level can be derived from the page index.

.. _`arch_shift.description`:

Description
-----------

The lowest three bits of the block index are set to 0 after packing and
unpacking.  Since the lowest n bits (9 for 4KiB blocksize) are ignored
anyway this is harmless.

.. _`logfs_seek_hole`:

logfs_seek_hole
===============

.. c:function:: u64 logfs_seek_hole(struct inode *inode, u64 bix)

    find next hole starting at a given block index

    :param struct inode \*inode:
        inode to search in

    :param u64 bix:
        block index to start searching

.. _`logfs_seek_hole.description`:

Description
-----------

Returns next hole.  If the file doesn't contain any further holes, the
block address next to eof is returned instead.

.. _`logfs_seek_data`:

logfs_seek_data
===============

.. c:function:: u64 logfs_seek_data(struct inode *inode, u64 bix)

    find next data block after a given block index

    :param struct inode \*inode:
        inode to search in

    :param u64 bix:
        block index to start searching

.. _`logfs_seek_data.description`:

Description
-----------

Returns next data block.  If the file doesn't contain any further data
blocks, the last block in the file is returned instead.

.. _`logfs_is_valid_block`:

logfs_is_valid_block
====================

.. c:function:: int logfs_is_valid_block(struct super_block *sb, u64 ofs, u64 ino, u64 bix, gc_level_t gc_level)

    check whether this block is still valid

    :param struct super_block \*sb:
        superblock

    :param u64 ofs:
        block physical offset

    :param u64 ino:
        block inode number

    :param u64 bix:
        block index

    :param gc_level_t gc_level:
        block level

.. _`logfs_is_valid_block.description`:

Description
-----------

Returns 0 if the block is invalid, 1 if it is valid and 2 if it will
become invalid once the journal is written.

.. _`fill_shadow_tree`:

fill_shadow_tree
================

.. c:function:: void fill_shadow_tree(struct inode *inode, struct page *page, struct logfs_shadow *shadow)

    Propagate shadow tree changes due to a write

    :param struct inode \*inode:
        Inode owning the page

    :param struct page \*page:
        Struct page that was written

    :param struct logfs_shadow \*shadow:
        Shadow for the current write

.. _`fill_shadow_tree.description`:

Description
-----------

Writes in logfs can result in two semi-valid objects.  The old object
is still valid as long as it can be reached by following pointers on
the medium.  Only when writes propagate all the way up to the journal
has the new object safely replaced the old one.

To handle this problem, a struct logfs_shadow is used to represent
every single write.  It is attached to the indirect block, which is
marked dirty.  When the indirect block is written, its shadows are
handed up to the next indirect block (or inode).  Untimately they
will reach the master inode and be freed upon journal commit.

This function handles a single step in the propagation.  It adds the
shadow for the current write to the tree, along with any shadows in
the page's tree, in case it was an indirect block.  If a page is
written, the inode parameter is left NULL, if an inode is written,
the page parameter is left NULL.

.. _`logfs_inode_write`:

logfs_inode_write
=================

.. c:function:: int logfs_inode_write(struct inode *inode, const void *buf, size_t count, loff_t bix, long flags, struct shadow_tree *shadow_tree)

    write inode or dentry objects

    :param struct inode \*inode:
        parent inode (ifile or directory)

    :param const void \*buf:
        object to write (inode or dentry)

    :param size_t count:
        object size

    :param loff_t bix:
        block index

    :param long flags:
        write flags

    :param struct shadow_tree \*shadow_tree:
        shadow below this inode

.. _`logfs_inode_write.fixme`:

FIXME
-----

All caller of this put a 200-300 byte variable on the stack,
only to call here and do a memcpy from that stack variable.  A good
example of wasted performance and stack space.

.. This file was automatic generated / don't edit.

