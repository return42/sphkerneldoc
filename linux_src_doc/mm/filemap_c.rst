.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/filemap.c

.. _`delete_from_page_cache`:

delete_from_page_cache
======================

.. c:function:: void delete_from_page_cache(struct page *page)

    delete page from page cache

    :param struct page \*page:
        the page which the kernel is trying to remove from page cache

.. _`delete_from_page_cache.description`:

Description
-----------

This must be called only on pages that have been verified to be in the page
cache and locked.  It will never put the page into the free list, the caller
has a reference on the page.

.. _`__filemap_fdatawrite_range`:

__filemap_fdatawrite_range
==========================

.. c:function:: int __filemap_fdatawrite_range(struct address_space *mapping, loff_t start, loff_t end, int sync_mode)

    start writeback on mapping dirty pages in range

    :param struct address_space \*mapping:
        address space structure to write

    :param loff_t start:
        offset in bytes where the range starts

    :param loff_t end:
        offset in bytes where the range ends (inclusive)

    :param int sync_mode:
        enable synchronous operation

.. _`__filemap_fdatawrite_range.description`:

Description
-----------

Start writeback against all of a mapping's dirty pages that lie
within the byte offsets <start, end> inclusive.

If sync_mode is WB_SYNC_ALL then this is a "data integrity" operation, as
opposed to a regular memory cleansing writeback.  The difference between
these two operations is that if a dirty page/buffer is encountered, it must
be waited upon, and not just skipped over.

.. _`filemap_flush`:

filemap_flush
=============

.. c:function:: int filemap_flush(struct address_space *mapping)

    mostly a non-blocking flush

    :param struct address_space \*mapping:
        target address_space

.. _`filemap_flush.description`:

Description
-----------

This is a mostly non-blocking flush.  Not suitable for data-integrity
purposes - I/O may not be started against all dirty pages.

.. _`filemap_range_has_page`:

filemap_range_has_page
======================

.. c:function:: bool filemap_range_has_page(struct address_space *mapping, loff_t start_byte, loff_t end_byte)

    check if a page exists in range.

    :param struct address_space \*mapping:
        address space within which to check

    :param loff_t start_byte:
        offset in bytes where the range starts

    :param loff_t end_byte:
        offset in bytes where the range ends (inclusive)

.. _`filemap_range_has_page.description`:

Description
-----------

Find at least one page in the range supplied, usually used to check if
direct writing in this range will trigger a writeback.

.. _`filemap_fdatawait_range`:

filemap_fdatawait_range
=======================

.. c:function:: int filemap_fdatawait_range(struct address_space *mapping, loff_t start_byte, loff_t end_byte)

    wait for writeback to complete

    :param struct address_space \*mapping:
        address space structure to wait for

    :param loff_t start_byte:
        offset in bytes where the range starts

    :param loff_t end_byte:
        offset in bytes where the range ends (inclusive)

.. _`filemap_fdatawait_range.description`:

Description
-----------

Walk the list of under-writeback pages of the given address space
in the given range and wait for all of them.  Check error status of
the address space and return it.

Since the error status of the address space is cleared by this function,
callers are responsible for checking the return value and handling and/or
reporting the error.

.. _`file_fdatawait_range`:

file_fdatawait_range
====================

.. c:function:: int file_fdatawait_range(struct file *file, loff_t start_byte, loff_t end_byte)

    wait for writeback to complete

    :param struct file \*file:
        file pointing to address space structure to wait for

    :param loff_t start_byte:
        offset in bytes where the range starts

    :param loff_t end_byte:
        offset in bytes where the range ends (inclusive)

.. _`file_fdatawait_range.description`:

Description
-----------

Walk the list of under-writeback pages of the address space that file
refers to, in the given range and wait for all of them.  Check error
status of the address space vs. the file->f_wb_err cursor and return it.

Since the error status of the file is advanced by this function,
callers are responsible for checking the return value and handling and/or
reporting the error.

.. _`filemap_fdatawait_keep_errors`:

filemap_fdatawait_keep_errors
=============================

.. c:function:: int filemap_fdatawait_keep_errors(struct address_space *mapping)

    wait for writeback without clearing errors

    :param struct address_space \*mapping:
        address space structure to wait for

.. _`filemap_fdatawait_keep_errors.description`:

Description
-----------

