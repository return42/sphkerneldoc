.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_tvout.c

.. _`tvout_vip_set_color_order`:

tvout_vip_set_color_order
=========================

.. c:function:: void tvout_vip_set_color_order(struct sti_tvout *tvout, int reg, u32 cr_r, u32 y_g, u32 cb_b)

    :param tvout:
        tvout structure
    :type tvout: struct sti_tvout \*

    :param reg:
        register to set
    :type reg: int

    :param cr_r:
        *undescribed*
    :type cr_r: u32

    :param y_g:
        *undescribed*
    :type y_g: u32

    :param cb_b:
        *undescribed*
    :type cb_b: u32

.. _`tvout_vip_set_clip_mode`:

tvout_vip_set_clip_mode
=======================

.. c:function:: void tvout_vip_set_clip_mode(struct sti_tvout *tvout, int reg, u32 range)

    :param tvout:
        tvout structure
    :type tvout: struct sti_tvout \*

    :param reg:
        register to set
    :type reg: int

    :param range:
        clipping range
    :type range: u32

.. _`tvout_vip_set_rnd`:

tvout_vip_set_rnd
=================

.. c:function:: void tvout_vip_set_rnd(struct sti_tvout *tvout, int reg, u32 rnd)

    :param tvout:
        tvout structure
    :type tvout: struct sti_tvout \*

    :param reg:
        register to set
    :type reg: int

    :param rnd:
        rounded val per component
    :type rnd: u32

.. _`tvout_vip_set_sel_input`:

tvout_vip_set_sel_input
=======================

.. c:function:: void tvout_vip_set_sel_input(struct sti_tvout *tvout, int reg, bool main_path, enum sti_tvout_video_out_type video_out)

    :param tvout:
        tvout structure
    :type tvout: struct sti_tvout \*

    :param reg:
        register to set
    :type reg: int

    :param main_path:
        main or auxiliary path
    :type main_path: bool

    :param video_out:
        *undescribed*
    :type video_out: enum sti_tvout_video_out_type

.. _`tvout_vip_set_in_vid_fmt`:

tvout_vip_set_in_vid_fmt
========================

.. c:function:: void tvout_vip_set_in_vid_fmt(struct sti_tvout *tvout, int reg, u32 in_vid_fmt)

    :param tvout:
        tvout structure
    :type tvout: struct sti_tvout \*

    :param reg:
        register to set
    :type reg: int

    :param in_vid_fmt:
        *undescribed*
    :type in_vid_fmt: u32

.. _`tvout_preformatter_set_matrix`:

tvout_preformatter_set_matrix
=============================

.. c:function:: void tvout_preformatter_set_matrix(struct sti_tvout *tvout, struct drm_display_mode *mode)

    :param tvout:
        tvout structure
    :type tvout: struct sti_tvout \*

    :param mode:
        display mode structure
    :type mode: struct drm_display_mode \*

.. _`tvout_dvo_start`:

tvout_dvo_start
===============

.. c:function:: void tvout_dvo_start(struct sti_tvout *tvout, bool main_path)

    :param tvout:
        pointer on tvout structure
    :type tvout: struct sti_tvout \*

    :param main_path:
        true if main path has to be used in the vip configuration
        else aux path is used.
    :type main_path: bool

.. _`tvout_hdmi_start`:

tvout_hdmi_start
================

.. c:function:: void tvout_hdmi_start(struct sti_tvout *tvout, bool main_path)

    :param tvout:
        pointer on tvout structure
    :type tvout: struct sti_tvout \*

    :param main_path:
        true if main path has to be used in the vip configuration
        else aux path is used.
    :type main_path: bool

.. _`tvout_hda_start`:

tvout_hda_start
===============

.. c:function:: void tvout_hda_start(struct sti_tvout *tvout, bool main_path)

    :param tvout:
        pointer on tvout structure
    :type tvout: struct sti_tvout \*

    :param main_path:
        true if main path has to be used in the vip configuration
        else aux path is used.
    :type main_path: bool

.. This file was automatic generated / don't edit.

