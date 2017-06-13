.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_internal.c

.. _`i915_gem_object_create_internal`:

i915_gem_object_create_internal
===============================

.. c:function:: struct drm_i915_gem_object *i915_gem_object_create_internal(struct drm_i915_private *i915, phys_addr_t size)

    This object is not backed by swappable storage, and as such its contents are volatile and only valid whilst pinned. If the object is reaped by the shrinker, its pages and data will be discarded. Equally, it is not a full GEM object and so not valid for access from userspace. This makes it useful for hardware interfaces like ringbuffers (which are pinned from the time the request is written to the time the hardware stops accessing it), but not for contexts (which need to be preserved when not active for later reuse). Note that it is not cleared upon allocation.

    :param struct drm_i915_private \*i915:
        *undescribed*

    :param phys_addr_t size:
        *undescribed*

.. This file was automatic generated / don't edit.

