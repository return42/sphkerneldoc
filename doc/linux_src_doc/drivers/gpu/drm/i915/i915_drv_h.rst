.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_drv.h

.. _`intel_context`:

struct intel_context
====================

.. c:type:: struct intel_context

    as the name implies, represents a context.

.. _`intel_context.definition`:

Definition
----------

.. code-block:: c

    struct intel_context {
        struct kref ref;
        int user_handle;
        uint8_t remap_slice;
        struct drm_i915_private *i915;
        int flags;
        struct drm_i915_file_private *file_priv;
        struct i915_ctx_hang_stats hang_stats;
        struct i915_hw_ppgtt *ppgtt;
        struct engine[I915_NUM_ENGINES];
        struct list_head link;
    }

.. _`intel_context.members`:

Members
-------

ref
    reference count.

user_handle
    userspace tracking identity for this context.

remap_slice
    l3 row remapping information.

i915
    *undescribed*

flags
    context specific flags:
    CONTEXT_NO_ZEROMAP: do not allow mapping things to page 0.

file_priv
    filp associated with this context (NULL for global default
    context).

hang_stats
    information about the role of this context in possible GPU
    hangs.

ppgtt
    virtual memory space used by this context.

link
    link in the global list of contexts.

.. _`intel_context.description`:

Description
-----------

Contexts are memory images used by the hardware to store copies of their
internal state.

.. _`i915_gem_object_pin_map`:

i915_gem_object_pin_map
=======================

.. c:function:: void *i915_gem_object_pin_map(struct drm_i915_gem_object *obj)

    return a contiguous mapping of the entire object \ ``obj``\  - the object to map into kernel address space

    :param struct drm_i915_gem_object \*obj:
        *undescribed*

.. _`i915_gem_object_pin_map.description`:

Description
-----------

Calls \ :c:func:`i915_gem_object_pin_pages`\  to prevent reaping of the object's
pages and then returns a contiguous mapping of the backing storage into
the kernel address space.

The caller must hold the struct_mutex, and is responsible for calling
\ :c:func:`i915_gem_object_unpin_map`\  when the mapping is no longer required.

Returns the pointer through which to access the mapped object, or an
\ :c:func:`ERR_PTR`\  on error.

.. _`i915_gem_object_unpin_map`:

i915_gem_object_unpin_map
=========================

.. c:function:: void i915_gem_object_unpin_map(struct drm_i915_gem_object *obj)

    releases an earlier mapping \ ``obj``\  - the object to unmap

    :param struct drm_i915_gem_object \*obj:
        *undescribed*

.. _`i915_gem_object_unpin_map.description`:

Description
-----------

After pinning the object and mapping its pages, once you are finished
with your access, call \ :c:func:`i915_gem_object_unpin_map`\  to release the pin
upon the mapping. Once the pin count reaches zero, that mapping may be
removed.

The caller must hold the struct_mutex.

.. _`i915_seqno_passed`:

i915_seqno_passed
=================

.. c:function:: bool i915_seqno_passed(uint32_t seq1, uint32_t seq2)

    :param uint32_t seq1:
        *undescribed*

    :param uint32_t seq2:
        *undescribed*

.. This file was automatic generated / don't edit.

