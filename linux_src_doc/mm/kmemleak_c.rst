.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/kmemleak.c

.. _`kmemleak_alloc`:

kmemleak_alloc
==============

.. c:function:: void __ref kmemleak_alloc(const void *ptr, size_t size, int min_count, gfp_t gfp)

    register a newly allocated object

    :param const void \*ptr:
        pointer to beginning of the object

    :param size_t size:
        size of the object

    :param int min_count:
        minimum number of references to this object. If during memory
        scanning a number of references less than \ ``min_count``\  is found,
        the object is reported as a memory leak. If \ ``min_count``\  is 0,
        the object is never reported as a leak. If \ ``min_count``\  is -1,
        the object is ignored (not scanned and not reported as a leak)

    :param gfp_t gfp:
        kmalloc() flags used for kmemleak internal memory allocations

.. _`kmemleak_alloc.description`:

Description
-----------

This function is called from the kernel allocators when a new object
(memory block) is allocated (kmem_cache_alloc, kmalloc, vmalloc etc.).

.. _`kmemleak_alloc_percpu`:

kmemleak_alloc_percpu
=====================

.. c:function:: void __ref kmemleak_alloc_percpu(const void __percpu *ptr, size_t size, gfp_t gfp)

    register a newly allocated \__percpu object

    :param const void __percpu \*ptr:
        __percpu pointer to beginning of the object

    :param size_t size:
        size of the object

    :param gfp_t gfp:
        flags used for kmemleak internal memory allocations

.. _`kmemleak_alloc_percpu.description`:

Description
-----------

This function is called from the kernel percpu allocator when a new object
(memory block) is allocated (alloc_percpu).

.. _`kmemleak_free`:

kmemleak_free
=============

.. c:function:: void __ref kmemleak_free(const void *ptr)

    unregister a previously registered object

    :param const void \*ptr:
        pointer to beginning of the object

.. _`kmemleak_free.description`:

Description
-----------

This function is called from the kernel allocators when an object (memory
block) is freed (kmem_cache_free, kfree, vfree etc.).

.. _`kmemleak_free_part`:

kmemleak_free_part
==================

.. c:function:: void __ref kmemleak_free_part(const void *ptr, size_t size)

    partially unregister a previously registered object

    :param const void \*ptr:
        pointer to the beginning or inside the object. This also
        represents the start of the range to be freed

    :param size_t size:
        size to be unregistered

.. _`kmemleak_free_part.description`:

Description
-----------

This function is called when only a part of a memory block is freed
(usually from the bootmem allocator).

.. _`kmemleak_free_percpu`:

kmemleak_free_percpu
====================

.. c:function:: void __ref kmemleak_free_percpu(const void __percpu *ptr)

    unregister a previously registered \__percpu object

    :param const void __percpu \*ptr:
        __percpu pointer to beginning of the object

.. _`kmemleak_free_percpu.description`:

Description
-----------

This function is called from the kernel percpu allocator when an object
(memory block) is freed (free_percpu).

.. _`kmemleak_update_trace`:

kmemleak_update_trace
=====================

.. c:function:: void __ref kmemleak_update_trace(const void *ptr)

    update object allocation stack trace

    :param const void \*ptr:
        pointer to beginning of the object

.. _`kmemleak_update_trace.description`:

Description
-----------

Override the object allocation stack trace for cases where the actual
allocation place is not always useful.

.. _`kmemleak_not_leak`:

kmemleak_not_leak
=================

.. c:function:: void __ref kmemleak_not_leak(const void *ptr)

    mark an allocated object as false positive

    :param const void \*ptr:
        pointer to beginning of the object

.. _`kmemleak_not_leak.description`:

Description
-----------

Calling this function on an object will cause the memory block to no longer
be reported as leak and always be scanned.

.. _`kmemleak_ignore`:

kmemleak_ignore
===============

.. c:function:: void __ref kmemleak_ignore(const void *ptr)

    ignore an allocated object

    :param const void \*ptr:
        pointer to beginning of the object

.. _`kmemleak_ignore.description`:

Description
-----------

Calling this function on an object will cause the memory block to be
ignored (not scanned and not reported as a leak). This is usually done when
it is known that the corresponding block is not a leak and does not contain
any references to other allocated memory blocks.

.. _`kmemleak_scan_area`:

kmemleak_scan_area
==================

.. c:function:: void __ref kmemleak_scan_area(const void *ptr, size_t size, gfp_t gfp)

    limit the range to be scanned in an allocated object

    :param const void \*ptr:
        pointer to beginning or inside the object. This also
        represents the start of the scan area

    :param size_t size:
        size of the scan area

    :param gfp_t gfp:
        kmalloc() flags used for kmemleak internal memory allocations

.. _`kmemleak_scan_area.description`:

Description
-----------

This function is used when it is known that only certain parts of an object
contain references to other objects. Kmemleak will only scan these areas
reducing the number false negatives.

.. _`kmemleak_no_scan`:

kmemleak_no_scan
================

.. c:function:: void __ref kmemleak_no_scan(const void *ptr)

    do not scan an allocated object

    :param const void \*ptr:
        pointer to beginning of the object

.. _`kmemleak_no_scan.description`:

Description
-----------

This function notifies kmemleak not to scan the given memory block. Useful
in situations where it is known that the given object does not contain any
references to other objects. Kmemleak will not scan such objects reducing
the number of false negatives.

.. _`kmemleak_alloc_phys`:

kmemleak_alloc_phys
===================

.. c:function:: void __ref kmemleak_alloc_phys(phys_addr_t phys, size_t size, int min_count, gfp_t gfp)

    similar to kmemleak_alloc but taking a physical address argument

    :param phys_addr_t phys:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param int min_count:
        *undescribed*

    :param gfp_t gfp:
        *undescribed*

.. _`kmemleak_free_part_phys`:

kmemleak_free_part_phys
=======================

.. c:function:: void __ref kmemleak_free_part_phys(phys_addr_t phys, size_t size)

    similar to kmemleak_free_part but taking a physical address argument

    :param phys_addr_t phys:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`kmemleak_not_leak_phys`:

kmemleak_not_leak_phys
======================

.. c:function:: void __ref kmemleak_not_leak_phys(phys_addr_t phys)

    similar to kmemleak_not_leak but taking a physical address argument

    :param phys_addr_t phys:
        *undescribed*

.. _`kmemleak_ignore_phys`:

kmemleak_ignore_phys
====================

.. c:function:: void __ref kmemleak_ignore_phys(phys_addr_t phys)

    similar to kmemleak_ignore but taking a physical address argument

    :param phys_addr_t phys:
        *undescribed*

.. This file was automatic generated / don't edit.

