.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-bootmem.h

.. _`cvmx_bootmem_init`:

cvmx_bootmem_init
=================

.. c:function:: int cvmx_bootmem_init(void *mem_desc_ptr)

    normally called inside of \ :c:func:`cvmx_user_app_init`\ 

    :param mem_desc_ptr:
        Address of the free memory list
    :type mem_desc_ptr: void \*

.. _`cvmx_bootmem_alloc`:

cvmx_bootmem_alloc
==================

.. c:function:: void *cvmx_bootmem_alloc(uint64_t size, uint64_t alignment)

    to the application by the bootloader. This is an allocate-only algorithm, so freeing memory is not possible.

    :param size:
        Size in bytes of block to allocate
    :type size: uint64_t

    :param alignment:
        Alignment required - must be power of 2
    :type alignment: uint64_t

.. _`cvmx_bootmem_alloc.description`:

Description
-----------

Returns pointer to block of memory, NULL on error

.. _`cvmx_bootmem_alloc_address`:

cvmx_bootmem_alloc_address
==========================

.. c:function:: void *cvmx_bootmem_alloc_address(uint64_t size, uint64_t address, uint64_t alignment)

    passed to the application by the bootloader at a specific address. This is an allocate-only algorithm, so freeing memory is not possible. Allocation will fail if memory cannot be allocated at the specified address.

    :param size:
        Size in bytes of block to allocate
    :type size: uint64_t

    :param address:
        Physical address to allocate memory at.  If this memory is not
        available, the allocation fails.
    :type address: uint64_t

    :param alignment:
        Alignment required - must be power of 2
        Returns pointer to block of memory, NULL on error
    :type alignment: uint64_t

.. _`cvmx_bootmem_alloc_range`:

cvmx_bootmem_alloc_range
========================

.. c:function:: void *cvmx_bootmem_alloc_range(uint64_t size, uint64_t alignment, uint64_t min_addr, uint64_t max_addr)

    passed to the application by the bootloader within a specified address range. This is an allocate-only algorithm, so freeing memory is not possible. Allocation will fail if memory cannot be allocated in the requested range.

    :param size:
        Size in bytes of block to allocate
    :type size: uint64_t

    :param alignment:
        Alignment required - must be power of 2
        Returns pointer to block of memory, NULL on error
    :type alignment: uint64_t

    :param min_addr:
        defines the minimum address of the range
    :type min_addr: uint64_t

    :param max_addr:
        defines the maximum address of the range
    :type max_addr: uint64_t

.. _`cvmx_bootmem_alloc_named`:

cvmx_bootmem_alloc_named
========================

.. c:function:: void *cvmx_bootmem_alloc_named(uint64_t size, uint64_t alignment, char *name)

    :param size:
        *undescribed*
    :type size: uint64_t

    :param alignment:
        *undescribed*
    :type alignment: uint64_t

    :param name:
        name of block to free
    :type name: char \*

.. _`cvmx_bootmem_alloc_named.description`:

Description
-----------

Returns 0 on failure,
!0 on success

.. _`cvmx_bootmem_alloc_named_address`:

cvmx_bootmem_alloc_named_address
================================

.. c:function:: void *cvmx_bootmem_alloc_named_address(uint64_t size, uint64_t address, char *name)

    to the application by the bootloader, and assign it a name in the global named block table.  (part of the cvmx_bootmem_descriptor_t structure) Named blocks can later be freed.

    :param size:
        Size in bytes of block to allocate
    :type size: uint64_t

    :param address:
        Physical address to allocate memory at.  If this
        memory is not available, the allocation fails.
    :type address: uint64_t

    :param name:
        name of block - must be less than CVMX_BOOTMEM_NAME_LEN
        bytes
    :type name: char \*

.. _`cvmx_bootmem_alloc_named_address.description`:

Description
-----------

Returns a pointer to block of memory, NULL on error

.. _`cvmx_bootmem_alloc_named_range`:

cvmx_bootmem_alloc_named_range
==============================

