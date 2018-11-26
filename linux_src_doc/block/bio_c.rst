.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bio.c

.. _`bio_reset`:

bio_reset
=========

.. c:function:: void bio_reset(struct bio *bio)

    reinitialize a bio

    :param bio:
        bio to reset
    :type bio: struct bio \*

.. _`bio_reset.description`:

Description
-----------

  After calling \ :c:func:`bio_reset`\ , \ ``bio``\  will be in the same state as a freshly
  allocated bio returned bio \ :c:func:`bio_alloc_bioset`\  - the only fields that are
  preserved are the ones that are initialized by \ :c:func:`bio_alloc_bioset`\ . See
  comment in struct bio.

.. _`bio_chain`:

bio_chain
=========

.. c:function:: void bio_chain(struct bio *bio, struct bio *parent)

    chain bio completions

    :param bio:
        the target bio
    :type bio: struct bio \*

    :param parent:
        the \ ``bio``\ 's parent bio
    :type parent: struct bio \*

.. _`bio_chain.description`:

Description
-----------

The caller won't have a bi_end_io called when \ ``bio``\  completes - instead,
\ ``parent``\ 's bi_end_io won't be called until both \ ``parent``\  and \ ``bio``\  have
completed; the chained bio will also be freed when it completes.

The caller must not set bi_private or bi_end_io in \ ``bio``\ .

.. _`bio_alloc_bioset`:

bio_alloc_bioset
================

.. c:function:: struct bio *bio_alloc_bioset(gfp_t gfp_mask, unsigned int nr_iovecs, struct bio_set *bs)

    allocate a bio for I/O

    :param gfp_mask:
        the GFP_* mask given to the slab allocator
    :type gfp_mask: gfp_t

    :param nr_iovecs:
        number of iovecs to pre-allocate
    :type nr_iovecs: unsigned int

    :param bs:
        the bio_set to allocate from.
    :type bs: struct bio_set \*

.. _`bio_alloc_bioset.description`:

Description
-----------

  If \ ``bs``\  is NULL, uses \ :c:func:`kmalloc`\  to allocate the bio; else the allocation is
  backed by the \ ``bs``\ 's mempool.

  When \ ``bs``\  is not NULL, if \ ``__GFP_DIRECT_RECLAIM``\  is set then bio_alloc will
  always be able to allocate a bio. This is due to the mempool guarantees.
  To make this work, callers must never allocate more than 1 bio at a time
  from this pool. Callers that need to allocate more than 1 bio must always
  submit the previously allocated bio for IO before attempting to allocate
  a new one. Failure to do so can cause deadlocks under memory pressure.

  Note that when running under \ :c:func:`generic_make_request`\  (i.e. any block
  driver), bios are not submitted until after you return - see the code in
  \ :c:func:`generic_make_request`\  that converts recursion into iteration, to prevent
  stack overflows.

  This would normally mean allocating multiple bios under
  \ :c:func:`generic_make_request`\  would be susceptible to deadlocks, but we have
  deadlock avoidance code that resubmits any blocked bios from a rescuer
  thread.

  However, we do not guarantee forward progress for allocations from other
  mempools. Doing multiple allocations from the same mempool under
  \ :c:func:`generic_make_request`\  should be avoided - instead, use bio_set's front_pad
  for per bio allocations.

.. _`bio_alloc_bioset.return`:

Return
------

  Pointer to new bio on success, NULL on failure.

.. _`bio_put`:

bio_put
=======

.. c:function:: void bio_put(struct bio *bio)

    release a reference to a bio

    :param bio:
        bio to release reference to
    :type bio: struct bio \*

.. _`bio_put.description`:

Description
-----------

  Put a reference to a \ :c:type:`struct bio <bio>`\ , either one you have gotten with
  bio_alloc, bio_get or bio_clone_*. The last put of a bio will free it.

.. _`__bio_clone_fast`:

__bio_clone_fast
================

.. c:function:: void __bio_clone_fast(struct bio *bio, struct bio *bio_src)

    clone a bio that shares the original bio's biovec

    :param bio:
        destination bio
    :type bio: struct bio \*

    :param bio_src:
        bio to clone
    :type bio_src: struct bio \*

.. _`__bio_clone_fast.description`:

Description
-----------

     Clone a \ :c:type:`struct bio <bio>`\ . Caller will own the returned bio, but not
     the actual data it points to. Reference count of returned
     bio will be one.

     Caller must ensure that \ ``bio_src``\  is not freed before \ ``bio``\ .

.. _`bio_clone_fast`:

bio_clone_fast
==============

