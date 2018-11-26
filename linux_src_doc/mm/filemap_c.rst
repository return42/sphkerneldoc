.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/filemap.c

.. _`delete_from_page_cache`:

delete_from_page_cache
======================

.. c:function:: void delete_from_page_cache(struct page *page)

    delete page from page cache

    :param page:
        the page which the kernel is trying to remove from page cache
    :type page: struct page \*

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

    :param mapping:
        address space structure to write
    :type mapping: struct address_space \*

    :param start:
        offset in bytes where the range starts
    :type start: loff_t

    :param end:
        offset in bytes where the range ends (inclusive)
    :type end: loff_t

    :param sync_mode:
        enable synchronous operation
    :type sync_mode: int

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

    :param mapping:
        target address_space
    :type mapping: struct address_space \*

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

    :param mapping:
        address space within which to check
    :type mapping: struct address_space \*

    :param start_byte:
        offset in bytes where the range starts
    :type start_byte: loff_t

    :param end_byte:
        offset in bytes where the range ends (inclusive)
    :type end_byte: loff_t

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

    :param mapping:
        address space structure to wait for
    :type mapping: struct address_space \*

    :param start_byte:
        offset in bytes where the range starts
    :type start_byte: loff_t

    :param end_byte:
        offset in bytes where the range ends (inclusive)
    :type end_byte: loff_t

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

    :param file:
        file pointing to address space structure to wait for
    :type file: struct file \*

    :param start_byte:
        offset in bytes where the range starts
    :type start_byte: loff_t

    :param end_byte:
        offset in bytes where the range ends (inclusive)
    :type end_byte: loff_t

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

    :param mapping:
        address space structure to wait for
    :type mapping: struct address_space \*

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

    :param mapping:
        the address_space for the pages
    :type mapping: struct address_space \*

    :param lstart:
        offset in bytes where the range starts
    :type lstart: loff_t

    :param lend:
        offset in bytes where the range ends (inclusive)
    :type lend: loff_t

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

    :param file:
        struct file on which the error is being reported
    :type file: struct file \*

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

    :param file:
        file pointing to address_space with pages
    :type file: struct file \*

    :param lstart:
        offset in bytes where the range starts
    :type lstart: loff_t

    :param lend:
        offset in bytes where the range ends (inclusive)
    :type lend: loff_t

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

    :param old:
        page to be replaced
    :type old: struct page \*

    :param new:
        page to replace with
    :type new: struct page \*

    :param gfp_mask:
        allocation mode
    :type gfp_mask: gfp_t

.. _`replace_page_cache_page.description`:

Description
-----------

This function replaces a page in the pagecache with a new one.  On
success it acquires the pagecache reference for the new page and
drops it for the old page.  Both the old and new pages must be
locked.  This function does not add the new page to the LRU, the
caller must do that.

The remove + add is atomic.  This function cannot fail.

.. _`add_to_page_cache_locked`:

add_to_page_cache_locked
========================

.. c:function:: int add_to_page_cache_locked(struct page *page, struct address_space *mapping, pgoff_t offset, gfp_t gfp_mask)

    add a locked page to the pagecache

    :param page:
        page to add
    :type page: struct page \*

    :param mapping:
        the page's address_space
    :type mapping: struct address_space \*

    :param offset:
        page index
    :type offset: pgoff_t

    :param gfp_mask:
        page allocation mode
    :type gfp_mask: gfp_t

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

    :param page:
        Page defining the wait queue of interest
    :type page: struct page \*

    :param waiter:
        Waiter to add to the queue
    :type waiter: wait_queue_entry_t \*

.. _`add_page_wait_queue.description`:

Description
-----------

Add an arbitrary \ ``waiter``\  to the wait queue for the nominated \ ``page``\ .

.. _`unlock_page`:

unlock_page
===========

.. c:function:: void unlock_page(struct page *page)

    unlock a locked page

    :param page:
        the page
    :type page: struct page \*

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

    :param page:
        the page
    :type page: struct page \*

.. _`__lock_page`:

__lock_page
===========

.. c:function:: void __lock_page(struct page *__page)

    get a lock on the page, assuming we need to sleep to get it

    :param __page:
        the page to lock
    :type __page: struct page \*

.. _`page_cache_next_miss`:

page_cache_next_miss
====================

