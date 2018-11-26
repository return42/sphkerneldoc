.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fs.h

.. _`positive_aop_returns`:

enum positive_aop_returns
=========================

.. c:type:: enum positive_aop_returns

    aop return codes with specific semantics

.. _`positive_aop_returns.definition`:

Definition
----------

.. code-block:: c

    enum positive_aop_returns {
        AOP_WRITEPAGE_ACTIVATE,
        AOP_TRUNCATED_PAGE
    };

.. _`positive_aop_returns.constants`:

Constants
---------

AOP_WRITEPAGE_ACTIVATE
    Informs the caller that page writeback has
    completed, that the page is still locked, and
    should be considered active.  The VM uses this hint
    to return the page to the active list -- it won't
    be a candidate for writeback again in the near
    future.  Other callers must be careful to unlock
    the page if they get this return.  Returned by
    \ :c:func:`writepage`\ ;

AOP_TRUNCATED_PAGE
    The AOP method that was handed a locked page has
    unlocked it and the page might have been truncated.
    The caller should back up to acquiring a new page and
    trying again.  The aop will be taking reasonable
    precautions not to livelock.  If the caller held a page
    reference, it should drop it before retrying.  Returned
    by \ :c:func:`readpage`\ .

.. _`positive_aop_returns.description`:

Description
-----------

address_space_operation functions return these large constants to indicate
special semantics to the caller.  These are much larger than the bytes in a
page to allow for functions that return the number of bytes operated on in a
given page.

.. _`address_space`:

struct address_space
====================

.. c:type:: struct address_space

    Contents of a cacheable, mappable object.

.. _`address_space.definition`:

Definition
----------

.. code-block:: c

    struct address_space {
        struct inode *host;
        struct xarray i_pages;
        gfp_t gfp_mask;
        atomic_t i_mmap_writable;
        struct rb_root_cached i_mmap;
        struct rw_semaphore i_mmap_rwsem;
        unsigned long nrpages;
        unsigned long nrexceptional;
        pgoff_t writeback_index;
        const struct address_space_operations *a_ops;
        unsigned long flags;
        errseq_t wb_err;
        spinlock_t private_lock;
        struct list_head private_list;
        void *private_data;
    }

.. _`address_space.members`:

Members
-------

host
    Owner, either the inode or the block_device.

i_pages
    Cached pages.

gfp_mask
    Memory allocation flags to use for allocating pages.

i_mmap_writable
    Number of VM_SHARED mappings.

i_mmap
    Tree of private and shared mappings.

i_mmap_rwsem
    Protects \ ``i_mmap``\  and \ ``i_mmap_writable``\ .

nrpages
    Number of page entries, protected by the i_pages lock.

nrexceptional
    Shadow or DAX entries, protected by the i_pages lock.

writeback_index
    Writeback starts here.

a_ops
    Methods.

flags
    Error bits and flags (AS_*).

wb_err
    The most recent error which has occurred.

private_lock
    For use by the owner of the address_space.

private_list
    For use by the owner of the address_space.

private_data
    For use by the owner of the address_space.

.. _`sb_end_write`:

sb_end_write
============

.. c:function:: void sb_end_write(struct super_block *sb)

    drop write access to a superblock

    :param sb:
        the super we wrote to
    :type sb: struct super_block \*

.. _`sb_end_write.description`:

Description
-----------

Decrement number of writers to the filesystem. Wake up possible waiters
wanting to freeze the filesystem.

.. _`sb_end_pagefault`:

sb_end_pagefault
================

.. c:function:: void sb_end_pagefault(struct super_block *sb)

    drop write access to a superblock from a page fault

    :param sb:
        the super we wrote to
    :type sb: struct super_block \*

.. _`sb_end_pagefault.description`:

Description
-----------

Decrement number of processes handling write page fault to the filesystem.
Wake up possible waiters wanting to freeze the filesystem.

.. _`sb_end_intwrite`:

sb_end_intwrite
===============

