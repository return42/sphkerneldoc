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
        void (*enable)(struct drm_simple_display_pipe *pipe,struct drm_crtc_state *crtc_state);
        void (*disable)(struct drm_simple_display_pipe *pipe);
        int (*check)(struct drm_simple_display_pipe *pipe,struct drm_plane_state *plane_state,struct drm_crtc_state *crtc_state);
        void (*update)(struct drm_simple_display_pipe *pipe,struct drm_plane_state *old_plane_state);
        int (*prepare_fb)(struct drm_simple_display_pipe *pipe,struct drm_plane_state *plane_state);
        void (*cleanup_fb)(struct drm_simple_display_pipe *pipe,struct drm_plane_state *plane_state);
    }

.. _`drm_simple_display_pipe_funcs.members`:

Members
-------

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

cleanup_fb

    Optional, called by \ :c:type:`drm_plane_helper_funcs.cleanup_fb <drm_plane_helper_funcs>`\ .  Please read
    the documentation for the \ :c:type:`drm_plane_helper_funcs.cleanup_fb <drm_plane_helper_funcs>`\  hook for
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

