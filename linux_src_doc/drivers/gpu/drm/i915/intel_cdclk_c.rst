.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_cdclk.c

.. _`skl_init_cdclk`:

skl_init_cdclk
==============

.. c:function:: void skl_init_cdclk(struct drm_i915_private *dev_priv)

    Initialize CDCLK on SKL

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`skl_init_cdclk.description`:

Description
-----------

Initialize CDCLK for SKL and derivatives. This is generally
done only during the display core initialization sequence,
after which the DMC will take care of turning CDCLK off/on
as needed.

.. _`skl_uninit_cdclk`:

skl_uninit_cdclk
================

.. c:function:: void skl_uninit_cdclk(struct drm_i915_private *dev_priv)

    Uninitialize CDCLK on SKL

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`skl_uninit_cdclk.description`:

Description
-----------

Uninitialize CDCLK for SKL and derivatives. This is done only
during the display core uninitialization sequence.

.. _`bxt_init_cdclk`:

bxt_init_cdclk
==============

.. c:function:: void bxt_init_cdclk(struct drm_i915_private *dev_priv)

    Initialize CDCLK on BXT

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`bxt_init_cdclk.description`:

Description
-----------

Initialize CDCLK for BXT and derivatives. This is generally
done only during the display core initialization sequence,
after which the DMC will take care of turning CDCLK off/on
as needed.

.. _`bxt_uninit_cdclk`:

bxt_uninit_cdclk
================

.. c:function:: void bxt_uninit_cdclk(struct drm_i915_private *dev_priv)

    Uninitialize CDCLK on BXT

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`bxt_uninit_cdclk.description`:

Description
-----------

Uninitialize CDCLK for BXT and derivatives. This is done only
during the display core uninitialization sequence.

.. _`intel_cdclk_state_compare`:

intel_cdclk_state_compare
=========================

.. c:function:: bool intel_cdclk_state_compare(const struct intel_cdclk_state *a, const struct intel_cdclk_state *b)

    Determine if two CDCLK states differ

    :param const struct intel_cdclk_state \*a:
        first CDCLK state

    :param const struct intel_cdclk_state \*b:
        second CDCLK state

.. _`intel_cdclk_state_compare.return`:

Return
------

True if the CDCLK states are identical, false if they differ.

.. _`intel_set_cdclk`:

intel_set_cdclk
===============

.. c:function:: void intel_set_cdclk(struct drm_i915_private *dev_priv, const struct intel_cdclk_state *cdclk_state)

    Push the CDCLK state to the hardware

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param const struct intel_cdclk_state \*cdclk_state:
        new CDCLK state

.. _`intel_set_cdclk.description`:

Description
-----------

Program the hardware based on the passed in CDCLK state,
if necessary.

.. _`intel_update_max_cdclk`:

intel_update_max_cdclk
======================

.. c:function:: void intel_update_max_cdclk(struct drm_i915_private *dev_priv)

    Determine the maximum support CDCLK frequency

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`intel_update_max_cdclk.description`:

Description
-----------

Determine the maximum CDCLK frequency the platform supports, and also
derive the maximum dot clock frequency the maximum CDCLK frequency
allows.

.. _`intel_update_cdclk`:

intel_update_cdclk
==================

.. c:function:: void intel_update_cdclk(struct drm_i915_private *dev_priv)

    Determine the current CDCLK frequency

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`intel_update_cdclk.description`:

Description
-----------

Determine the current CDCLK frequency.

.. _`intel_update_rawclk`:

intel_update_rawclk
===================

.. c:function:: void intel_update_rawclk(struct drm_i915_private *dev_priv)

    Determine the current RAWCLK frequency

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`intel_update_rawclk.description`:

Description
-----------

Determine the current RAWCLK frequency. RAWCLK is a fixed
frequency clock so this needs to done only once.

.. _`intel_init_cdclk_hooks`:

intel_init_cdclk_hooks
======================

.. c:function:: void intel_init_cdclk_hooks(struct drm_i915_private *dev_priv)

    Initialize CDCLK related modesetting hooks

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. This file was automatic generated / don't edit.

