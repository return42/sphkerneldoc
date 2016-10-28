.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/percpu.c

.. _`pcpu_mem_zalloc`:

pcpu_mem_zalloc
===============

.. c:function:: void *pcpu_mem_zalloc(size_t size)

    allocate memory

    :param size_t size:
        bytes to allocate

.. _`pcpu_mem_zalloc.description`:

Description
-----------

Allocate \ ``size``\  bytes.  If \ ``size``\  is smaller than PAGE_SIZE,
\ :c:func:`kzalloc`\  is used; otherwise, \ :c:func:`vzalloc`\  is used.  The returned
memory is always zeroed.

.. _`pcpu_mem_zalloc.context`:

Context
-------

Does GFP_KERNEL allocation.

.. _`pcpu_mem_zalloc.return`:

Return
------

Pointer to the allocated area on success, NULL on failure.

.. _`pcpu_mem_free`:

pcpu_mem_free
=============

.. c:function:: void pcpu_mem_free(void *ptr)

    free memory

    :param void \*ptr:
        memory to free

.. _`pcpu_mem_free.description`:

Description
-----------

Free \ ``ptr``\ .  \ ``ptr``\  should have been allocated using \ :c:func:`pcpu_mem_zalloc`\ .

.. _`pcpu_count_occupied_pages`:

pcpu_count_occupied_pages
=========================

.. c:function:: int pcpu_count_occupied_pages(struct pcpu_chunk *chunk, int i)

    count the number of pages an area occupies

    :param struct pcpu_chunk \*chunk:
        chunk of interest

    :param int i:
        index of the area in question

.. _`pcpu_count_occupied_pages.description`:

Description
-----------

Count the number of pages chunk's \ ``i``\ 'th area occupies.  When the area's
start and/or end address isn't aligned to page boundary, the straddled
page is included in the count iff the rest of the page is free.

.. _`pcpu_chunk_relocate`:

pcpu_chunk_relocate
===================

.. c:function:: void pcpu_chunk_relocate(struct pcpu_chunk *chunk, int oslot)

    put chunk in the appropriate chunk slot

    :param struct pcpu_chunk \*chunk:
        chunk of interest

    :param int oslot:
        the previous slot it was on

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

.. _`pcpu_need_to_extend`:

pcpu_need_to_extend
===================

.. c:function:: int pcpu_need_to_extend(struct pcpu_chunk *chunk, bool is_atomic)

    determine whether chunk area map needs to be extended

    :param struct pcpu_chunk \*chunk:
        chunk of interest

    :param bool is_atomic:
        the allocation context

.. _`pcpu_need_to_extend.description`:

Description
-----------

Determine whether area map of \ ``chunk``\  needs to be extended.  If
\ ``is_atomic``\ , only the amount necessary for a new allocation is
considered; however, async extension is scheduled if the left amount is
low.  If !\ ``is_atomic``\ , it aims for more empty space.  Combined, this
ensures that the map is likely to have enough available space to
accomodate atomic allocations which can't extend maps directly.

.. _`pcpu_need_to_extend.context`:

Context
-------

pcpu_lock.

.. _`pcpu_need_to_extend.return`:

Return
------

New target map allocation length if extension is necessary, 0
otherwise.

.. _`pcpu_extend_area_map`:

pcpu_extend_area_map
====================

.. c:function:: int pcpu_extend_area_map(struct pcpu_chunk *chunk, int new_alloc)

    extend area map of a chunk

    :param struct pcpu_chunk \*chunk:
        chunk of interest

    :param int new_alloc:
        new target allocation length of the area map

.. _`pcpu_extend_area_map.description`:

Description
-----------

Extend area map of \ ``chunk``\  to have \ ``new_alloc``\  entries.

.. _`pcpu_extend_area_map.context`:

Context
-------

Does GFP_KERNEL allocation.  Grabs and releases pcpu_lock.

.. _`pcpu_extend_area_map.return`:

Return
------

0 on success, -errno on failure.

.. _`pcpu_fit_in_area`:

pcpu_fit_in_area
================

