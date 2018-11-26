.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_crtc.c

.. _`_dpu_crtc_blend_setup`:

\_dpu_crtc_blend_setup
======================

.. c:function:: void _dpu_crtc_blend_setup(struct drm_crtc *crtc)

    configure crtc mixers

    :param crtc:
        Pointer to drm crtc structure
    :type crtc: struct drm_crtc \*

.. _`_dpu_crtc_complete_flip`:

\_dpu_crtc_complete_flip
========================

.. c:function:: void _dpu_crtc_complete_flip(struct drm_crtc *crtc)

    signal pending page_flip events Any pending vblank events are added to the vblank_event_list so that the next vblank interrupt shall signal them. However PAGE_FLIP events are not handled through the vblank_event_list. This API signals any pending PAGE_FLIP events requested through DRM_IOCTL_MODE_PAGE_FLIP and are cached in the dpu_crtc->event.

    :param crtc:
        Pointer to drm crtc structure
    :type crtc: struct drm_crtc \*

.. _`dpu_crtc_destroy_state`:

dpu_crtc_destroy_state
======================

.. c:function:: void dpu_crtc_destroy_state(struct drm_crtc *crtc, struct drm_crtc_state *state)

    state destroy hook

    :param crtc:
        drm CRTC
    :type crtc: struct drm_crtc \*

    :param state:
        CRTC state object to release
    :type state: struct drm_crtc_state \*

.. _`_dpu_crtc_vblank_enable_no_lock`:

\_dpu_crtc_vblank_enable_no_lock
================================

.. c:function:: void _dpu_crtc_vblank_enable_no_lock(struct dpu_crtc *dpu_crtc, bool enable)

    update power resource and vblank request

    :param dpu_crtc:
        Pointer to dpu crtc structure
    :type dpu_crtc: struct dpu_crtc \*

    :param enable:
        Whether to enable/disable vblanks
    :type enable: bool

.. _`_dpu_crtc_set_suspend`:

\_dpu_crtc_set_suspend
======================

.. c:function:: void _dpu_crtc_set_suspend(struct drm_crtc *crtc, bool enable)

    notify crtc of suspend enable/disable

    :param crtc:
        Pointer to drm crtc object
    :type crtc: struct drm_crtc \*

    :param enable:
        true to enable suspend, false to indicate resume
    :type enable: bool

.. _`dpu_crtc_duplicate_state`:

dpu_crtc_duplicate_state
========================

.. c:function:: struct drm_crtc_state *dpu_crtc_duplicate_state(struct drm_crtc *crtc)

    state duplicate hook

    :param crtc:
        Pointer to drm crtc structure
    :type crtc: struct drm_crtc \*

.. _`dpu_crtc_reset`:

dpu_crtc_reset
==============

.. c:function:: void dpu_crtc_reset(struct drm_crtc *crtc)

    reset hook for CRTCs Resets the atomic state for \ ``crtc``\  by freeing the state pointer (which might be NULL, e.g. at driver load time) and allocating a new empty state object.

    :param crtc:
        Pointer to drm crtc structure
    :type crtc: struct drm_crtc \*

.. This file was automatic generated / don't edit.