.. c:function:: struct bio *bio_clone_fast(struct bio *bio, gfp_t gfp_mask, struct bio_set *bs)

    clone a bio that shares the original bio's biovec

    :param bio:
        bio to clone
    :type bio: struct bio \*

    :param gfp_mask:
        allocation priority
    :type gfp_mask: gfp_t

    :param bs:
        bio_set to allocate from
    :type bs: struct bio_set \*

.. _`bio_clone_fast.description`:

Description
-----------

     Like __bio_clone_fast, only also allocates the returned bio

.. _`bio_add_pc_page`:

bio_add_pc_page
===============

.. c:function:: int bio_add_pc_page(struct request_queue *q, struct bio *bio, struct page *page, unsigned int len, unsigned int offset)

    attempt to add page to bio

    :param q:
        the target queue
    :type q: struct request_queue \*

    :param bio:
        destination bio
    :type bio: struct bio \*

    :param page:
        page to add
    :type page: struct page \*

    :param len:
        vec entry length
    :type len: unsigned int

    :param offset:
        vec entry offset
    :type offset: unsigned int

.. _`bio_add_pc_page.description`:

Description
-----------

     Attempt to add a page to the bio_vec maplist. This can fail for a
     number of reasons, such as the bio being full or target block device
     limitations. The target block device must allow bio's up to PAGE_SIZE,
     so it is always possible to add a single page to an empty bio.

     This should only be used by REQ_PC bios.

.. _`__bio_try_merge_page`:

__bio_try_merge_page
====================

.. c:function:: bool __bio_try_merge_page(struct bio *bio, struct page *page, unsigned int len, unsigned int off)

    try appending data to an existing bvec.

    :param bio:
        destination bio
    :type bio: struct bio \*

    :param page:
        page to add
    :type page: struct page \*

    :param len:
        length of the data to add
    :type len: unsigned int

    :param off:
        offset of the data in \ ``page``\ 
    :type off: unsigned int

.. _`__bio_try_merge_page.description`:

Description
-----------

Try to add the data at \ ``page``\  + \ ``off``\  to the last bvec of \ ``bio``\ .  This is a
a useful optimisation for file systems with a block size smaller than the
page size.

Return \ ``true``\  on success or \ ``false``\  on failure.

.. _`__bio_add_page`:

__bio_add_page
==============

.. c:function:: void __bio_add_page(struct bio *bio, struct page *page, unsigned int len, unsigned int off)

    add page to a bio in a new segment

    :param bio:
        destination bio
    :type bio: struct bio \*

    :param page:
        page to add
    :type page: struct page \*

    :param len:
        length of the data to add
    :type len: unsigned int

    :param off:
        offset of the data in \ ``page``\ 
    :type off: unsigned int

.. _`__bio_add_page.description`:

Description
-----------

Add the data at \ ``page``\  + \ ``off``\  to \ ``bio``\  as a new bvec.  The caller must ensure
that \ ``bio``\  has space for another bvec.

.. _`bio_add_page`:

bio_add_page
============

.. c:function:: int bio_add_page(struct bio *bio, struct page *page, unsigned int len, unsigned int offset)

    attempt to add page to bio

    :param bio:
        destination bio
    :type bio: struct bio \*

    :param page:
        page to add
    :type page: struct page \*

    :param len:
        vec entry length
    :type len: unsigned int

    :param offset:
        vec entry offset
    :type offset: unsigned int

.. _`bio_add_page.description`:

Description
-----------

     Attempt to add a page to the bio_vec maplist. This will only fail
     if either bio->bi_vcnt == bio->bi_max_vecs or it's a cloned bio.

.. _`__bio_iov_iter_get_pages`:

__bio_iov_iter_get_pages
========================

.. c:function:: int __bio_iov_iter_get_pages(struct bio *bio, struct iov_iter *iter)

    pin user or kernel pages and add them to a bio

    :param bio:
        bio to add pages to
    :type bio: struct bio \*

    :param iter:
        iov iterator describing the region to be mapped
    :type iter: struct iov_iter \*

.. _`__bio_iov_iter_get_pages.description`:

Description
-----------

Pins pages from *iter and appends them to \ ``bio``\ 's bvec array. The
pages will have to be released using \ :c:func:`put_page`\  when done.
For multi-segment *iter, this function only adds pages from the
the next non-empty segment of the iov iterator.

.. _`bio_iov_iter_get_pages`:

bio_iov_iter_get_pages
======================

.. c:function:: int bio_iov_iter_get_pages(struct bio *bio, struct iov_iter *iter)

    pin user or kernel pages and add them to a bio

    :param bio:
        bio to add pages to
    :type bio: struct bio \*

    :param iter:
        iov iterator describing the region to be mapped
    :type iter: struct iov_iter \*