.. c:function:: int pcpu_fit_in_area(struct pcpu_chunk *chunk, int off, int this_size, int size, int align, bool pop_only)

    try to fit the requested allocation in a candidate area

    :param struct pcpu_chunk \*chunk:
        chunk the candidate area belongs to

    :param int off:
        the offset to the start of the candidate area

    :param int this_size:
        the size of the candidate area

    :param int size:
        the size of the target allocation

    :param int align:
        the alignment of the target allocation

    :param bool pop_only:
        only allocate from already populated region

.. _`pcpu_fit_in_area.description`:

Description
-----------

We're trying to allocate \ ``size``\  bytes aligned at \ ``align``\ .  \ ``chunk``\ 's area
at \ ``off``\  sized \ ``this_size``\  is a candidate.  This function determines
whether the target allocation fits in the candidate area and returns the
number of bytes to pad after \ ``off``\ .  If the target area doesn't fit, -1
is returned.

If \ ``pop_only``\  is \ ``true``\ , this function only considers the already
populated part of the candidate area.

.. _`pcpu_alloc_area`:

pcpu_alloc_area
===============

.. c:function:: int pcpu_alloc_area(struct pcpu_chunk *chunk, int size, int align, bool pop_only, int *occ_pages_p)

    allocate area from a pcpu_chunk

    :param struct pcpu_chunk \*chunk:
        chunk of interest

    :param int size:
        wanted size in bytes

    :param int align:
        wanted align

    :param bool pop_only:
        allocate only from the populated area

    :param int \*occ_pages_p:
        out param for the number of pages the area occupies

.. _`pcpu_alloc_area.description`:

Description
-----------

Try to allocate \ ``size``\  bytes area aligned at \ ``align``\  from \ ``chunk``\ .
Note that this function only allocates the offset.  It doesn't
populate or map the area.

\ ``chunk``\ ->map must have at least two free slots.

.. _`pcpu_alloc_area.context`:

Context
-------

pcpu_lock.

.. _`pcpu_alloc_area.return`:

Return
------

Allocated offset in \ ``chunk``\  on success, -1 if no matching area is
found.

.. _`pcpu_free_area`:

pcpu_free_area
==============

.. c:function:: void pcpu_free_area(struct pcpu_chunk *chunk, int freeme, int *occ_pages_p)

    free area to a pcpu_chunk

    :param struct pcpu_chunk \*chunk:
        chunk of interest

    :param int freeme:
        offset of area to free

    :param int \*occ_pages_p:
        out param for the number of pages the area occupies

.. _`pcpu_free_area.description`:

Description
-----------

Free area starting from \ ``freeme``\  to \ ``chunk``\ .  Note that this function
only modifies the allocation map.  It doesn't depopulate or unmap
the area.

.. _`pcpu_free_area.context`:

Context
-------

pcpu_lock.

.. _`pcpu_chunk_populated`:

pcpu_chunk_populated
====================

.. c:function:: void pcpu_chunk_populated(struct pcpu_chunk *chunk, int page_start, int page_end)

    post-population bookkeeping

    :param struct pcpu_chunk \*chunk:
        pcpu_chunk which got populated

    :param int page_start:
        the start page

    :param int page_end:
        the end page

.. _`pcpu_chunk_populated.description`:

Description
-----------

Pages in [\ ``page_start``\ ,\ ``page_end``\ ) have been populated to \ ``chunk``\ .  Update
the bookkeeping information accordingly.  Must be called after each
successful population.

.. _`pcpu_chunk_depopulated`:

pcpu_chunk_depopulated
======================

.. c:function:: void pcpu_chunk_depopulated(struct pcpu_chunk *chunk, int page_start, int page_end)

    post-depopulation bookkeeping

    :param struct pcpu_chunk \*chunk:
        pcpu_chunk which got depopulated

    :param int page_start:
        the start page

    :param int page_end:
        the end page

.. _`pcpu_chunk_depopulated.description`:

Description
-----------

Pages in [\ ``page_start``\ ,\ ``page_end``\ ) have been depopulated from \ ``chunk``\ .
Update the bookkeeping information accordingly.  Must be called after
each successful depopulation.

.. _`pcpu_chunk_addr_search`:

pcpu_chunk_addr_search
======================

.. c:function:: struct pcpu_chunk *pcpu_chunk_addr_search(void *addr)

    determine chunk containing specified address

    :param void \*addr:
        address for which the chunk needs to be determined.

