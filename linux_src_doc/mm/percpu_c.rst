.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/percpu.c

.. _`pcpu_addr_in_chunk`:

pcpu_addr_in_chunk
==================

.. c:function:: bool pcpu_addr_in_chunk(struct pcpu_chunk *chunk, void *addr)

    check if the address is served from this chunk

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param addr:
        percpu address
    :type addr: void \*

.. _`pcpu_addr_in_chunk.return`:

Return
------

True if the address is served from this chunk.

.. _`pcpu_next_md_free_region`:

pcpu_next_md_free_region
========================

.. c:function:: void pcpu_next_md_free_region(struct pcpu_chunk *chunk, int *bit_off, int *bits)

    finds the next hint free area

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param bit_off:
        chunk offset
    :type bit_off: int \*

    :param bits:
        size of free area
    :type bits: int \*

.. _`pcpu_next_md_free_region.description`:

Description
-----------

Helper function for pcpu_for_each_md_free_region.  It checks
block->contig_hint and performs aggregation across blocks to find the
next hint.  It modifies bit_off and bits in-place to be consumed in the
loop.

.. _`pcpu_next_fit_region`:

pcpu_next_fit_region
====================

.. c:function:: void pcpu_next_fit_region(struct pcpu_chunk *chunk, int alloc_bits, int align, int *bit_off, int *bits)

    finds fit areas for a given allocation request

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param alloc_bits:
        size of allocation
    :type alloc_bits: int

    :param align:
        alignment of area (max PAGE_SIZE)
    :type align: int

    :param bit_off:
        chunk offset
    :type bit_off: int \*

    :param bits:
        size of free area
    :type bits: int \*

.. _`pcpu_next_fit_region.description`:

Description
-----------

Finds the next free region that is viable for use with a given size and
alignment.  This only returns if there is a valid area to be used for this
allocation.  block->first_free is returned if the allocation request fits
within the block to see if the request can be fulfilled prior to the contig
hint.

.. _`pcpu_mem_zalloc`:

pcpu_mem_zalloc
===============

.. c:function:: void *pcpu_mem_zalloc(size_t size, gfp_t gfp)

    allocate memory

    :param size:
        bytes to allocate
    :type size: size_t

    :param gfp:
        allocation flags
    :type gfp: gfp_t

.. _`pcpu_mem_zalloc.description`:

Description
-----------

Allocate \ ``size``\  bytes.  If \ ``size``\  is smaller than PAGE_SIZE,
\ :c:func:`kzalloc`\  is used; otherwise, the equivalent of \ :c:func:`vzalloc`\  is used.
This is to facilitate passing through whitelisted flags.  The
returned memory is always zeroed.

.. _`pcpu_mem_zalloc.return`:

Return
------

Pointer to the allocated area on success, NULL on failure.

.. _`pcpu_mem_free`:

pcpu_mem_free
=============

.. c:function:: void pcpu_mem_free(void *ptr)

    free memory

    :param ptr:
        memory to free
    :type ptr: void \*

.. _`pcpu_mem_free.description`:

Description
-----------

Free \ ``ptr``\ .  \ ``ptr``\  should have been allocated using \ :c:func:`pcpu_mem_zalloc`\ .

.. _`pcpu_chunk_relocate`:

pcpu_chunk_relocate
===================

.. c:function:: void pcpu_chunk_relocate(struct pcpu_chunk *chunk, int oslot)

    put chunk in the appropriate chunk slot

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param oslot:
        the previous slot it was on
    :type oslot: int

.. _`pcpu_chunk_relocate.description`:

Description
-----------

This function is called after an allocation or free changed \ ``chunk``\ .
New slot according to the changed state is determined and \ ``chunk``\  is
moved to the slot.  Note that the reserved chunk is never put on
chunk slots.

.. _`pcpu_chunk_relocate.context`:

Context
-------

pcpu_lock.

.. _`pcpu_cnt_pop_pages`:

pcpu_cnt_pop_pages
==================

.. c:function:: int pcpu_cnt_pop_pages(struct pcpu_chunk *chunk, int bit_off, int bits)

    counts populated backing pages in range

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param bit_off:
        start offset
    :type bit_off: int

    :param bits:
        size of area to check
    :type bits: int

.. _`pcpu_cnt_pop_pages.description`:

Description
-----------

