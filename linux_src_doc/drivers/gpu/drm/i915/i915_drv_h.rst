.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_drv.h

.. _`i915_perf_stream_ops`:

struct i915_perf_stream_ops
===========================

.. c:type:: struct i915_perf_stream_ops

    the OPs to support a specific stream type

.. _`i915_perf_stream_ops.definition`:

Definition
----------

.. code-block:: c

    struct i915_perf_stream_ops {
        void (*enable)(struct i915_perf_stream *stream);
        void (*disable)(struct i915_perf_stream *stream);
        void (*poll_wait)(struct i915_perf_stream *stream,struct file *file,poll_table *wait);
        int (*wait_unlocked)(struct i915_perf_stream *stream);
        int (*read)(struct i915_perf_stream *stream,char __user *buf,size_t count,size_t *offset);
        void (*destroy)(struct i915_perf_stream *stream);
    }

.. _`i915_perf_stream_ops.members`:

Members
-------

enable
    Enables the collection of HW samples, either in response to`I915_PERF_IOCTL_ENABLE` or implicitly called when stream is opened
    without `I915_PERF_FLAG_DISABLED`.

disable
    Disables the collection of HW samples, either in responseto `I915_PERF_IOCTL_DISABLE` or implicitly called before destroying
    the stream.

poll_wait
    Call poll_wait, passing a wait queue that will be wokenonce there is something ready to \ :c:func:`read`\  for the stream

wait_unlocked
    For handling a blocking read, wait until there issomething to ready to \ :c:func:`read`\  for the stream. E.g. wait on the same
    wait queue that would be passed to \ :c:func:`poll_wait`\ .

read
    Copy buffered metrics as records to userspace**buf**: the userspace, destination buffer
    **count**: the number of bytes to copy, requested by userspace
    **offset**: zero at the start of the read, updated as the read
    proceeds, it represents how many bytes have been copied so far and
    the buffer offset for copying the next record.

    Copy as many buffered i915 perf samples and records for this stream
    to userspace as will fit in the given buffer.

    Only write complete records; returning -%ENOSPC if there isn't room
    for a complete record.

    Return any error condition that results in a short read such as
    -%ENOSPC or -%EFAULT, even though these may be squashed before
    returning to userspace.

destroy
    Cleanup any stream specific resources.
    The stream will always be disabled before this is called.

.. _`i915_perf_stream`:

struct i915_perf_stream
=======================

.. c:type:: struct i915_perf_stream

    state for a single open stream FD

.. _`i915_perf_stream.definition`:

Definition
----------

.. code-block:: c

    struct i915_perf_stream {
        struct drm_i915_private *dev_priv;
        struct list_head link;
        u32 sample_flags;
        int sample_size;
        struct i915_gem_context *ctx;
        bool enabled;
        const struct i915_perf_stream_ops *ops;
    }

.. _`i915_perf_stream.members`:

Members
-------

dev_priv
    i915 drm device

link
    Links the stream into ``&drm_i915_private->streams``

sample_flags
    Flags representing the `DRM_I915_PERF_PROP_SAMPLE_*`properties given when opening a stream, representing the contents
    of a single sample as \ :c:func:`read`\  by userspace.

sample_size
    Considering the configured contents of a samplecombined with the required header size, this is the total size
    of a single sample record.

ctx
    %NULL if measuring system-wide across all contexts or aspecific context that is being monitored.

enabled
    Whether the stream is currently enabled, consideringwhether the stream was opened in a disabled state and based
    on `I915_PERF_IOCTL_ENABLE` and `I915_PERF_IOCTL_DISABLE` calls.

ops
    The callbacks providing the implementation of this specifictype of configured stream.

.. _`i915_oa_ops`:

struct i915_oa_ops
==================

.. c:type:: struct i915_oa_ops

    Gen specific implementation of an OA unit stream

.. _`i915_oa_ops.definition`:

Definition
----------

.. code-block:: c

    struct i915_oa_ops {
        void (*init_oa_buffer)(struct drm_i915_private *dev_priv);
        int (*enable_metric_set)(struct drm_i915_private *dev_priv);
        void (*disable_metric_set)(struct drm_i915_private *dev_priv);
        void (*oa_enable)(struct drm_i915_private *dev_priv);
        void (*oa_disable)(struct drm_i915_private *dev_priv);
        int (*read)(struct i915_perf_stream *stream,char __user *buf,size_t count,size_t *offset);
        bool (*oa_buffer_is_empty)(struct drm_i915_private *dev_priv);
    }

.. _`i915_oa_ops.members`:

Members
-------

init_oa_buffer
    Resets the head and tail pointers of thecircular buffer for periodic OA reports.

    Called when first opening a stream for OA metrics, but also may be
    called in response to an OA buffer overflow or other error
    condition.

    Note it may be necessary to clear the full OA buffer here as part of
    maintaining the invariable that new reports must be written to
    zeroed memory for us to be able to reliable detect if an expected
    report has not yet landed in memory.  (At least on Haswell the OA
    buffer tail pointer is not synchronized with reports being visible
    to the CPU)

enable_metric_set
    Applies any MUX configuration to set up theBoolean and Custom (B/C) counters that are part of the counter
    reports being sampled. May apply system constraints such as
    disabling EU clock gating as required.

disable_metric_set
    Remove system constraints associated with usingthe OA unit.

oa_enable
    Enable periodic sampling

oa_disable
    Disable periodic sampling

read
    Copy data from the circular OA buffer into a given userspacebuffer.

oa_buffer_is_empty
    Check if OA buffer empty (false positives OK)
    This is either called via fops or the poll check hrtimer (atomic
    ctx) without any locks taken.

    It's safe to read OA config state here unlocked, assuming that this
    is only called while the stream is enabled, while the global OA
    configuration can't be modified.

    Efficiency is more important than avoiding some false positives
    here, which will be handled gracefully - likely resulting in an
    \ ``EAGAIN``\  error for userspace.

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

    return a contiguous mapping of the entire object

    :param struct drm_i915_gem_object \*obj:
        the object to map into kernel address space

    :param enum i915_map_type type:
        the type of mapping, used to select pgprot_t

.. _`i915_gem_object_pin_map.description`:

Description
-----------

Calls \ :c:func:`i915_gem_object_pin_pages`\  to prevent reaping of the object's
pages and then returns a contiguous mapping of the backing storage into
the kernel address space. Based on the \ ``type``\  of mapping, the PTE will be
set to either WriteBack or WriteCombine (via pgprot_t).

The caller is responsible for calling \ :c:func:`i915_gem_object_unpin_map`\  when the
mapping is no longer required.

Returns the pointer through which to access the mapped object, or an
\ :c:func:`ERR_PTR`\  on error.

.. _`i915_gem_object_unpin_map`:

i915_gem_object_unpin_map
=========================

.. c:function:: void i915_gem_object_unpin_map(struct drm_i915_gem_object *obj)

    releases an earlier mapping

    :param struct drm_i915_gem_object \*obj:
        the object to unmap

.. _`i915_gem_object_unpin_map.description`:

Description
-----------

After pinning the object and mapping its pages, once you are finished
with your access, call \ :c:func:`i915_gem_object_unpin_map`\  to release the pin
upon the mapping. Once the pin count reaches zero, that mapping may be
removed.

.. This file was automatic generated / don't edit.

