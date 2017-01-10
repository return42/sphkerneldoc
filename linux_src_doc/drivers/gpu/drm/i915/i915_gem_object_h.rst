.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_object.h

.. _`i915_gem_object_lookup_rcu`:

i915_gem_object_lookup_rcu
==========================

.. c:function:: struct drm_i915_gem_object *i915_gem_object_lookup_rcu(struct drm_file *file, u32 handle)

    look up a temporary GEM object from its handle

    :param struct drm_file \*file:
        *undescribed*

    :param u32 handle:
        userspace handle

.. _`i915_gem_object_lookup_rcu.return`:

Return
------


A pointer to the object named by the handle if such exists on \ ``filp``\ , NULL
otherwise. This object is only valid whilst under the RCU read lock, and
note carefully the object may be in the process of being destroyed.

.. This file was automatic generated / don't edit.