Calculates the number of populated pages in the region
[page_start, page_end).  This keeps track of how many empty populated
pages are available and decide if async work should be scheduled.

.. _`pcpu_cnt_pop_pages.return`:

Return
------

The nr of populated pages.

.. _`pcpu_chunk_update`:

pcpu_chunk_update
=================

.. c:function:: void pcpu_chunk_update(struct pcpu_chunk *chunk, int bit_off, int bits)

    updates the chunk metadata given a free area

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param bit_off:
        chunk offset
    :type bit_off: int

    :param bits:
        size of free area
    :type bits: int

.. _`pcpu_chunk_update.description`:

Description
-----------

This updates the chunk's contig hint and starting offset given a free area.
Choose the best starting offset if the contig hint is equal.

.. _`pcpu_chunk_refresh_hint`:

pcpu_chunk_refresh_hint
=======================

.. c:function:: void pcpu_chunk_refresh_hint(struct pcpu_chunk *chunk)

    updates metadata about a chunk

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

.. _`pcpu_chunk_refresh_hint.description`:

Description
-----------

Iterates over the metadata blocks to find the largest contig area.
It also counts the populated pages and uses the delta to update the
global count.

.. _`pcpu_chunk_refresh_hint.updates`:

Updates
-------

chunk->contig_bits
chunk->contig_bits_start
nr_empty_pop_pages (chunk and global)

.. _`pcpu_block_update`:

pcpu_block_update
=================

.. c:function:: void pcpu_block_update(struct pcpu_block_md *block, int start, int end)

    updates a block given a free area

    :param block:
        block of interest
    :type block: struct pcpu_block_md \*

    :param start:
        start offset in block
    :type start: int

    :param end:
        end offset in block
    :type end: int

.. _`pcpu_block_update.description`:

Description
-----------

Updates a block given a known free area.  The region [start, end) is
expected to be the entirety of the free area within a block.  Chooses
the best starting offset if the contig hints are equal.

.. _`pcpu_block_refresh_hint`:

pcpu_block_refresh_hint
=======================

.. c:function:: void pcpu_block_refresh_hint(struct pcpu_chunk *chunk, int index)

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param index:
        index of the metadata block
    :type index: int

.. _`pcpu_block_refresh_hint.description`:

Description
-----------

Scans over the block beginning at first_free and updates the block
metadata accordingly.

.. _`pcpu_block_update_hint_alloc`:

pcpu_block_update_hint_alloc
============================

.. c:function:: void pcpu_block_update_hint_alloc(struct pcpu_chunk *chunk, int bit_off, int bits)

    update hint on allocation path

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param bit_off:
        chunk offset
    :type bit_off: int

    :param bits:
        size of request
    :type bits: int

.. _`pcpu_block_update_hint_alloc.description`:

Description
-----------

Updates metadata for the allocation path.  The metadata only has to be
refreshed by a full scan iff the chunk's contig hint is broken.  Block level
scans are required if the block's contig hint is broken.

.. _`pcpu_block_update_hint_free`:

pcpu_block_update_hint_free
===========================

.. c:function:: void pcpu_block_update_hint_free(struct pcpu_chunk *chunk, int bit_off, int bits)

    updates the block hints on the free path

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param bit_off:
        chunk offset
    :type bit_off: int

    :param bits:
        size of request
    :type bits: int

.. _`pcpu_block_update_hint_free.description`:

Description
-----------

Updates metadata for the allocation path.  This avoids a blind block
refresh by making use of the block contig hints.  If this fails, it scans
forward and backward to determine the extent of the free area.  This is
capped at the boundary of blocks.

A chunk update is triggered if a page becomes free, a block becomes free,
or the free spans across blocks.  This tradeoff is to minimize iterating
over the block metadata to update chunk->contig_bits.  chunk->contig_bits
may be off by up to a page, but it will never be more than the available
space.  If the contig hint is contained in one block, it will be accurate.

.. _`pcpu_is_populated`:

pcpu_is_populated
=================

.. c:function:: bool pcpu_is_populated(struct pcpu_chunk *chunk, int bit_off, int bits, int *next_off)

    determines if the region is populated

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param bit_off:
        chunk offset
    :type bit_off: int

    :param bits:
        size of area
    :type bits: int

    :param next_off:
        return value for the next offset to start searching
    :type next_off: int \*

.. _`pcpu_is_populated.description`:

Description
-----------

For atomic allocations, check if the backing pages are populated.

