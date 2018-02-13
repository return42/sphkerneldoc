.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_context.c

.. _`i915_gem_create_context`:

i915_gem_create_context
=======================

.. c:function:: struct i915_gem_context *i915_gem_create_context(struct drm_i915_private *dev_priv, struct drm_i915_file_private *file_priv)

    context state of the GPU for applications that don't utilize HW contexts, as well as an idle case.

    :param struct drm_i915_private \*dev_priv:
        *undescribed*

    :param struct drm_i915_file_private \*file_priv:
        *undescribed*

.. _`i915_gem_context_create_gvt`:

i915_gem_context_create_gvt
===========================

.. c:function:: struct i915_gem_context *i915_gem_context_create_gvt(struct drm_device *dev)

    create a GVT GEM context

    :param struct drm_device \*dev:
        drm device \*

.. _`i915_gem_context_create_gvt.description`:

Description
-----------

This function is used to create a GVT specific GEM context.

.. _`i915_gem_context_create_gvt.return`:

Return
------

pointer to i915_gem_context on success, error pointer if failed

.. This file was automatic generated / don't edit.

