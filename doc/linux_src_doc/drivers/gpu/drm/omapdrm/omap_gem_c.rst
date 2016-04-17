.. -*- coding: utf-8; mode: rst -*-

==========
omap_gem.c
==========


.. _`omap_gem_fault`:

omap_gem_fault
==============

.. c:function:: int omap_gem_fault (struct vm_area_struct *vma, struct vm_fault *vmf)

    pagefault handler for GEM objects

    :param struct vm_area_struct \*vma:
        the VMA of the GEM object

    :param struct vm_fault \*vmf:
        fault detail



.. _`omap_gem_fault.description`:

Description
-----------

Invoked when a fault occurs on an mmap of a GEM managed area. GEM
does most of the work for us including the actual map/unmap calls
but we need to do the actual page work.

The VMA was set up by GEM. In doing so it also ensured that the
vma->vm_private_data points to the GEM object that is backing this
mapping.



.. _`omap_gem_dumb_create`:

omap_gem_dumb_create
====================

.. c:function:: int omap_gem_dumb_create (struct drm_file *file, struct drm_device *dev, struct drm_mode_create_dumb *args)

    create a dumb buffer

    :param struct drm_file \*file:

        *undescribed*

    :param struct drm_device \*dev:
        our device

    :param struct drm_mode_create_dumb \*args:
        the requested arguments copied from userspace



.. _`omap_gem_dumb_create.description`:

Description
-----------

Allocate a buffer suitable for use for a frame buffer of the
form described by user space. Give userspace a handle by which
to reference it.



.. _`omap_gem_dumb_map_offset`:

omap_gem_dumb_map_offset
========================

.. c:function:: int omap_gem_dumb_map_offset (struct drm_file *file, struct drm_device *dev, uint32_t handle, uint64_t *offset)

    buffer mapping for dumb interface

    :param struct drm_file \*file:
        our drm client file

    :param struct drm_device \*dev:
        drm device

    :param uint32_t handle:
        GEM handle to the object (from dumb_create)

    :param uint64_t \*offset:

        *undescribed*



.. _`omap_gem_dumb_map_offset.description`:

Description
-----------

Do the necessary setup to allow the mapping of the frame buffer
into user memory. We don't have to do much here at the moment.



.. _`is_cached_coherent`:

is_cached_coherent
==================

.. c:function:: bool is_cached_coherent (struct drm_gem_object *obj)

    :param struct drm_gem_object \*obj:

        *undescribed*



.. _`is_cached_coherent.description`:

Description
-----------

page faulting to keep track of dirty pages

