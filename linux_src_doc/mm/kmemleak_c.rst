.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/kmemleak.c

.. _`kmemleak_alloc`:

kmemleak_alloc
==============

.. c:function:: void __ref kmemleak_alloc(const void *ptr, size_t size, int min_count, gfp_t gfp)

    register a newly allocated object

    :param ptr:
        pointer to beginning of the object
    :type ptr: const void \*

    :param size:
        size of the object
    :type size: size_t

    :param min_count:
        minimum number of references to this object. If during memory
        scanning a number of references less than \ ``min_count``\  is found,
        the object is reported as a memory leak. If \ ``min_count``\  is 0,
        the object is never reported as a leak. If \ ``min_count``\  is -1,
        the object is ignored (not scanned and not reported as a leak)
    :type min_count: int

    :param gfp:
        \ :c:func:`kmalloc`\  flags used for kmemleak internal memory allocations
    :type gfp: gfp_t

.. _`kmemleak_alloc.description`:

Description
-----------

This function is called from the kernel allocators when a new object
(memory block) is allocated (kmem_cache_alloc, kmalloc etc.).

.. _`kmemleak_alloc_percpu`:

kmemleak_alloc_percpu
=====================

.. c:function:: void __ref kmemleak_alloc_percpu(const void __percpu *ptr, size_t size, gfp_t gfp)

    register a newly allocated \__percpu object

    :param ptr:
        \__percpu pointer to beginning of the object
    :type ptr: const void __percpu \*

    :param size:
        size of the object
    :type size: size_t

    :param gfp:
        flags used for kmemleak internal memory allocations
    :type gfp: gfp_t

.. _`kmemleak_alloc_percpu.description`:

Description
-----------

This function is called from the kernel percpu allocator when a new object
(memory block) is allocated (alloc_percpu).

.. _`kmemleak_vmalloc`:

kmemleak_vmalloc
================

.. c:function:: void __ref kmemleak_vmalloc(const struct vm_struct *area, size_t size, gfp_t gfp)

    register a newly vmalloc'ed object

    :param area:
        pointer to vm_struct
    :type area: const struct vm_struct \*

    :param size:
        size of the object
    :type size: size_t

    :param gfp:
        \__vmalloc() flags used for kmemleak internal memory allocations
    :type gfp: gfp_t

.. _`kmemleak_vmalloc.description`:

Description
-----------

This function is called from the \ :c:func:`vmalloc`\  kernel allocator when a new
object (memory block) is allocated.

.. _`kmemleak_free`:

kmemleak_free
=============

.. c:function:: void __ref kmemleak_free(const void *ptr)

    unregister a previously registered object

    :param ptr:
        pointer to beginning of the object
    :type ptr: const void \*

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

    :param ptr:
        pointer to the beginning or inside the object. This also
        represents the start of the range to be freed
    :type ptr: const void \*

    :param size:
        size to be unregistered
    :type size: size_t

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

    :param ptr:
        \__percpu pointer to beginning of the object
    :type ptr: const void __percpu \*

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

    :param ptr:
        pointer to beginning of the object
    :type ptr: const void \*

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

    :param ptr:
        pointer to beginning of the object
    :type ptr: const void \*

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

    :param ptr:
        pointer to beginning of the object
    :type ptr: const void \*

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

    :param ptr:
        pointer to beginning or inside the object. This also
        represents the start of the scan area
    :type ptr: const void \*

    :param size:
        size of the scan area
    :type size: size_t

    :param gfp:
        \ :c:func:`kmalloc`\  flags used for kmemleak internal memory allocations
    :type gfp: gfp_t

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

    :param ptr:
        pointer to beginning of the object
    :type ptr: const void \*

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

    :param phys:
        physical address of the object
    :type phys: phys_addr_t

    :param size:
        size of the object
    :type size: size_t

    :param min_count:
        minimum number of references to this object.
        See \ :c:func:`kmemleak_alloc`\ 
    :type min_count: int

    :param gfp:
        \ :c:func:`kmalloc`\  flags used for kmemleak internal memory allocations
    :type gfp: gfp_t

.. _`kmemleak_free_part_phys`:

kmemleak_free_part_phys
=======================

.. c:function:: void __ref kmemleak_free_part_phys(phys_addr_t phys, size_t size)

    similar to kmemleak_free_part but taking a physical address argument

    :param phys:
        physical address if the beginning or inside an object. This
        also represents the start of the range to be freed
    :type phys: phys_addr_t

    :param size:
        size to be unregistered
    :type size: size_t

.. _`kmemleak_not_leak_phys`:

kmemleak_not_leak_phys
======================

.. c:function:: void __ref kmemleak_not_leak_phys(phys_addr_t phys)

    similar to kmemleak_not_leak but taking a physical address argument

    :param phys:
        physical address of the object
    :type phys: phys_addr_t

.. _`kmemleak_ignore_phys`:

kmemleak_ignore_phys
====================

.. c:function:: void __ref kmemleak_ignore_phys(phys_addr_t phys)

    similar to kmemleak_ignore but taking a physical address argument

    :param phys:
        physical address of the object
    :type phys: phys_addr_t

.. This file was automatic generated / don't edit.