.. _`pcpu_chunk_addr_search.return`:

Return
------

The address of the found chunk.

.. _`pcpu_alloc`:

pcpu_alloc
==========

.. c:function:: void __percpu *pcpu_alloc(size_t size, size_t align, bool reserved, gfp_t gfp)

    the percpu allocator

    :param size_t size:
        size of area to allocate in bytes

    :param size_t align:
        alignment of area (max PAGE_SIZE)

    :param bool reserved:
        allocate from the reserved chunk if available

    :param gfp_t gfp:
        allocation flags

.. _`pcpu_alloc.description`:

Description
-----------

Allocate percpu area of \ ``size``\  bytes aligned at \ ``align``\ .  If \ ``gfp``\  doesn't
contain \ ``GFP_KERNEL``\ , the allocation is atomic.

.. _`pcpu_alloc.return`:

Return
------

Percpu pointer to the allocated area on success, NULL on failure.

.. _`__alloc_percpu_gfp`:

__alloc_percpu_gfp
==================

.. c:function:: void __percpu *__alloc_percpu_gfp(size_t size, size_t align, gfp_t gfp)

    allocate dynamic percpu area

    :param size_t size:
        size of area to allocate in bytes

    :param size_t align:
        alignment of area (max PAGE_SIZE)

    :param gfp_t gfp:
        allocation flags

.. _`__alloc_percpu_gfp.description`:

Description
-----------

Allocate zero-filled percpu area of \ ``size``\  bytes aligned at \ ``align``\ .  If
\ ``gfp``\  doesn't contain \ ``GFP_KERNEL``\ , the allocation doesn't block and can
be called from any context but is a lot more likely to fail.

.. _`__alloc_percpu_gfp.return`:

Return
------

Percpu pointer to the allocated area on success, NULL on failure.

.. _`__alloc_percpu`:

__alloc_percpu
==============

.. c:function:: void __percpu *__alloc_percpu(size_t size, size_t align)

    allocate dynamic percpu area

    :param size_t size:
        size of area to allocate in bytes

    :param size_t align:
        alignment of area (max PAGE_SIZE)

.. _`__alloc_percpu.description`:

Description
-----------

Equivalent to \__alloc_percpu_gfp(size, align, \ ``GFP_KERNEL``\ ).

.. _`__alloc_reserved_percpu`:

__alloc_reserved_percpu
=======================

.. c:function:: void __percpu *__alloc_reserved_percpu(size_t size, size_t align)

    allocate reserved percpu area

    :param size_t size:
        size of area to allocate in bytes

    :param size_t align:
        alignment of area (max PAGE_SIZE)

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

    :param struct work_struct \*work:
        unused

.. _`pcpu_balance_workfn.description`:

Description
-----------

Reclaim all fully free chunks except for the first one.

.. _`free_percpu`:

free_percpu
===========

.. c:function:: void free_percpu(void __percpu *ptr)

    free percpu area

    :param void __percpu \*ptr:
        pointer to area to free

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

    :param unsigned long addr:
        address to test

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

    :param void \*addr:
        the address to be converted to physical address

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

    :param int nr_groups:
        the number of groups

    :param int nr_units:
        the number of units

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

    :param struct pcpu_alloc_info \*ai:
        pcpu_alloc_info to free

.. _`pcpu_free_alloc_info.description`:

Description
-----------

Free \ ``ai``\  which was allocated by \ :c:func:`pcpu_alloc_alloc_info`\ .

.. _`pcpu_dump_alloc_info`:

pcpu_dump_alloc_info
====================

.. c:function:: void pcpu_dump_alloc_info(const char *lvl, const struct pcpu_alloc_info *ai)

    print out information about pcpu_alloc_info

    :param const char \*lvl:
        loglevel

    :param const struct pcpu_alloc_info \*ai:
        allocation info to dump

.. _`pcpu_dump_alloc_info.description`:

Description
-----------

Print out information about \ ``ai``\  using loglevel \ ``lvl``\ .

.. _`pcpu_setup_first_chunk`:

pcpu_setup_first_chunk
======================

