.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_ldu.c

.. _`vmw_ldu_crtc_mode_set_nofb`:

vmw_ldu_crtc_mode_set_nofb
==========================

.. c:function:: void vmw_ldu_crtc_mode_set_nofb(struct drm_crtc *crtc)

    Enable svga

    :param struct drm_crtc \*crtc:
        CRTC associated with the new screen

.. _`vmw_ldu_crtc_mode_set_nofb.description`:

Description
-----------

For LDU, just enable the svga

.. _`vmw_ldu_crtc_atomic_enable`:

vmw_ldu_crtc_atomic_enable
==========================

.. c:function:: void vmw_ldu_crtc_atomic_enable(struct drm_crtc *crtc, struct drm_crtc_state *old_state)

    Noop

    :param struct drm_crtc \*crtc:
        CRTC associated with the new screen

    :param struct drm_crtc_state \*old_state:
        *undescribed*

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

    :param struct drm_crtc \*crtc:
        CRTC to be turned off

    :param struct drm_crtc_state \*old_state:
        *undescribed*

.. This file was automatic generated / don't edit.

