.. -*- coding: utf-8; mode: rst -*-

==================
i915_gem_context.c
==================


.. _`i915_gem_create_context`:

i915_gem_create_context
=======================

.. c:function:: struct intel_context *i915_gem_create_context (struct drm_device *dev, struct drm_i915_file_private *file_priv)

    :param struct drm_device \*dev:

        *undescribed*

    :param struct drm_i915_file_private \*file_priv:

        *undescribed*



.. _`i915_gem_create_context.description`:

Description
-----------

context state of the GPU for applications that don't utilize HW contexts, as
well as an idle case.



.. _`i915_switch_context`:

i915_switch_context
===================

.. c:function:: int i915_switch_context (struct drm_i915_gem_request *req)

    perform a GPU context switch.

    :param struct drm_i915_gem_request \*req:
        request for which we'll execute the context switch



.. _`i915_switch_context.description`:

Description
-----------

The context life cycle is simple. The context refcount is incremented and
decremented by 1 and create and destroy. If the context is in use by the GPU,
it will have a refcount > 1. This allows us to destroy the context abstract
object while letting the normal object tracking destroy the backing BO.

This function should not be used in execlists mode.  Instead the context is
switched by writing to the ELSP and requests keep a reference to their
context.