.. _`bio_iov_iter_get_pages.description`:

Description
-----------

Pins pages from *iter and appends them to \ ``bio``\ 's bvec array. The
pages will have to be released using \ :c:func:`put_page`\  when done.
The function tries, but does not guarantee, to pin as many pages as
fit into the bio, or are requested in *iter, whatever is smaller.
If MM encounters an error pinning the requested pages, it stops.
Error is returned only if 0 pages could be pinned.

.. _`submit_bio_wait`:

submit_bio_wait
===============

.. c:function:: int submit_bio_wait(struct bio *bio)

    submit a bio, and wait until it completes

    :param bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O
    :type bio: struct bio \*

.. _`submit_bio_wait.description`:

Description
-----------

Simple wrapper around \ :c:func:`submit_bio`\ . Returns 0 on success, or the error from
\ :c:func:`bio_endio`\  on failure.

WARNING: Unlike to how \ :c:func:`submit_bio`\  is usually used, this function does not
result in bio reference to be consumed. The caller must drop the reference
on his own.

.. _`bio_advance`:

bio_advance
===========

.. c:function:: void bio_advance(struct bio *bio, unsigned bytes)

    increment/complete a bio by some number of bytes

    :param bio:
        bio to advance
    :type bio: struct bio \*

    :param bytes:
        number of bytes to complete
    :type bytes: unsigned

.. _`bio_advance.description`:

Description
-----------

This updates bi_sector, bi_size and bi_idx; if the number of bytes to
complete doesn't align with a bvec boundary, then bv_len and bv_offset will
be updated on the last bvec as well.

\ ``bio``\  will then represent the remaining, uncompleted portion of the io.

.. _`bio_copy_data`:

bio_copy_data
=============

.. c:function:: void bio_copy_data(struct bio *dst, struct bio *src)

    copy contents of data buffers from one bio to another

    :param dst:
        destination bio
    :type dst: struct bio \*

    :param src:
        source bio
    :type src: struct bio \*

.. _`bio_copy_data.description`:

Description
-----------

Stops when it reaches the end of either \ ``src``\  or \ ``dst``\  - that is, copies
min(src->bi_size, dst->bi_size) bytes (or the equivalent for lists of bios).

.. _`bio_list_copy_data`:

bio_list_copy_data
==================

.. c:function:: void bio_list_copy_data(struct bio *dst, struct bio *src)

    copy contents of data buffers from one chain of bios to another

    :param dst:
        destination bio list
    :type dst: struct bio \*

    :param src:
        source bio list
    :type src: struct bio \*

.. _`bio_list_copy_data.description`:

Description
-----------

Stops when it reaches the end of either the \ ``src``\  list or \ ``dst``\  list - that is,
copies min(src->bi_size, dst->bi_size) bytes (or the equivalent for lists of
bios).

.. _`bio_copy_from_iter`:

bio_copy_from_iter
==================

.. c:function:: int bio_copy_from_iter(struct bio *bio, struct iov_iter *iter)

    copy all pages from iov_iter to bio

    :param bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O as destination
    :type bio: struct bio \*

    :param iter:
        iov_iter as source
    :type iter: struct iov_iter \*

.. _`bio_copy_from_iter.description`:

Description
-----------

Copy all pages from iov_iter to bio.
Returns 0 on success, or error on failure.

.. _`bio_copy_to_iter`:

bio_copy_to_iter
================

.. c:function:: int bio_copy_to_iter(struct bio *bio, struct iov_iter iter)

    copy all pages from bio to iov_iter

    :param bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O as source
    :type bio: struct bio \*

    :param iter:
        iov_iter as destination
    :type iter: struct iov_iter

.. _`bio_copy_to_iter.description`:

Description
-----------

Copy all pages from bio to iov_iter.
Returns 0 on success, or error on failure.

.. _`bio_uncopy_user`:

bio_uncopy_user
===============

.. c:function:: int bio_uncopy_user(struct bio *bio)

    finish previously mapped bio

    :param bio:
        bio being terminated
    :type bio: struct bio \*

.. _`bio_uncopy_user.description`:

Description
-----------

     Free pages allocated from \ :c:func:`bio_copy_user_iov`\  and write back data
     to user space in case of a read.

.. _`bio_copy_user_iov`:

bio_copy_user_iov
=================

.. c:function:: struct bio *bio_copy_user_iov(struct request_queue *q, struct rq_map_data *map_data, struct iov_iter *iter, gfp_t gfp_mask)

    copy user data to bio

    :param q:
        destination block queue
    :type q: struct request_queue \*

    :param map_data:
        pointer to the rq_map_data holding pages (if necessary)
    :type map_data: struct rq_map_data \*

    :param iter:
        iovec iterator
    :type iter: struct iov_iter \*

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

