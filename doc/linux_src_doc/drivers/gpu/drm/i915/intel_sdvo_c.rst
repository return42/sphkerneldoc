.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_sdvo.c

.. _`intel_sdvo_write_sdvox`:

intel_sdvo_write_sdvox
======================

.. c:function:: void intel_sdvo_write_sdvox(struct intel_sdvo *intel_sdvo, u32 val)

    SDVOB and SDVOC to work around apparent hardware issues (according to comments in the BIOS).

    :param struct intel_sdvo \*intel_sdvo:
        *undescribed*

    :param u32 val:
        *undescribed*

.. _`intel_sdvo_get_trained_inputs`:

intel_sdvo_get_trained_inputs
=============================

.. c:function:: bool intel_sdvo_get_trained_inputs(struct intel_sdvo *intel_sdvo, bool *input_1, bool *input_2)

    :param struct intel_sdvo \*intel_sdvo:
        *undescribed*

    :param bool \*input_1:
        *undescribed*

    :param bool \*input_2:
        *undescribed*

.. _`intel_sdvo_get_trained_inputs.description`:

Description
-----------

This function is making an assumption about the layout of the response,
which should be checked against the docs.

.. _`intel_sdvo_select_ddc_bus`:

intel_sdvo_select_ddc_bus
=========================

.. c:function:: void intel_sdvo_select_ddc_bus(struct drm_i915_private *dev_priv, struct intel_sdvo *sdvo)

    SDVO output based on the controlled output.

    :param struct drm_i915_private \*dev_priv:
        *undescribed*

    :param struct intel_sdvo \*sdvo:
        *undescribed*

.. _`intel_sdvo_select_ddc_bus.description`:

Description
-----------

DDC bus number assignment is in a priority order of RGB outputs, then TMDS
outputs, then LVDS outputs.

.. This file was automatic generated / don't edit.

