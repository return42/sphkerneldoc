.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dcn10/dcn10_timing_generator.c

.. _`tgn10_apply_front_porch_workaround`:

tgn10_apply_front_porch_workaround
==================================

.. c:function:: void tgn10_apply_front_porch_workaround(struct timing_generator *tg, struct dc_crtc_timing *timing)

    :param struct timing_generator \*tg:
        *undescribed*

    :param struct dc_crtc_timing \*timing:
        *undescribed*

.. _`tgn10_apply_front_porch_workaround.description`:

Description
-----------

This is a workaround for a bug that has existed since R5xx and has not been
fixed keep Front porch at minimum 2 for Interlaced mode or 1 for progressive.

.. _`tgn10_program_timing`:

tgn10_program_timing
====================

.. c:function:: void tgn10_program_timing(struct timing_generator *tg, const struct dc_crtc_timing *dc_crtc_timing, bool use_vbios)

    Program CRTC Timing Registers - OTG_H\_\*, OTG_V\_\*, Pixel repetition. Including SYNC. Call BIOS command table to program Timings.

    :param struct timing_generator \*tg:
        *undescribed*

    :param const struct dc_crtc_timing \*dc_crtc_timing:
        *undescribed*

    :param bool use_vbios:
        *undescribed*

.. _`tgn10_unblank_crtc`:

tgn10_unblank_crtc
==================

.. c:function:: void tgn10_unblank_crtc(struct timing_generator *tg)

    Call ASIC Control Object to UnBlank CRTC.

    :param struct timing_generator \*tg:
        *undescribed*

.. _`tgn10_blank_crtc`:

tgn10_blank_crtc
================

.. c:function:: void tgn10_blank_crtc(struct timing_generator *tg)

    Call ASIC Control Object to Blank CRTC.

    :param struct timing_generator \*tg:
        *undescribed*

.. _`tgn10_enable_crtc`:

tgn10_enable_crtc
=================

.. c:function:: bool tgn10_enable_crtc(struct timing_generator *tg)

    Enable CRTC - call ASIC Control Object to enable Timing generator.

    :param struct timing_generator \*tg:
        *undescribed*

.. This file was automatic generated / don't edit.