.. _`pcpu_is_populated.return`:

Return
------

Bool if the backing pages are populated.
next_index is to skip over unpopulated blocks in pcpu_find_block_fit.

.. _`pcpu_find_block_fit`:

pcpu_find_block_fit
===================

.. c:function:: int pcpu_find_block_fit(struct pcpu_chunk *chunk, int alloc_bits, size_t align, bool pop_only)

    finds the block index to start searching

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param alloc_bits:
        size of request in allocation units
    :type alloc_bits: int

    :param align:
        alignment of area (max PAGE_SIZE bytes)
    :type align: size_t

    :param pop_only:
        use populated regions only
    :type pop_only: bool

.. _`pcpu_find_block_fit.description`:

Description
-----------

Given a chunk and an allocation spec, find the offset to begin searching
for a free region.  This iterates over the bitmap metadata blocks to
find an offset that will be guaranteed to fit the requirements.  It is
not quite first fit as if the allocation does not fit in the contig hint
of a block or chunk, it is skipped.  This errs on the side of caution
to prevent excess iteration.  Poor alignment can cause the allocator to
skip over blocks and chunks that have valid free areas.

.. _`pcpu_find_block_fit.return`:

Return
------

The offset in the bitmap to begin searching.
-1 if no offset is found.

.. _`pcpu_alloc_area`:

pcpu_alloc_area
===============

.. c:function:: int pcpu_alloc_area(struct pcpu_chunk *chunk, int alloc_bits, size_t align, int start)

    allocates an area from a pcpu_chunk

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param alloc_bits:
        size of request in allocation units
    :type alloc_bits: int

    :param align:
        alignment of area (max PAGE_SIZE)
    :type align: size_t

    :param start:
        bit_off to start searching
    :type start: int

.. _`pcpu_alloc_area.description`:

Description
-----------

This function takes in a \ ``start``\  offset to begin searching to fit an
allocation of \ ``alloc_bits``\  with alignment \ ``align``\ .  It needs to scan
the allocation map because if it fits within the block's contig hint,
\ ``start``\  will be block->first_free. This is an attempt to fill the
allocation prior to breaking the contig hint.  The allocation and
boundary maps are updated accordingly if it confirms a valid
free area.

.. _`pcpu_alloc_area.return`:

Return
------

Allocated addr offset in \ ``chunk``\  on success.
-1 if no matching area is found.

.. _`pcpu_free_area`:

pcpu_free_area
==============

.. c:function:: void pcpu_free_area(struct pcpu_chunk *chunk, int off)

    frees the corresponding offset

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param off:
        addr offset into chunk
    :type off: int

.. _`pcpu_free_area.description`:

Description
-----------

This function determines the size of an allocation to free using
the boundary bitmap and clears the allocation map.

.. _`pcpu_alloc_first_chunk`:

pcpu_alloc_first_chunk
======================

.. c:function:: struct pcpu_chunk *pcpu_alloc_first_chunk(unsigned long tmp_addr, int map_size)

    creates chunks that serve the first chunk

    :param tmp_addr:
        the start of the region served
    :type tmp_addr: unsigned long

    :param map_size:
        size of the region served
    :type map_size: int

.. _`pcpu_alloc_first_chunk.description`:

Description
-----------

This is responsible for creating the chunks that serve the first chunk.  The
base_addr is page aligned down of \ ``tmp_addr``\  while the region end is page
aligned up.  Offsets are kept track of to determine the region served. All
this is done to appease the bitmap allocator in avoiding partial blocks.

.. _`pcpu_alloc_first_chunk.return`:

Return
------

Chunk serving the region at \ ``tmp_addr``\  of \ ``map_size``\ .

.. _`pcpu_chunk_populated`:

pcpu_chunk_populated
====================

.. c:function:: void pcpu_chunk_populated(struct pcpu_chunk *chunk, int page_start, int page_end, bool for_alloc)

    post-population bookkeeping

    :param chunk:
        pcpu_chunk which got populated
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        the start page
    :type page_start: int

    :param page_end:
        the end page
    :type page_end: int

    :param for_alloc:
        if this is to populate for allocation
    :type for_alloc: bool

.. _`pcpu_chunk_populated.description`:

Description
-----------

Pages in [@page_start,@page_end) have been populated to \ ``chunk``\ .  Update
the bookkeeping information accordingly.  Must be called after each
successful population.

