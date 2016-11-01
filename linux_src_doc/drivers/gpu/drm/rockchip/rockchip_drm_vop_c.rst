.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rockchip/rockchip_drm_vop.c

.. _`rockchip_drm_wait_line_flag`:

rockchip_drm_wait_line_flag
===========================

.. c:function:: int rockchip_drm_wait_line_flag(struct drm_crtc *crtc, unsigned int line_num, unsigned int mstimeout)

    acqiure the give line flag event

    :param struct drm_crtc \*crtc:
        CRTC to enable line flag

    :param unsigned int line_num:
        interested line number

    :param unsigned int mstimeout:
        millisecond for timeout

.. _`rockchip_drm_wait_line_flag.description`:

Description
-----------

Driver would hold here until the interested line flag interrupt have
happened or timeout to wait.

.. _`rockchip_drm_wait_line_flag.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

