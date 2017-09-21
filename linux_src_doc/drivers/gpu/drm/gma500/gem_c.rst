.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/gem.c

.. _`psb_gem_create`:

psb_gem_create
==============

.. c:function:: int psb_gem_create(struct drm_file *file, struct drm_device *dev, u64 size, u32 *handlep, int stolen, u32 align)

    create a mappable object

    :param struct drm_file \*file:
        the DRM file of the client

    :param struct drm_device \*dev:
        our device

    :param u64 size:
        the size requested

    :param u32 \*handlep:
        returned handle (opaque number)

    :param int stolen:
        *undescribed*

    :param u32 align:
        *undescribed*

.. _`psb_gem_create.description`:

Description
-----------

Create a GEM object, fill in the boilerplate and attach a handle to
it so that userspace can speak about it. This does the core work
for the various methods that do/will create GEM objects for things

.. _`psb_gem_dumb_create`:

psb_gem_dumb_create
===================

.. c:function:: int psb_gem_dumb_create(struct drm_file *file, struct drm_device *dev, struct drm_mode_create_dumb *args)

    create a dumb buffer

    :param struct drm_file \*file:
        *undescribed*

    :param struct drm_device \*dev:
        our device

    :param struct drm_mode_create_dumb \*args:
        the requested arguments copied from userspace

.. _`psb_gem_dumb_create.description`:

Description
-----------

Allocate a buffer suitable for use for a frame buffer of the
form described by user space. Give userspace a handle by which
to reference it.

.. _`psb_gem_fault`:

psb_gem_fault
=============

.. c:function:: int psb_gem_fault(struct vm_fault *vmf)

    pagefault handler for GEM objects

    :param struct vm_fault \*vmf:
        fault detail

.. _`psb_gem_fault.description`:

Description
-----------

Invoked when a fault occurs on an mmap of a GEM managed area. GEM
does most of the work for us including the actual map/unmap calls
but we need to do the actual page work.

This code eventually needs to handle faulting objects in and out
of the GTT and repacking it when we run out of space. We can put
that off for now and for our simple uses

The VMA was set up by GEM. In doing so it also ensured that the
vma->vm_private_data points to the GEM object that is backing this
mapping.

.. This file was automatic generated / don't edit.

