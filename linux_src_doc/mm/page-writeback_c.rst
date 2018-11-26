.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/page-writeback.c

.. _`node_dirtyable_memory`:

node_dirtyable_memory
=====================

.. c:function:: unsigned long node_dirtyable_memory(struct pglist_data *pgdat)

    number of dirtyable pages in a node

    :param pgdat:
        the node
    :type pgdat: struct pglist_data \*

.. _`node_dirtyable_memory.description`:

Description
-----------

Returns the node's number of pages potentially available for dirty
page cache.  This is the base value for the per-node dirty limits.

.. _`global_dirtyable_memory`:

global_dirtyable_memory
=======================

.. c:function:: unsigned long global_dirtyable_memory( void)

    number of globally dirtyable pages

    :param void:
        no arguments
    :type void: 

.. _`global_dirtyable_memory.description`:

Description
-----------

Returns the global number of pages potentially available for dirty
page cache.  This is the base value for the global dirty limits.

.. _`domain_dirty_limits`:

domain_dirty_limits
===================

.. c:function:: void domain_dirty_limits(struct dirty_throttle_control *dtc)

    calculate thresh and bg_thresh for a wb_domain

    :param dtc:
        dirty_throttle_control of interest
    :type dtc: struct dirty_throttle_control \*

.. _`domain_dirty_limits.description`:

Description
-----------

Calculate \ ``dtc->thresh``\  and ->bg_thresh considering
vm_dirty_{bytes|ratio} and dirty_background_{bytes|ratio}.  The caller
must ensure that \ ``dtc->avail``\  is set before calling this function.  The
dirty limits will be lifted by 1/4 for PF_LESS_THROTTLE (ie. nfsd) and
real-time tasks.

.. _`global_dirty_limits`:

global_dirty_limits
===================

.. c:function:: void global_dirty_limits(unsigned long *pbackground, unsigned long *pdirty)

    background-writeback and dirty-throttling thresholds

    :param pbackground:
        out parameter for bg_thresh
    :type pbackground: unsigned long \*

    :param pdirty:
        out parameter for thresh
    :type pdirty: unsigned long \*

.. _`global_dirty_limits.description`:

Description
-----------

Calculate bg_thresh and thresh for global_wb_domain.  See
\ :c:func:`domain_dirty_limits`\  for details.

.. _`node_dirty_limit`:

node_dirty_limit
================

.. c:function:: unsigned long node_dirty_limit(struct pglist_data *pgdat)

    maximum number of dirty pages allowed in a node

    :param pgdat:
        the node
    :type pgdat: struct pglist_data \*

.. _`node_dirty_limit.description`:

Description
-----------

Returns the maximum number of dirty pages allowed in a node, based
on the node's dirtyable memory.

.. _`node_dirty_ok`:

node_dirty_ok
=============

.. c:function:: bool node_dirty_ok(struct pglist_data *pgdat)

    tells whether a node is within its dirty limits

    :param pgdat:
        the node to check
    :type pgdat: struct pglist_data \*

.. _`node_dirty_ok.description`:

Description
-----------

Returns \ ``true``\  when the dirty pages in \ ``pgdat``\  are within the node's
dirty limit, \ ``false``\  if the limit is exceeded.

.. _`__wb_calc_thresh`:

__wb_calc_thresh
================

.. c:function:: unsigned long __wb_calc_thresh(struct dirty_throttle_control *dtc)

    \ ``wb``\ 's share of dirty throttling threshold

    :param dtc:
        dirty_throttle_context of interest
    :type dtc: struct dirty_throttle_control \*

.. _`__wb_calc_thresh.description`:

Description
-----------

Returns \ ``wb``\ 's dirty limit in pages. The term "dirty" in the context of
dirty balancing includes all PG_dirty, PG_writeback and NFS unstable pages.

Note that \ :c:func:`balance_dirty_pages`\  will only seriously take it as a hard limit
when sleeping max_pause per page is not enough to keep the dirty pages under
control. For example, when the device is completely stalled due to some error
conditions, or when there are 1000 dd tasks writing to a slow 10MB/s USB key.
In the other normal situations, it acts more gently by throttling the tasks
more (rather than completely block them) when the wb dirty pages go high.

It allocates high/low dirty limits to fast/slow devices, in order to prevent
- starving fast devices
- piling up dirty pages (that will take long time to sync) on slow devices

The wb's share of dirty limit will be adapting to its throughput and
bounded by the bdi->min_ratio and/or bdi->max_ratio parameters, if set.

.. _`balance_dirty_pages_ratelimited`:

balance_dirty_pages_ratelimited
===============================

.. c:function:: void balance_dirty_pages_ratelimited(struct address_space *mapping)

    balance dirty memory state

    :param mapping:
        address_space which was dirtied
    :type mapping: struct address_space \*

.. _`balance_dirty_pages_ratelimited.description`:

Description
-----------

Processes which are dirtying memory should call in here once for each page
which was newly dirtied.  The function will periodically check the system's
dirty state and will initiate writeback if needed.

