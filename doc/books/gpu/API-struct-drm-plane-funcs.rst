
.. _API-struct-drm-plane-funcs:

======================
struct drm_plane_funcs
======================

*man struct drm_plane_funcs(9)*

*4.6.0-rc1*

driver plane control functions


Synopsis
========

.. code-block:: c

    struct drm_plane_funcs {
      int (* update_plane) (struct drm_plane *plane,struct drm_crtc *crtc, struct drm_framebuffer *fb,int crtc_x, int crtc_y,unsigned int crtc_w, unsigned int crtc_h,uint32_t src_x, uint32_t src_y,uint32_t src_w, uint32_t src_h);
      int (* disable_plane) (struct drm_plane *plane);
      void (* destroy) (struct drm_plane *plane);
      void (* reset) (struct drm_plane *plane);
      int (* set_property) (struct drm_plane *plane,struct drm_property *property, uint64_t val);
      struct drm_plane_state *(* atomic_duplicate_state) (struct drm_plane *plane);
      void (* atomic_destroy_state) (struct drm_plane *plane,struct drm_plane_state *state);
      int (* atomic_set_property) (struct drm_plane *plane,struct drm_plane_state *state,struct drm_property *property,uint64_t val);
      int (* atomic_get_property) (struct drm_plane *plane,const struct drm_plane_state *state,struct drm_property *property,uint64_t *val);
    };


Members
=======

update_plane
    This is the legacy entry point to enable and configure the plane for the given CRTC and framebuffer. It is never called to disable the plane, i.e. the passed-in crtc and fb
    paramters are never NULL.

    The source rectangle in frame buffer memory coordinates is given by the src_x, src_y, src_w and src_h parameters (as 16.16 fixed point values). Devices that don't support
    subpixel plane coordinates can ignore the fractional part.

    The destination rectangle in CRTC coordinates is given by the crtc_x, crtc_y, crtc_w and crtc_h parameters (as integer values). Devices scale the source rectangle to the
    destination rectangle. If scaling is not supported, and the source rectangle size doesn't match the destination rectangle size, the driver must return a
    -<errorname>EINVAL</errorname> error.

    Drivers implementing atomic modeset should use ``drm_atomic_helper_update_plane`` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

disable_plane
    This is the legacy entry point to disable the plane. The DRM core calls this method in response to a DRM_IOCTL_MODE_SETPLANE IOCTL call with the frame buffer ID set to 0.
    Disabled planes must not be processed by the CRTC.

    Drivers implementing atomic modeset should use ``drm_atomic_helper_disable_plane`` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

destroy
    Clean up plane resources. This is only called at driver unload time through ``drm_mode_config_cleanup`` since a plane cannot be hotplugged in DRM.

reset
    Reset plane hardware and software state to off. This function isn't called by the core directly, only through ``drm_mode_config_reset``. It's not a helper hook only for
    historical reasons.

    Atomic drivers can use ``drm_atomic_helper_plane_reset`` to reset atomic state using this hook.

set_property
    This is the legacy entry point to update a property attached to the plane.

    Drivers implementing atomic modeset should use ``drm_atomic_helper_plane_set_property`` to implement this hook.

    This callback is optional if the driver does not support any legacy driver-private properties.

    RETURNS:

    0 on success or a negative error code on failure.

atomic_duplicate_state
    Duplicate the current atomic state for this plane and return it. The core and helpers gurantee that any atomic state duplicated with this hook and still owned by the caller
    (i.e. not transferred to the driver by calling ->``atomic_commit`` from struct ``drm_mode_config_funcs``) will be cleaned up by calling the ``atomic_destroy_state`` hook in
    this structure.

    Atomic drivers which don't subclass struct ``drm_plane_state`` should use ``drm_atomic_helper_plane_duplicate_state``. Drivers that subclass the state structure to extend it
    with driver-private state should use ``__drm_atomic_helper_plane_duplicate_state`` to make sure shared state is duplicated in a consistent fashion across drivers.

    It is an error to call this hook before plane->state has been initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook must acquire a reference for each of them. The driver must release these references again in
    ``atomic_destroy_state``.

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

atomic_destroy_state
    Destroy a state duplicated with ``atomic_duplicate_state`` and release or unreference all resources it references

atomic_set_property
    Decode a driver-private property value and store the decoded value into the passed-in state structure. Since the atomic core decodes all standardized properties (even for
    extensions beyond the core set of properties which might not be implemented by all drivers) this requires drivers to subclass the state structure.

    Such driver-private properties should really only be implemented for truly hardware/vendor specific state. Instead it is preferred to standardize atomic extension and decode
    the properties used to expose such an extension in the core.

    Do not call this function directly, use ``drm_atomic_plane_set_property`` instead.

    This callback is optional if the driver does not support any driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic modesets, which can be aborted for any reason (including on userspace's request to just check whether a
    configuration would be possible). Drivers MUST NOT touch any persistent state (hardware or software) or data structures except the passed in ``state`` parameter.

    Also since userspace controls in which order properties are set this function must not do any input validation (since the state update is incomplete and hence likely
    inconsistent). Instead any such input validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't implemented by the driver (which shouldn't ever happen, the core only asks for properties attached to this
    plane). No other validation is allowed by the driver. The core already checks that the property value is within the range (integer, valid enum value, ...) the driver set when
    registering the property.

atomic_get_property
    Reads out the decoded driver-private property. This is used to implement the GETPLANE IOCTL.

    Do not call this function directly, use ``drm_atomic_plane_get_property`` instead.

    This callback is optional if the driver does not support any driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the driver (which should never happen, the core only asks for properties attached to this plane).
