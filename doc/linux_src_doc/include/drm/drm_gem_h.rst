.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_gem.h

.. _`drm_gem_object`:

struct drm_gem_object
=====================

.. c:type:: struct drm_gem_object

    GEM buffer object

.. _`drm_gem_object.definition`:

Definition
----------

.. code-block:: c

    struct drm_gem_object {
        struct kref refcount;
        unsigned handle_count;
        struct drm_device *dev;
        struct file *filp;
        struct drm_vma_offset_node vma_node;
        size_t size;
        int name;
        uint32_t read_domains;
        uint32_t write_domain;
        uint32_t pending_read_domains;
        uint32_t pending_write_domain;
        struct dma_buf *dma_buf;
        struct dma_buf_attachment *import_attach;
    }

.. _`drm_gem_object.members`:

Members
-------

refcount

    Reference count of this object

    Please use \ :c:func:`drm_gem_object_reference`\  to acquire and
    \ :c:func:`drm_gem_object_unreference`\  or \ :c:func:`drm_gem_object_unreference_unlocked`\ 
    to release a reference to a GEM buffer object.

handle_count

    This is the GEM file_priv handle count of this object.

    Each handle also holds a reference. Note that when the handle_count
    drops to 0 any global names (e.g. the id in the flink namespace) will
    be cleared.

    Protected by dev->object_name_lock.

dev
    DRM dev this object belongs to.

filp

    SHMEM file node used as backing storage for swappable buffer objects.
    GEM also supports driver private objects with driver-specific backing
    storage (contiguous CMA memory, special reserved blocks). In this
    case \ ``filp``\  is NULL.

vma_node

    Mapping info for this object to support mmap. Drivers are supposed to
    allocate the mmap offset using \ :c:func:`drm_gem_create_mmap_offset`\ . The
    offset itself can be retrieved using \ :c:func:`drm_vma_node_offset_addr`\ .

    Memory mapping itself is handled by \ :c:func:`drm_gem_mmap`\ , which also checks
    that userspace is allowed to access the object.

size

    Size of the object, in bytes.  Immutable over the object's
    lifetime.

name

    Global name for this object, starts at 1. 0 means unnamed.
    Access is covered by dev->object_name_lock. This is used by the GEM_FLINK
    and GEM_OPEN ioctls.

read_domains

    Read memory domains. These monitor which caches contain read/write data
    related to the object. When transitioning from one set of domains
    to another, the driver is called to ensure that caches are suitably
    flushed and invalidated.

write_domain
    Corresponding unique write memory domain.

pending_read_domains

    While validating an exec operation, the
    new read/write domain values are computed here.
    They will be transferred to the above values
    at the point that any cache flushing occurs

pending_write_domain
    Write domain similar to \ ``pending_read_domains``\ .

dma_buf

    dma-buf associated with this GEM object.

    Pointer to the dma-buf associated with this gem object (either
    through importing or exporting). We break the resulting reference
    loop when the last gem handle for this object is released.

    Protected by obj->object_name_lock.

import_attach

    dma-buf attachment backing this object.

    Any foreign dma_buf imported as a gem object has this set to the
    attachment point for the device. This is invariant over the lifetime
    of a gem object.

    The driver's ->gem_free_object callback is responsible for cleaning
    up the dma_buf attachment and references acquired at import time.

    Note that the drm gem/prime core does not depend upon drivers setting
    this field any more. So for drivers where this doesn't make sense
    (e.g. virtual devices or a displaylink behind an usb bus) they can
    simply leave it as NULL.

.. _`drm_gem_object.description`:

Description
-----------

This structure defines the generic parts for GEM buffer objects, which are
mostly around handling mmap and userspace handles.

Buffer objects are often abbreviated to BO.

.. _`drm_gem_object_reference`:

drm_gem_object_reference
========================

.. c:function:: void drm_gem_object_reference(struct drm_gem_object *obj)

    acquire a GEM BO reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`drm_gem_object_reference.description`:

Description
-----------

This acquires additional reference to \ ``obj``\ . It is illegal to call this
without already holding a reference. No locks required.

.. _`__drm_gem_object_unreference`:

__drm_gem_object_unreference
============================

.. c:function:: void __drm_gem_object_unreference(struct drm_gem_object *obj)

    raw function to release a GEM BO reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`__drm_gem_object_unreference.description`:

Description
-----------

This function is meant to be used by drivers which are not encumbered with
dev->struct_mutex legacy locking and which are using the
gem_free_object_unlocked callback. It avoids all the locking checks and
locking overhead of \ :c:func:`drm_gem_object_unreference`\  and
\ :c:func:`drm_gem_object_unreference_unlocked`\ .

Drivers should never call this directly in their code. Instead they should
wrap it up into a driver_gem_object_unreference(struct driver_gem_object
\*obj) wrapper function, and use that. Shared code should never call this, to
avoid breaking drivers by accident which still depend upon dev->struct_mutex
locking.

.. This file was automatic generated / don't edit.

