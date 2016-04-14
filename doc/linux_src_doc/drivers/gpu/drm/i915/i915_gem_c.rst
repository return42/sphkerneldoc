.. -*- coding: utf-8; mode: rst -*-

==========
i915_gem.c
==========

.. _`i915_gem_create_ioctl`:

i915_gem_create_ioctl
=====================

.. c:function:: int i915_gem_create_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_pread_ioctl`:

i915_gem_pread_ioctl
====================

.. c:function:: int i915_gem_pread_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_pread_ioctl.description`:

Description
-----------


On error, the contents of \*data are undefined.


.. _`i915_gem_gtt_pwrite_fast`:

i915_gem_gtt_pwrite_fast
========================

.. c:function:: int i915_gem_gtt_pwrite_fast (struct drm_device *dev, struct drm_i915_gem_object *obj, struct drm_i915_gem_pwrite *args, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param struct drm_i915_gem_object \*obj:

        *undescribed*

    :param struct drm_i915_gem_pwrite \*args:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_gtt_pwrite_fast.description`:

Description
-----------

user into the GTT, uncached.


.. _`i915_gem_pwrite_ioctl`:

i915_gem_pwrite_ioctl
=====================

.. c:function:: int i915_gem_pwrite_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_pwrite_ioctl.description`:

Description
-----------


On error, the contents of the buffer that were to be modified are undefined.


.. _`__i915_wait_request`:

__i915_wait_request
===================

.. c:function:: int __i915_wait_request (struct drm_i915_gem_request *req, unsigned reset_counter, bool interruptible, s64 *timeout, struct intel_rps_client *rps)

    wait until execution of request has finished

    :param struct drm_i915_gem_request \*req:
        duh!

    :param unsigned reset_counter:
        reset sequence associated with the given request

    :param bool interruptible:
        do an interruptible wait (normally yes)

    :param s64 \*timeout:
        in - how long to wait (NULL forever); out - how much time remaining

    :param struct intel_rps_client \*rps:

        *undescribed*


.. _`__i915_wait_request.description`:

Description
-----------

Note: It is of utmost importance that the passed in seqno and reset_counter
values have been read by the caller in an smp safe manner. Where read-side
locks are involved, it is sufficient to read the reset_counter before
unlocking the lock that protects the seqno. For lockless tricks, the
reset_counter _must_ be read before, and an appropriate smp_rmb must be
inserted.

Returns 0 if the request was found within the alloted time. Else returns the
errno with remaining time filled in timeout argument.


.. _`i915_wait_request`:

i915_wait_request
=================

.. c:function:: int i915_wait_request (struct drm_i915_gem_request *req)

    :param struct drm_i915_gem_request \*req:

        *undescribed*


.. _`i915_wait_request.description`:

Description
-----------

request and object lists appropriately for that event.


.. _`i915_gem_object_wait_rendering`:

i915_gem_object_wait_rendering
==============================

.. c:function:: int i915_gem_object_wait_rendering (struct drm_i915_gem_object *obj, bool readonly)

    :param struct drm_i915_gem_object \*obj:

        *undescribed*

    :param bool readonly:

        *undescribed*


.. _`i915_gem_object_wait_rendering.description`:

Description
-----------

safe to unbind from the GTT or access from the CPU.


.. _`i915_gem_set_domain_ioctl`:

i915_gem_set_domain_ioctl
=========================

.. c:function:: int i915_gem_set_domain_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_set_domain_ioctl.description`:

Description
-----------

through the mmap ioctl's mapping or a GTT mapping.


.. _`i915_gem_sw_finish_ioctl`:

i915_gem_sw_finish_ioctl
========================

.. c:function:: int i915_gem_sw_finish_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_mmap_ioctl`:

i915_gem_mmap_ioctl
===================

.. c:function:: int i915_gem_mmap_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_mmap_ioctl.description`:

Description
-----------

into.

While the mapping holds a reference on the contents of the object, it doesn't
imply a ref on the object itself.

IMPORTANT:

DRM driver writers who look a this function as an example for how to do GEM
mmap support, please don't implement mmap support like here. The modern way
to implement DRM mmap support is with an mmap offset ioctl (like
i915_gem_mmap_gtt) and then using the mmap syscall on the DRM fd directly.
That way debug tooling like valgrind will understand what's going on, hiding
the mmap call in a driver private ioctl will break that. The i915 driver only
does cpu mmaps this way because we didn't know better.


.. _`i915_gem_fault`:

i915_gem_fault
==============

.. c:function:: int i915_gem_fault (struct vm_area_struct *vma, struct vm_fault *vmf)

    fault a page into the GTT

    :param struct vm_area_struct \*vma:
        VMA in question

    :param struct vm_fault \*vmf:
        fault info


.. _`i915_gem_fault.description`:

Description
-----------

The fault handler is set up by :c:func:`drm_gem_mmap` when a object is GTT mapped
from userspace.  The fault handler takes care of binding the object to
the GTT (if needed), allocating and programming a fence register (again,
only if needed based on whether the old reg is still valid or the object
is tiled) and inserting a new PTE into the faulting process.

Note that the faulting process may involve evicting existing objects
from the GTT and/or fence registers to make room.  So performance may
suffer if the GTT working set is large or there are few fence registers
left.


.. _`i915_gem_release_mmap`:

i915_gem_release_mmap
=====================

.. c:function:: void i915_gem_release_mmap (struct drm_i915_gem_object *obj)

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
fixup by :c:func:`i915_gem_fault`.


.. _`i915_gem_get_gtt_alignment`:

i915_gem_get_gtt_alignment
==========================

.. c:function:: uint32_t i915_gem_get_gtt_alignment (struct drm_device *dev, uint32_t size, int tiling_mode, bool fenced)

    return required GTT alignment for an object

    :param struct drm_device \*dev:

        *undescribed*

    :param uint32_t size:

        *undescribed*

    :param int tiling_mode:

        *undescribed*

    :param bool fenced:

        *undescribed*


.. _`i915_gem_get_gtt_alignment.description`:

Description
-----------

Return the required GTT alignment for an object, taking into account
potential fence register mapping.


.. _`i915_gem_mmap_gtt_ioctl`:

i915_gem_mmap_gtt_ioctl
=======================

.. c:function:: int i915_gem_mmap_gtt_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

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
The mmap call will end up in :c:func:`drm_gem_mmap`, which will set things
up so we can get faults in the handler above.

The fault handler will take care of binding the object into the GTT
(since it may have been evicted to make room for something), allocating
a fence register, and mapping the appropriate aperture address into
userspace.


.. _`i915_gem_request_alloc`:

i915_gem_request_alloc
======================

.. c:function:: struct drm_i915_gem_request *i915_gem_request_alloc (struct intel_engine_cs *engine, struct intel_context *ctx)

    allocate a request structure

    :param struct intel_engine_cs \*engine:
        engine that we wish to issue the request on.

    :param struct intel_context \*ctx:
        context that the request will be associated with.::

              This can be NULL if the request is not directly related to
              any specific user context, in which case this function will
              choose an appropriate context to use.


.. _`i915_gem_request_alloc.description`:

Description
-----------

Returns a pointer to the allocated request if successful,
or an error code if not.


.. _`i915_gem_retire_requests_ring`:

i915_gem_retire_requests_ring
=============================

.. c:function:: void i915_gem_retire_requests_ring (struct intel_engine_cs *ring)

    :param struct intel_engine_cs \*ring:

        *undescribed*


.. _`i915_gem_object_flush_active`:

i915_gem_object_flush_active
============================

.. c:function:: int i915_gem_object_flush_active (struct drm_i915_gem_object *obj)

    busy by flushing any required write domains, emitting any outstanding lazy request and retiring and completed requests.

    :param struct drm_i915_gem_object \*obj:

        *undescribed*


.. _`i915_gem_wait_ioctl`:

i915_gem_wait_ioctl
===================

.. c:function:: int i915_gem_wait_ioctl (struct drm_device *dev, void *data, struct drm_file *file)

    implements DRM_IOCTL_I915_GEM_WAIT

    :param struct drm_device \*dev:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param struct drm_file \*file:

        *undescribed*


.. _`i915_gem_wait_ioctl.description`:

Description
-----------

Returns 0 if successful, else an error is returned with the remaining time in
the timeout parameter.::

 -ETIME: object is still busy after timeout
 -ERESTARTSYS: signal interrupted the wait
 -ENONENT: object doesn't exist

Also possible, but rare::

 -EAGAIN: GPU wedged
 -ENOMEM: damn
 -ENODEV: Internal IRQ fail
 -E?: The add request failed

The wait ioctl with a timeout of 0 reimplements the busy ioctl. With any
non-zero timeout parameter the wait ioctl will wait for the given number of
nanoseconds on an object becoming unbusy. Since the wait itself does so
without holding struct_mutex the object may become re-busied before this
function completes. A similar but shorter * race condition exists in the busy
ioctl


.. _`i915_gem_object_sync`:

i915_gem_object_sync
====================

.. c:function:: int i915_gem_object_sync (struct drm_i915_gem_object *obj, struct intel_engine_cs *to, struct drm_i915_gem_request **to_req)

    sync an object to a ring.

    :param struct drm_i915_gem_object \*obj:
        object which may be in use on another ring.

    :param struct intel_engine_cs \*to:
        ring we wish to use the object on. May be NULL.

    :param struct drm_i915_gem_request \*\*to_req:
        request we wish to use the object for. See below.::

                 This will be allocated and returned if a request is
                 required but not passed in.


.. _`i915_gem_object_sync.description`:

Description
-----------

This code is meant to abstract object synchronization with the GPU.
Calling with NULL implies synchronizing the object with the CPU
rather than a particular GPU ring. Conceptually we serialise writes
between engines inside the GPU. We only allow one engine to write
into a buffer at any time, but multiple readers. To ensure each has
a coherent view of memory, we must:

- If there is an outstanding write request to the object, the new
  request must wait for it to complete (either CPU or in hw, requests
  on the same ring will be naturally ordered).

- If we are a write request (pending_write_domain is set), the new
  request must wait for outstanding read requests to complete.

For CPU synchronisation (NULL to) no request is required. For syncing with
rings to_req must be non-NULL. However, a request does not have to be
pre-allocated. If \*to_req is NULL and sync commands will be emitted then a
request will be allocated automatically and returned through \*to_req. Note
that it is not guaranteed that commands will be emitted (because the system
might already be idle). Hence there is no need to create a request that
might never have any work submitted. Note further that if a request is
returned in \*to_req, it is the responsibility of the caller to submit
that request (after potentially adding more work to it).

Returns 0 if successful, else propagates up the lower layer error.


.. _`i915_gem_object_bind_to_vm`:

i915_gem_object_bind_to_vm
==========================

.. c:function:: struct i915_vma *i915_gem_object_bind_to_vm (struct drm_i915_gem_object *obj, struct i915_address_space *vm, const struct i915_ggtt_view *ggtt_view, unsigned alignment, uint64_t flags)

    :param struct drm_i915_gem_object \*obj:

        *undescribed*

    :param struct i915_address_space \*vm:

        *undescribed*

    :param const struct i915_ggtt_view \*ggtt_view:

        *undescribed*

    :param unsigned alignment:

        *undescribed*

    :param uint64_t flags:

        *undescribed*


.. _`i915_gem_object_bind_to_vm.description`:

Description
-----------

there.


.. _`i915_gem_object_set_to_gtt_domain`:

i915_gem_object_set_to_gtt_domain
=================================

.. c:function:: int i915_gem_object_set_to_gtt_domain (struct drm_i915_gem_object *obj, bool write)

    :param struct drm_i915_gem_object \*obj:

        *undescribed*

    :param bool write:

        *undescribed*


.. _`i915_gem_object_set_to_gtt_domain.description`:

Description
-----------


This function returns when the move is complete, including waiting on
flushes to occur.


.. _`i915_gem_object_set_cache_level`:

i915_gem_object_set_cache_level
===============================

.. c:function:: int i915_gem_object_set_cache_level (struct drm_i915_gem_object *obj, enum i915_cache_level cache_level)

    level of an object across all VMA.

    :param struct drm_i915_gem_object \*obj:

        *undescribed*

    :param enum i915_cache_level cache_level:

        *undescribed*


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

.. c:function:: int i915_gem_object_set_to_cpu_domain (struct drm_i915_gem_object *obj, bool write)

    :param struct drm_i915_gem_object \*obj:

        *undescribed*

    :param bool write:

        *undescribed*


.. _`i915_gem_object_set_to_cpu_domain.description`:

Description
-----------


This function returns when the move is complete, including waiting on
flushes to occur.


.. _`i915_gem_track_fb`:

i915_gem_track_fb
=================

.. c:function:: void i915_gem_track_fb (struct drm_i915_gem_object *old, struct drm_i915_gem_object *new, unsigned frontbuffer_bits)

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

This updates the frontbuffer tracking bits ``frontbuffer_bits`` by clearing them
from ``old`` and setting them in ``new``\ . Both ``old`` and ``new`` can be NULL.

