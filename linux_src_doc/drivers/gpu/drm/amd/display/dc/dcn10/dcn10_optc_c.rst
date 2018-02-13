.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dcn10/dcn10_optc.c

.. _`optc1_apply_front_porch_workaround`:

optc1_apply_front_porch_workaround
==================================

.. c:function:: void optc1_apply_front_porch_workaround(struct timing_generator *optc, struct dc_crtc_timing *timing)

    :param struct timing_generator \*optc:
        *undescribed*

    :param struct dc_crtc_timing \*timing:
        *undescribed*

.. _`optc1_apply_front_porch_workaround.description`:

Description
-----------

This is a workaround for a bug that has existed since R5xx and has not been
fixed keep Front porch at minimum 2 for Interlaced mode or 1 for progressive.

.. _`optc1_program_timing`:

optc1_program_timing
====================

.. c:function:: void optc1_program_timing(struct timing_generator *optc, const struct dc_crtc_timing *dc_crtc_timing, bool use_vbios)

    Program CRTC Timing Registers - OTG_H\_\*, OTG_V\_\*, Pixel repetition. Including SYNC. Call BIOS command table to program Timings.

    :param struct timing_generator \*optc:
        *undescribed*

    :param const struct dc_crtc_timing \*dc_crtc_timing:
        *undescribed*

    :param bool use_vbios:
        *undescribed*

.. _`optc1_unblank_crtc`:

optc1_unblank_crtc
==================

.. c:function:: void optc1_unblank_crtc(struct timing_generator *optc)

    Call ASIC Control Object to UnBlank CRTC.

    :param struct timing_generator \*optc:
        *undescribed*

.. _`optc1_blank_crtc`:

optc1_blank_crtc
================

.. c:function:: void optc1_blank_crtc(struct timing_generator *optc)

    Call ASIC Control Object to Blank CRTC.

    :param struct timing_generator \*optc:
        *undescribed*

.. _`optc1_enable_crtc`:

optc1_enable_crtc
=================

.. c:function:: bool optc1_enable_crtc(struct timing_generator *optc)

    Enable CRTC - call ASIC Control Object to enable Timing generator.

    :param struct timing_generator \*optc:
        *undescribed*

.. This file was automatic generated / don't edit.