.. c:function:: pgoff_t page_cache_next_miss(struct address_space *mapping, pgoff_t index, unsigned long max_scan)

    Find the next gap in the page cache.

    :param mapping:
        Mapping.
    :type mapping: struct address_space \*

    :param index:
        Index.
    :type index: pgoff_t

    :param max_scan:
        Maximum range to search.
    :type max_scan: unsigned long

.. _`page_cache_next_miss.description`:

Description
-----------

Search the range [index, min(index + max_scan - 1, ULONG_MAX)] for the
gap with the lowest index.

This function may be called under the rcu_read_lock.  However, this will
not atomically search a snapshot of the cache at a single point in time.
For example, if a gap is created at index 5, then subsequently a gap is
created at index 10, page_cache_next_miss covering both indices may
return 10 if called under the rcu_read_lock.

.. _`page_cache_next_miss.return`:

Return
------

The index of the gap if found, otherwise an index outside the
range specified (in which case 'return - index >= max_scan' will be true).
In the rare case of index wrap-around, 0 will be returned.

.. _`page_cache_prev_miss`:

page_cache_prev_miss
====================

.. c:function:: pgoff_t page_cache_prev_miss(struct address_space *mapping, pgoff_t index, unsigned long max_scan)

    Find the next gap in the page cache.

    :param mapping:
        Mapping.
    :type mapping: struct address_space \*

    :param index:
        Index.
    :type index: pgoff_t

    :param max_scan:
        Maximum range to search.
    :type max_scan: unsigned long

.. _`page_cache_prev_miss.description`:

Description
-----------

Search the range [max(index - max_scan + 1, 0), index] for the
gap with the highest index.

This function may be called under the rcu_read_lock.  However, this will
not atomically search a snapshot of the cache at a single point in time.
For example, if a gap is created at index 10, then subsequently a gap is
created at index 5, \ :c:func:`page_cache_prev_miss`\  covering both indices may
return 5 if called under the rcu_read_lock.

.. _`page_cache_prev_miss.return`:

Return
------

The index of the gap if found, otherwise an index outside the
range specified (in which case 'index - return >= max_scan' will be true).
In the rare case of wrap-around, ULONG_MAX will be returned.

.. _`find_get_entry`:

find_get_entry
==============

.. c:function:: struct page *find_get_entry(struct address_space *mapping, pgoff_t offset)

    find and get a page cache entry

    :param mapping:
        the address_space to search
    :type mapping: struct address_space \*

    :param offset:
        the page cache index
    :type offset: pgoff_t

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

    :param mapping:
        the address_space to search
    :type mapping: struct address_space \*

    :param offset:
        the page cache index
    :type offset: pgoff_t

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

    :param mapping:
        the address_space to search
    :type mapping: struct address_space \*

    :param offset:
        the page index
    :type offset: pgoff_t

    :param fgp_flags:
        *undescribed*
    :type fgp_flags: int

    :param gfp_mask:
        gfp mask to use for the page cache data page allocation
    :type gfp_mask: gfp_t

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

    :param mapping:
        The address_space to search
    :type mapping: struct address_space \*

    :param start:
        The starting page cache index
    :type start: pgoff_t

    :param nr_entries:
        The maximum number of entries
    :type nr_entries: unsigned int

    :param entries:
        Where the resulting entries are placed
    :type entries: struct page \*\*

    :param indices:
        The cache indices corresponding to the entries in \ ``entries``\ 
    :type indices: pgoff_t \*

.. _`find_get_entries.description`:

Description
-----------

\ :c:func:`find_get_entries`\  will search for and return a group of up to
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

    :param mapping:
        The address_space to search
    :type mapping: struct address_space \*

    :param start:
        The starting page index
    :type start: pgoff_t \*

    :param end:
        The final page index (inclusive)
    :type end: pgoff_t

    :param nr_pages:
        The maximum number of pages
    :type nr_pages: unsigned int

    :param pages:
        Where the resulting pages are placed
    :type pages: struct page \*\*

.. _`find_get_pages_range.description`:

Description
-----------

\ :c:func:`find_get_pages_range`\  will search for and return a group of up to \ ``nr_pages``\ 
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

    :param mapping:
        The address_space to search
    :type mapping: struct address_space \*

    :param index:
        The starting page index
    :type index: pgoff_t

    :param nr_pages:
        The maximum number of pages
    :type nr_pages: unsigned int

    :param pages:
        Where the resulting pages are placed
    :type pages: struct page \*\*

