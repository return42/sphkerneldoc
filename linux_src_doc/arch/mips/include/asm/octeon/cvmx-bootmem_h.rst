.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-bootmem.h

.. _`cvmx_bootmem_init`:

cvmx_bootmem_init
=================

.. c:function:: int cvmx_bootmem_init(void *mem_desc_ptr)

    normally called inside of \ :c:func:`cvmx_user_app_init`\ 

    :param void \*mem_desc_ptr:
        Address of the free memory list

.. _`cvmx_bootmem_alloc`:

cvmx_bootmem_alloc
==================

.. c:function:: void *cvmx_bootmem_alloc(uint64_t size, uint64_t alignment)

    to the application by the bootloader. This is an allocate-only algorithm, so freeing memory is not possible.

    :param uint64_t size:
        Size in bytes of block to allocate

    :param uint64_t alignment:
        Alignment required - must be power of 2

.. _`cvmx_bootmem_alloc.description`:

Description
-----------

Returns pointer to block of memory, NULL on error

.. _`cvmx_bootmem_alloc_address`:

cvmx_bootmem_alloc_address
==========================

.. c:function:: void *cvmx_bootmem_alloc_address(uint64_t size, uint64_t address, uint64_t alignment)

    passed to the application by the bootloader at a specific address. This is an allocate-only algorithm, so freeing memory is not possible. Allocation will fail if memory cannot be allocated at the specified address.

    :param uint64_t size:
        Size in bytes of block to allocate

    :param uint64_t address:
        Physical address to allocate memory at.  If this memory is not
        available, the allocation fails.

    :param uint64_t alignment:
        Alignment required - must be power of 2
        Returns pointer to block of memory, NULL on error

.. _`cvmx_bootmem_alloc_range`:

cvmx_bootmem_alloc_range
========================

.. c:function:: void *cvmx_bootmem_alloc_range(uint64_t size, uint64_t alignment, uint64_t min_addr, uint64_t max_addr)

    passed to the application by the bootloader within a specified address range. This is an allocate-only algorithm, so freeing memory is not possible. Allocation will fail if memory cannot be allocated in the requested range.

    :param uint64_t size:
        Size in bytes of block to allocate

    :param uint64_t alignment:
        Alignment required - must be power of 2
        Returns pointer to block of memory, NULL on error

    :param uint64_t min_addr:
        defines the minimum address of the range

    :param uint64_t max_addr:
        defines the maximum address of the range

.. _`cvmx_bootmem_alloc_named`:

cvmx_bootmem_alloc_named
========================

.. c:function:: void *cvmx_bootmem_alloc_named(uint64_t size, uint64_t alignment, char *name)

    :param uint64_t size:
        *undescribed*

    :param uint64_t alignment:
        *undescribed*

    :param char \*name:
        name of block to free

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

    :param uint64_t size:
        Size in bytes of block to allocate

    :param uint64_t address:
        Physical address to allocate memory at.  If this
        memory is not available, the allocation fails.

    :param char \*name:
        name of block - must be less than CVMX_BOOTMEM_NAME_LEN
        bytes

.. _`cvmx_bootmem_alloc_named_address.description`:

Description
-----------

Returns a pointer to block of memory, NULL on error

.. _`cvmx_bootmem_alloc_named_range`:

cvmx_bootmem_alloc_named_range
==============================

.. c:function:: void *cvmx_bootmem_alloc_named_range(uint64_t size, uint64_t min_addr, uint64_t max_addr, uint64_t align, char *name)

    that was passed to the application by the bootloader, and assign it a name in the global named block table.  (part of the cvmx_bootmem_descriptor_t structure) Named blocks can later be freed.  If request cannot be satisfied within the address range specified, NULL is returned

    :param uint64_t size:
        Size in bytes of block to allocate

    :param uint64_t min_addr:
        minimum address of range

    :param uint64_t max_addr:
        maximum address of range

    :param uint64_t align:
        Alignment of memory to be allocated. (must be a power of 2)

    :param char \*name:
        name of block - must be less than CVMX_BOOTMEM_NAME_LEN bytes

.. _`cvmx_bootmem_alloc_named_range.description`:

Description
-----------

Returns a pointer to block of memory, NULL on error

.. _`cvmx_bootmem_find_named_block`:

cvmx_bootmem_find_named_block
=============================

.. c:function:: struct cvmx_bootmem_named_block_desc *cvmx_bootmem_find_named_block(char *name)

    :param char \*name:
        name of block to free

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

    :param uint64_t req_size:
        size of region to allocate.  All requests are rounded up
        to be a multiple CVMX_BOOTMEM_ALIGNMENT_SIZE bytes size

    :param uint64_t address_min:
        Minimum address that block can occupy.

    :param uint64_t address_max:
        Specifies the maximum address_min (inclusive) that
        the allocation can use.

    :param uint64_t alignment:
        Requested alignment of the block.  If this alignment
        cannot be met, the allocation fails.  This must be a
        power of 2.  (Note: Alignment of
        CVMX_BOOTMEM_ALIGNMENT_SIZE bytes is required, and
        internally enforced.  Requested alignments of less than
        CVMX_BOOTMEM_ALIGNMENT_SIZE are set to
        CVMX_BOOTMEM_ALIGNMENT_SIZE.)

    :param uint32_t flags:
        Flags to control options for the allocation.

.. _`cvmx_bootmem_phy_alloc.description`:

Description
-----------

Returns physical address of block allocated, or -1 on failure

.. _`cvmx_bootmem_phy_named_block_alloc`:

cvmx_bootmem_phy_named_block_alloc
==================================

.. c:function:: int64_t cvmx_bootmem_phy_named_block_alloc(uint64_t size, uint64_t min_addr, uint64_t max_addr, uint64_t alignment, char *name, uint32_t flags)

    (optional) requested address and alignment.

    :param uint64_t size:
        *undescribed*

    :param uint64_t min_addr:
        *undescribed*

    :param uint64_t max_addr:
        *undescribed*

    :param uint64_t alignment:
        *undescribed*

    :param char \*name:
        *undescribed*

    :param uint32_t flags:
        *undescribed*

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

    :param char \*name:
        Name of memory block to find.  If NULL pointer given, then
        finds unused descriptor, if available.

    :param uint32_t flags:
        Flags to control options for the allocation.

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

    :param char \*name:
        name of block to free

    :param uint32_t flags:
        flags for passing options

.. _`cvmx_bootmem_phy_named_block_free.description`:

Description
-----------

Returns 0 on failure
1 on success

.. _`__cvmx_bootmem_phy_free`:

__cvmx_bootmem_phy_free
=======================

.. c:function:: int __cvmx_bootmem_phy_free(uint64_t phy_addr, uint64_t size, uint32_t flags)

    be used with care, as the size provided must match the size of the block that was allocated, or the list will become corrupted.

    :param uint64_t phy_addr:
        physical address of block

    :param uint64_t size:
        size of block in bytes.

    :param uint32_t flags:
        flags for passing options

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

    :param  void:
        no arguments

.. _`cvmx_bootmem_unlock`:

cvmx_bootmem_unlock
===================

.. c:function:: void cvmx_bootmem_unlock( void)

    where multiple allocations must be made without being interrupted. This should be used with the CVMX_BOOTMEM_FLAG_NO_LOCKING flag.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.
