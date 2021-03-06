.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/slab.h

.. _`kmalloc`:

kmalloc
=======

.. c:function:: void *kmalloc(size_t size, gfp_t flags)

    allocate memory

    :param size:
        how many bytes of memory are required.
    :type size: size_t

    :param flags:
        the type of memory to allocate.
    :type flags: gfp_t

.. _`kmalloc.description`:

Description
-----------

kmalloc is the normal method of allocating memory
for objects smaller than page size in the kernel.

The \ ``flags``\  argument may be one of:

\ ``GFP_USER``\  - Allocate memory on behalf of user.  May sleep.

\ ``GFP_KERNEL``\  - Allocate normal kernel ram.  May sleep.

\ ``GFP_ATOMIC``\  - Allocation will not sleep.  May use emergency pools.
  For example, use this inside interrupt handlers.

\ ``GFP_HIGHUSER``\  - Allocate pages from high memory.

\ ``GFP_NOIO``\  - Do not do any I/O at all while trying to get memory.

\ ``GFP_NOFS``\  - Do not make any fs calls while trying to get memory.

\ ``GFP_NOWAIT``\  - Allocation will not sleep.

\ ``__GFP_THISNODE``\  - Allocate node-local memory only.

\ ``GFP_DMA``\  - Allocation suitable for DMA.
  Should only be used for \ :c:func:`kmalloc`\  caches. Otherwise, use a
  slab created with SLAB_DMA.

Also it is possible to set different flags by OR'ing
in one or more of the following additional \ ``flags``\ :

\ ``__GFP_HIGH``\  - This allocation has high priority and may use emergency pools.

\ ``__GFP_NOFAIL``\  - Indicate that this allocation is in no way allowed to fail
  (think twice before using).

\ ``__GFP_NORETRY``\  - If memory is not immediately available,
  then give up at once.

\ ``__GFP_NOWARN``\  - If allocation fails, don't issue any warnings.

\ ``__GFP_RETRY_MAYFAIL``\  - Try really hard to succeed the allocation but fail
  eventually.

There are other flags available as well, but these are not intended
for general use, and so are not documented here. For a full list of
potential flags, always refer to linux/gfp.h.

.. _`kmalloc_array`:

kmalloc_array
=============

.. c:function:: void *kmalloc_array(size_t n, size_t size, gfp_t flags)

    allocate memory for an array.

    :param n:
        number of elements.
    :type n: size_t

    :param size:
        element size.
    :type size: size_t

    :param flags:
        the type of memory to allocate (see kmalloc).
    :type flags: gfp_t

.. _`kcalloc`:

kcalloc
=======

.. c:function:: void *kcalloc(size_t n, size_t size, gfp_t flags)

    allocate memory for an array. The memory is set to zero.

    :param n:
        number of elements.
    :type n: size_t

    :param size:
        element size.
    :type size: size_t

    :param flags:
        the type of memory to allocate (see kmalloc).
    :type flags: gfp_t

.. _`kzalloc`:

kzalloc
=======

.. c:function:: void *kzalloc(size_t size, gfp_t flags)

    allocate memory. The memory is set to zero.

    :param size:
        how many bytes of memory are required.
    :type size: size_t

    :param flags:
        the type of memory to allocate (see kmalloc).
    :type flags: gfp_t

.. _`kzalloc_node`:

kzalloc_node
============

.. c:function:: void *kzalloc_node(size_t size, gfp_t flags, int node)

    allocate zeroed memory from a particular memory node.

    :param size:
        how many bytes of memory are required.
    :type size: size_t

    :param flags:
        the type of memory to allocate (see kmalloc).
    :type flags: gfp_t

    :param node:
        memory node from which to allocate
    :type node: int

.. This file was automatic generated / don't edit.

