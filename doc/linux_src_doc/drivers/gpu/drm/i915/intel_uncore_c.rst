.. -*- coding: utf-8; mode: rst -*-

==============
intel_uncore.c
==============


.. _`intel_uncore_forcewake_get`:

intel_uncore_forcewake_get
==========================

.. c:function:: void intel_uncore_forcewake_get (struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    grab forcewake domain references

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to get reference on



.. _`intel_uncore_forcewake_get.description`:

Description
-----------

This function can be used get GT's forcewake domain references.
Normal register access will handle the forcewake domains automatically.
However if some sequence requires the GT to not power down a particular
forcewake domains this function should be called at the beginning of the
sequence. And subsequently the reference should be dropped by symmetric
call to :c:func:`intel_unforce_forcewake_put`. Usually caller wants all the domains
to be kept awake so the ``fw_domains`` would be then FORCEWAKE_ALL.



.. _`intel_uncore_forcewake_get__locked`:

intel_uncore_forcewake_get__locked
==================================

.. c:function:: void intel_uncore_forcewake_get__locked (struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    grab forcewake domain references

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to get reference on



.. _`intel_uncore_forcewake_get__locked.description`:

Description
-----------

See :c:func:`intel_uncore_forcewake_get`. This variant places the onus
on the caller to explicitly handle the dev_priv->uncore.lock spinlock.



.. _`intel_uncore_forcewake_put`:

intel_uncore_forcewake_put
==========================

.. c:function:: void intel_uncore_forcewake_put (struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    release a forcewake domain reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to put references



.. _`intel_uncore_forcewake_put.description`:

Description
-----------

This function drops the device-level forcewakes for specified
domains obtained by :c:func:`intel_uncore_forcewake_get`.



.. _`intel_uncore_forcewake_put__locked`:

intel_uncore_forcewake_put__locked
==================================

.. c:function:: void intel_uncore_forcewake_put__locked (struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    grab forcewake domain references

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to get reference on



.. _`intel_uncore_forcewake_put__locked.description`:

Description
-----------

See :c:func:`intel_uncore_forcewake_put`. This variant places the onus
on the caller to explicitly handle the dev_priv->uncore.lock spinlock.

