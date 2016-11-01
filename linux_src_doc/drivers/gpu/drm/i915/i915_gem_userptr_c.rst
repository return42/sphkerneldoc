.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_userptr.c

.. _`i915_gem_userptr_ioctl`:

i915_gem_userptr_ioctl
======================

.. c:function:: int i915_gem_userptr_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    context - user memory.

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file:
        *undescribed*

.. _`i915_gem_userptr_ioctl.description`:

Description
-----------

We impose several restrictions upon the memory being mapped
into the GPU.
1. It must be page aligned (both start/end addresses, i.e ptr and size).
2. It must be normal system memory, not a pointer into another map of IO
space (e.g. it must not be a GTT mmapping of another object).
3. We only allow a bo as large as we could in theory map into the GTT,
that is we limit the size to the total size of the GTT.
4. The bo is marked as being snoopable. The backing pages are left
accessible directly by the CPU, but reads and writes by the GPU may
incur the cost of a snoop (unless you have an LLC architecture).

Synchronisation between multiple users and the GPU is left to userspace
through the normal set-domain-ioctl. The kernel will enforce that the
GPU relinquishes the VMA before it is returned back to the system
i.e. upon \ :c:func:`free`\ , \ :c:func:`munmap`\  or process termination. However, the userspace
\ :c:func:`malloc`\  library may not immediately relinquish the VMA after \ :c:func:`free`\  and
instead reuse it whilst the GPU is still reading and writing to the VMA.
Caveat emptor.

Also note, that the object created here is not currently a "first class"
object, in that several ioctls are banned. These are the CPU access

.. _`i915_gem_userptr_ioctl.ioctls`:

ioctls
------

mmap(), pwrite and pread. In practice, you are expected to use
direct access via your pointer rather than use those ioctls. Another
restriction is that we do not allow userptr surfaces to be pinned to the
hardware and so we reject any attempt to create a framebuffer out of a
userptr.

If you think this is a good interface to use to pass GPU memory between
drivers, please use dma-buf instead. In fact, wherever possible use
dma-buf instead.

.. This file was automatic generated / don't edit.