.. _`find_get_pages_contig.description`:

Description
-----------

\ :c:func:`find_get_pages_contig`\  works exactly like \ :c:func:`find_get_pages`\ , except
that the returned number of pages are guaranteed to be contiguous.

\ :c:func:`find_get_pages_contig`\  returns the number of pages which were found.

.. _`find_get_pages_range_tag`:

find_get_pages_range_tag
========================

.. c:function:: unsigned find_get_pages_range_tag(struct address_space *mapping, pgoff_t *index, pgoff_t end, xa_mark_t tag, unsigned int nr_pages, struct page **pages)

    find and return pages in given range matching \ ``tag``\ 

    :param mapping:
        the address_space to search
    :type mapping: struct address_space \*

    :param index:
        the starting page index
    :type index: pgoff_t \*

    :param end:
        The final page index (inclusive)
    :type end: pgoff_t

    :param tag:
        the tag index
    :type tag: xa_mark_t

    :param nr_pages:
        the maximum number of pages
    :type nr_pages: unsigned int

    :param pages:
        where the resulting pages are placed
    :type pages: struct page \*\*

.. _`find_get_pages_range_tag.description`:

Description
-----------

Like find_get_pages, except we only return pages which are tagged with
\ ``tag``\ .   We update \ ``index``\  to index the next page for the traversal.

.. _`find_get_entries_tag`:

find_get_entries_tag
====================

.. c:function:: unsigned find_get_entries_tag(struct address_space *mapping, pgoff_t start, xa_mark_t tag, unsigned int nr_entries, struct page **entries, pgoff_t *indices)

    find and return entries that match \ ``tag``\ 

    :param mapping:
        the address_space to search
    :type mapping: struct address_space \*

    :param start:
        the starting page cache index
    :type start: pgoff_t

    :param tag:
        the tag index
    :type tag: xa_mark_t

    :param nr_entries:
        the maximum number of entries
    :type nr_entries: unsigned int

    :param entries:
        where the resulting entries are placed
    :type entries: struct page \*\*

    :param indices:
        the cache indices corresponding to the entries in \ ``entries``\ 
    :type indices: pgoff_t \*

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

    :param iocb:
        the iocb to read
    :type iocb: struct kiocb \*

    :param iter:
        data destination
    :type iter: struct iov_iter \*

    :param written:
        already copied
    :type written: ssize_t

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

    :param iocb:
        kernel I/O control block
    :type iocb: struct kiocb \*

    :param iter:
        destination for the data read
    :type iter: struct iov_iter \*

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

    :param file:
        file to read
    :type file: struct file \*

    :param offset:
        page index
    :type offset: pgoff_t

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

.. _`page_cache_read.description`:

Description
-----------

This adds the requested page to the page cache if it isn't already there,
and schedules an I/O to read in its contents from disk.

.. _`filemap_fault`:

filemap_fault
=============

.. c:function:: vm_fault_t filemap_fault(struct vm_fault *vmf)

    read in file data for page fault handling

    :param vmf:
        struct vm_fault containing details of the fault
    :type vmf: struct vm_fault \*

.. _`filemap_fault.description`:

Description
-----------

\ :c:func:`filemap_fault`\  is invoked via the vma operations vector for a
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

    :param mapping:
        the page's address_space
    :type mapping: struct address_space \*

    :param index:
        the page index
    :type index: pgoff_t

    :param int (\*filler)(void \*, struct page \*):
        function to perform the read

    :param data:
        first arg to filler(data, page) function, often left as NULL
    :type data: void \*

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

    :param mapping:
        the page's address_space
    :type mapping: struct address_space \*

    :param index:
        the page index
    :type index: pgoff_t

    :param gfp:
        the page allocator flags to use if allocating
    :type gfp: gfp_t

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

    :param iocb:
        IO state structure (file, offset, etc.)
    :type iocb: struct kiocb \*

    :param from:
        iov_iter with data to write
    :type from: struct iov_iter \*

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

    :param iocb:
        IO state structure
    :type iocb: struct kiocb \*

    :param from:
        iov_iter with data to write
    :type from: struct iov_iter \*

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

    :param page:
        the page which the kernel is trying to free
    :type page: struct page \*

    :param gfp_mask:
        memory allocation flags (and I/O mode)
    :type gfp_mask: gfp_t

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

