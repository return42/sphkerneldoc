.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_cdclk.c

.. _`cdclk---rawclk`:

CDCLK / RAWCLK
==============

The display engine uses several different clocks to do its work. There
are two main clocks involved that aren't directly related to the actual
pixel clock or any symbol/bit clock of the actual output port. These
are the core display clock (CDCLK) and RAWCLK.

CDCLK clocks most of the display pipe logic, and thus its frequency
must be high enough to support the rate at which pixels are flowing
through the pipes. Downscaling must also be accounted as that increases
the effective pixel rate.

On several platforms the CDCLK frequency can be changed dynamically
to minimize power consumption for a given display configuration.
Typically changes to the CDCLK frequency require all the display pipes
to be shut down while the frequency is being changed.

On SKL+ the DMC will toggle the CDCLK off/on during DC5/6 entry/exit.
DMC will not change the active CDCLK frequency however, so that part
will still be performed by the driver directly.

RAWCLK is a fixed frequency clock, often used by various auxiliary
blocks such as AUX CH or backlight PWM. Hence the only thing we
really need to know about RAWCLK is its frequency so that various
dividers can be programmed correctly.

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

.. _`cnl_init_cdclk`:

cnl_init_cdclk
==============

.. c:function:: void cnl_init_cdclk(struct drm_i915_private *dev_priv)

    Initialize CDCLK on CNL

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`cnl_init_cdclk.description`:

Description
-----------

Initialize CDCLK for CNL. This is generally
done only during the display core initialization sequence,
after which the DMC will take care of turning CDCLK off/on
as needed.

.. _`cnl_uninit_cdclk`:

cnl_uninit_cdclk
================

.. c:function:: void cnl_uninit_cdclk(struct drm_i915_private *dev_priv)

    Uninitialize CDCLK on CNL

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`cnl_uninit_cdclk.description`:

Description
-----------

Uninitialize CDCLK for CNL. This is done only
during the display core uninitialization sequence.

.. _`intel_cdclk_needs_modeset`:

intel_cdclk_needs_modeset
=========================

.. c:function:: bool intel_cdclk_needs_modeset(const struct intel_cdclk_state *a, const struct intel_cdclk_state *b)

    Determine if two CDCLK states require a modeset on all pipes

    :param const struct intel_cdclk_state \*a:
        first CDCLK state

    :param const struct intel_cdclk_state \*b:
        second CDCLK state

.. _`intel_cdclk_needs_modeset.return`:

Return
------

True if the CDCLK states require pipes to be off during reprogramming, false if not.

.. _`intel_cdclk_changed`:

intel_cdclk_changed
===================

.. c:function:: bool intel_cdclk_changed(const struct intel_cdclk_state *a, const struct intel_cdclk_state *b)

    Determine if two CDCLK states are different

    :param const struct intel_cdclk_state \*a:
        first CDCLK state

    :param const struct intel_cdclk_state \*b:
        second CDCLK state

.. _`intel_cdclk_changed.return`:

Return
------

True if the CDCLK states don't match, false if they do.

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

