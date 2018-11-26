.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_plane.c

.. _`dpu_plane_qos`:

enum dpu_plane_qos
==================

.. c:type:: enum dpu_plane_qos

    Different qos configurations for each pipe

.. _`dpu_plane_qos.definition`:

Definition
----------

.. code-block:: c

    enum dpu_plane_qos {
        DPU_PLANE_QOS_VBLANK_CTRL,
        DPU_PLANE_QOS_VBLANK_AMORTIZE,
        DPU_PLANE_QOS_PANIC_CTRL
    };

.. _`dpu_plane_qos.constants`:

Constants
---------

DPU_PLANE_QOS_VBLANK_CTRL
    Setup VBLANK qos for the pipe.

DPU_PLANE_QOS_VBLANK_AMORTIZE
    Enables Amortization within pipe.
    this configuration is mutually exclusive from VBLANK_CTRL.

DPU_PLANE_QOS_PANIC_CTRL
    Setup panic for the pipe.

.. _`_dpu_plane_calc_fill_level`:

\_dpu_plane_calc_fill_level
===========================

.. c:function:: int _dpu_plane_calc_fill_level(struct drm_plane *plane, const struct dpu_format *fmt, u32 src_width)

    calculate fill level of the given source format

    :param plane:
        Pointer to drm plane
    :type plane: struct drm_plane \*

    :param fmt:
        Pointer to source buffer format
    :type fmt: const struct dpu_format \*

    :param src_width:
        *undescribed*
    :type src_width: u32

.. _`_dpu_plane_calc_fill_level.return`:

Return
------

fill level corresponding to the source buffer/format or 0 if error

.. _`_dpu_plane_get_qos_lut`:

\_dpu_plane_get_qos_lut
=======================

.. c:function:: u64 _dpu_plane_get_qos_lut(const struct dpu_qos_lut_tbl *tbl, u32 total_fl)

    get LUT mapping based on fill level

    :param tbl:
        Pointer to LUT table
    :type tbl: const struct dpu_qos_lut_tbl \*

    :param total_fl:
        fill level
    :type total_fl: u32

.. _`_dpu_plane_get_qos_lut.return`:

Return
------

LUT setting corresponding to the fill level

.. _`_dpu_plane_set_qos_lut`:

\_dpu_plane_set_qos_lut
=======================

.. c:function:: void _dpu_plane_set_qos_lut(struct drm_plane *plane, struct drm_framebuffer *fb)

    set QoS LUT of the given plane

    :param plane:
        Pointer to drm plane
    :type plane: struct drm_plane \*

    :param fb:
        Pointer to framebuffer associated with the given plane
    :type fb: struct drm_framebuffer \*

.. _`_dpu_plane_set_danger_lut`:

\_dpu_plane_set_danger_lut
==========================

.. c:function:: void _dpu_plane_set_danger_lut(struct drm_plane *plane, struct drm_framebuffer *fb)

    set danger/safe LUT of the given plane

    :param plane:
        Pointer to drm plane
    :type plane: struct drm_plane \*

    :param fb:
        Pointer to framebuffer associated with the given plane
    :type fb: struct drm_framebuffer \*

.. _`_dpu_plane_set_qos_ctrl`:

\_dpu_plane_set_qos_ctrl
========================

.. c:function:: void _dpu_plane_set_qos_ctrl(struct drm_plane *plane, bool enable, u32 flags)

    set QoS control of the given plane

    :param plane:
        Pointer to drm plane
    :type plane: struct drm_plane \*

    :param enable:
        true to enable QoS control
    :type enable: bool

    :param flags:
        QoS control mode (enum dpu_plane_qos)
    :type flags: u32

.. _`_dpu_plane_set_ot_limit`:

\_dpu_plane_set_ot_limit
========================

.. c:function:: void _dpu_plane_set_ot_limit(struct drm_plane *plane, struct drm_crtc *crtc)

    set OT limit for the given plane

    :param plane:
        Pointer to drm plane
    :type plane: struct drm_plane \*

    :param crtc:
        Pointer to drm crtc
    :type crtc: struct drm_crtc \*

.. _`_dpu_plane_set_qos_remap`:

\_dpu_plane_set_qos_remap
=========================

.. c:function:: void _dpu_plane_set_qos_remap(struct drm_plane *plane)

    set vbif QoS for the given plane

    :param plane:
        Pointer to drm plane
    :type plane: struct drm_plane \*

.. _`_dpu_plane_get_aspace`:

\_dpu_plane_get_aspace
======================

.. c:function:: struct msm_gem_address_space *_dpu_plane_get_aspace(struct dpu_plane *pdpu)

    gets the address space

    :param pdpu:
        *undescribed*
    :type pdpu: struct dpu_plane \*

.. _`_dpu_plane_color_fill`:

\_dpu_plane_color_fill
======================

.. c:function:: int _dpu_plane_color_fill(struct dpu_plane *pdpu, uint32_t color, uint32_t alpha)

    enables color fill on plane

    :param pdpu:
        Pointer to DPU plane object
    :type pdpu: struct dpu_plane \*

    :param color:
        RGB fill color value, [23..16] Blue, [15..8] Green, [7..0] Red
    :type color: uint32_t

    :param alpha:
        8-bit fill alpha value, 255 selects 100% alpha
    :type alpha: uint32_t

.. _`_dpu_plane_color_fill.return`:

Return
------

0 on success

.. _`dpu_plane_get_ctl_flush`:

dpu_plane_get_ctl_flush
=======================

.. c:function:: void dpu_plane_get_ctl_flush(struct drm_plane *plane, struct dpu_hw_ctl *ctl, u32 *flush_sspp)

    get control flush for the given plane

    :param plane:
        Pointer to drm plane structure
    :type plane: struct drm_plane \*

    :param ctl:
        Pointer to hardware control driver
    :type ctl: struct dpu_hw_ctl \*

    :param flush_sspp:
        Pointer to sspp flush control word
    :type flush_sspp: u32 \*

.. _`dpu_plane_set_error`:

dpu_plane_set_error
===================

.. c:function:: void dpu_plane_set_error(struct drm_plane *plane, bool error)

    enable/disable error condition

    :param plane:
        pointer to drm_plane structure
    :type plane: struct drm_plane \*

    :param error:
        *undescribed*
    :type error: bool

.. This file was automatic generated / don't edit.