.. c:function:: void sb_end_intwrite(struct super_block *sb)

    drop write access to a superblock for internal fs purposes

    :param sb:
        the super we wrote to
    :type sb: struct super_block \*

.. _`sb_end_intwrite.description`:

Description
-----------

Decrement fs-internal number of writers to the filesystem.  Wake up possible
waiters wanting to freeze the filesystem.

.. _`sb_start_write`:

sb_start_write
==============

.. c:function:: void sb_start_write(struct super_block *sb)

    get write access to a superblock

    :param sb:
        the super we write to
    :type sb: struct super_block \*

.. _`sb_start_write.description`:

Description
-----------

When a process wants to write data or metadata to a file system (i.e. dirty
a page or an inode), it should embed the operation in a \ :c:func:`sb_start_write`\  -
\ :c:func:`sb_end_write`\  pair to get exclusion against file system freezing. This
function increments number of writers preventing freezing. If the file
system is already frozen, the function waits until the file system is
thawed.

Since freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. Generally,
freeze protection should be the outermost lock. In particular, we have:

sb_start_write
  -> i_mutex                 (write path, truncate, directory ops, ...)
  -> s_umount                (freeze_super, thaw_super)

.. _`sb_start_pagefault`:

sb_start_pagefault
==================

.. c:function:: void sb_start_pagefault(struct super_block *sb)

    get write access to a superblock from a page fault

    :param sb:
        the super we write to
    :type sb: struct super_block \*

.. _`sb_start_pagefault.description`:

Description
-----------

When a process starts handling write page fault, it should embed the
operation into \ :c:func:`sb_start_pagefault`\  - \ :c:func:`sb_end_pagefault`\  pair to get
exclusion against file system freezing. This is needed since the page fault
is going to dirty a page. This function increments number of running page
faults preventing freezing. If the file system is already frozen, the
function waits until the file system is thawed.

Since page fault freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. It is advised to
put \ :c:func:`sb_start_pagefault`\  close to mmap_sem in lock ordering. Page fault

.. _`sb_start_pagefault.handling-code-implies-lock-dependency`:

handling code implies lock dependency
-------------------------------------


mmap_sem
  -> sb_start_pagefault

.. _`filemap_set_wb_err`:

filemap_set_wb_err
==================

.. c:function:: void filemap_set_wb_err(struct address_space *mapping, int err)

    set a writeback error on an address_space

    :param mapping:
        mapping in which to set writeback error
    :type mapping: struct address_space \*

    :param err:
        error to be set in mapping
    :type err: int

.. _`filemap_set_wb_err.description`:

Description
-----------

When writeback fails in some way, we must record that error so that
userspace can be informed when fsync and the like are called.  We endeavor
to report errors on any file that was open at the time of the error.  Some
internal callers also need to know when writeback errors have occurred.

When a writeback error occurs, most filesystems will want to call
filemap_set_wb_err to record the error in the mapping so that it will be
automatically reported whenever fsync is called on the file.

.. _`filemap_check_wb_err`:

filemap_check_wb_err
====================

.. c:function:: int filemap_check_wb_err(struct address_space *mapping, errseq_t since)

    has an error occurred since the mark was sampled?

    :param mapping:
        mapping to check for writeback errors
    :type mapping: struct address_space \*

    :param since:
        previously-sampled errseq_t
    :type since: errseq_t

.. _`filemap_check_wb_err.description`:

Description
-----------

Grab the errseq_t value from the mapping, and see if it has changed "since"
the given value was sampled.

If it has then report the latest error set, otherwise return 0.

.. _`filemap_sample_wb_err`:

filemap_sample_wb_err
=====================

.. c:function:: errseq_t filemap_sample_wb_err(struct address_space *mapping)

    sample the current errseq_t to test for later errors

    :param mapping:
        mapping to be sampled
    :type mapping: struct address_space \*

.. _`filemap_sample_wb_err.description`:

Description
-----------

Writeback errors are always reported relative to a particular sample point
in the past. This function provides those sample points.

.. This file was automatic generated / don't edit.

