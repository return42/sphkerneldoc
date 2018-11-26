.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/uverbs_ioctl.c

.. _`_uverbs_alloc`:

\_uverbs_alloc
==============

.. c:function:: __malloc void *_uverbs_alloc(struct uverbs_attr_bundle *bundle, size_t size, gfp_t flags)

    Quickly allocate memory for use with a bundle

    :param bundle:
        The bundle
    :type bundle: struct uverbs_attr_bundle \*

    :param size:
        Number of bytes to allocate
    :type size: size_t

    :param flags:
        Allocator flags
    :type flags: gfp_t

.. _`_uverbs_alloc.description`:

Description
-----------

The bundle allocator is intended for allocations that are connected with
processing the system call related to the bundle. The allocated memory is
always freed once the system call completes, and cannot be freed any other
way.

This tries to use a small pool of pre-allocated memory for performance.

.. This file was automatic generated / don't edit.