If this is \ ``for_alloc``\ , do not increment pcpu_nr_empty_pop_pages because it
is to serve an allocation in that area.

.. _`pcpu_chunk_depopulated`:

pcpu_chunk_depopulated
======================

.. c:function:: void pcpu_chunk_depopulated(struct pcpu_chunk *chunk, int page_start, int page_end)

    post-depopulation bookkeeping

    :param chunk:
        pcpu_chunk which got depopulated
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        the start page
    :type page_start: int

    :param page_end:
        the end page
    :type page_end: int

.. _`pcpu_chunk_depopulated.description`:

Description
-----------

Pages in [@page_start,@page_end) have been depopulated from \ ``chunk``\ .
Update the bookkeeping information accordingly.  Must be called after
each successful depopulation.

.. _`pcpu_chunk_addr_search`:

pcpu_chunk_addr_search
======================

.. c:function:: struct pcpu_chunk *pcpu_chunk_addr_search(void *addr)

    determine chunk containing specified address

    :param addr:
        address for which the chunk needs to be determined.
    :type addr: void \*

.. _`pcpu_chunk_addr_search.description`:

Description
-----------

This is an internal function that handles all but static allocations.
Static percpu address values should never be passed into the allocator.

.. _`pcpu_chunk_addr_search.return`:

Return
------

The address of the found chunk.

.. _`pcpu_alloc`:

pcpu_alloc
==========

.. c:function:: void __percpu *pcpu_alloc(size_t size, size_t align, bool reserved, gfp_t gfp)

    the percpu allocator

    :param size:
        size of area to allocate in bytes
    :type size: size_t

    :param align:
        alignment of area (max PAGE_SIZE)
    :type align: size_t

    :param reserved:
        allocate from the reserved chunk if available
    :type reserved: bool

    :param gfp:
        allocation flags
    :type gfp: gfp_t

.. _`pcpu_alloc.description`:

Description
-----------

Allocate percpu area of \ ``size``\  bytes aligned at \ ``align``\ .  If \ ``gfp``\  doesn't
contain \ ``GFP_KERNEL``\ , the allocation is atomic. If \ ``gfp``\  has \__GFP_NOWARN
then no warning will be triggered on invalid or failed allocation
requests.

.. _`pcpu_alloc.return`:

Return
------

Percpu pointer to the allocated area on success, NULL on failure.

.. _`__alloc_percpu_gfp`:

\__alloc_percpu_gfp
===================

.. c:function:: void __percpu *__alloc_percpu_gfp(size_t size, size_t align, gfp_t gfp)

    allocate dynamic percpu area

    :param size:
        size of area to allocate in bytes
    :type size: size_t

    :param align:
        alignment of area (max PAGE_SIZE)
    :type align: size_t

    :param gfp:
        allocation flags
    :type gfp: gfp_t

.. _`__alloc_percpu_gfp.description`:

Description
-----------

Allocate zero-filled percpu area of \ ``size``\  bytes aligned at \ ``align``\ .  If
\ ``gfp``\  doesn't contain \ ``GFP_KERNEL``\ , the allocation doesn't block and can
be called from any context but is a lot more likely to fail. If \ ``gfp``\ 
has \__GFP_NOWARN then no warning will be triggered on invalid or failed
allocation requests.

.. _`__alloc_percpu_gfp.return`:

Return
------

Percpu pointer to the allocated area on success, NULL on failure.

.. _`__alloc_percpu`:

\__alloc_percpu
===============

.. c:function:: void __percpu *__alloc_percpu(size_t size, size_t align)

    allocate dynamic percpu area

    :param size:
        size of area to allocate in bytes
    :type size: size_t

    :param align:
        alignment of area (max PAGE_SIZE)
    :type align: size_t

.. _`__alloc_percpu.description`:

Description
-----------

Equivalent to \__alloc_percpu_gfp(size, align, \ ``GFP_KERNEL``\ ).

.. _`__alloc_reserved_percpu`:

\__alloc_reserved_percpu
========================

.. c:function:: void __percpu *__alloc_reserved_percpu(size_t size, size_t align)

    allocate reserved percpu area

    :param size:
        size of area to allocate in bytes
    :type size: size_t

    :param align:
        alignment of area (max PAGE_SIZE)
    :type align: size_t

.. _`__alloc_reserved_percpu.description`:

Description
-----------

