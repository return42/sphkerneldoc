.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem.c

.. _`i915_gem_object_wait`:

i915_gem_object_wait
====================

.. c:function:: int i915_gem_object_wait(struct drm_i915_gem_object *obj, unsigned int flags, long timeout, struct intel_rps_client *rps_client)

    :param struct drm_i915_gem_object \*obj:
        i915 gem object

    :param unsigned int flags:
        how to wait (under a lock, for all rendering or just for writes etc)

    :param long timeout:
        how long to wait

    :param struct intel_rps_client \*rps_client:
        client (user process) to charge for any waitboosting

.. _`i915_gem_create_ioctl`:

i915_gem_create_ioctl
=====================

.. c:function:: int i915_gem_create_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:
        drm device pointer

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file pointer

.. _`i915_gem_pread_ioctl`:

i915_gem_pread_ioctl
====================

.. c:function:: int i915_gem_pread_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:
        drm device pointer

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file pointer

.. _`i915_gem_pread_ioctl.description`:

Description
-----------

On error, the contents of *data are undefined.

.. _`i915_gem_gtt_pwrite_fast`:

i915_gem_gtt_pwrite_fast
========================

.. c:function:: int i915_gem_gtt_pwrite_fast(struct drm_i915_gem_object *obj, const struct drm_i915_gem_pwrite *args)

    user into the GTT, uncached.

    :param struct drm_i915_gem_object \*obj:
        i915 GEM object

    :param const struct drm_i915_gem_pwrite \*args:
        pwrite arguments structure

.. _`i915_gem_pwrite_ioctl`:

i915_gem_pwrite_ioctl
=====================

.. c:function:: int i915_gem_pwrite_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file

.. _`i915_gem_pwrite_ioctl.description`:

Description
-----------

On error, the contents of the buffer that were to be modified are undefined.

.. _`i915_gem_set_domain_ioctl`:

i915_gem_set_domain_ioctl
=========================

.. c:function:: int i915_gem_set_domain_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    through the mmap ioctl's mapping or a GTT mapping.

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file

.. _`i915_gem_sw_finish_ioctl`:

i915_gem_sw_finish_ioctl
========================

.. c:function:: int i915_gem_sw_finish_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file

.. _`i915_gem_mmap_ioctl`:

i915_gem_mmap_ioctl
===================

.. c:function:: int i915_gem_mmap_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    Maps the contents of an object, returning the address it is mapped to.

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file

.. _`i915_gem_mmap_ioctl.description`:

Description
-----------

While the mapping holds a reference on the contents of the object, it doesn't
imply a ref on the object itself.

.. _`i915_gem_mmap_ioctl.important`:

IMPORTANT
---------


DRM driver writers who look a this function as an example for how to do GEM
mmap support, please don't implement mmap support like here. The modern way
to implement DRM mmap support is with an mmap offset ioctl (like
i915_gem_mmap_gtt) and then using the mmap syscall on the DRM fd directly.
That way debug tooling like valgrind will understand what's going on, hiding
the mmap call in a driver private ioctl will break that. The i915 driver only
does cpu mmaps this way because we didn't know better.

.. _`i915_gem_mmap_gtt_version`:

i915_gem_mmap_gtt_version
=========================

.. c:function:: int i915_gem_mmap_gtt_version( void)

    report the current feature set for GTT mmaps

    :param  void:
        no arguments

.. _`i915_gem_mmap_gtt_version.a-history-of-the-gtt-mmap-interface`:

A history of the GTT mmap interface
-----------------------------------


0 - Everything had to fit into the GTT. Both parties of a memcpy had to
    aligned and suitable for fencing, and still fit into the available
    mappable space left by the pinned display objects. A classic problem
    we called the page-fault-of-doom where we would ping-pong between
    two objects that could not fit inside the GTT and so the memcpy
    would page one object in at the expense of the other between every
    single byte.

1 - Objects can be any size, and have any compatible fencing (X Y, or none
    as set via \ :c:func:`i915_gem_set_tiling`\  [DRM_I915_GEM_SET_TILING]). If the
    object is too large for the available space (or simply too large
    for the mappable aperture!), a view is created instead and faulted
    into userspace. (This view is aligned and sized appropriately for
    fenced access.)