.. _`bio_copy_user_iov.description`:

Description
-----------

     Prepares and returns a bio for indirect user io, bouncing data
     to/from kernel pages as necessary. Must be paired with
     call \ :c:func:`bio_uncopy_user`\  on io completion.

.. _`bio_map_user_iov`:

bio_map_user_iov
================

.. c:function:: struct bio *bio_map_user_iov(struct request_queue *q, struct iov_iter *iter, gfp_t gfp_mask)

    map user iovec into bio

    :param q:
        the struct request_queue for the bio
    :type q: struct request_queue \*

    :param iter:
        iovec iterator
    :type iter: struct iov_iter \*

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

.. _`bio_map_user_iov.description`:

Description
-----------

     Map the user space address into a bio suitable for io to a block
     device. Returns an error pointer in case of error.

.. _`bio_unmap_user`:

bio_unmap_user
==============

.. c:function:: void bio_unmap_user(struct bio *bio)

    unmap a bio

    :param bio:
        the bio being unmapped
    :type bio: struct bio \*

.. _`bio_unmap_user.description`:

Description
-----------

     Unmap a bio previously mapped by \ :c:func:`bio_map_user_iov`\ . Must be called from
     process context.

     \ :c:func:`bio_unmap_user`\  may sleep.

.. _`bio_map_kern`:

bio_map_kern
============

.. c:function:: struct bio *bio_map_kern(struct request_queue *q, void *data, unsigned int len, gfp_t gfp_mask)

    map kernel address into bio

    :param q:
        the struct request_queue for the bio
    :type q: struct request_queue \*

    :param data:
        pointer to buffer to map
    :type data: void \*

    :param len:
        length in bytes
    :type len: unsigned int

    :param gfp_mask:
        allocation flags for bio allocation
    :type gfp_mask: gfp_t

.. _`bio_map_kern.description`:

Description
-----------

     Map the kernel address into a bio suitable for io to a block
     device. Returns an error pointer in case of error.

.. _`bio_copy_kern`:

bio_copy_kern
=============

.. c:function:: struct bio *bio_copy_kern(struct request_queue *q, void *data, unsigned int len, gfp_t gfp_mask, int reading)

    copy kernel address into bio

    :param q:
        the struct request_queue for the bio
    :type q: struct request_queue \*

    :param data:
        pointer to buffer to copy
    :type data: void \*

    :param len:
        length in bytes
    :type len: unsigned int

    :param gfp_mask:
        allocation flags for bio and page allocation
    :type gfp_mask: gfp_t

    :param reading:
        data direction is READ
    :type reading: int

.. _`bio_copy_kern.description`:

Description
-----------

     copy the kernel address into a bio suitable for io to a block
     device. Returns an error pointer in case of error.

.. _`bio_endio`:

bio_endio
=========

.. c:function:: void bio_endio(struct bio *bio)

    end I/O on a bio

    :param bio:
        bio
    :type bio: struct bio \*

.. _`bio_endio.description`:

Description
-----------

  \ :c:func:`bio_endio`\  will end I/O on the whole bio. \ :c:func:`bio_endio`\  is the preferred
  way to end I/O on a bio. No one should call \ :c:func:`bi_end_io`\  directly on a
  bio unless they own it and thus know that it has an end_io function.

  \ :c:func:`bio_endio`\  can be called several times on a bio that has been chained
  using \ :c:func:`bio_chain`\ .  The ->bi_end_io() function will only be called the
  last time.  At this point the BLK_TA_COMPLETE tracing event will be
  generated if BIO_TRACE_COMPLETION is set.

.. _`bio_split`:

bio_split
=========

.. c:function:: struct bio *bio_split(struct bio *bio, int sectors, gfp_t gfp, struct bio_set *bs)

    split a bio

    :param bio:
        bio to split
    :type bio: struct bio \*

    :param sectors:
        number of sectors to split from the front of \ ``bio``\ 
    :type sectors: int

    :param gfp:
        gfp mask
    :type gfp: gfp_t

    :param bs:
        bio set to allocate from
    :type bs: struct bio_set \*

.. _`bio_split.description`:

Description
-----------

Allocates and returns a new bio which represents \ ``sectors``\  from the start of
\ ``bio``\ , and updates \ ``bio``\  to represent the remaining sectors.

Unless this is a discard request the newly allocated bio will point
to \ ``bio``\ 's bi_io_vec; it is the caller's responsibility to ensure that
\ ``bio``\  is not freed before the split.