Walk the list of under-writeback pages of the given address space
and wait for all of them.  Unlike \ :c:func:`filemap_fdatawait`\ , this function
does not clear error status of the address space.

Use this function if callers don't handle errors themselves.  Expected
call sites are system-wide / filesystem-wide data flushers: e.g. sync(2),
fsfreeze(8)

.. _`filemap_write_and_wait_range`:

filemap_write_and_wait_range
============================

.. c:function:: int filemap_write_and_wait_range(struct address_space *mapping, loff_t lstart, loff_t lend)

    write out & wait on a file range

    :param struct address_space \*mapping:
        the address_space for the pages

    :param loff_t lstart:
        offset in bytes where the range starts

    :param loff_t lend:
        offset in bytes where the range ends (inclusive)

.. _`filemap_write_and_wait_range.description`:

Description
-----------

Write out and wait upon file offsets lstart->lend, inclusive.

Note that \ ``lend``\  is inclusive (describes the last byte to be written) so
that this function can be used to write to the very end-of-file (end = -1).

.. _`file_check_and_advance_wb_err`:

file_check_and_advance_wb_err
=============================

.. c:function:: int file_check_and_advance_wb_err(struct file *file)

    report wb error (if any) that was previously and advance wb_err to current one

    :param struct file \*file:
        struct file on which the error is being reported

.. _`file_check_and_advance_wb_err.description`:

Description
-----------

