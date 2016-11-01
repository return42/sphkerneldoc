.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_drv.h

.. _`i915_gem_context`:

struct i915_gem_context
=======================

.. c:type:: struct i915_gem_context

    as the name implies, represents a context.

.. _`i915_gem_context.definition`:

Definition
----------

.. code-block:: c

    struct i915_gem_context {
        struct kref ref;
        struct drm_i915_private *i915;
        struct drm_i915_file_private *file_priv;
        struct i915_hw_ppgtt *ppgtt;
        struct pid *pid;
        struct i915_ctx_hang_stats hang_stats;
        unsigned long flags;
    #define CONTEXT_NO_ZEROMAP BIT(0)
    #define CONTEXT_NO_ERROR_CAPTURE BIT(1)
        unsigned int hw_id;
        u32 user_handle;
        u32 ggtt_alignment;
        struct intel_context engine[I915_NUM_ENGINES];
        u32 ring_size;
        u32 desc_template;
        struct atomic_notifier_head status_notifier;
        bool execlists_force_single_submission;
        struct list_head link;
        u8 remap_slice;
        bool closed:1;
    }

.. _`i915_gem_context.members`:

Members
-------

ref
    reference count.

i915
    *undescribed*

file_priv
    filp associated with this context (NULL for global default
    context).

ppgtt
    virtual memory space used by this context.

pid
    *undescribed*

hang_stats
    information about the role of this context in possible GPU
    hangs.

flags
    context specific flags:
    CONTEXT_NO_ZEROMAP: do not allow mapping things to page 0.

hw_id
    *undescribed*

user_handle
    userspace tracking identity for this context.

ggtt_alignment
    *undescribed*

ring_size
    *undescribed*

desc_template
    *undescribed*

status_notifier
    *undescribed*

execlists_force_single_submission
    *undescribed*

link
    link in the global list of contexts.

remap_slice
    l3 row remapping information.

closed
    *undescribed*

.. _`i915_gem_context.description`:

Description
-----------

Contexts are memory images used by the hardware to store copies of their
internal state.

.. _`__sg_next`:

__sg_next
=========

.. c:function:: struct scatterlist *__sg_next(struct scatterlist *sg)

    return the next scatterlist entry in a list

    :param struct scatterlist \*sg:
        The current sg entry

.. _`__sg_next.description`:

Description
-----------

If the entry is the last, return NULL; otherwise, step to the next
element in the array (@sg@+1). If that's a chain pointer, follow it;
otherwise just return the pointer to the current element.

.. _`for_each_sgt_dma`:

for_each_sgt_dma
================

.. c:function::  for_each_sgt_dma( __dmap,  __iter,  __sgt)

    iterate over the DMA addresses of the given sg_table

    :param  __dmap:
        DMA address (output)

    :param  __iter:
        'struct sgt_iter' (iterator state, internal)

    :param  __sgt:
        sg_table to iterate over (input)

.. _`for_each_sgt_page`:

for_each_sgt_page
=================

.. c:function::  for_each_sgt_page( __pp,  __iter,  __sgt)

    iterate over the pages of the given sg_table

    :param  __pp:
        page pointer (output)

    :param  __iter:
        'struct sgt_iter' (iterator state, internal)

    :param  __sgt:
        sg_table to iterate over (input)

.. _`i915_gem_object_pin_map`:

i915_gem_object_pin_map
=======================

.. c:function:: void *i915_gem_object_pin_map(struct drm_i915_gem_object *obj, enum i915_map_type type)

    return a contiguous mapping of the entire object \ ``obj``\  - the object to map into kernel address space \ ``type``\  - the type of mapping, used to select pgprot_t

    :param struct drm_i915_gem_object \*obj:
        *undescribed*

    :param enum i915_map_type type:
        *undescribed*

.. _`i915_gem_object_pin_map.description`:

Description
-----------

Calls \ :c:func:`i915_gem_object_pin_pages`\  to prevent reaping of the object's
pages and then returns a contiguous mapping of the backing storage into
the kernel address space. Based on the \ ``type``\  of mapping, the PTE will be
set to either WriteBack or WriteCombine (via pgprot_t).

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

.. _`i915_vma_pin_fence`:

i915_vma_pin_fence
==================

.. c:function:: bool i915_vma_pin_fence(struct i915_vma *vma)

    pin fencing state

    :param struct i915_vma \*vma:
        vma to pin fencing for

.. _`i915_vma_pin_fence.description`:

Description
-----------

This pins the fencing state (whether tiled or untiled) to make sure the
vma (and its object) is ready to be used as a scanout target. Fencing
status must be synchronize first by calling \ :c:func:`i915_vma_get_fence`\ :

The resulting fence pin reference must be released again with
\ :c:func:`i915_vma_unpin_fence`\ .

.. _`i915_vma_pin_fence.return`:

Return
------


True if the vma has a fence, false otherwise.

.. _`i915_vma_unpin_fence`:

i915_vma_unpin_fence
====================

.. c:function:: void i915_vma_unpin_fence(struct i915_vma *vma)

    unpin fencing state

    :param struct i915_vma \*vma:
        vma to unpin fencing for

.. _`i915_vma_unpin_fence.description`:

Description
-----------

This releases the fence pin reference acquired through
i915_vma_pin_fence. It will handle both objects with and without an
attached fence correctly, callers do not need to distinguish this.

.. This file was automatic generated / don't edit.

