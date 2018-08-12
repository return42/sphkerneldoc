.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_simple_kms_helper.h

.. _`drm_simple_display_pipe_funcs`:

struct drm_simple_display_pipe_funcs
====================================

.. c:type:: struct drm_simple_display_pipe_funcs

    helper operations for a simple display pipeline

.. _`drm_simple_display_pipe_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_simple_display_pipe_funcs {
        enum drm_mode_status (*mode_valid)(struct drm_crtc *crtc, const struct drm_display_mode *mode);
        void (*enable)(struct drm_simple_display_pipe *pipe,struct drm_crtc_state *crtc_state, struct drm_plane_state *plane_state);
        void (*disable)(struct drm_simple_display_pipe *pipe);
        int (*check)(struct drm_simple_display_pipe *pipe,struct drm_plane_state *plane_state, struct drm_crtc_state *crtc_state);
        void (*update)(struct drm_simple_display_pipe *pipe, struct drm_plane_state *old_plane_state);
        int (*prepare_fb)(struct drm_simple_display_pipe *pipe, struct drm_plane_state *plane_state);
        void (*cleanup_fb)(struct drm_simple_display_pipe *pipe, struct drm_plane_state *plane_state);
        int (*enable_vblank)(struct drm_simple_display_pipe *pipe);
        void (*disable_vblank)(struct drm_simple_display_pipe *pipe);
    }

.. _`drm_simple_display_pipe_funcs.members`:

Members
-------

mode_valid

    This callback is used to check if a specific mode is valid in the
    crtc used in this simple display pipe. This should be implemented
    if the display pipe has some sort of restriction in the modes
    it can display. For example, a given display pipe may be responsible
    to set a clock value. If the clock can not produce all the values
    for the available modes then this callback can be used to restrict
    the number of modes to only the ones that can be displayed. Another
    reason can be bandwidth mitigation: the memory port on the display
    controller can have bandwidth limitations not allowing pixel data
    to be fetched at any rate.

    This hook is used by the probe helpers to filter the mode list in
    \ :c:func:`drm_helper_probe_single_connector_modes`\ , and it is used by the
    atomic helpers to validate modes supplied by userspace in
    \ :c:func:`drm_atomic_helper_check_modeset`\ .

    This function is optional.

    NOTE:

    Since this function is both called from the check phase of an atomic
    commit, and the mode validation in the probe paths it is not allowed
    to look at anything else but the passed-in mode, and validate it
    against configuration-invariant hardware constraints.

    RETURNS:

    drm_mode_status Enum

enable

    This function should be used to enable the pipeline.
    It is called when the underlying crtc is enabled.
    This hook is optional.

disable

    This function should be used to disable the pipeline.
    It is called when the underlying crtc is disabled.
    This hook is optional.

check

    This function is called in the check phase of an atomic update,
    specifically when the underlying plane is checked.
    The simple display pipeline helpers already check that the plane is
    not scaled, fills the entire visible area and is always enabled
    when the crtc is also enabled.
    This hook is optional.

    RETURNS:

    0 on success, -EINVAL if the state or the transition can't be
    supported, -ENOMEM on memory allocation failure and -EDEADLK if an
    attempt to obtain another state object ran into a \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\ 
    deadlock.

update

    This function is called when the underlying plane state is updated.
    This hook is optional.

    This is the function drivers should submit the
    \ :c:type:`struct drm_pending_vblank_event <drm_pending_vblank_event>`\  from. Using either
    \ :c:func:`drm_crtc_arm_vblank_event`\ , when the driver supports vblank
    interrupt handling, or \ :c:func:`drm_crtc_send_vblank_event`\  directly in case
    the hardware lacks vblank support entirely.

prepare_fb

    Optional, called by \ :c:type:`drm_plane_helper_funcs.prepare_fb <drm_plane_helper_funcs>`\ .  Please read
    the documentation for the \ :c:type:`drm_plane_helper_funcs.prepare_fb <drm_plane_helper_funcs>`\  hook for
    more details.

    Drivers which always have their buffers pinned should use
    \ :c:func:`drm_gem_fb_simple_display_pipe_prepare_fb`\  for this hook.

cleanup_fb

    Optional, called by \ :c:type:`drm_plane_helper_funcs.cleanup_fb <drm_plane_helper_funcs>`\ .  Please read
    the documentation for the \ :c:type:`drm_plane_helper_funcs.cleanup_fb <drm_plane_helper_funcs>`\  hook for
    more details.

enable_vblank

    Optional, called by \ :c:type:`drm_crtc_funcs.enable_vblank <drm_crtc_funcs>`\ . Please read
    the documentation for the \ :c:type:`drm_crtc_funcs.enable_vblank <drm_crtc_funcs>`\  hook for
    more details.

disable_vblank

    Optional, called by \ :c:type:`drm_crtc_funcs.disable_vblank <drm_crtc_funcs>`\ . Please read
    the documentation for the \ :c:type:`drm_crtc_funcs.disable_vblank <drm_crtc_funcs>`\  hook for
    more details.

.. _`drm_simple_display_pipe`:

struct drm_simple_display_pipe
==============================

.. c:type:: struct drm_simple_display_pipe

    simple display pipeline

.. _`drm_simple_display_pipe.definition`:

Definition
----------

.. code-block:: c

    struct drm_simple_display_pipe {
        struct drm_crtc crtc;
        struct drm_plane plane;
        struct drm_encoder encoder;
        struct drm_connector *connector;
        const struct drm_simple_display_pipe_funcs *funcs;
    }

.. _`drm_simple_display_pipe.members`:

Members
-------

crtc
    CRTC control structure

plane
    Plane control structure

encoder
    Encoder control structure

connector
    Connector control structure

funcs
    Pipeline control functions (optional)

.. _`drm_simple_display_pipe.description`:

Description
-----------

Simple display pipeline with plane, crtc and encoder collapsed into one
entity. It should be initialized by calling \ :c:func:`drm_simple_display_pipe_init`\ .

.. This file was automatic generated / don't edit.

