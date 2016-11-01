.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bio.c

.. _`bio_reset`:

bio_reset
=========

.. c:function:: void bio_reset(struct bio *bio)

    reinitialize a bio

    :param struct bio \*bio:
        bio to reset

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

    :param struct bio \*bio:
        the target bio

    :param struct bio \*parent:
        the \ ``bio``\ 's parent bio

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

.. c:function:: struct bio *bio_alloc_bioset(gfp_t gfp_mask, int nr_iovecs, struct bio_set *bs)

    allocate a bio for I/O

    :param gfp_t gfp_mask:
        the GFP\_ mask given to the slab allocator

    :param int nr_iovecs:
        number of iovecs to pre-allocate

    :param struct bio_set \*bs:
        the bio_set to allocate from.

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

    :param struct bio \*bio:
        bio to release reference to

.. _`bio_put.description`:

Description
-----------

Put a reference to a \ :c:type:`struct bio <bio>`\ , either one you have gotten with
bio_alloc, bio_get or bio_clone. The last put of a bio will free it.

.. _`__bio_clone_fast`:

__bio_clone_fast
================

.. c:function:: void __bio_clone_fast(struct bio *bio, struct bio *bio_src)

    clone a bio that shares the original bio's biovec

    :param struct bio \*bio:
        destination bio

    :param struct bio \*bio_src:
        bio to clone

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

    :param struct bio \*bio:
        bio to clone

    :param gfp_t gfp_mask:
        allocation priority

    :param struct bio_set \*bs:
        bio_set to allocate from

.. _`bio_clone_fast.description`:

Description
-----------

Like \__bio_clone_fast, only also allocates the returned bio

.. _`bio_clone_bioset`:

bio_clone_bioset
================

.. c:function:: struct bio *bio_clone_bioset(struct bio *bio_src, gfp_t gfp_mask, struct bio_set *bs)

    clone a bio

    :param struct bio \*bio_src:
        bio to clone

    :param gfp_t gfp_mask:
        allocation priority

    :param struct bio_set \*bs:
        bio_set to allocate from

.. _`bio_clone_bioset.description`:

Description
-----------

Clone bio. Caller will own the returned bio, but not the actual data it
points to. Reference count of returned bio will be one.

.. _`bio_add_pc_page`:

bio_add_pc_page
===============

.. c:function:: int bio_add_pc_page(struct request_queue *q, struct bio *bio, struct page *page, unsigned int len, unsigned int offset)

    attempt to add page to bio

    :param struct request_queue \*q:
        the target queue

    :param struct bio \*bio:
        destination bio

    :param struct page \*page:
        page to add

    :param unsigned int len:
        vec entry length

    :param unsigned int offset:
        vec entry offset

.. _`bio_add_pc_page.description`:

Description
-----------

Attempt to add a page to the bio_vec maplist. This can fail for a
number of reasons, such as the bio being full or target block device
limitations. The target block device must allow bio's up to PAGE_SIZE,
so it is always possible to add a single page to an empty bio.

This should only be used by REQ_PC bios.

.. _`bio_add_page`:

bio_add_page
============

.. c:function:: int bio_add_page(struct bio *bio, struct page *page, unsigned int len, unsigned int offset)

    attempt to add page to bio

    :param struct bio \*bio:
        destination bio

    :param struct page \*page:
        page to add

    :param unsigned int len:
        vec entry length

    :param unsigned int offset:
        vec entry offset

.. _`bio_add_page.description`:

Description
-----------

Attempt to add a page to the bio_vec maplist. This will only fail
if either bio->bi_vcnt == bio->bi_max_vecs or it's a cloned bio.

.. _`submit_bio_wait`:

submit_bio_wait
===============

.. c:function:: int submit_bio_wait(struct bio *bio)

    submit a bio, and wait until it completes

    :param struct bio \*bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O

.. _`submit_bio_wait.description`:

Description
-----------

Simple wrapper around \ :c:func:`submit_bio`\ . Returns 0 on success, or the error from
\ :c:func:`bio_endio`\  on failure.

.. _`bio_advance`:

bio_advance
===========

.. c:function:: void bio_advance(struct bio *bio, unsigned bytes)

    increment/complete a bio by some number of bytes

    :param struct bio \*bio:
        bio to advance

    :param unsigned bytes:
        number of bytes to complete

.. _`bio_advance.description`:

Description
-----------