.. c:function:: void *cvmx_bootmem_alloc_named_range(uint64_t size, uint64_t min_addr, uint64_t max_addr, uint64_t align, char *name)

    that was passed to the application by the bootloader, and assign it a name in the global named block table.  (part of the cvmx_bootmem_descriptor_t structure) Named blocks can later be freed.  If request cannot be satisfied within the address range specified, NULL is returned

    :param size:
        Size in bytes of block to allocate
    :type size: uint64_t

    :param min_addr:
        minimum address of range
    :type min_addr: uint64_t

    :param max_addr:
        maximum address of range
    :type max_addr: uint64_t

    :param align:
        Alignment of memory to be allocated. (must be a power of 2)
    :type align: uint64_t

    :param name:
        name of block - must be less than CVMX_BOOTMEM_NAME_LEN bytes
    :type name: char \*

.. _`cvmx_bootmem_alloc_named_range.description`:

Description
-----------

Returns a pointer to block of memory, NULL on error

.. _`cvmx_bootmem_alloc_named_range_once`:

cvmx_bootmem_alloc_named_range_once
===================================

.. c:function:: void *cvmx_bootmem_alloc_named_range_once(uint64_t size, uint64_t min_addr, uint64_t max_addr, uint64_t align, char *name, void (*init)(void *))

    free list that was passed to the application by the bootloader, and assign it a name in the global named block table.  (part of the cvmx_bootmem_descriptor_t structure) Named blocks can later be freed.  If the requested name block is already allocated, return the pointer to block of memory.  If request cannot be satisfied within the address range specified, NULL is returned

    :param size:
        *undescribed*
    :type size: uint64_t

    :param min_addr:
        *undescribed*
    :type min_addr: uint64_t

    :param max_addr:
        *undescribed*
    :type max_addr: uint64_t

    :param align:
        *undescribed*
    :type align: uint64_t

    :param name:
        *undescribed*
    :type name: char \*

    :param void (\*init)(void \*):
        *undescribed*

.. _`cvmx_bootmem_alloc_named_range_once.description`:

Description
-----------

\ ``param``\  size   Size in bytes of block to allocate
\ ``param``\  min_addr  minimum address of range
\ ``param``\  max_addr  maximum address of range
\ ``param``\  align  Alignment of memory to be allocated. (must be a power of 2)
\ ``param``\  name   name of block - must be less than CVMX_BOOTMEM_NAME_LEN bytes
\ ``param``\  init   Initialization function

The initialization function is optional, if omitted the named block
is initialized to all zeros when it is created, i.e. once.

\ ``return``\  pointer to block of memory, NULL on error

.. _`cvmx_bootmem_find_named_block`:

cvmx_bootmem_find_named_block
=============================

.. c:function:: struct cvmx_bootmem_named_block_desc *cvmx_bootmem_find_named_block(char *name)

    :param name:
        name of block to free
    :type name: char \*

.. _`cvmx_bootmem_find_named_block.description`:

Description
-----------

Returns pointer to named block descriptor on success
0 on failure

.. _`cvmx_bootmem_phy_alloc`:

cvmx_bootmem_phy_alloc
======================

.. c:function:: int64_t cvmx_bootmem_phy_alloc(uint64_t req_size, uint64_t address_min, uint64_t address_max, uint64_t alignment, uint32_t flags)

    (optional) requested address and alignment.

    :param req_size:
        size of region to allocate.  All requests are rounded up
        to be a multiple CVMX_BOOTMEM_ALIGNMENT_SIZE bytes size
    :type req_size: uint64_t

    :param address_min:
        Minimum address that block can occupy.
    :type address_min: uint64_t

    :param address_max:
        Specifies the maximum address_min (inclusive) that
        the allocation can use.
    :type address_max: uint64_t

    :param alignment:
        Requested alignment of the block.  If this alignment
        cannot be met, the allocation fails.  This must be a
        power of 2.  (Note: Alignment of
        CVMX_BOOTMEM_ALIGNMENT_SIZE bytes is required, and
        internally enforced.  Requested alignments of less than
        CVMX_BOOTMEM_ALIGNMENT_SIZE are set to
        CVMX_BOOTMEM_ALIGNMENT_SIZE.)
    :type alignment: uint64_t

    :param flags:
        Flags to control options for the allocation.
    :type flags: uint32_t

.. _`cvmx_bootmem_phy_alloc.description`:

Description
-----------

Returns physical address of block allocated, or -1 on failure

.. _`cvmx_bootmem_phy_named_block_alloc`:

cvmx_bootmem_phy_named_block_alloc
==================================

