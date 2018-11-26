.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/scatterlist.c

.. _`sg_next`:

sg_next
=======

.. c:function:: struct scatterlist *sg_next(struct scatterlist *sg)

    return the next scatterlist entry in a list

    :param sg:
        The current sg entry
    :type sg: struct scatterlist \*

.. _`sg_next.description`:

Description
-----------

Usually the next entry will be \ ``sg``\ @ + 1, but if this sg element is part
of a chained scatterlist, it could jump to the start of a new
scatterlist array.

.. _`sg_nents`:

sg_nents
========

.. c:function:: int sg_nents(struct scatterlist *sg)

    return total count of entries in scatterlist

    :param sg:
        The scatterlist
    :type sg: struct scatterlist \*

.. _`sg_nents.description`:

Description
-----------

Allows to know how many entries are in sg, taking into acount
chaining as well

.. _`sg_nents_for_len`:

sg_nents_for_len
================

.. c:function:: int sg_nents_for_len(struct scatterlist *sg, u64 len)

    return total count of entries in scatterlist needed to satisfy the supplied length

    :param sg:
        The scatterlist
    :type sg: struct scatterlist \*

    :param len:
        The total required length
    :type len: u64

.. _`sg_nents_for_len.description`:

Description
-----------

Determines the number of entries in sg that are required to meet
the supplied length, taking into acount chaining as well

.. _`sg_nents_for_len.return`:

Return
------

the number of sg entries needed, negative error on failure

.. _`sg_last`:

sg_last
=======

.. c:function:: struct scatterlist *sg_last(struct scatterlist *sgl, unsigned int nents)

    return the last scatterlist entry in a list

    :param sgl:
        First entry in the scatterlist
    :type sgl: struct scatterlist \*

    :param nents:
        Number of entries in the scatterlist
    :type nents: unsigned int

.. _`sg_last.description`:

Description
-----------

Should only be used casually, it (currently) scans the entire list
to get the last entry.

Note that the \ ``sgl``\ @ pointer passed in need not be the first one,
the important bit is that \ ``nents``\ @ denotes the number of entries that
exist from \ ``sgl``\ @.

.. _`sg_init_table`:

sg_init_table
=============

.. c:function:: void sg_init_table(struct scatterlist *sgl, unsigned int nents)

    Initialize SG table

    :param sgl:
        The SG table
    :type sgl: struct scatterlist \*

    :param nents:
        Number of entries in table
    :type nents: unsigned int

.. _`sg_init_table.notes`:

Notes
-----

If this is part of a chained sg table, \ :c:func:`sg_mark_end`\  should be
used only on the last table part.

.. _`sg_init_one`:

sg_init_one
===========

.. c:function:: void sg_init_one(struct scatterlist *sg, const void *buf, unsigned int buflen)

    Initialize a single entry sg list

    :param sg:
        SG entry
    :type sg: struct scatterlist \*

    :param buf:
        Virtual address for IO
    :type buf: const void \*

    :param buflen:
        IO length
    :type buflen: unsigned int

.. _`__sg_free_table`:

\__sg_free_table
================

.. c:function:: void __sg_free_table(struct sg_table *table, unsigned int max_ents, bool skip_first_chunk, sg_free_fn *free_fn)

    Free a previously mapped sg table

    :param table:
        The sg table header to use
    :type table: struct sg_table \*

    :param max_ents:
        The maximum number of entries per single scatterlist
    :type max_ents: unsigned int

    :param skip_first_chunk:
        don't free the (preallocated) first scatterlist chunk
    :type skip_first_chunk: bool

    :param free_fn:
        Free function
    :type free_fn: sg_free_fn \*

.. _`__sg_free_table.description`:

Description
-----------

Free an sg table previously allocated and setup with
\__sg_alloc_table().  The \ ``max_ents``\  value must be identical to
that previously used with \__sg_alloc_table().

.. _`sg_free_table`:

sg_free_table
=============