.. _`bio_trim`:

bio_trim
========

.. c:function:: void bio_trim(struct bio *bio, int offset, int size)

    trim a bio

    :param bio:
        bio to trim
    :type bio: struct bio \*

    :param offset:
        number of sectors to trim from the front of \ ``bio``\ 
    :type offset: int

    :param size:
        size we want to trim \ ``bio``\  to, in sectors
    :type size: int

.. _`bioset_init`:

bioset_init
===========

.. c:function:: int bioset_init(struct bio_set *bs, unsigned int pool_size, unsigned int front_pad, int flags)

    Initialize a bio_set

    :param bs:
        pool to initialize
    :type bs: struct bio_set \*

    :param pool_size:
        Number of bio and bio_vecs to cache in the mempool
    :type pool_size: unsigned int

    :param front_pad:
        Number of bytes to allocate in front of the returned bio
    :type front_pad: unsigned int

    :param flags:
        Flags to modify behavior, currently \ ``BIOSET_NEED_BVECS``\ 
        and \ ``BIOSET_NEED_RESCUER``\ 
    :type flags: int

.. _`bioset_init.description`:

Description
-----------

   Set up a bio_set to be used with \ ``bio_alloc_bioset``\ . Allows the caller
   to ask for a number of bytes to be allocated in front of the bio.
   Front pad allocation is useful for embedding the bio inside
   another structure, to avoid allocating extra data to go with the bio.
   Note that the bio must be embedded at the END of that structure always,
   or things will break badly.
   If \ ``BIOSET_NEED_BVECS``\  is set in \ ``flags``\ , a separate pool will be allocated
   for allocating iovecs.  This pool is not needed e.g. for \ :c:func:`bio_clone_fast`\ .
   If \ ``BIOSET_NEED_RESCUER``\  is set, a workqueue is created which can be used to
   dispatch queued requests when the mempool runs out of space.

.. _`bio_associate_blkcg_from_page`:

bio_associate_blkcg_from_page
=============================

.. c:function:: int bio_associate_blkcg_from_page(struct bio *bio, struct page *page)

    associate a bio with the page's blkcg

    :param bio:
        target bio
    :type bio: struct bio \*

    :param page:
        the page to lookup the blkcg from
    :type page: struct page \*

.. _`bio_associate_blkcg_from_page.description`:

Description
-----------

Associate \ ``bio``\  with the blkcg from \ ``page``\ 's owning memcg.  This works like
every other associate function wrt references.

.. _`bio_associate_blkcg`:

bio_associate_blkcg
===================

.. c:function:: int bio_associate_blkcg(struct bio *bio, struct cgroup_subsys_state *blkcg_css)

    associate a bio with the specified blkcg

    :param bio:
        target bio
    :type bio: struct bio \*

    :param blkcg_css:
        css of the blkcg to associate
    :type blkcg_css: struct cgroup_subsys_state \*

.. _`bio_associate_blkcg.description`:

Description
-----------

Associate \ ``bio``\  with the blkcg specified by \ ``blkcg_css``\ .  Block layer will
treat \ ``bio``\  as if it were issued by a task which belongs to the blkcg.

This function takes an extra reference of \ ``blkcg_css``\  which will be put
when \ ``bio``\  is released.  The caller must own \ ``bio``\  and is responsible for
synchronizing calls to this function.

.. _`bio_associate_blkg`:

bio_associate_blkg
==================

.. c:function:: int bio_associate_blkg(struct bio *bio, struct blkcg_gq *blkg)

    associate a bio with the specified blkg

    :param bio:
        target bio
    :type bio: struct bio \*

    :param blkg:
        the blkg to associate
    :type blkg: struct blkcg_gq \*

.. _`bio_associate_blkg.description`:

Description
-----------

Associate \ ``bio``\  with the blkg specified by \ ``blkg``\ .  This is the queue specific
blkcg information associated with the \ ``bio``\ , a reference will be taken on the
\ ``blkg``\  and will be freed when the bio is freed.

.. _`bio_disassociate_task`:

bio_disassociate_task
=====================

.. c:function:: void bio_disassociate_task(struct bio *bio)

    undo \ :c:func:`bio_associate_current`\ 

    :param bio:
        target bio
    :type bio: struct bio \*

.. _`bio_clone_blkcg_association`:

bio_clone_blkcg_association
===========================

.. c:function:: void bio_clone_blkcg_association(struct bio *dst, struct bio *src)

    clone blkcg association from src to dst bio

    :param dst:
        destination bio
    :type dst: struct bio \*

    :param src:
        source bio
    :type src: struct bio \*

.. This file was automatic generated / don't edit.

