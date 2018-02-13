.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/efi/memmap.c

.. _`efi_memmap_alloc`:

efi_memmap_alloc
================

.. c:function:: phys_addr_t efi_memmap_alloc(unsigned int num_entries)

    Allocate memory for the EFI memory map

    :param unsigned int num_entries:
        Number of entries in the allocated map.

.. _`efi_memmap_alloc.description`:

Description
-----------

Depending on whether \ :c:func:`mm_init`\  has already been invoked or not,
either memblock or "normal" page allocation is used.

Returns the physical address of the allocated memory map on
success, zero on failure.

.. _`__efi_memmap_init`:

\__efi_memmap_init
==================

.. c:function:: int __efi_memmap_init(struct efi_memory_map_data *data, bool late)

    Common code for mapping the EFI memory map

    :param struct efi_memory_map_data \*data:
        EFI memory map data

    :param bool late:
        Use early or late mapping function?

.. _`__efi_memmap_init.description`:

Description
-----------

This function takes care of figuring out which function to use to
map the EFI memory map in efi.memmap based on how far into the boot
we are.

During bootup \ ``late``\  should be \ ``false``\  since we only have access to
the early_memremap\*() functions as the vmalloc space isn't setup.
Once the kernel is fully booted we can fallback to the more robust
memremap\*() API.

Returns zero on success, a negative error code on failure.

.. _`efi_memmap_init_early`:

efi_memmap_init_early
=====================

.. c:function:: int efi_memmap_init_early(struct efi_memory_map_data *data)

    Map the EFI memory map data structure

    :param struct efi_memory_map_data \*data:
        EFI memory map data

.. _`efi_memmap_init_early.description`:

Description
-----------

Use \ :c:func:`early_memremap`\  to map the passed in EFI memory map and assign
it to efi.memmap.

.. _`efi_memmap_init_late`:

efi_memmap_init_late
====================

.. c:function:: int efi_memmap_init_late(phys_addr_t addr, unsigned long size)

    Map efi.memmap with \ :c:func:`memremap`\ 

    :param phys_addr_t addr:
        *undescribed*

    :param unsigned long size:
        Size in bytes of the new EFI memory map

.. _`efi_memmap_init_late.description`:

Description
-----------

Setup a mapping of the EFI memory map using \ :c:func:`ioremap_cache`\ . This
function should only be called once the vmalloc space has been
setup and is therefore not suitable for calling during early EFI
initialise, e.g. in \ :c:func:`efi_init`\ . Additionally, it expects
\ :c:func:`efi_memmap_init_early`\  to have already been called.

The reason there are two EFI memmap initialisation
(efi_memmap_init_early() and this late version) is because the
early EFI memmap should be explicitly unmapped once EFI
initialisation is complete as the fixmap space used to map the EFI
memmap (via \ :c:func:`early_memremap`\ ) is a scarce resource.

This late mapping is intended to persist for the duration of
runtime so that things like \ :c:func:`efi_mem_desc_lookup`\  and
\ :c:func:`efi_mem_attributes`\  always work.

Returns zero on success, a negative error code on failure.

.. _`efi_memmap_install`:

efi_memmap_install
==================

.. c:function:: int efi_memmap_install(phys_addr_t addr, unsigned int nr_map)

    Install a new EFI memory map in efi.memmap

    :param phys_addr_t addr:
        Physical address of the memory map

    :param unsigned int nr_map:
        Number of entries in the memory map

.. _`efi_memmap_install.description`:

Description
-----------

Unlike efi_memmap_init\_\*(), this function does not allow the caller
to switch from early to late mappings. It simply uses the existing
mapping function and installs the new memmap.

Returns zero on success, a negative error code on failure.

.. _`efi_memmap_split_count`:

efi_memmap_split_count
======================

.. c:function:: int efi_memmap_split_count(efi_memory_desc_t *md, struct range *range)

    Count number of additional EFI memmap entries

    :param efi_memory_desc_t \*md:
        EFI memory descriptor to split

    :param struct range \*range:
        Address range (start, end) to split around

.. _`efi_memmap_split_count.description`:

Description
-----------

Returns the number of additional EFI memmap entries required to
accomodate \ ``range``\ .

.. _`efi_memmap_insert`:

efi_memmap_insert
=================

.. c:function:: void efi_memmap_insert(struct efi_memory_map *old_memmap, void *buf, struct efi_mem_range *mem)

    Insert a memory region in an EFI memmap

    :param struct efi_memory_map \*old_memmap:
        The existing EFI memory map structure

    :param void \*buf:
        Address of buffer to store new map

    :param struct efi_mem_range \*mem:
        Memory map entry to insert

.. _`efi_memmap_insert.description`:

Description
-----------

It is suggested that you call \ :c:func:`efi_memmap_split_count`\  first
to see how large \ ``buf``\  needs to be.

.. This file was automatic generated / don't edit.