.. c:function:: void sg_free_table(struct sg_table *table)

    Free a previously allocated sg table

    :param table:
        The mapped sg table header
    :type table: struct sg_table \*

.. _`__sg_alloc_table`:

\__sg_alloc_table
=================

.. c:function:: int __sg_alloc_table(struct sg_table *table, unsigned int nents, unsigned int max_ents, struct scatterlist *first_chunk, gfp_t gfp_mask, sg_alloc_fn *alloc_fn)

    Allocate and initialize an sg table with given allocator

    :param table:
        The sg table header to use
    :type table: struct sg_table \*

    :param nents:
        Number of entries in sg list
    :type nents: unsigned int

    :param max_ents:
        The maximum number of entries the allocator returns per call
    :type max_ents: unsigned int

    :param first_chunk:
        *undescribed*
    :type first_chunk: struct scatterlist \*

    :param gfp_mask:
        GFP allocation mask
    :type gfp_mask: gfp_t

    :param alloc_fn:
        Allocator to use
    :type alloc_fn: sg_alloc_fn \*

.. _`__sg_alloc_table.description`:

Description
-----------

This function returns a \ ``table``\  \ ``nents``\  long. The allocator is
defined to return scatterlist chunks of maximum size \ ``max_ents``\ .
Thus if \ ``nents``\  is bigger than \ ``max_ents``\ , the scatterlists will be
chained in units of \ ``max_ents``\ .

.. _`__sg_alloc_table.notes`:

Notes
-----

If this function returns non-0 (eg failure), the caller must call
\__sg_free_table() to cleanup any leftover allocations.

.. _`sg_alloc_table`:

sg_alloc_table
==============

.. c:function:: int sg_alloc_table(struct sg_table *table, unsigned int nents, gfp_t gfp_mask)

    Allocate and initialize an sg table

    :param table:
        The sg table header to use
    :type table: struct sg_table \*

    :param nents:
        Number of entries in sg list
    :type nents: unsigned int

    :param gfp_mask:
        GFP allocation mask
    :type gfp_mask: gfp_t

.. _`sg_alloc_table.description`:

Description
-----------

Allocate and initialize an sg table. If \ ``nents``\ @ is larger than
SG_MAX_SINGLE_ALLOC a chained sg table will be setup.

.. _`__sg_alloc_table_from_pages`:

\__sg_alloc_table_from_pages
============================

.. c:function:: int __sg_alloc_table_from_pages(struct sg_table *sgt, struct page **pages, unsigned int n_pages, unsigned int offset, unsigned long size, unsigned int max_segment, gfp_t gfp_mask)

    Allocate and initialize an sg table from an array of pages

    :param sgt:
        The sg table header to use
    :type sgt: struct sg_table \*

    :param pages:
        Pointer to an array of page pointers
    :type pages: struct page \*\*

    :param n_pages:
        Number of pages in the pages array
    :type n_pages: unsigned int

    :param offset:
        Offset from start of the first page to the start of a buffer
    :type offset: unsigned int

    :param size:
        Number of valid bytes in the buffer (after offset)
    :type size: unsigned long

    :param max_segment:
        Maximum size of a scatterlist node in bytes (page aligned)
    :type max_segment: unsigned int

    :param gfp_mask:
        GFP allocation mask
    :type gfp_mask: gfp_t

.. _`__sg_alloc_table_from_pages.description`:

Description
-----------

Allocate and initialize an sg table from a list of pages. Contiguous
ranges of the pages are squashed into a single scatterlist node up to the
maximum size specified in \ ``max_segment``\ . An user may provide an offset at a
start and a size of valid data in a buffer specified by the page array.
The returned sg table is released by sg_free_table.

.. _`__sg_alloc_table_from_pages.return`:

Return
------

0 on success, negative error on failure

.. _`sg_alloc_table_from_pages`:

sg_alloc_table_from_pages
=========================