Allocate zero-filled percpu area of \ ``size``\  bytes aligned at \ ``align``\ 
from reserved percpu area if arch has set it up; otherwise,
allocation is served from the same dynamic area.  Might sleep.
Might trigger writeouts.

.. _`__alloc_reserved_percpu.context`:

Context
-------

Does GFP_KERNEL allocation.

.. _`__alloc_reserved_percpu.return`:

Return
------

Percpu pointer to the allocated area on success, NULL on failure.

.. _`pcpu_balance_workfn`:

pcpu_balance_workfn
===================

.. c:function:: void pcpu_balance_workfn(struct work_struct *work)

    manage the amount of free chunks and populated pages

    :param work:
        unused
    :type work: struct work_struct \*

.. _`pcpu_balance_workfn.description`:

Description
-----------

Reclaim all fully free chunks except for the first one.  This is also
responsible for maintaining the pool of empty populated pages.  However,
it is possible that this is called when physical memory is scarce causing
OOM killer to be triggered.  We should avoid doing so until an actual
allocation causes the failure as it is possible that requests can be
serviced from already backed regions.

.. _`free_percpu`:

free_percpu
===========

.. c:function:: void free_percpu(void __percpu *ptr)

    free percpu area

    :param ptr:
        pointer to area to free
    :type ptr: void __percpu \*

.. _`free_percpu.description`:

Description
-----------

Free percpu area \ ``ptr``\ .

.. _`free_percpu.context`:

Context
-------

Can be called from atomic context.

.. _`is_kernel_percpu_address`:

is_kernel_percpu_address
========================

.. c:function:: bool is_kernel_percpu_address(unsigned long addr)

    test whether address is from static percpu area

    :param addr:
        address to test
    :type addr: unsigned long

.. _`is_kernel_percpu_address.description`:

Description
-----------

Test whether \ ``addr``\  belongs to in-kernel static percpu area.  Module
static percpu areas are not considered.  For those, use
\ :c:func:`is_module_percpu_address`\ .

.. _`is_kernel_percpu_address.return`:

Return
------

\ ``true``\  if \ ``addr``\  is from in-kernel static percpu area, \ ``false``\  otherwise.

.. _`per_cpu_ptr_to_phys`:

per_cpu_ptr_to_phys
===================

.. c:function:: phys_addr_t per_cpu_ptr_to_phys(void *addr)

    convert translated percpu address to physical address

    :param addr:
        the address to be converted to physical address
    :type addr: void \*

.. _`per_cpu_ptr_to_phys.description`:

Description
-----------

Given \ ``addr``\  which is dereferenceable address obtained via one of
percpu access macros, this function translates it into its physical
address.  The caller is responsible for ensuring \ ``addr``\  stays valid
until this function finishes.

percpu allocator has special setup for the first chunk, which currently
supports either embedding in linear address space or vmalloc mapping,
and, from the second one, the backing allocator (currently either vm or
km) provides translation.

The addr can be translated simply without checking if it falls into the
first chunk. But the current code reflects better how percpu allocator
actually works, and the verification can discover both bugs in percpu
allocator itself and \ :c:func:`per_cpu_ptr_to_phys`\  callers. So we keep current
code.

.. _`per_cpu_ptr_to_phys.return`:

Return
------

The physical address for \ ``addr``\ .

.. _`pcpu_alloc_alloc_info`:

pcpu_alloc_alloc_info
=====================

.. c:function:: struct pcpu_alloc_info *pcpu_alloc_alloc_info(int nr_groups, int nr_units)

    allocate percpu allocation info

    :param nr_groups:
        the number of groups
    :type nr_groups: int

    :param nr_units:
        the number of units
    :type nr_units: int

.. _`pcpu_alloc_alloc_info.description`:

Description
-----------

Allocate ai which is large enough for \ ``nr_groups``\  groups containing
\ ``nr_units``\  units.  The returned ai's groups[0].cpu_map points to the
cpu_map array which is long enough for \ ``nr_units``\  and filled with
NR_CPUS.  It's the caller's responsibility to initialize cpu_map
pointer of other groups.

.. _`pcpu_alloc_alloc_info.return`:

Return
------

Pointer to the allocated pcpu_alloc_info on success, NULL on
failure.

.. _`pcpu_free_alloc_info`:

pcpu_free_alloc_info
====================

