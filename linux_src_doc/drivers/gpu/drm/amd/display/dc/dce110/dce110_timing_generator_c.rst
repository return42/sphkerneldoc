.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dce110/dce110_timing_generator.c

.. _`dce110_timing_generator_enable_crtc`:

dce110_timing_generator_enable_crtc
===================================

.. c:function:: bool dce110_timing_generator_enable_crtc(struct timing_generator *tg)

    Enable CRTC - call ASIC Control Object to enable Timing generator.

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

.. _`dce110_timing_generator_disable_crtc`:

dce110_timing_generator_disable_crtc
====================================

.. c:function:: bool dce110_timing_generator_disable_crtc(struct timing_generator *tg)

    call ASIC Control Object to disable Timing generator.

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

.. _`program_horz_count_by_2`:

program_horz_count_by_2
=======================

.. c:function:: void program_horz_count_by_2(struct timing_generator *tg, const struct dc_crtc_timing *timing)

    Programs DxCRTC_HORZ_COUNT_BY2_EN - 1 for DVI 30bpp mode, 0 otherwise

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

    :param timing:
        *undescribed*
    :type timing: const struct dc_crtc_timing \*

.. _`dce110_timing_generator_program_timing_generator`:

dce110_timing_generator_program_timing_generator
================================================

.. c:function:: bool dce110_timing_generator_program_timing_generator(struct timing_generator *tg, const struct dc_crtc_timing *dc_crtc_timing)

    Program CRTC Timing Registers - DxCRTC_H\_\*, DxCRTC_V\_\*, Pixel repetition. Call ASIC Control Object to program Timings.

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

    :param dc_crtc_timing:
        *undescribed*
    :type dc_crtc_timing: const struct dc_crtc_timing \*

.. _`dce110_timing_generator_validate_timing`:

dce110_timing_generator_validate_timing
=======================================

.. c:function:: bool dce110_timing_generator_validate_timing(struct timing_generator *tg, const struct dc_crtc_timing *timing, enum signal_type signal)

    The timing generators support a maximum display size of is 8192 x 8192 pixels, including both active display and blanking periods. Check H Total and V Total.

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

    :param timing:
        *undescribed*
    :type timing: const struct dc_crtc_timing \*

    :param signal:
        *undescribed*
    :type signal: enum signal_type

.. _`dce110_timing_generator_wait_for_vblank`:

dce110_timing_generator_wait_for_vblank
=======================================

.. c:function:: void dce110_timing_generator_wait_for_vblank(struct timing_generator *tg)

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

.. _`dce110_timing_generator_wait_for_vactive`:

dce110_timing_generator_wait_for_vactive
========================================

.. c:function:: void dce110_timing_generator_wait_for_vactive(struct timing_generator *tg)

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

.. _`dce110_timing_generator_disable_vga`:

dce110_timing_generator_disable_vga
===================================

.. c:function:: void dce110_timing_generator_disable_vga(struct timing_generator *tg)

    Turn OFF VGA Mode and Timing  - DxVGA_CONTROL VGA Mode and VGA Timing is used by VBIOS on CRT Monitors;

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

.. _`dce110_timing_generator_set_overscan_color_black`:

dce110_timing_generator_set_overscan_color_black
================================================

.. c:function:: void dce110_timing_generator_set_overscan_color_black(struct timing_generator *tg, const struct tg_color *color)

    :param tg:
        *undescribed*
    :type tg: struct timing_generator \*

    :param color:
        *undescribed*
    :type color: const struct tg_color \*

.. This file was automatic generated / don't edit.