.. c:function:: int pcpu_setup_first_chunk(const struct pcpu_alloc_info *ai, void *base_addr)

    initialize the first percpu chunk

    :param const struct pcpu_alloc_info \*ai:
        pcpu_alloc_info describing how to percpu area is shaped

    :param void \*base_addr:
        mapped address

.. _`pcpu_setup_first_chunk.description`:

Description
-----------

Initialize the first percpu chunk which contains the kernel static
perpcu area.  This function is to be called from arch percpu area
setup path.

\ ``ai``\  contains all information necessary to initialize the first
chunk and prime the dynamic percpu allocator.

\ ``ai``\ ->static_size is the size of static percpu area.

\ ``ai``\ ->reserved_size, if non-zero, specifies the amount of bytes to
reserve after the static area in the first chunk.  This reserves
the first chunk such that it's available only through reserved
percpu allocation.  This is primarily used to serve module percpu
static areas on architectures where the addressing model has
limited offset range for symbol relocations to guarantee module
percpu symbols fall inside the relocatable range.

\ ``ai``\ ->dyn_size determines the number of bytes available for dynamic
allocation in the first chunk.  The area between \ ``ai``\ ->static_size +
\ ``ai``\ ->reserved_size + \ ``ai``\ ->dyn_size and \ ``ai``\ ->unit_size is unused.

\ ``ai``\ ->unit_size specifies unit size and must be aligned to PAGE_SIZE
and equal to or larger than \ ``ai``\ ->static_size + \ ``ai``\ ->reserved_size +
\ ``ai``\ ->dyn_size.

\ ``ai``\ ->atom_size is the allocation atom size and used as alignment
for vm areas.

\ ``ai``\ ->alloc_size is the allocation size and always multiple of
\ ``ai``\ ->atom_size.  This is larger than \ ``ai``\ ->atom_size if
\ ``ai``\ ->unit_size is larger than \ ``ai``\ ->atom_size.

\ ``ai``\ ->nr_groups and \ ``ai``\ ->groups describe virtual memory layout of
percpu areas.  Units which should be colocated are put into the
same group.  Dynamic VM areas will be allocated according to these
groupings.  If \ ``ai``\ ->nr_groups is zero, a single group containing
all units is assumed.

The caller should have mapped the first chunk at \ ``base_addr``\  and
copied static data to each unit.

If the first chunk ends up with both reserved and dynamic areas, it
is served by two chunks - one to serve the core static and reserved
areas and the other for the dynamic area.  They share the same vm
and page map but uses different area allocation map to stay away
from each other.  The latter chunk is circulated in the chunk slots
and available for dynamic allocation like any other chunks.

.. _`pcpu_setup_first_chunk.return`:

Return
------

0 on success, -errno on failure.

.. _`pcpu_build_alloc_info`:

pcpu_build_alloc_info
=====================

.. c:function:: struct pcpu_alloc_info *pcpu_build_alloc_info(size_t reserved_size, size_t dyn_size, size_t atom_size, pcpu_fc_cpu_distance_fn_t cpu_distance_fn)

    build alloc_info considering distances between CPUs

    :param size_t reserved_size:
        the size of reserved percpu area in bytes

    :param size_t dyn_size:
        minimum free size for dynamic allocation in bytes

    :param size_t atom_size:
        allocation atom size

    :param pcpu_fc_cpu_distance_fn_t cpu_distance_fn:
        callback to determine distance between cpus, optional

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

    :param size_t reserved_size:
        the size of reserved percpu area in bytes

    :param size_t dyn_size:
        minimum free size for dynamic allocation in bytes

    :param size_t atom_size:
        allocation atom size

    :param pcpu_fc_cpu_distance_fn_t cpu_distance_fn:
        callback to determine distance between cpus, optional

    :param pcpu_fc_alloc_fn_t alloc_fn:
        function to allocate percpu page

    :param pcpu_fc_free_fn_t free_fn:
        function to free percpu page

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

    :param size_t reserved_size:
        the size of reserved percpu area in bytes

    :param pcpu_fc_alloc_fn_t alloc_fn:
        function to allocate percpu page, always called with PAGE_SIZE

    :param pcpu_fc_free_fn_t free_fn:
        function to free percpu page, always called with PAGE_SIZE

    :param pcpu_fc_populate_pte_fn_t populate_pte_fn:
        function to populate pte

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

