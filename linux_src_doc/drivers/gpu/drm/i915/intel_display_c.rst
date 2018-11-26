.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_display.c

.. _`skl_update_scaler_crtc`:

skl_update_scaler_crtc
======================

.. c:function:: int skl_update_scaler_crtc(struct intel_crtc_state *state)

    Stages update to scaler state for a given crtc.

    :param state:
        crtc's scaler state
    :type state: struct intel_crtc_state \*

.. _`skl_update_scaler_crtc.description`:

Description
-----------

Return
0 - scaler_usage updated successfully
error - requested scaling cannot be supported or other error condition

.. _`skl_update_scaler_plane`:

skl_update_scaler_plane
=======================

.. c:function:: int skl_update_scaler_plane(struct intel_crtc_state *crtc_state, struct intel_plane_state *plane_state)

    Stages update to scaler state for a given plane.

    :param crtc_state:
        crtc's scaler state
    :type crtc_state: struct intel_crtc_state \*

    :param plane_state:
        atomic plane state to update
    :type plane_state: struct intel_plane_state \*

.. _`skl_update_scaler_plane.description`:

Description
-----------

Return
0 - scaler_usage updated successfully
error - requested scaling cannot be supported or other error condition

.. _`intel_post_enable_primary`:

intel_post_enable_primary
=========================

.. c:function:: void intel_post_enable_primary(struct drm_crtc *crtc, const struct intel_crtc_state *new_crtc_state)

    Perform operations after enabling primary plane

    :param crtc:
        the CRTC whose primary plane was just enabled
    :type crtc: struct drm_crtc \*

    :param new_crtc_state:
        the enabling state
    :type new_crtc_state: const struct intel_crtc_state \*

.. _`intel_post_enable_primary.description`:

Description
-----------

Performs potentially sleeping operations that must be done after the primary
plane is enabled, such as updating FBC and IPS.  Note that this may be
called due to an explicit primary plane update, or due to an implicit
re-enable that is caused when a sprite plane is updated to no longer
completely hide the primary plane.

.. _`vlv_force_pll_on`:

vlv_force_pll_on
================

.. c:function:: int vlv_force_pll_on(struct drm_i915_private *dev_priv, enum pipe pipe, const struct dpll *dpll)

    forcibly enable just the PLL

    :param dev_priv:
        i915 private structure
    :type dev_priv: struct drm_i915_private \*

    :param pipe:
        pipe PLL to enable
    :type pipe: enum pipe

    :param dpll:
        PLL configuration
    :type dpll: const struct dpll \*

.. _`vlv_force_pll_on.description`:

Description
-----------

Enable the PLL for \ ``pipe``\  using the supplied \ ``dpll``\  config. To be used
in cases where we need the PLL enabled even when \ ``pipe``\  is not going to
be enabled.

.. _`vlv_force_pll_off`:

vlv_force_pll_off
=================

.. c:function:: void vlv_force_pll_off(struct drm_i915_private *dev_priv, enum pipe pipe)

    forcibly disable just the PLL

    :param dev_priv:
        i915 private structure
    :type dev_priv: struct drm_i915_private \*

    :param pipe:
        pipe PLL to disable
    :type pipe: enum pipe

.. _`vlv_force_pll_off.description`:

Description
-----------

Disable the PLL for \ ``pipe``\ . To be used in cases where we need
the PLL enabled even when \ ``pipe``\  is not going to be enabled.

.. _`intel_wm_need_update`:

intel_wm_need_update
====================

.. c:function:: bool intel_wm_need_update(struct drm_plane *plane, struct drm_plane_state *state)

    Check whether watermarks need updating

    :param plane:
        drm plane
    :type plane: struct drm_plane \*

    :param state:
        new plane state
    :type state: struct drm_plane_state \*

.. _`intel_wm_need_update.description`:

Description
-----------

Check current plane state versus the new one to determine whether
watermarks need to be recalculated.

Returns true or false.

.. _`intel_atomic_check`:

intel_atomic_check
==================

.. c:function:: int intel_atomic_check(struct drm_device *dev, struct drm_atomic_state *state)

    validate state object

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param state:
        state to validate
    :type state: struct drm_atomic_state \*

.. _`intel_atomic_commit`:

intel_atomic_commit
===================

.. c:function:: int intel_atomic_commit(struct drm_device *dev, struct drm_atomic_state *state, bool nonblock)

    commit validated state object

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param state:
        the top-level driver state object
    :type state: struct drm_atomic_state \*

    :param nonblock:
        nonblocking commit
    :type nonblock: bool

.. _`intel_atomic_commit.description`:

Description
-----------

This function commits a top-level state object that has been validated
with \ :c:func:`drm_atomic_helper_check`\ .

RETURNS
Zero for success or -errno.

.. _`intel_prepare_plane_fb`:

intel_prepare_plane_fb
======================

.. c:function:: int intel_prepare_plane_fb(struct drm_plane *plane, struct drm_plane_state *new_state)

    Prepare fb for usage on plane

    :param plane:
        drm plane to prepare for
    :type plane: struct drm_plane \*

    :param new_state:
        the plane state being prepared
    :type new_state: struct drm_plane_state \*

.. _`intel_prepare_plane_fb.description`:

Description
-----------

Prepares a framebuffer for usage on a display plane.  Generally this
involves pinning the underlying object and updating the frontbuffer tracking
bits.  Some older platforms need special physical address handling for
cursor planes.

Must be called with struct_mutex held.

Returns 0 on success, negative error code on failure.

.. _`intel_cleanup_plane_fb`:

intel_cleanup_plane_fb
======================

.. c:function:: void intel_cleanup_plane_fb(struct drm_plane *plane, struct drm_plane_state *old_state)

    Cleans up an fb after plane use

    :param plane:
        drm plane to clean up for
    :type plane: struct drm_plane \*

    :param old_state:
        the state from the previous modeset
    :type old_state: struct drm_plane_state \*

.. _`intel_cleanup_plane_fb.description`:

Description
-----------

Cleans up a framebuffer that has just been removed from a plane.

Must be called with struct_mutex held.

.. _`intel_plane_destroy`:

intel_plane_destroy
===================

.. c:function:: void intel_plane_destroy(struct drm_plane *plane)

    destroy a plane

    :param plane:
        plane to destroy
    :type plane: struct drm_plane \*

.. _`intel_plane_destroy.description`:

Description
-----------

Common destruction function for all types of planes (primary, cursor,
sprite).

.. _`intel_init_display_hooks`:

intel_init_display_hooks
========================

.. c:function:: void intel_init_display_hooks(struct drm_i915_private *dev_priv)

    initialize the display modesetting hooks

    :param dev_priv:
        device private
    :type dev_priv: struct drm_i915_private \*

.. This file was automatic generated / don't edit.