This updates bi_sector, bi_size and bi_idx; if the number of bytes to
complete doesn't align with a bvec boundary, then bv_len and bv_offset will
be updated on the last bvec as well.

\ ``bio``\  will then represent the remaining, uncompleted portion of the io.

.. _`bio_alloc_pages`:

bio_alloc_pages
===============

.. c:function:: int bio_alloc_pages(struct bio *bio, gfp_t gfp_mask)

    allocates a single page for each bvec in a bio

    :param struct bio \*bio:
        bio to allocate pages for

    :param gfp_t gfp_mask:
        flags for allocation

.. _`bio_alloc_pages.description`:

Description
-----------

Allocates pages up to \ ``bio``\ ->bi_vcnt.

Returns 0 on success, -ENOMEM on failure. On failure, any allocated pages are
freed.

.. _`bio_copy_data`:

bio_copy_data
=============

.. c:function:: void bio_copy_data(struct bio *dst, struct bio *src)

    copy contents of data buffers from one chain of bios to another

    :param struct bio \*dst:
        destination bio list

    :param struct bio \*src:
        source bio list

.. _`bio_copy_data.description`:

Description
-----------

If \ ``src``\  and \ ``dst``\  are single bios, bi_next must be NULL - otherwise, treats
\ ``src``\  and \ ``dst``\  as linked lists of bios.

Stops when it reaches the end of either \ ``src``\  or \ ``dst``\  - that is, copies
min(src->bi_size, dst->bi_size) bytes (or the equivalent for lists of bios).

.. _`bio_copy_from_iter`:

bio_copy_from_iter
==================

.. c:function:: int bio_copy_from_iter(struct bio *bio, struct iov_iter iter)

    copy all pages from iov_iter to bio

    :param struct bio \*bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O as destination

    :param struct iov_iter iter:
        iov_iter as source

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

    :param struct bio \*bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O as source

    :param struct iov_iter iter:
        iov_iter as destination

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

    :param struct bio \*bio:
        bio being terminated

.. _`bio_uncopy_user.description`:

Description
-----------

Free pages allocated from \ :c:func:`bio_copy_user_iov`\  and write back data
to user space in case of a read.

.. _`bio_copy_user_iov`:

bio_copy_user_iov
=================

.. c:function:: struct bio *bio_copy_user_iov(struct request_queue *q, struct rq_map_data *map_data, const struct iov_iter *iter, gfp_t gfp_mask)

    copy user data to bio

    :param struct request_queue \*q:
        destination block queue

    :param struct rq_map_data \*map_data:
        pointer to the rq_map_data holding pages (if necessary)

    :param const struct iov_iter \*iter:
        iovec iterator

    :param gfp_t gfp_mask:
        memory allocation flags

.. _`bio_copy_user_iov.description`:

Description
-----------

Prepares and returns a bio for indirect user io, bouncing data
to/from kernel pages as necessary. Must be paired with
call \ :c:func:`bio_uncopy_user`\  on io completion.

.. _`bio_map_user_iov`:

bio_map_user_iov
================

.. c:function:: struct bio *bio_map_user_iov(struct request_queue *q, const struct iov_iter *iter, gfp_t gfp_mask)

    map user iovec into bio

    :param struct request_queue \*q:
        the struct request_queue for the bio

    :param const struct iov_iter \*iter:
        iovec iterator

    :param gfp_t gfp_mask:
        memory allocation flags

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

    :param struct bio \*bio:
        the bio being unmapped

.. _`bio_unmap_user.description`:

Description
-----------

Unmap a bio previously mapped by \ :c:func:`bio_map_user`\ . Must be called with
a process context.

\ :c:func:`bio_unmap_user`\  may sleep.

.. _`bio_map_kern`:

bio_map_kern
============

.. c:function:: struct bio *bio_map_kern(struct request_queue *q, void *data, unsigned int len, gfp_t gfp_mask)

    map kernel address into bio

    :param struct request_queue \*q:
        the struct request_queue for the bio

    :param void \*data:
        pointer to buffer to map

    :param unsigned int len:
        length in bytes

    :param gfp_t gfp_mask:
        allocation flags for bio allocation

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

    :param struct request_queue \*q:
        the struct request_queue for the bio

    :param void \*data:
        pointer to buffer to copy

    :param unsigned int len:
        length in bytes

    :param gfp_t gfp_mask:
        allocation flags for bio and page allocation

    :param int reading:
        data direction is READ

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

    :param struct bio \*bio:
        bio

.. _`bio_endio.description`:

Description
-----------

bio_endio() will end I/O on the whole bio. \ :c:func:`bio_endio`\  is the preferred
way to end I/O on a bio. No one should call \ :c:func:`bi_end_io`\  directly on a
bio unless they own it and thus know that it has an end_io function.

.. _`bio_split`:

bio_split
=========

.. c:function:: struct bio *bio_split(struct bio *bio, int sectors, gfp_t gfp, struct bio_set *bs)

    split a bio

    :param struct bio \*bio:
        bio to split

    :param int sectors:
        number of sectors to split from the front of \ ``bio``\ 

    :param gfp_t gfp:
        gfp mask

    :param struct bio_set \*bs:
        bio set to allocate from

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

    :param struct bio \*bio:
        bio to trim

    :param int offset:
        number of sectors to trim from the front of \ ``bio``\ 

    :param int size:
        size we want to trim \ ``bio``\  to, in sectors

.. _`bioset_create`:

bioset_create
=============

.. c:function:: struct bio_set *bioset_create(unsigned int pool_size, unsigned int front_pad)

    Create a bio_set

    :param unsigned int pool_size:
        Number of bio and bio_vecs to cache in the mempool

    :param unsigned int front_pad:
        Number of bytes to allocate in front of the returned bio

.. _`bioset_create.description`:

Description
-----------

Set up a bio_set to be used with \ ``bio_alloc_bioset``\ . Allows the caller
to ask for a number of bytes to be allocated in front of the bio.
Front pad allocation is useful for embedding the bio inside
another structure, to avoid allocating extra data to go with the bio.
Note that the bio must be embedded at the END of that structure always,
or things will break badly.

.. _`bioset_create_nobvec`:

bioset_create_nobvec
====================

.. c:function:: struct bio_set *bioset_create_nobvec(unsigned int pool_size, unsigned int front_pad)

    Create a bio_set without bio_vec mempool

    :param unsigned int pool_size:
        Number of bio to cache in the mempool

    :param unsigned int front_pad:
        Number of bytes to allocate in front of the returned bio

.. _`bioset_create_nobvec.description`:

Description
-----------

Same functionality as \ :c:func:`bioset_create`\  except that mempool is not
created for bio_vecs. Saving some memory for \ :c:func:`bio_clone_fast`\  users.

.. _`bio_associate_blkcg`:

bio_associate_blkcg
===================

.. c:function:: int bio_associate_blkcg(struct bio *bio, struct cgroup_subsys_state *blkcg_css)

    associate a bio with the specified blkcg

    :param struct bio \*bio:
        target bio

    :param struct cgroup_subsys_state \*blkcg_css:
        css of the blkcg to associate

.. _`bio_associate_blkcg.description`:

Description
-----------

Associate \ ``bio``\  with the blkcg specified by \ ``blkcg_css``\ .  Block layer will
treat \ ``bio``\  as if it were issued by a task which belongs to the blkcg.

This function takes an extra reference of \ ``blkcg_css``\  which will be put
when \ ``bio``\  is released.  The caller must own \ ``bio``\  and is responsible for
synchronizing calls to this function.

.. _`bio_associate_current`:

bio_associate_current
=====================

.. c:function:: int bio_associate_current(struct bio *bio)

    associate a bio with \ ``current``\ 

    :param struct bio \*bio:
        target bio

.. _`bio_associate_current.description`:

Description
-----------

Associate \ ``bio``\  with \ ``current``\  if it hasn't been associated yet.  Block
layer will treat \ ``bio``\  as if it were issued by \ ``current``\  no matter which
task actually issues it.

This function takes an extra reference of \ ``task``\ 's io_context and blkcg
which will be put when \ ``bio``\  is released.  The caller must own \ ``bio``\ ,
ensure \ ``current-``\ >io_context exists, and is responsible for synchronizing
calls to this function.

.. _`bio_disassociate_task`:

bio_disassociate_task
=====================

.. c:function:: void bio_disassociate_task(struct bio *bio)

    undo \ :c:func:`bio_associate_current`\ 

    :param struct bio \*bio:
        target bio

.. _`bio_clone_blkcg_association`:

bio_clone_blkcg_association
===========================

.. c:function:: void bio_clone_blkcg_association(struct bio *dst, struct bio *src)

    clone blkcg association from src to dst bio

    :param struct bio \*dst:
        destination bio

    :param struct bio \*src:
        source bio

.. This file was automatic generated / don't edit.

