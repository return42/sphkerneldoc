.. -*- coding: utf-8; mode: rst -*-

=====================
psb_intel_sdvo_regs.h
=====================


.. _`sdvo_cmd_get_trained_inputs`:

SDVO_CMD_GET_TRAINED_INPUTS
===========================

.. c:function:: SDVO_CMD_GET_TRAINED_INPUTS ()



.. _`sdvo_cmd_get_trained_inputs.description`:

Description
-----------


Devices must have trained within 2 vsyncs of a mode change.



.. _`sdvo_cmd_set_active_outputs`:

SDVO_CMD_SET_ACTIVE_OUTPUTS
===========================

.. c:function:: SDVO_CMD_SET_ACTIVE_OUTPUTS ()



.. _`sdvo_cmd_set_active_outputs.description`:

Description
-----------


Takes a struct intel_sdvo_output_flags.  Must be preceded by a SET_IN_OUT_MAP
on multi-output devices.



.. _`sdvo_cmd_get_in_out_map`:

SDVO_CMD_GET_IN_OUT_MAP
=======================

.. c:function:: SDVO_CMD_GET_IN_OUT_MAP ()



.. _`sdvo_cmd_get_in_out_map.description`:

Description
-----------


Returns two struct intel_sdvo_output_flags structures.



.. _`sdvo_cmd_set_in_out_map`:

SDVO_CMD_SET_IN_OUT_MAP
=======================

.. c:function:: SDVO_CMD_SET_IN_OUT_MAP ()



.. _`sdvo_cmd_set_in_out_map.description`:

Description
-----------


Takes two struct i380_sdvo_output_flags structures.



.. _`sdvo_cmd_get_attached_displays`:

SDVO_CMD_GET_ATTACHED_DISPLAYS
==============================

.. c:function:: SDVO_CMD_GET_ATTACHED_DISPLAYS ()



.. _`sdvo_cmd_get_hot_plug_support`:

SDVO_CMD_GET_HOT_PLUG_SUPPORT
=============================

.. c:function:: SDVO_CMD_GET_HOT_PLUG_SUPPORT ()



.. _`sdvo_cmd_set_active_hot_plug`:

SDVO_CMD_SET_ACTIVE_HOT_PLUG
============================

.. c:function:: SDVO_CMD_SET_ACTIVE_HOT_PLUG ()



.. _`sdvo_cmd_get_active_hot_plug`:

SDVO_CMD_GET_ACTIVE_HOT_PLUG
============================

.. c:function:: SDVO_CMD_GET_ACTIVE_HOT_PLUG ()



.. _`sdvo_cmd_get_active_hot_plug.description`:

Description
-----------

interrupts enabled.



.. _`sdvo_cmd_set_target_input`:

SDVO_CMD_SET_TARGET_INPUT
=========================

.. c:function:: SDVO_CMD_SET_TARGET_INPUT ()



.. _`sdvo_cmd_set_target_input.description`:

Description
-----------


Commands affected include SET_INPUT_TIMINGS_PART[12],
GET_INPUT_TIMINGS_PART[12], GET_PREFERRED_INPUT_TIMINGS_PART[12],
GET_INPUT_PIXEL_CLOCK_RANGE, and CREATE_PREFERRED_INPUT_TIMINGS.



.. _`sdvo_cmd_set_target_output`:

SDVO_CMD_SET_TARGET_OUTPUT
==========================

.. c:function:: SDVO_CMD_SET_TARGET_OUTPUT ()



.. _`sdvo_cmd_set_target_output.description`:

Description
-----------

future output commands.

Affected commands inclue SET_OUTPUT_TIMINGS_PART[12],
GET_OUTPUT_TIMINGS_PART[12], and GET_OUTPUT_PIXEL_CLOCK_RANGE.



.. _`sdvo_cmd_create_preferred_input_timing`:

SDVO_CMD_CREATE_PREFERRED_INPUT_TIMING
======================================

.. c:function:: SDVO_CMD_CREATE_PREFERRED_INPUT_TIMING ()



.. _`sdvo_cmd_create_preferred_input_timing.description`:

Description
-----------


This will be supported by any device supporting scaling or interlaced
modes.