.. c:function:: int sg_alloc_table_from_pages(struct sg_table *sgt, struct page **pages, unsigned int n_pages, unsigned int offset, unsigned long size, gfp_t gfp_mask)

    Allocate and initialize an sg table from an array of pages

    :param sgt:
        The sg table header to use
    :type sgt: struct sg_table \*

    :param pages:
        Pointer to an array of page pointers
    :type pages: struct page \*\*

    :param n_pages:
        Number of pages in the pages array
    :type n_pages: unsigned int

    :param offset:
        Offset from start of the first page to the start of a buffer
    :type offset: unsigned int

    :param size:
        Number of valid bytes in the buffer (after offset)
    :type size: unsigned long

    :param gfp_mask:
        GFP allocation mask
    :type gfp_mask: gfp_t

.. _`sg_alloc_table_from_pages.description`:

Description
-----------

Allocate and initialize an sg table from a list of pages. Contiguous
ranges of the pages are squashed into a single scatterlist node. A user
may provide an offset at a start and a size of valid data in a buffer
specified by the page array. The returned sg table is released by
sg_free_table.

.. _`sg_alloc_table_from_pages.return`:

Return
------

0 on success, negative error on failure

.. _`sgl_alloc_order`:

sgl_alloc_order
===============

.. c:function:: struct scatterlist *sgl_alloc_order(unsigned long long length, unsigned int order, bool chainable, gfp_t gfp, unsigned int *nent_p)

    allocate a scatterlist and its pages

    :param length:
        Length in bytes of the scatterlist. Must be at least one
    :type length: unsigned long long

    :param order:
        Second argument for \ :c:func:`alloc_pages`\ 
    :type order: unsigned int

    :param chainable:
        Whether or not to allocate an extra element in the scatterlist
        for scatterlist chaining purposes
    :type chainable: bool

    :param gfp:
        Memory allocation flags
    :type gfp: gfp_t

    :param nent_p:
        [out] Number of entries in the scatterlist that have pages
    :type nent_p: unsigned int \*

.. _`sgl_alloc_order.return`:

Return
------

A pointer to an initialized scatterlist or \ ``NULL``\  upon failure.

.. _`sgl_alloc`:

sgl_alloc
=========

.. c:function:: struct scatterlist *sgl_alloc(unsigned long long length, gfp_t gfp, unsigned int *nent_p)

    allocate a scatterlist and its pages

    :param length:
        Length in bytes of the scatterlist
    :type length: unsigned long long

    :param gfp:
        Memory allocation flags
    :type gfp: gfp_t

    :param nent_p:
        [out] Number of entries in the scatterlist
    :type nent_p: unsigned int \*

.. _`sgl_alloc.return`:

Return
------

A pointer to an initialized scatterlist or \ ``NULL``\  upon failure.

.. _`sgl_free_n_order`:

sgl_free_n_order
================

.. c:function:: void sgl_free_n_order(struct scatterlist *sgl, int nents, int order)

    free a scatterlist and its pages

    :param sgl:
        Scatterlist with one or more elements
    :type sgl: struct scatterlist \*

    :param nents:
        Maximum number of elements to free
    :type nents: int

    :param order:
        Second argument for \__free_pages()
    :type order: int

.. _`sgl_free_n_order.notes`:

Notes
-----

- If several scatterlists have been chained and each chain element is
freed separately then it's essential to set nents correctly to avoid that a
page would get freed twice.
- All pages in a chained scatterlist can be freed at once by setting \ ``nents``\ 
to a high number.

.. _`sgl_free_order`:

sgl_free_order
==============

.. c:function:: void sgl_free_order(struct scatterlist *sgl, int order)

    free a scatterlist and its pages

    :param sgl:
        Scatterlist with one or more elements
    :type sgl: struct scatterlist \*

    :param order:
        Second argument for \__free_pages()
    :type order: int

.. _`sgl_free`:

sgl_free
========

.. c:function:: void sgl_free(struct scatterlist *sgl)

    free a scatterlist and its pages

    :param sgl:
        Scatterlist with one or more elements
    :type sgl: struct scatterlist \*

.. _`sg_miter_start`:

sg_miter_start
==============

.. c:function:: void sg_miter_start(struct sg_mapping_iter *miter, struct scatterlist *sgl, unsigned int nents, unsigned int flags)

    start mapping iteration over a sg list

    :param miter:
        sg mapping iter to be started
    :type miter: struct sg_mapping_iter \*

    :param sgl:
        sg list to iterate over
    :type sgl: struct scatterlist \*

    :param nents:
        number of sg entries
    :type nents: unsigned int

    :param flags:
        *undescribed*
    :type flags: unsigned int

.. _`sg_miter_start.description`:

Description
-----------

Starts mapping iterator \ ``miter``\ .

.. _`sg_miter_start.context`:

Context
-------

Don't care.

.. _`sg_miter_skip`:

sg_miter_skip
=============

.. c:function:: bool sg_miter_skip(struct sg_mapping_iter *miter, off_t offset)

    reposition mapping iterator

    :param miter:
        sg mapping iter to be skipped
    :type miter: struct sg_mapping_iter \*

    :param offset:
        number of bytes to plus the current location
    :type offset: off_t

.. _`sg_miter_skip.description`:

Description
-----------

Sets the offset of \ ``miter``\  to its current location plus \ ``offset``\  bytes.
If mapping iterator \ ``miter``\  has been proceeded by \ :c:func:`sg_miter_next`\ , this
stops \ ``miter``\ .

.. _`sg_miter_skip.context`:

Context
-------

Don't care if \ ``miter``\  is stopped, or not proceeded yet.
Otherwise, preemption disabled if the SG_MITER_ATOMIC is set.

.. _`sg_miter_skip.return`:

Return
------

true if \ ``miter``\  contains the valid mapping.  false if end of sg
list is reached.

.. _`sg_miter_next`:

sg_miter_next
=============

.. c:function:: bool sg_miter_next(struct sg_mapping_iter *miter)

    proceed mapping iterator to the next mapping

    :param miter:
        sg mapping iter to proceed
    :type miter: struct sg_mapping_iter \*

.. _`sg_miter_next.description`:

Description
-----------

Proceeds \ ``miter``\  to the next mapping.  \ ``miter``\  should have been started
using \ :c:func:`sg_miter_start`\ .  On successful return, \ ``miter->page``\ ,
\ ``miter->addr``\  and \ ``miter->length``\  point to the current mapping.

.. _`sg_miter_next.context`:

Context
-------

Preemption disabled if SG_MITER_ATOMIC.  Preemption must stay disabled
till \ ``miter``\  is stopped.  May sleep if !SG_MITER_ATOMIC.

.. _`sg_miter_next.return`:

Return
------

true if \ ``miter``\  contains the next mapping.  false if end of sg
list is reached.

.. _`sg_miter_stop`:

sg_miter_stop
=============

.. c:function:: void sg_miter_stop(struct sg_mapping_iter *miter)

    stop mapping iteration

    :param miter:
        sg mapping iter to be stopped
    :type miter: struct sg_mapping_iter \*

.. _`sg_miter_stop.description`:

Description
-----------

Stops mapping iterator \ ``miter``\ .  \ ``miter``\  should have been started
using \ :c:func:`sg_miter_start`\ .  A stopped iteration can be resumed by
calling \ :c:func:`sg_miter_next`\  on it.  This is useful when resources (kmap)
need to be released during iteration.

.. _`sg_miter_stop.context`:

Context
-------

Preemption disabled if the SG_MITER_ATOMIC is set.  Don't care
otherwise.

.. _`sg_copy_buffer`:

sg_copy_buffer
==============