On really big machines, get_writeback_state is expensive, so try to avoid
calling it too often (ratelimiting).  But once we're over the dirty memory
limit we decrease the ratelimiting by a lot, to prevent individual processes
from overshooting the limit by (ratelimit_pages) each.

.. _`wb_over_bg_thresh`:

wb_over_bg_thresh
=================

.. c:function:: bool wb_over_bg_thresh(struct bdi_writeback *wb)

    does \ ``wb``\  need to be written back?

    :param wb:
        bdi_writeback of interest
    :type wb: struct bdi_writeback \*

.. _`wb_over_bg_thresh.description`:

Description
-----------

Determines whether background writeback should keep writing \ ``wb``\  or it's
clean enough.  Returns \ ``true``\  if writeback should continue.

.. _`tag_pages_for_writeback`:

tag_pages_for_writeback
=======================

.. c:function:: void tag_pages_for_writeback(struct address_space *mapping, pgoff_t start, pgoff_t end)

    tag pages to be written by write_cache_pages

    :param mapping:
        address space structure to write
    :type mapping: struct address_space \*

    :param start:
        starting page index
    :type start: pgoff_t

    :param end:
        ending page index (inclusive)
    :type end: pgoff_t

.. _`tag_pages_for_writeback.description`:

Description
-----------

This function scans the page range from \ ``start``\  to \ ``end``\  (inclusive) and tags
all pages that have DIRTY tag set with a special TOWRITE tag. The idea is
that write_cache_pages (or whoever calls this function) will then use
TOWRITE tag to identify pages eligible for writeback.  This mechanism is
used to avoid livelocking of writeback by a process steadily creating new
dirty pages in the file (thus it is important for this function to be quick
so that it can tag pages faster than a dirtying process can create them).

.. _`write_cache_pages`:

write_cache_pages
=================

.. c:function:: int write_cache_pages(struct address_space *mapping, struct writeback_control *wbc, writepage_t writepage, void *data)

    walk the list of dirty pages of the given address space and write all of them.

    :param mapping:
        address space structure to write
    :type mapping: struct address_space \*

    :param wbc:
        subtract the number of written pages from *@wbc->nr_to_write
    :type wbc: struct writeback_control \*

    :param writepage:
        function called for each page
    :type writepage: writepage_t

    :param data:
        data passed to writepage function
    :type data: void \*

.. _`write_cache_pages.description`:

Description
-----------

If a page is already under I/O, \ :c:func:`write_cache_pages`\  skips it, even
if it's dirty.  This is desirable behaviour for memory-cleaning writeback,
but it is INCORRECT for data-integrity system calls such as \ :c:func:`fsync`\ .  \ :c:func:`fsync`\ 
and \ :c:func:`msync`\  need to guarantee that all the data which was dirty at the time
the call was made get new I/O started against them.  If wbc->sync_mode is
WB_SYNC_ALL then we were called for data integrity and we must wait for
existing IO to complete.

To avoid livelocks (when other process dirties new pages), we first tag
pages which should be written back with TOWRITE tag and only then start
writing them. For data-integrity sync we have to be careful so that we do
not miss some pages (e.g., because some other process has cleared TOWRITE
tag we set). The rule we follow is that TOWRITE tag can be cleared only
by the process clearing the DIRTY tag (and submitting the page for IO).

To avoid deadlocks between range_cyclic writeback and callers that hold
pages in PageWriteback to aggregate IO until \ :c:func:`write_cache_pages`\  returns,
we do not loop back to the start of the file. Doing so causes a page
lock/page writeback access order inversion - we should only ever lock
multiple pages in ascending page->index order, and looping back to the start
of the file violates that rule and causes deadlocks.

.. _`generic_writepages`:

generic_writepages
==================

.. c:function:: int generic_writepages(struct address_space *mapping, struct writeback_control *wbc)

    walk the list of dirty pages of the given address space and \ :c:func:`writepage`\  all of them.

    :param mapping:
        address space structure to write
    :type mapping: struct address_space \*

    :param wbc:
        subtract the number of written pages from *@wbc->nr_to_write
    :type wbc: struct writeback_control \*

.. _`generic_writepages.description`:

Description
-----------

This is a library function, which implements the \ :c:func:`writepages`\ 
address_space_operation.

.. _`write_one_page`:

write_one_page
==============

.. c:function:: int write_one_page(struct page *page)

    write out a single page and wait on I/O

    :param page:
        the page to write
    :type page: struct page \*

.. _`write_one_page.description`:

Description
-----------

The page must be locked by the caller and will be unlocked upon return.

Note that the mapping's AS_EIO/AS_ENOSPC flags will be cleared when this
function returns.

.. _`wait_for_stable_page`:

wait_for_stable_page
====================

.. c:function:: void wait_for_stable_page(struct page *page)

    wait for writeback to finish, if necessary.

    :param page:
        The page to wait on.
    :type page: struct page \*

.. _`wait_for_stable_page.description`:

Description
-----------

This function determines if the given page is related to a backing device
that requires page contents to be held stable during writeback.  If so, then
it will wait for any pending writeback to complete.

.. This file was automatic generated / don't edit.