2 - Recognise WC as a separate cache domain so that we can flush the
    delayed writes via GTT before performing direct access via WC.

.. _`i915_gem_mmap_gtt_version.restrictions`:

Restrictions
------------


 * snoopable objects cannot be accessed via the GTT. It can cause machine
   hangs on some architectures, corruption on others. An attempt to service
   a GTT page fault from a snoopable object will generate a SIGBUS.

 * the object must be able to fit into RAM (physical memory, though no
   limited to the mappable aperture).

.. _`i915_gem_mmap_gtt_version.caveats`:

Caveats
-------


 * a new GTT page fault will synchronize rendering from the GPU and flush
   all data to system memory. Subsequent access will not be synchronized.

 * all mappings are revoked on runtime device suspend.

 * there are only 8, 16 or 32 fence registers to share between all users
   (older machines require fence register for display and blitter access
   as well). Contention of the fence registers will cause the previous users
   to be unmapped and any new access will generate new page faults.

 * running out of memory while servicing a fault may generate a SIGBUS,
   rather than the expected SIGSEGV.

.. _`i915_gem_fault`:

i915_gem_fault
==============

.. c:function:: int i915_gem_fault(struct vm_fault *vmf)

    fault a page into the GTT

    :param struct vm_fault \*vmf:
        fault info

.. _`i915_gem_fault.description`:

Description
-----------

The fault handler is set up by \ :c:func:`drm_gem_mmap`\  when a object is GTT mapped
from userspace.  The fault handler takes care of binding the object to
the GTT (if needed), allocating and programming a fence register (again,
only if needed based on whether the old reg is still valid or the object
is tiled) and inserting a new PTE into the faulting process.

Note that the faulting process may involve evicting existing objects
from the GTT and/or fence registers to make room.  So performance may
suffer if the GTT working set is large or there are few fence registers
left.

The current feature set supported by \ :c:func:`i915_gem_fault`\  and thus GTT mmaps
is exposed via I915_PARAM_MMAP_GTT_VERSION (see i915_gem_mmap_gtt_version).

.. _`i915_gem_release_mmap`:

i915_gem_release_mmap
=====================

.. c:function:: void i915_gem_release_mmap(struct drm_i915_gem_object *obj)

    remove physical page mappings

    :param struct drm_i915_gem_object \*obj:
        obj in question

.. _`i915_gem_release_mmap.description`:

Description
-----------

Preserve the reservation of the mmapping with the DRM core code, but
relinquish ownership of the pages back to the system.

It is vital that we remove the page mapping if we have mapped a tiled
object through the GTT and then lose the fence register due to
resource pressure. Similarly if the object has been moved out of the
aperture, than pages mapped into userspace must be revoked. Removing the
mapping will then trigger a page fault on the next user access, allowing
fixup by \ :c:func:`i915_gem_fault`\ .

.. _`i915_gem_mmap_gtt_ioctl`:

i915_gem_mmap_gtt_ioctl
=======================

.. c:function:: int i915_gem_mmap_gtt_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    prepare an object for GTT mmap'ing

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        GTT mapping ioctl data

    :param struct drm_file \*file:
        GEM object info

.. _`i915_gem_mmap_gtt_ioctl.description`:

Description
-----------

Simply returns the fake offset to userspace so it can mmap it.
The mmap call will end up in \ :c:func:`drm_gem_mmap`\ , which will set things
up so we can get faults in the handler above.

The fault handler will take care of binding the object into the GTT
(since it may have been evicted to make room for something), allocating
a fence register, and mapping the appropriate aperture address into
userspace.

.. _`i915_gem_wait_ioctl`:

i915_gem_wait_ioctl
===================

.. c:function:: int i915_gem_wait_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    implements DRM_IOCTL_I915_GEM_WAIT

    :param struct drm_device \*dev:
        drm device pointer

    :param void \*data:
        ioctl data blob

    :param struct drm_file \*file:
        drm file pointer

.. _`i915_gem_wait_ioctl.description`:

Description
-----------

Returns 0 if successful, else an error is returned with the remaining time in
the timeout parameter.
 -ETIME: object is still busy after timeout
 -ERESTARTSYS: signal interrupted the wait
 -ENONENT: object doesn't exist
Also possible, but rare:
 -EAGAIN: incomplete, restart syscall
 -ENOMEM: damn
 -ENODEV: Internal IRQ fail
 -E?: The add request failed

The wait ioctl with a timeout of 0 reimplements the busy ioctl. With any
non-zero timeout parameter the wait ioctl will wait for the given number of
nanoseconds on an object becoming unbusy. Since the wait itself does so
without holding struct_mutex the object may become re-busied before this
function completes. A similar but shorter * race condition exists in the busy
ioctl

.. _`i915_gem_object_set_to_wc_domain`:

i915_gem_object_set_to_wc_domain
================================

.. c:function:: int i915_gem_object_set_to_wc_domain(struct drm_i915_gem_object *obj, bool write)

    :param struct drm_i915_gem_object \*obj:
        object to act on

    :param bool write:
        ask for write access or read only

.. _`i915_gem_object_set_to_wc_domain.description`:

Description
-----------

This function returns when the move is complete, including waiting on
flushes to occur.

.. _`i915_gem_object_set_to_gtt_domain`:

i915_gem_object_set_to_gtt_domain
=================================

.. c:function:: int i915_gem_object_set_to_gtt_domain(struct drm_i915_gem_object *obj, bool write)

    :param struct drm_i915_gem_object \*obj:
        object to act on

    :param bool write:
        ask for write access or read only

.. _`i915_gem_object_set_to_gtt_domain.description`:

Description
-----------

This function returns when the move is complete, including waiting on
flushes to occur.

.. _`i915_gem_object_set_cache_level`:

i915_gem_object_set_cache_level
===============================

.. c:function:: int i915_gem_object_set_cache_level(struct drm_i915_gem_object *obj, enum i915_cache_level cache_level)

    level of an object across all VMA.

    :param struct drm_i915_gem_object \*obj:
        object to act on

    :param enum i915_cache_level cache_level:
        new cache level to set for the object

.. _`i915_gem_object_set_cache_level.description`:

Description
-----------

After this function returns, the object will be in the new cache-level
across all GTT and the contents of the backing storage will be coherent,
with respect to the new cache-level. In order to keep the backing storage
coherent for all users, we only allow a single cache level to be set
globally on the object and prevent it from being changed whilst the
hardware is reading from the object. That is if the object is currently
on the scanout it will be set to uncached (or equivalent display
cache coherency) and all non-MOCS GPU access will also be uncached so
that all direct access to the scanout remains coherent.

.. _`i915_gem_object_set_to_cpu_domain`:

i915_gem_object_set_to_cpu_domain
=================================

.. c:function:: int i915_gem_object_set_to_cpu_domain(struct drm_i915_gem_object *obj, bool write)

    :param struct drm_i915_gem_object \*obj:
        object to act on

    :param bool write:
        requesting write or read-only access

.. _`i915_gem_object_set_to_cpu_domain.description`:

Description
-----------

This function returns when the move is complete, including waiting on
flushes to occur.

.. _`i915_gem_track_fb`:

i915_gem_track_fb
=================

.. c:function:: void i915_gem_track_fb(struct drm_i915_gem_object *old, struct drm_i915_gem_object *new, unsigned frontbuffer_bits)

    update frontbuffer tracking

    :param struct drm_i915_gem_object \*old:
        current GEM buffer for the frontbuffer slots

    :param struct drm_i915_gem_object \*new:
        new GEM buffer for the frontbuffer slots

    :param unsigned frontbuffer_bits:
        bitmask of frontbuffer slots

.. _`i915_gem_track_fb.description`:

Description
-----------

This updates the frontbuffer tracking bits \ ``frontbuffer_bits``\  by clearing them
from \ ``old``\  and setting them in \ ``new``\ . Both \ ``old``\  and \ ``new``\  can be NULL.

.. This file was automatic generated / don't edit.

