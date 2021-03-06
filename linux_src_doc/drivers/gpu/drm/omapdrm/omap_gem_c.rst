.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/omap_gem.c

.. _`omap_gem_fault`:

omap_gem_fault
==============

.. c:function:: vm_fault_t omap_gem_fault(struct vm_fault *vmf)

    pagefault handler for GEM objects

    :param vmf:
        fault detail
    :type vmf: struct vm_fault \*

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

.. c:function:: int omap_gem_dumb_create(struct drm_file *file, struct drm_device *dev, struct drm_mode_create_dumb *args)

    create a dumb buffer

    :param file:
        *undescribed*
    :type file: struct drm_file \*

    :param dev:
        our device
    :type dev: struct drm_device \*

    :param args:
        the requested arguments copied from userspace
    :type args: struct drm_mode_create_dumb \*

.. _`omap_gem_dumb_create.description`:

Description
-----------

Allocate a buffer suitable for use for a frame buffer of the
form described by user space. Give userspace a handle by which
to reference it.

.. _`omap_gem_dumb_map_offset`:

omap_gem_dumb_map_offset
========================

.. c:function:: int omap_gem_dumb_map_offset(struct drm_file *file, struct drm_device *dev, u32 handle, u64 *offset)

    buffer mapping for dumb interface

    :param file:
        our drm client file
    :type file: struct drm_file \*

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param handle:
        GEM handle to the object (from dumb_create)
    :type handle: u32

    :param offset:
        *undescribed*
    :type offset: u64 \*

.. _`omap_gem_dumb_map_offset.description`:

Description
-----------

Do the necessary setup to allow the mapping of the frame buffer
into user memory. We don't have to do much here at the moment.

.. _`omap_gem_pin`:

omap_gem_pin
============

.. c:function:: int omap_gem_pin(struct drm_gem_object *obj, dma_addr_t *dma_addr)

    Pin a GEM object in memory

    :param obj:
        the GEM object
    :type obj: struct drm_gem_object \*

    :param dma_addr:
        the DMA address
    :type dma_addr: dma_addr_t \*

.. _`omap_gem_pin.description`:

Description
-----------

Pin the given GEM object in memory and fill the dma_addr pointer with the
object's DMA address. If the buffer is not physically contiguous it will be
remapped through the TILER to provide a contiguous view.

Pins are reference-counted, calling this function multiple times is allowed
as long the corresponding \ :c:func:`omap_gem_unpin`\  calls are balanced.

Return 0 on success or a negative error code otherwise.

.. _`omap_gem_unpin`:

omap_gem_unpin
==============

.. c:function:: void omap_gem_unpin(struct drm_gem_object *obj)

    Unpin a GEM object from memory

    :param obj:
        the GEM object
    :type obj: struct drm_gem_object \*

.. _`omap_gem_unpin.description`:

Description
-----------

Unpin the given GEM object previously pinned with \ :c:func:`omap_gem_pin`\ . Pins are
reference-counted, the actualy unpin will only be performed when the number
of calls to this function matches the number of calls to \ :c:func:`omap_gem_pin`\ .

.. This file was automatic generated / don't edit.