.. c:function:: void pcpu_free_alloc_info(struct pcpu_alloc_info *ai)

    free percpu allocation info

    :param ai:
        pcpu_alloc_info to free
    :type ai: struct pcpu_alloc_info \*

.. _`pcpu_free_alloc_info.description`:

Description
-----------

Free \ ``ai``\  which was allocated by \ :c:func:`pcpu_alloc_alloc_info`\ .

.. _`pcpu_dump_alloc_info`:

pcpu_dump_alloc_info
====================

.. c:function:: void pcpu_dump_alloc_info(const char *lvl, const struct pcpu_alloc_info *ai)

    print out information about pcpu_alloc_info

    :param lvl:
        loglevel
    :type lvl: const char \*

    :param ai:
        allocation info to dump
    :type ai: const struct pcpu_alloc_info \*

.. _`pcpu_dump_alloc_info.description`:

Description
-----------

Print out information about \ ``ai``\  using loglevel \ ``lvl``\ .

.. _`pcpu_setup_first_chunk`:

pcpu_setup_first_chunk
======================

.. c:function:: int pcpu_setup_first_chunk(const struct pcpu_alloc_info *ai, void *base_addr)

    initialize the first percpu chunk

    :param ai:
        pcpu_alloc_info describing how to percpu area is shaped
    :type ai: const struct pcpu_alloc_info \*

    :param base_addr:
        mapped address
    :type base_addr: void \*

.. _`pcpu_setup_first_chunk.description`:

Description
-----------

Initialize the first percpu chunk which contains the kernel static
perpcu area.  This function is to be called from arch percpu area
setup path.

\ ``ai``\  contains all information necessary to initialize the first
chunk and prime the dynamic percpu allocator.

\ ``ai->static_size``\  is the size of static percpu area.

\ ``ai->reserved_size``\ , if non-zero, specifies the amount of bytes to
reserve after the static area in the first chunk.  This reserves
the first chunk such that it's available only through reserved
percpu allocation.  This is primarily used to serve module percpu
static areas on architectures where the addressing model has
limited offset range for symbol relocations to guarantee module
percpu symbols fall inside the relocatable range.

\ ``ai->dyn_size``\  determines the number of bytes available for dynamic
allocation in the first chunk.  The area between \ ``ai->static_size``\  +
\ ``ai->reserved_size``\  + \ ``ai->dyn_size``\  and \ ``ai->unit_size``\  is unused.

\ ``ai->unit_size``\  specifies unit size and must be aligned to PAGE_SIZE
and equal to or larger than \ ``ai->static_size``\  + \ ``ai->reserved_size``\  +
\ ``ai->dyn_size``\ .

\ ``ai->atom_size``\  is the allocation atom size and used as alignment
for vm areas.

\ ``ai->alloc_size``\  is the allocation size and always multiple of
\ ``ai->atom_size``\ .  This is larger than \ ``ai->atom_size``\  if
\ ``ai->unit_size``\  is larger than \ ``ai->atom_size``\ .

\ ``ai->nr_groups``\  and \ ``ai->groups``\  describe virtual memory layout of
percpu areas.  Units which should be colocated are put into the
same group.  Dynamic VM areas will be allocated according to these
groupings.  If \ ``ai->nr_groups``\  is zero, a single group containing
all units is assumed.

The caller should have mapped the first chunk at \ ``base_addr``\  and
copied static data to each unit.

The first chunk will always contain a static and a dynamic region.
However, the static region is not managed by any chunk.  If the first
chunk also contains a reserved region, it is served by two chunks -
one for the reserved region and one for the dynamic region.  They
share the same vm, but use offset regions in the area allocation map.
The chunk serving the dynamic region is circulated in the chunk slots
and available for dynamic allocation like any other chunk.

.. _`pcpu_setup_first_chunk.return`:

Return
------

0 on success, -errno on failure.

.. _`pcpu_build_alloc_info`:

pcpu_build_alloc_info
=====================

.. c:function:: struct pcpu_alloc_info *pcpu_build_alloc_info(size_t reserved_size, size_t dyn_size, size_t atom_size, pcpu_fc_cpu_distance_fn_t cpu_distance_fn)

    build alloc_info considering distances between CPUs

    :param reserved_size:
        the size of reserved percpu area in bytes
    :type reserved_size: size_t

    :param dyn_size:
        minimum free size for dynamic allocation in bytes
    :type dyn_size: size_t

    :param atom_size:
        allocation atom size
    :type atom_size: size_t

    :param cpu_distance_fn:
        callback to determine distance between cpus, optional
    :type cpu_distance_fn: pcpu_fc_cpu_distance_fn_t