When userland calls fsync (or something like nfsd does the equivalent), we
want to report any writeback errors that occurred since the last fsync (or
since the file was opened if there haven't been any).

Grab the wb_err from the mapping. If it matches what we have in the file,
then just quickly return 0. The file is all caught up.

If it doesn't match, then take the mapping value, set the "seen" flag in
it and try to swap it into place. If it works, or another task beat us
to it with the new value, then update the f_wb_err and return the error
portion. The error at this point must be reported via proper channels
(a'la fsync, or NFS COMMIT operation, etc.).

While we handle mapping->wb_err with atomic operations, the f_wb_err
value is protected by the f_lock since we must ensure that it reflects
the latest value swapped in for this file descriptor.

.. _`file_write_and_wait_range`:

file_write_and_wait_range
=========================

.. c:function:: int file_write_and_wait_range(struct file *file, loff_t lstart, loff_t lend)

    write out & wait on a file range

    :param struct file \*file:
        file pointing to address_space with pages

    :param loff_t lstart:
        offset in bytes where the range starts

    :param loff_t lend:
        offset in bytes where the range ends (inclusive)

.. _`file_write_and_wait_range.description`:

Description
-----------

Write out and wait upon file offsets lstart->lend, inclusive.

Note that \ ``lend``\  is inclusive (describes the last byte to be written) so
that this function can be used to write to the very end-of-file (end = -1).

After writing out and waiting on the data, we check and advance the
f_wb_err cursor to the latest value, and return any errors detected there.

.. _`replace_page_cache_page`:

replace_page_cache_page
=======================

.. c:function:: int replace_page_cache_page(struct page *old, struct page *new, gfp_t gfp_mask)

    replace a pagecache page with a new one

    :param struct page \*old:
        page to be replaced

    :param struct page \*new:
        page to replace with

    :param gfp_t gfp_mask:
        allocation mode

.. _`replace_page_cache_page.description`:

Description
-----------

This function replaces a page in the pagecache with a new one.  On
success it acquires the pagecache reference for the new page and
drops it for the old page.  Both the old and new pages must be
locked.  This function does not add the new page to the LRU, the
caller must do that.

The remove + add is atomic.  The only way this function can fail is
memory allocation failure.

.. _`add_to_page_cache_locked`:

add_to_page_cache_locked
========================

.. c:function:: int add_to_page_cache_locked(struct page *page, struct address_space *mapping, pgoff_t offset, gfp_t gfp_mask)

    add a locked page to the pagecache

    :param struct page \*page:
        page to add

    :param struct address_space \*mapping:
        the page's address_space

    :param pgoff_t offset:
        page index

    :param gfp_t gfp_mask:
        page allocation mode

.. _`add_to_page_cache_locked.description`:

Description
-----------

This function is used to add a page to the pagecache. It must be locked.
This function does not add the page to the LRU.  The caller must do that.

.. _`add_page_wait_queue`:

add_page_wait_queue
===================

.. c:function:: void add_page_wait_queue(struct page *page, wait_queue_entry_t *waiter)

    Add an arbitrary waiter to a page's wait queue

    :param struct page \*page:
        Page defining the wait queue of interest

    :param wait_queue_entry_t \*waiter:
        Waiter to add to the queue

.. _`add_page_wait_queue.description`:

Description
-----------

Add an arbitrary \ ``waiter``\  to the wait queue for the nominated \ ``page``\ .

.. _`unlock_page`:

unlock_page
===========

.. c:function:: void unlock_page(struct page *page)

    unlock a locked page

    :param struct page \*page:
        the page

.. _`unlock_page.description`:

Description
-----------

Unlocks the page and wakes up sleepers in \ :c:func:`___wait_on_page_locked`\ .
Also wakes sleepers in \ :c:func:`wait_on_page_writeback`\  because the wakeup
mechanism between PageLocked pages and PageWriteback pages is shared.
But that's OK - sleepers in \ :c:func:`wait_on_page_writeback`\  just go back to sleep.

Note that this depends on PG_waiters being the sign bit in the byte
that contains PG_locked - thus the \ :c:func:`BUILD_BUG_ON`\ . That allows us to
clear the PG_locked bit and test PG_waiters at the same time fairly
portably (architectures that do LL/SC can test any bit, while x86 can
test the sign bit).

.. _`end_page_writeback`:

end_page_writeback
==================

.. c:function:: void end_page_writeback(struct page *page)

    end writeback against a page

    :param struct page \*page:
        the page

.. _`__lock_page`:

__lock_page
===========

.. c:function:: void __lock_page(struct page *__page)

    get a lock on the page, assuming we need to sleep to get it

    :param struct page \*__page:
        the page to lock

.. _`page_cache_next_hole`:

page_cache_next_hole
====================

.. c:function:: pgoff_t page_cache_next_hole(struct address_space *mapping, pgoff_t index, unsigned long max_scan)

    find the next hole (not-present entry)

    :param struct address_space \*mapping:
        mapping

    :param pgoff_t index:
        index

    :param unsigned long max_scan:
        maximum range to search

.. _`page_cache_next_hole.description`:

Description
-----------

Search the set [index, min(index+max_scan-1, MAX_INDEX)] for the
lowest indexed hole.

.. _`page_cache_next_hole.return`:

Return
------

the index of the hole if found, otherwise returns an index
outside of the set specified (in which case 'return - index >=
max_scan' will be true). In rare cases of index wrap-around, 0 will
be returned.

page_cache_next_hole may be called under rcu_read_lock. However,
like radix_tree_gang_lookup, this will not atomically search a
snapshot of the tree at a single point in time. For example, if a
hole is created at index 5, then subsequently a hole is created at
index 10, page_cache_next_hole covering both indexes may return 10
if called under rcu_read_lock.

.. _`page_cache_prev_hole`:

page_cache_prev_hole
====================

.. c:function:: pgoff_t page_cache_prev_hole(struct address_space *mapping, pgoff_t index, unsigned long max_scan)

    find the prev hole (not-present entry)

    :param struct address_space \*mapping:
        mapping

    :param pgoff_t index:
        index

    :param unsigned long max_scan:
        maximum range to search

.. _`page_cache_prev_hole.description`:

Description
-----------

Search backwards in the range [max(index-max_scan+1, 0), index] for
the first hole.

.. _`page_cache_prev_hole.return`:

Return
------

the index of the hole if found, otherwise returns an index
outside of the set specified (in which case 'index - return >=
max_scan' will be true). In rare cases of wrap-around, ULONG_MAX
will be returned.

page_cache_prev_hole may be called under rcu_read_lock. However,
like radix_tree_gang_lookup, this will not atomically search a
snapshot of the tree at a single point in time. For example, if a
hole is created at index 10, then subsequently a hole is created at
index 5, page_cache_prev_hole covering both indexes may return 5 if
called under rcu_read_lock.

.. _`find_get_entry`:

find_get_entry
==============

.. c:function:: struct page *find_get_entry(struct address_space *mapping, pgoff_t offset)

    find and get a page cache entry

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t offset:
        the page cache index

.. _`find_get_entry.description`:

Description
-----------

Looks up the page cache slot at \ ``mapping``\  & \ ``offset``\ .  If there is a
page cache page, it is returned with an increased refcount.

If the slot holds a shadow entry of a previously evicted page, or a
swap entry from shmem/tmpfs, it is returned.

Otherwise, \ ``NULL``\  is returned.

.. _`find_lock_entry`:

find_lock_entry
===============

.. c:function:: struct page *find_lock_entry(struct address_space *mapping, pgoff_t offset)

    locate, pin and lock a page cache entry

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t offset:
        the page cache index

.. _`find_lock_entry.description`:

Description
-----------

Looks up the page cache slot at \ ``mapping``\  & \ ``offset``\ .  If there is a
page cache page, it is returned locked and with an increased
refcount.

If the slot holds a shadow entry of a previously evicted page, or a
swap entry from shmem/tmpfs, it is returned.

Otherwise, \ ``NULL``\  is returned.

\ :c:func:`find_lock_entry`\  may sleep.

.. _`pagecache_get_page`:

pagecache_get_page
==================

.. c:function:: struct page *pagecache_get_page(struct address_space *mapping, pgoff_t offset, int fgp_flags, gfp_t gfp_mask)

    find and get a page reference

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t offset:
        the page index

    :param int fgp_flags:
        *undescribed*

    :param gfp_t gfp_mask:
        gfp mask to use for the page cache data page allocation

.. _`pagecache_get_page.description`:

Description
-----------

Looks up the page cache slot at \ ``mapping``\  & \ ``offset``\ .

PCG flags modify how the page is returned.

- FGP_ACCESSED: the page will be marked accessed
- FGP_LOCK: Page is return locked
- FGP_CREAT: If page is not present then a new page is allocated using
  \ ``gfp_mask``\  and added to the page cache and the VM's LRU
  list. The page is returned locked and with an increased
  refcount. Otherwise, NULL is returned.

If FGP_LOCK or FGP_CREAT are specified then the function may sleep even
if the GFP flags specified for FGP_CREAT are atomic.

If there is a page cache page, it is returned with an increased refcount.

.. _`find_get_entries`:

find_get_entries
================

.. c:function:: unsigned find_get_entries(struct address_space *mapping, pgoff_t start, unsigned int nr_entries, struct page **entries, pgoff_t *indices)

    gang pagecache lookup

    :param struct address_space \*mapping:
        The address_space to search

    :param pgoff_t start:
        The starting page cache index

    :param unsigned int nr_entries:
        The maximum number of entries

    :param struct page \*\*entries:
        Where the resulting entries are placed

    :param pgoff_t \*indices:
        The cache indices corresponding to the entries in \ ``entries``\ 

.. _`find_get_entries.description`:

Description
-----------

find_get_entries() will search for and return a group of up to
\ ``nr_entries``\  entries in the mapping.  The entries are placed at
\ ``entries``\ .  \ :c:func:`find_get_entries`\  takes a reference against any actual
pages it returns.

The search returns a group of mapping-contiguous page cache entries
with ascending indexes.  There may be holes in the indices due to
not-present pages.

Any shadow entries of evicted pages, or swap entries from
shmem/tmpfs, are included in the returned array.

\ :c:func:`find_get_entries`\  returns the number of pages and shadow entries
which were found.

.. _`find_get_pages_range`:

find_get_pages_range
====================

.. c:function:: unsigned find_get_pages_range(struct address_space *mapping, pgoff_t *start, pgoff_t end, unsigned int nr_pages, struct page **pages)

    gang pagecache lookup

    :param struct address_space \*mapping:
        The address_space to search

    :param pgoff_t \*start:
        The starting page index

    :param pgoff_t end:
        The final page index (inclusive)

    :param unsigned int nr_pages:
        The maximum number of pages

    :param struct page \*\*pages:
        Where the resulting pages are placed

.. _`find_get_pages_range.description`:

Description
-----------

find_get_pages_range() will search for and return a group of up to \ ``nr_pages``\ 
pages in the mapping starting at index \ ``start``\  and up to index \ ``end``\ 
(inclusive).  The pages are placed at \ ``pages``\ .  \ :c:func:`find_get_pages_range`\  takes
a reference against the returned pages.

The search returns a group of mapping-contiguous pages with ascending
indexes.  There may be holes in the indices due to not-present pages.
We also update \ ``start``\  to index the next page for the traversal.

\ :c:func:`find_get_pages_range`\  returns the number of pages which were found. If this
number is smaller than \ ``nr_pages``\ , the end of specified range has been
reached.

.. _`find_get_pages_contig`:

find_get_pages_contig
=====================

.. c:function:: unsigned find_get_pages_contig(struct address_space *mapping, pgoff_t index, unsigned int nr_pages, struct page **pages)

    gang contiguous pagecache lookup

    :param struct address_space \*mapping:
        The address_space to search

    :param pgoff_t index:
        The starting page index

    :param unsigned int nr_pages:
        The maximum number of pages

    :param struct page \*\*pages:
        Where the resulting pages are placed

.. _`find_get_pages_contig.description`:

Description
-----------

find_get_pages_contig() works exactly like \ :c:func:`find_get_pages`\ , except
that the returned number of pages are guaranteed to be contiguous.

\ :c:func:`find_get_pages_contig`\  returns the number of pages which were found.

.. _`find_get_pages_tag`:

find_get_pages_tag
==================

.. c:function:: unsigned find_get_pages_tag(struct address_space *mapping, pgoff_t *index, int tag, unsigned int nr_pages, struct page **pages)

    find and return pages that match \ ``tag``\ 

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t \*index:
        the starting page index

    :param int tag:
        the tag index

    :param unsigned int nr_pages:
        the maximum number of pages

    :param struct page \*\*pages:
        where the resulting pages are placed

.. _`find_get_pages_tag.description`:

Description
-----------

Like find_get_pages, except we only return pages which are tagged with
\ ``tag``\ .   We update \ ``index``\  to index the next page for the traversal.

.. _`find_get_entries_tag`:

find_get_entries_tag
====================

.. c:function:: unsigned find_get_entries_tag(struct address_space *mapping, pgoff_t start, int tag, unsigned int nr_entries, struct page **entries, pgoff_t *indices)

    find and return entries that match \ ``tag``\ 

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t start:
        the starting page cache index

    :param int tag:
        the tag index

    :param unsigned int nr_entries:
        the maximum number of entries

    :param struct page \*\*entries:
        where the resulting entries are placed

    :param pgoff_t \*indices:
        the cache indices corresponding to the entries in \ ``entries``\ 

.. _`find_get_entries_tag.description`:

Description
-----------

Like find_get_entries, except we only return entries which are tagged with
\ ``tag``\ .

.. _`generic_file_buffered_read`:

generic_file_buffered_read
==========================

.. c:function:: ssize_t generic_file_buffered_read(struct kiocb *iocb, struct iov_iter *iter, ssize_t written)

    generic file read routine

    :param struct kiocb \*iocb:
        the iocb to read

    :param struct iov_iter \*iter:
        data destination

    :param ssize_t written:
        already copied

.. _`generic_file_buffered_read.description`:

Description
-----------

This is a generic file read routine, and uses the
mapping->a_ops->readpage() function for the actual low-level stuff.

This is really ugly. But the goto's actually try to clarify some
of the logic when it comes to error handling etc.

.. _`generic_file_read_iter`:

generic_file_read_iter
======================

.. c:function:: ssize_t generic_file_read_iter(struct kiocb *iocb, struct iov_iter *iter)

    generic filesystem read routine

    :param struct kiocb \*iocb:
        kernel I/O control block

    :param struct iov_iter \*iter:
        destination for the data read

.. _`generic_file_read_iter.description`:

Description
-----------

This is the "read_iter()" routine for all filesystems
that can use the page cache directly.

.. _`page_cache_read`:

page_cache_read
===============

.. c:function:: int page_cache_read(struct file *file, pgoff_t offset, gfp_t gfp_mask)

    adds requested page to the page cache if not already there

    :param struct file \*file:
        file to read

    :param pgoff_t offset:
        page index

    :param gfp_t gfp_mask:
        memory allocation flags

.. _`page_cache_read.description`:

Description
-----------

This adds the requested page to the page cache if it isn't already there,
and schedules an I/O to read in its contents from disk.

.. _`filemap_fault`:

filemap_fault
=============

.. c:function:: int filemap_fault(struct vm_fault *vmf)

    read in file data for page fault handling

    :param struct vm_fault \*vmf:
        struct vm_fault containing details of the fault

.. _`filemap_fault.description`:

Description
-----------

filemap_fault() is invoked via the vma operations vector for a
mapped memory region to read in file data during a page fault.

The goto's are kind of ugly, but this streamlines the normal case of having
it in the page cache, and handles the special cases reasonably without
having a lot of duplicated code.

vma->vm_mm->mmap_sem must be held on entry.

If our return value has VM_FAULT_RETRY set, it's because
\ :c:func:`lock_page_or_retry`\  returned 0.
The mmap_sem has usually been released in this case.
See \ :c:func:`__lock_page_or_retry`\  for the exception.

If our return value does not have VM_FAULT_RETRY set, the mmap_sem
has not been released.

We never return with VM_FAULT_RETRY and a bit from VM_FAULT_ERROR set.

.. _`read_cache_page`:

read_cache_page
===============

.. c:function:: struct page *read_cache_page(struct address_space *mapping, pgoff_t index, int (*filler)(void *, struct page *), void *data)

    read into page cache, fill it if needed

    :param struct address_space \*mapping:
        the page's address_space

    :param pgoff_t index:
        the page index

    :param int (\*filler)(void \*, struct page \*):
        function to perform the read

    :param void \*data:
        first arg to filler(data, page) function, often left as NULL

.. _`read_cache_page.description`:

Description
-----------

Read into the page cache. If a page already exists, and \ :c:func:`PageUptodate`\  is
not set, try to fill the page and wait for it to become unlocked.

If the page does not get brought uptodate, return -EIO.

.. _`read_cache_page_gfp`:

read_cache_page_gfp
===================

.. c:function:: struct page *read_cache_page_gfp(struct address_space *mapping, pgoff_t index, gfp_t gfp)

    read into page cache, using specified page allocation flags.

    :param struct address_space \*mapping:
        the page's address_space

    :param pgoff_t index:
        the page index

    :param gfp_t gfp:
        the page allocator flags to use if allocating

.. _`read_cache_page_gfp.description`:

Description
-----------

This is the same as "read_mapping_page(mapping, index, NULL)", but with
any new page allocations done using the specified allocation flags.

If the page does not get brought uptodate, return -EIO.

.. _`__generic_file_write_iter`:

__generic_file_write_iter
=========================

.. c:function:: ssize_t __generic_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    write data to a file

    :param struct kiocb \*iocb:
        IO state structure (file, offset, etc.)

    :param struct iov_iter \*from:
        iov_iter with data to write

.. _`__generic_file_write_iter.description`:

Description
-----------

This function does all the work needed for actually writing data to a
file. It does all basic checks, removes SUID from the file, updates
modification times and calls proper subroutines depending on whether we
do direct IO or a standard buffered write.

It expects i_mutex to be grabbed unless we work on a block device or similar
object which does not need locking at all.

This function does *not* take care of syncing data in case of O_SYNC write.
A caller has to handle it. This is mainly due to the fact that we want to
avoid syncing under i_mutex.

.. _`generic_file_write_iter`:

generic_file_write_iter
=======================

.. c:function:: ssize_t generic_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    write data to a file

    :param struct kiocb \*iocb:
        IO state structure

    :param struct iov_iter \*from:
        iov_iter with data to write

.. _`generic_file_write_iter.description`:

Description
-----------

This is a wrapper around \ :c:func:`__generic_file_write_iter`\  to be used by most
filesystems. It takes care of syncing the file in case of O_SYNC file
and acquires i_mutex as needed.

.. _`try_to_release_page`:

try_to_release_page
===================

.. c:function:: int try_to_release_page(struct page *page, gfp_t gfp_mask)

    release old fs-specific metadata on a page

    :param struct page \*page:
        the page which the kernel is trying to free

    :param gfp_t gfp_mask:
        memory allocation flags (and I/O mode)

.. _`try_to_release_page.description`:

Description
-----------

The address_space is to try to release any data against the page
(presumably at page->private).  If the release was successful, return '1'.
Otherwise return zero.

This may also be called if PG_fscache is set on a page, indicating that the
page is known to the local caching routines.

The \ ``gfp_mask``\  argument specifies whether I/O may be performed to release
this page (__GFP_IO), and whether the call may block (__GFP_RECLAIM & __GFP_FS).

.. This file was automatic generated / don't edit.

