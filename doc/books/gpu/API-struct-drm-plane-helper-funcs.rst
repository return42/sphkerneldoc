
.. _API-struct-drm-plane-helper-funcs:

=============================
struct drm_plane_helper_funcs
=============================

*man struct drm_plane_helper_funcs(9)*

*4.6.0-rc1*

helper operations for planes


Synopsis
========

.. code-block:: c

    struct drm_plane_helper_funcs {
      int (* prepare_fb) (struct drm_plane *plane,const struct drm_plane_state *new_state);
      void (* cleanup_fb) (struct drm_plane *plane,const struct drm_plane_state *old_state);
      int (* atomic_check) (struct drm_plane *plane,struct drm_plane_state *state);
      void (* atomic_update) (struct drm_plane *plane,struct drm_plane_state *old_state);
      void (* atomic_disable) (struct drm_plane *plane,struct drm_plane_state *old_state);
    };


Members
=======

prepare_fb
    This hook is to prepare a framebuffer for scanout by e.g. pinning it's backing storage or relocating it into a contiguous block of VRAM. Other possible preparatory work
    includes flushing caches.

    This function must not block for outstanding rendering, since it is called in the context of the atomic IOCTL even for async commits to be able to return any errors to
    userspace. Instead the recommended way is to fill out the fence member of the passed-in ``drm_plane_state``. If the driver doesn't support native fences then equivalent
    functionality should be implemented through private members in the plane structure.

    The helpers will call ``cleanup_fb`` with matching arguments for every successful call to this hook.

    This callback is used by the atomic modeset helpers and by the transitional plane helpers, but it is optional.

    RETURNS:

    0 on success or one of the following negative error codes allowed by the atomic_commit hook in ``drm_mode_config_funcs``. When using helpers this callback is the only one
    which can fail an atomic commit, everything else must complete successfully.

cleanup_fb
    This hook is called to clean up any resources allocated for the given framebuffer and plane configuration in ``prepare_fb``.

    This callback is used by the atomic modeset helpers and by the transitional plane helpers, but it is optional.

atomic_check
    Drivers should check plane specific constraints in this hook.

    When using ``drm_atomic_helper_check_planes`` plane's ->``atomic_check`` hooks are called before the ones for CRTCs, which allows drivers to request shared resources that the
    CRTC controls here. For more complicated dependencies the driver can call the provided check helpers multiple times until the computed state has a final configuration and
    everything has been checked.

    This function is also allowed to inspect any other object's state and can add more state objects to the atomic commit if needed. Care must be taken though to ensure that state
    check\ ``compute`` functions for these added states are all called, and derived state in other objects all updated. Again the recommendation is to just call check helpers until
    a maximal configuration is reached.

    This callback is used by the atomic modeset helpers and by the transitional plane helpers, but it is optional.

    NOTE:

    This function is called in the check phase of an atomic update. The driver is not allowed to change anything outside of the free-standing state objects passed-in or assembled
    in the overall ``drm_atomic_state`` update tracking structure.

    RETURNS:

    0 on success, -EINVAL if the state or the transition can't be supported, -ENOMEM on memory allocation failure and -EDEADLK if an attempt to obtain another state object ran into
    a ``drm_modeset_lock`` deadlock.

atomic_update
    Drivers should use this function to update the plane state. This hook is called in-between the ->``atomic_begin`` and ->``atomic_flush`` of ``drm_crtc_helper_funcs``.

    Note that the power state of the display pipe when this function is called depends upon the exact helpers and calling sequence the driver has picked. See
    ``drm_atomic_commit_planes`` for a discussion of the tradeoffs and variants of plane commit helpers.

    This callback is used by the atomic modeset helpers and by the transitional plane helpers, but it is optional.

atomic_disable
    Drivers should use this function to unconditionally disable a plane. This hook is called in-between the ->``atomic_begin`` and ->``atomic_flush`` of ``drm_crtc_helper_funcs``.
    It is an alternative to ``atomic_update``, which will be called for disabling planes, too, if the ``atomic_disable`` hook isn't implemented.

    This hook is also useful to disable planes in preparation of a modeset, by calling ``drm_atomic_helper_disable_planes_on_crtc`` from the ->``disable`` hook in
    ``drm_crtc_helper_funcs``.

    Note that the power state of the display pipe when this function is called depends upon the exact helpers and calling sequence the driver has picked. See
    ``drm_atomic_commit_planes`` for a discussion of the tradeoffs and variants of plane commit helpers.

    This callback is used by the atomic modeset helpers and by the transitional plane helpers, but it is optional.


Description
===========

These functions are used by the atomic helpers and by the transitional plane helpers.