.. _`pcpu_build_alloc_info.description`:

Description
-----------

This function determines grouping of units, their mappings to cpus
and other parameters considering needed percpu size, allocation
atom size and distances between CPUs.

Groups are always multiples of atom size and CPUs which are of
LOCAL_DISTANCE both ways are grouped together and share space for
units in the same group.  The returned configuration is guaranteed
to have CPUs on different nodes on different groups and >=75% usage
of allocated virtual address space.

.. _`pcpu_build_alloc_info.return`:

Return
------

On success, pointer to the new allocation_info is returned.  On
failure, ERR_PTR value is returned.

.. _`pcpu_embed_first_chunk`:

pcpu_embed_first_chunk
======================

.. c:function:: int pcpu_embed_first_chunk(size_t reserved_size, size_t dyn_size, size_t atom_size, pcpu_fc_cpu_distance_fn_t cpu_distance_fn, pcpu_fc_alloc_fn_t alloc_fn, pcpu_fc_free_fn_t free_fn)

    embed the first percpu chunk into bootmem

    :param reserved_size:
        the size of reserved percpu area in bytes
    :type reserved_size: size_t

    :param dyn_size:
        minimum free size for dynamic allocation in bytes
    :type dyn_size: size_t

    :param atom_size:
        allocation atom size
    :type atom_size: size_t

    :param cpu_distance_fn:
        callback to determine distance between cpus, optional
    :type cpu_distance_fn: pcpu_fc_cpu_distance_fn_t

    :param alloc_fn:
        function to allocate percpu page
    :type alloc_fn: pcpu_fc_alloc_fn_t

    :param free_fn:
        function to free percpu page
    :type free_fn: pcpu_fc_free_fn_t

.. _`pcpu_embed_first_chunk.description`:

Description
-----------

This is a helper to ease setting up embedded first percpu chunk and
can be called where \ :c:func:`pcpu_setup_first_chunk`\  is expected.

If this function is used to setup the first chunk, it is allocated
by calling \ ``alloc_fn``\  and used as-is without being mapped into
vmalloc area.  Allocations are always whole multiples of \ ``atom_size``\ 
aligned to \ ``atom_size``\ .

This enables the first chunk to piggy back on the linear physical
mapping which often uses larger page size.  Please note that this
can result in very sparse cpu->unit mapping on NUMA machines thus
requiring large vmalloc address space.  Don't use this allocator if
vmalloc space is not orders of magnitude larger than distances
between node memory addresses (ie. 32bit NUMA machines).

\ ``dyn_size``\  specifies the minimum dynamic area size.

If the needed size is smaller than the minimum or specified unit
size, the leftover is returned using \ ``free_fn``\ .

.. _`pcpu_embed_first_chunk.return`:

Return
------

0 on success, -errno on failure.

.. _`pcpu_page_first_chunk`:

pcpu_page_first_chunk
=====================

.. c:function:: int pcpu_page_first_chunk(size_t reserved_size, pcpu_fc_alloc_fn_t alloc_fn, pcpu_fc_free_fn_t free_fn, pcpu_fc_populate_pte_fn_t populate_pte_fn)

    map the first chunk using PAGE_SIZE pages

    :param reserved_size:
        the size of reserved percpu area in bytes
    :type reserved_size: size_t

    :param alloc_fn:
        function to allocate percpu page, always called with PAGE_SIZE
    :type alloc_fn: pcpu_fc_alloc_fn_t

    :param free_fn:
        function to free percpu page, always called with PAGE_SIZE
    :type free_fn: pcpu_fc_free_fn_t

    :param populate_pte_fn:
        function to populate pte
    :type populate_pte_fn: pcpu_fc_populate_pte_fn_t

.. _`pcpu_page_first_chunk.description`:

Description
-----------

This is a helper to ease setting up page-remapped first percpu
chunk and can be called where \ :c:func:`pcpu_setup_first_chunk`\  is expected.

This is the basic allocator.  Static percpu area is allocated
page-by-page into vmalloc area.

.. _`pcpu_page_first_chunk.return`:

Return
------

0 on success, -errno on failure.

.. This file was automatic generated / don't edit.

