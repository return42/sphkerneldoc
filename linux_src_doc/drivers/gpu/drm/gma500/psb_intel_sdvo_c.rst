.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/psb_intel_sdvo.c

.. _`psb_intel_sdvo_write_sdvox`:

psb_intel_sdvo_write_sdvox
==========================

.. c:function:: void psb_intel_sdvo_write_sdvox(struct psb_intel_sdvo *psb_intel_sdvo, u32 val)

    SDVOB and SDVOC to work around apparent hardware issues (according to comments in the BIOS).

    :param psb_intel_sdvo:
        *undescribed*
    :type psb_intel_sdvo: struct psb_intel_sdvo \*

    :param val:
        *undescribed*
    :type val: u32

.. _`psb_intel_sdvo_get_trained_inputs`:

psb_intel_sdvo_get_trained_inputs
=================================

.. c:function:: bool psb_intel_sdvo_get_trained_inputs(struct psb_intel_sdvo *psb_intel_sdvo, bool *input_1, bool *input_2)

    :param psb_intel_sdvo:
        *undescribed*
    :type psb_intel_sdvo: struct psb_intel_sdvo \*

    :param input_1:
        *undescribed*
    :type input_1: bool \*

    :param input_2:
        *undescribed*
    :type input_2: bool \*

.. _`psb_intel_sdvo_get_trained_inputs.description`:

Description
-----------

This function is making an assumption about the layout of the response,
which should be checked against the docs.

.. _`psb_intel_sdvo_select_ddc_bus`:

psb_intel_sdvo_select_ddc_bus
=============================

.. c:function:: void psb_intel_sdvo_select_ddc_bus(struct drm_psb_private *dev_priv, struct psb_intel_sdvo *sdvo, u32 reg)

    SDVO output based on the controlled output.

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct drm_psb_private \*

    :param sdvo:
        *undescribed*
    :type sdvo: struct psb_intel_sdvo \*

    :param reg:
        *undescribed*
    :type reg: u32

.. _`psb_intel_sdvo_select_ddc_bus.description`:

Description
-----------

DDC bus number assignment is in a priority order of RGB outputs, then TMDS
outputs, then LVDS outputs.

.. This file was automatic generated / don't edit.