.. c:function:: size_t sg_copy_buffer(struct scatterlist *sgl, unsigned int nents, void *buf, size_t buflen, off_t skip, bool to_buffer)

    Copy data between a linear buffer and an SG list

    :param sgl:
        The SG list
    :type sgl: struct scatterlist \*

    :param nents:
        Number of SG entries
    :type nents: unsigned int

    :param buf:
        Where to copy from
    :type buf: void \*

    :param buflen:
        The number of bytes to copy
    :type buflen: size_t

    :param skip:
        Number of bytes to skip before copying
    :type skip: off_t

    :param to_buffer:
        transfer direction (true == from an sg list to a
        buffer, false == from a buffer to an sg list
    :type to_buffer: bool

.. _`sg_copy_buffer.description`:

Description
-----------

Returns the number of copied bytes.

.. _`sg_copy_from_buffer`:

sg_copy_from_buffer
===================

.. c:function:: size_t sg_copy_from_buffer(struct scatterlist *sgl, unsigned int nents, const void *buf, size_t buflen)

    Copy from a linear buffer to an SG list

    :param sgl:
        The SG list
    :type sgl: struct scatterlist \*

    :param nents:
        Number of SG entries
    :type nents: unsigned int

    :param buf:
        Where to copy from
    :type buf: const void \*

    :param buflen:
        The number of bytes to copy
    :type buflen: size_t

.. _`sg_copy_from_buffer.description`:

Description
-----------

Returns the number of copied bytes.

.. _`sg_copy_to_buffer`:

sg_copy_to_buffer
=================

.. c:function:: size_t sg_copy_to_buffer(struct scatterlist *sgl, unsigned int nents, void *buf, size_t buflen)

    Copy from an SG list to a linear buffer

    :param sgl:
        The SG list
    :type sgl: struct scatterlist \*

    :param nents:
        Number of SG entries
    :type nents: unsigned int

    :param buf:
        Where to copy to
    :type buf: void \*

    :param buflen:
        The number of bytes to copy
    :type buflen: size_t

.. _`sg_copy_to_buffer.description`:

Description
-----------

Returns the number of copied bytes.

.. _`sg_pcopy_from_buffer`:

sg_pcopy_from_buffer
====================

.. c:function:: size_t sg_pcopy_from_buffer(struct scatterlist *sgl, unsigned int nents, const void *buf, size_t buflen, off_t skip)

    Copy from a linear buffer to an SG list

    :param sgl:
        The SG list
    :type sgl: struct scatterlist \*

    :param nents:
        Number of SG entries
    :type nents: unsigned int

    :param buf:
        Where to copy from
    :type buf: const void \*

    :param buflen:
        The number of bytes to copy
    :type buflen: size_t

    :param skip:
        Number of bytes to skip before copying
    :type skip: off_t

.. _`sg_pcopy_from_buffer.description`:

Description
-----------

Returns the number of copied bytes.

.. _`sg_pcopy_to_buffer`:

sg_pcopy_to_buffer
==================

.. c:function:: size_t sg_pcopy_to_buffer(struct scatterlist *sgl, unsigned int nents, void *buf, size_t buflen, off_t skip)

    Copy from an SG list to a linear buffer

    :param sgl:
        The SG list
    :type sgl: struct scatterlist \*

    :param nents:
        Number of SG entries
    :type nents: unsigned int

    :param buf:
        Where to copy to
    :type buf: void \*

    :param buflen:
        The number of bytes to copy
    :type buflen: size_t

    :param skip:
        Number of bytes to skip before copying
    :type skip: off_t

.. _`sg_pcopy_to_buffer.description`:

Description
-----------

Returns the number of copied bytes.

.. _`sg_zero_buffer`:

sg_zero_buffer
==============

.. c:function:: size_t sg_zero_buffer(struct scatterlist *sgl, unsigned int nents, size_t buflen, off_t skip)

    Zero-out a part of a SG list

    :param sgl:
        The SG list
    :type sgl: struct scatterlist \*

    :param nents:
        Number of SG entries
    :type nents: unsigned int

    :param buflen:
        The number of bytes to zero out
    :type buflen: size_t

    :param skip:
        Number of bytes to skip before zeroing
    :type skip: off_t

.. _`sg_zero_buffer.description`:

Description
-----------

Returns the number of bytes zeroed.

.. This file was automatic generated / don't edit.