.. c:function:: int64_t cvmx_bootmem_phy_named_block_alloc(uint64_t size, uint64_t min_addr, uint64_t max_addr, uint64_t alignment, char *name, uint32_t flags)

    (optional) requested address and alignment.

    :param size:
        *undescribed*
    :type size: uint64_t

    :param min_addr:
        *undescribed*
    :type min_addr: uint64_t

    :param max_addr:
        *undescribed*
    :type max_addr: uint64_t

    :param alignment:
        *undescribed*
    :type alignment: uint64_t

    :param name:
        *undescribed*
    :type name: char \*

    :param flags:
        *undescribed*
    :type flags: uint32_t

.. _`cvmx_bootmem_phy_named_block_alloc.description`:

Description
-----------

\ ``param``\  size      size of region to allocate.  All requests are rounded
up to be a multiple CVMX_BOOTMEM_ALIGNMENT_SIZE
bytes size
\ ``param``\  min_addr Minimum address that block can occupy.
\ ``param``\  max_addr  Specifies the maximum address_min (inclusive) that
the allocation can use.
\ ``param``\  alignment Requested alignment of the block.  If this
alignment cannot be met, the allocation fails.
This must be a power of 2.  (Note: Alignment of
CVMX_BOOTMEM_ALIGNMENT_SIZE bytes is required, and
internally enforced.  Requested alignments of less
than CVMX_BOOTMEM_ALIGNMENT_SIZE are set to
CVMX_BOOTMEM_ALIGNMENT_SIZE.)
\ ``param``\  name      name to assign to named block
\ ``param``\  flags     Flags to control options for the allocation.

\ ``return``\  physical address of block allocated, or -1 on failure

.. _`cvmx_bootmem_phy_named_block_find`:

cvmx_bootmem_phy_named_block_find
=================================

.. c:function:: struct cvmx_bootmem_named_block_desc *cvmx_bootmem_phy_named_block_find(char *name, uint32_t flags)

    Also used for finding an unused entry in the named block table.

    :param name:
        Name of memory block to find.  If NULL pointer given, then
        finds unused descriptor, if available.
    :type name: char \*

    :param flags:
        Flags to control options for the allocation.
    :type flags: uint32_t

.. _`cvmx_bootmem_phy_named_block_find.description`:

Description
-----------

Returns Pointer to memory block descriptor, NULL if not found.
If NULL returned when name parameter is NULL, then no memory
block descriptors are available.

.. _`cvmx_bootmem_phy_named_block_free`:

cvmx_bootmem_phy_named_block_free
=================================

.. c:function:: int cvmx_bootmem_phy_named_block_free(char *name, uint32_t flags)

    :param name:
        name of block to free
    :type name: char \*

    :param flags:
        flags for passing options
    :type flags: uint32_t

.. _`cvmx_bootmem_phy_named_block_free.description`:

Description
-----------

Returns 0 on failure
1 on success

.. _`__cvmx_bootmem_phy_free`:

\__cvmx_bootmem_phy_free
========================

.. c:function:: int __cvmx_bootmem_phy_free(uint64_t phy_addr, uint64_t size, uint32_t flags)

    be used with care, as the size provided must match the size of the block that was allocated, or the list will become corrupted.

    :param phy_addr:
        physical address of block
    :type phy_addr: uint64_t

    :param size:
        size of block in bytes.
    :type size: uint64_t

    :param flags:
        flags for passing options
    :type flags: uint32_t

.. _`__cvmx_bootmem_phy_free.important`:

IMPORTANT
---------

This is only intended to be used as part of named block
frees and initial population of the free memory list.
\*

.. _`__cvmx_bootmem_phy_free.description`:

Description
-----------

Returns 1 on success,
0 on failure

.. _`cvmx_bootmem_lock`:

cvmx_bootmem_lock
=================

.. c:function:: void cvmx_bootmem_lock( void)

    where multiple allocations must be made without being interrupted. This should be used with the CVMX_BOOTMEM_FLAG_NO_LOCKING flag.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_bootmem_unlock`:

cvmx_bootmem_unlock
===================

.. c:function:: void cvmx_bootmem_unlock( void)

    where multiple allocations must be made without being interrupted. This should be used with the CVMX_BOOTMEM_FLAG_NO_LOCKING flag.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

