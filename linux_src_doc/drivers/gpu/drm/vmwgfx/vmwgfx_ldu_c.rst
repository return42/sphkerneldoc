.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_ldu.c

.. _`vmw_ldu_crtc_mode_set_nofb`:

vmw_ldu_crtc_mode_set_nofb
==========================

.. c:function:: void vmw_ldu_crtc_mode_set_nofb(struct drm_crtc *crtc)

    Enable svga

    :param crtc:
        CRTC associated with the new screen
    :type crtc: struct drm_crtc \*

.. _`vmw_ldu_crtc_mode_set_nofb.description`:

Description
-----------

For LDU, just enable the svga

.. _`vmw_ldu_crtc_atomic_enable`:

vmw_ldu_crtc_atomic_enable
==========================

.. c:function:: void vmw_ldu_crtc_atomic_enable(struct drm_crtc *crtc, struct drm_crtc_state *old_state)

    Noop

    :param crtc:
        CRTC associated with the new screen
    :type crtc: struct drm_crtc \*

    :param old_state:
        *undescribed*
    :type old_state: struct drm_crtc_state \*

.. _`vmw_ldu_crtc_atomic_enable.description`:

Description
-----------

This is called after a mode set has been completed.  Here's
usually a good place to call vmw_ldu_add_active/vmw_ldu_del_active
but since for LDU the display plane is closely tied to the
CRTC, it makes more sense to do those at plane update time.

.. _`vmw_ldu_crtc_atomic_disable`:

vmw_ldu_crtc_atomic_disable
===========================

.. c:function:: void vmw_ldu_crtc_atomic_disable(struct drm_crtc *crtc, struct drm_crtc_state *old_state)

    Turns off CRTC

    :param crtc:
        CRTC to be turned off
    :type crtc: struct drm_crtc \*

    :param old_state:
        *undescribed*
    :type old_state: struct drm_crtc_state \*

.. This file was automatic generated / don't edit.

