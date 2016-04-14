.. -*- coding: utf-8; mode: rst -*-

====
fs.h
====

.. _`positive_aop_returns`:

enum positive_aop_returns
=========================

.. c:type:: enum positive_aop_returns

    aop return codes with specific semantics



Constants
---------

:``AOP_WRITEPAGE_ACTIVATE``:
    Informs the caller that page writeback has
    completed, that the page is still locked, and
    should be considered active.  The VM uses this hint
    to return the page to the active list -- it won't
    be a candidate for writeback again in the near
    future.  Other callers must be careful to unlock
    the page if they get this return.  Returned by
    :c:func:`writepage`; 

:``AOP_TRUNCATED_PAGE``:
    The AOP method that was handed a locked page has
    unlocked it and the page might have been truncated.
    The caller should back up to acquiring a new page and
    trying again.  The aop will be taking reasonable
    precautions not to livelock.  If the caller held a page
    reference, it should drop it before retrying.  Returned
    by :c:func:`readpage`.


Description
-----------

address_space_operation functions return these large constants to indicate
special semantics to the caller.  These are much larger than the bytes in a
page to allow for functions that return the number of bytes operated on in a
given page.


.. _`sb_end_write`:

sb_end_write
============

.. c:function:: void sb_end_write (struct super_block *sb)

    drop write access to a superblock

    :param struct super_block \*sb:
        the super we wrote to


.. _`sb_end_write.description`:

Description
-----------

Decrement number of writers to the filesystem. Wake up possible waiters
wanting to freeze the filesystem.


.. _`sb_end_pagefault`:

sb_end_pagefault
================

.. c:function:: void sb_end_pagefault (struct super_block *sb)

    drop write access to a superblock from a page fault

    :param struct super_block \*sb:
        the super we wrote to


.. _`sb_end_pagefault.description`:

Description
-----------

Decrement number of processes handling write page fault to the filesystem.
Wake up possible waiters wanting to freeze the filesystem.


.. _`sb_end_intwrite`:

sb_end_intwrite
===============

.. c:function:: void sb_end_intwrite (struct super_block *sb)

    drop write access to a superblock for internal fs purposes

    :param struct super_block \*sb:
        the super we wrote to


.. _`sb_end_intwrite.description`:

Description
-----------

Decrement fs-internal number of writers to the filesystem.  Wake up possible
waiters wanting to freeze the filesystem.


.. _`sb_start_write`:

sb_start_write
==============

.. c:function:: void sb_start_write (struct super_block *sb)

    get write access to a superblock

    :param struct super_block \*sb:
        the super we write to


.. _`sb_start_write.description`:

Description
-----------

When a process wants to write data or metadata to a file system (i.e. dirty
a page or an inode), it should embed the operation in a :c:func:`sb_start_write` -
:c:func:`sb_end_write` pair to get exclusion against file system freezing. This
function increments number of writers preventing freezing. If the file
system is already frozen, the function waits until the file system is
thawed.

Since freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. Generally,
freeze protection should be the outermost lock. In particular, we have:

sb_start_write
-> i_mutex                        (write path, truncate, directory ops, ...)
-> s_umount                (freeze_super, thaw_super)


.. _`sb_start_pagefault`:

sb_start_pagefault
==================

.. c:function:: void sb_start_pagefault (struct super_block *sb)

    get write access to a superblock from a page fault

    :param struct super_block \*sb:
        the super we write to


.. _`sb_start_pagefault.description`:

Description
-----------

When a process starts handling write page fault, it should embed the
operation into :c:func:`sb_start_pagefault` - :c:func:`sb_end_pagefault` pair to get
exclusion against file system freezing. This is needed since the page fault
is going to dirty a page. This function increments number of running page
faults preventing freezing. If the file system is already frozen, the
function waits until the file system is thawed.

Since page fault freeze protection behaves as a lock, users have to preserve
ordering of freeze protection and other filesystem locks. It is advised to
put :c:func:`sb_start_pagefault` close to mmap_sem in lock ordering. Page fault
handling code implies lock dependency:

mmap_sem
-> sb_start_pagefault


.. _`inode_inc_iversion`:

inode_inc_iversion
==================

.. c:function:: void inode_inc_iversion (struct inode *inode)

    increments i_version

    :param struct inode \*inode:
        inode that need to be updated


.. _`inode_inc_iversion.description`:

Description
-----------

Every time the inode is modified, the i_version field will be incremented.
The filesystem has to be mounted with i_version flag

