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
        struct dma_buf *dma_buf;
        struct dma_buf_attachment *import_attach;
    }

.. _`drm_gem_object.members`:

Members
-------

refcount

    Reference count of this object

    Please use \ :c:func:`drm_gem_object_get`\  to acquire and \ :c:func:`drm_gem_object_put`\ 
    or \ :c:func:`drm_gem_object_put_unlocked`\  to release a reference to a GEM
    buffer object.

handle_count

    This is the GEM file_priv handle count of this object.

    Each handle also holds a reference. Note that when the handle_count
    drops to 0 any global names (e.g. the id in the flink namespace) will
    be cleared.

    Protected by \ :c:type:`drm_device.object_name_lock <drm_device>`\ .

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
    Access is covered by \ :c:type:`drm_device.object_name_lock <drm_device>`\ . This is used by
    the GEM_FLINK and GEM_OPEN ioctls.

read_domains

    Read memory domains. These monitor which caches contain read/write data
    related to the object. When transitioning from one set of domains
    to another, the driver is called to ensure that caches are suitably
    flushed and invalidated.

write_domain
    Corresponding unique write memory domain.

dma_buf

    dma-buf associated with this GEM object.

    Pointer to the dma-buf associated with this gem object (either
    through importing or exporting). We break the resulting reference
    loop when the last gem handle for this object is released.

    Protected by \ :c:type:`drm_device.object_name_lock <drm_device>`\ .

import_attach

    dma-buf attachment backing this object.

    Any foreign dma_buf imported as a gem object has this set to the
    attachment point for the device. This is invariant over the lifetime
    of a gem object.

    The \ :c:type:`drm_driver.gem_free_object <drm_driver>`\  callback is responsible for cleaning
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

.. _`define_drm_gem_fops`:

DEFINE_DRM_GEM_FOPS
===================

.. c:function::  DEFINE_DRM_GEM_FOPS( name)

    macro to generate file operations for GEM drivers

    :param  name:
        name for the generated structure

.. _`define_drm_gem_fops.description`:

Description
-----------

This macro autogenerates a suitable \ :c:type:`struct file_operations <file_operations>`\  for GEM based
drivers, which can be assigned to \ :c:type:`drm_driver.fops <drm_driver>`\ . Note that this structure
cannot be shared between drivers, because it contains a reference to the
current module using THIS_MODULE.

Note that the declaration is already marked as static - if you need a
non-static version of this you're probably doing it wrong and will break the
THIS_MODULE reference by accident.

.. _`drm_gem_object_get`:

drm_gem_object_get
==================

.. c:function:: void drm_gem_object_get(struct drm_gem_object *obj)

    acquire a GEM buffer object reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`drm_gem_object_get.description`:

Description
-----------

This function acquires an additional reference to \ ``obj``\ . It is illegal to
call this without already holding a reference. No locks required.

.. _`__drm_gem_object_put`:

__drm_gem_object_put
====================

.. c:function:: void __drm_gem_object_put(struct drm_gem_object *obj)

    raw function to release a GEM buffer object reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`__drm_gem_object_put.description`:

Description
-----------

This function is meant to be used by drivers which are not encumbered with
\ :c:type:`drm_device.struct_mutex <drm_device>`\  legacy locking and which are using the
gem_free_object_unlocked callback. It avoids all the locking checks and
locking overhead of \ :c:func:`drm_gem_object_put`\  and \ :c:func:`drm_gem_object_put_unlocked`\ .

Drivers should never call this directly in their code. Instead they should
wrap it up into a ``driver_gem_object_put(struct driver_gem_object *obj)``
wrapper function, and use that. Shared code should never call this, to
avoid breaking drivers by accident which still depend upon
\ :c:type:`drm_device.struct_mutex <drm_device>`\  locking.

.. _`drm_gem_object_reference`:

drm_gem_object_reference
========================

.. c:function:: void drm_gem_object_reference(struct drm_gem_object *obj)

    acquire a GEM buffer object reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`drm_gem_object_reference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_gem_object_get`\  and should not be
used by new code.

.. _`__drm_gem_object_unreference`:

__drm_gem_object_unreference
============================

.. c:function:: void __drm_gem_object_unreference(struct drm_gem_object *obj)

    raw function to release a GEM buffer object reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`__drm_gem_object_unreference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`__drm_gem_object_put`\  and should not be
used by new code.

.. _`drm_gem_object_unreference_unlocked`:

drm_gem_object_unreference_unlocked
===================================

.. c:function:: void drm_gem_object_unreference_unlocked(struct drm_gem_object *obj)

    release a GEM buffer object reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`drm_gem_object_unreference_unlocked.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_gem_object_put_unlocked`\  and should
not be used by new code.

.. _`drm_gem_object_unreference`:

drm_gem_object_unreference
==========================

.. c:function:: void drm_gem_object_unreference(struct drm_gem_object *obj)

    release a GEM buffer object reference

    :param struct drm_gem_object \*obj:
        GEM buffer object

.. _`drm_gem_object_unreference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_gem_object_put`\  and should not be
used by new code.

.. This file was automatic generated / don't edit.

