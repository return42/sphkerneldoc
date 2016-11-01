.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_tvout.c

.. _`tvout_vip_set_color_order`:

tvout_vip_set_color_order
=========================

.. c:function:: void tvout_vip_set_color_order(struct sti_tvout *tvout, int reg, u32 cr_r, u32 y_g, u32 cb_b)

    :param struct sti_tvout \*tvout:
        tvout structure

    :param int reg:
        register to set

    :param u32 cr_r:
        *undescribed*

    :param u32 y_g:
        *undescribed*

    :param u32 cb_b:
        *undescribed*

.. _`tvout_vip_set_clip_mode`:

tvout_vip_set_clip_mode
=======================

.. c:function:: void tvout_vip_set_clip_mode(struct sti_tvout *tvout, int reg, u32 range)

    :param struct sti_tvout \*tvout:
        tvout structure

    :param int reg:
        register to set

    :param u32 range:
        clipping range

.. _`tvout_vip_set_rnd`:

tvout_vip_set_rnd
=================

.. c:function:: void tvout_vip_set_rnd(struct sti_tvout *tvout, int reg, u32 rnd)

    :param struct sti_tvout \*tvout:
        tvout structure

    :param int reg:
        register to set

    :param u32 rnd:
        rounded val per component

.. _`tvout_vip_set_sel_input`:

tvout_vip_set_sel_input
=======================

.. c:function:: void tvout_vip_set_sel_input(struct sti_tvout *tvout, int reg, bool main_path, enum sti_tvout_video_out_type video_out)

    :param struct sti_tvout \*tvout:
        tvout structure

    :param int reg:
        register to set

    :param bool main_path:
        main or auxiliary path

    :param enum sti_tvout_video_out_type video_out:
        *undescribed*

.. _`tvout_vip_set_in_vid_fmt`:

tvout_vip_set_in_vid_fmt
========================

.. c:function:: void tvout_vip_set_in_vid_fmt(struct sti_tvout *tvout, int reg, u32 in_vid_fmt)

    :param struct sti_tvout \*tvout:
        tvout structure

    :param int reg:
        register to set

    :param u32 in_vid_fmt:
        *undescribed*

.. _`tvout_preformatter_set_matrix`:

tvout_preformatter_set_matrix
=============================

.. c:function:: void tvout_preformatter_set_matrix(struct sti_tvout *tvout, struct drm_display_mode *mode)

    :param struct sti_tvout \*tvout:
        tvout structure

    :param struct drm_display_mode \*mode:
        display mode structure

.. _`tvout_dvo_start`:

tvout_dvo_start
===============

.. c:function:: void tvout_dvo_start(struct sti_tvout *tvout, bool main_path)

    :param struct sti_tvout \*tvout:
        pointer on tvout structure

    :param bool main_path:
        true if main path has to be used in the vip configuration
        else aux path is used.

.. _`tvout_hdmi_start`:

tvout_hdmi_start
================

.. c:function:: void tvout_hdmi_start(struct sti_tvout *tvout, bool main_path)

    :param struct sti_tvout \*tvout:
        pointer on tvout structure

    :param bool main_path:
        true if main path has to be used in the vip configuration
        else aux path is used.

.. _`tvout_hda_start`:

tvout_hda_start
===============

.. c:function:: void tvout_hda_start(struct sti_tvout *tvout, bool main_path)

    :param struct sti_tvout \*tvout:
        pointer on tvout structure

    :param bool main_path:
        true if main path has to be used in the vip configuration
        else aux path is used.

.. This file was automatic generated / don't edit.

