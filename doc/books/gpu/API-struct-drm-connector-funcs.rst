
.. _API-struct-drm-connector-funcs:

==========================
struct drm_connector_funcs
==========================

*man struct drm_connector_funcs(9)*

*4.6.0-rc1*

control connectors on a given device


Synopsis
========

.. code-block:: c

    struct drm_connector_funcs {
      int (* dpms) (struct drm_connector *connector, int mode);
      void (* reset) (struct drm_connector *connector);
      enum drm_connector_status (* detect) (struct drm_connector *connector,bool force);
      void (* force) (struct drm_connector *connector);
      int (* fill_modes) (struct drm_connector *connector, uint32_t max_width, uint32_t max_height);
      int (* set_property) (struct drm_connector *connector, struct drm_property *property,uint64_t val);
      void (* destroy) (struct drm_connector *connector);
      struct drm_connector_state *(* atomic_duplicate_state) (struct drm_connector *connector);
      void (* atomic_destroy_state) (struct drm_connector *connector,struct drm_connector_state *state);
      int (* atomic_set_property) (struct drm_connector *connector,struct drm_connector_state *state,struct drm_property *property,uint64_t val);
      int (* atomic_get_property) (struct drm_connector *connector,const struct drm_connector_state *state,struct drm_property *property,uint64_t *val);
    };


Members
=======

dpms
    Legacy entry point to set the per-connector DPMS state. Legacy DPMS is exposed as a standard property on the connector, but diverted to this callback in the drm core. Note that
    atomic drivers don't implement the 4 level DPMS support on the connector any more, but instead only have an on/off “ACTIVE” property on the CRTC object.

    Drivers implementing atomic modeset should use ``drm_atomic_helper_connector_dpms`` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

reset
    Reset connector hardware and software state to off. This function isn't called by the core directly, only through ``drm_mode_config_reset``. It's not a helper hook only for
    historical reasons.

    Atomic drivers can use ``drm_atomic_helper_connector_reset`` to reset atomic state using this hook.

detect
    Check to see if anything is attached to the connector. The parameter force is set to false whilst polling, true when checking the connector due to a user request. force can be
    used by the driver to avoid expensive, destructive operations during automated probing.

    FIXME:

    Note that this hook is only called by the probe helper. It's not in the helper library vtable purely for historical reasons. The only DRM core entry point to probe connector
    state is ``fill_modes``.

    RETURNS:

    drm_connector_status indicating the connector's status.

force
    This function is called to update internal encoder state when the connector is forced to a certain state by userspace, either through the sysfs interfaces or on the kernel
    cmdline. In that case the ``detect`` callback isn't called.

    FIXME:

    Note that this hook is only called by the probe helper. It's not in the helper library vtable purely for historical reasons. The only DRM core entry point to probe connector
    state is ``fill_modes``.

fill_modes
    Entry point for output detection and basic mode validation. The driver should reprobe the output if needed (e.g. when hotplug handling is unreliable), add all detected modes to
    connector->modes and filter out any the device can't support in any configuration. It also needs to filter out any modes wider or higher than the parameters max_width and
    max_height indicate.

    The drivers must also prune any modes no longer valid from connector->modes. Furthermore it must update connector->status and connector->edid. If no EDID has been received for
    this output connector->edid must be NULL.

    Drivers using the probe helpers should use ``drm_helper_probe_single_connector_modes`` or ``drm_helper_probe_single_connector_modes_nomerge`` to implement this function.

    RETURNS:

    The number of modes detected and filled into connector->modes.

set_property
    This is the legacy entry point to update a property attached to the connector.

    Drivers implementing atomic modeset should use ``drm_atomic_helper_connector_set_property`` to implement this hook.

    This callback is optional if the driver does not support any legacy driver-private properties.

    RETURNS:

    0 on success or a negative error code on failure.

destroy
    Clean up connector resources. This is called at driver unload time through ``drm_mode_config_cleanup``. It can also be called at runtime when a connector is being hot-unplugged
    for drivers that support connector hotplugging (e.g. DisplayPort MST).

atomic_duplicate_state
    Duplicate the current atomic state for this connector and return it. The core and helpers gurantee that any atomic state duplicated with this hook and still owned by the caller
    (i.e. not transferred to the driver by calling ->``atomic_commit`` from struct ``drm_mode_config_funcs``) will be cleaned up by calling the ``atomic_destroy_state`` hook in
    this structure.

    Atomic drivers which don't subclass struct ``drm_connector_state`` should use ``drm_atomic_helper_connector_duplicate_state``. Drivers that subclass the state structure to
    extend it with driver-private state should use ``__drm_atomic_helper_connector_duplicate_state`` to make sure shared state is duplicated in a consistent fashion across drivers.

    It is an error to call this hook before connector->state has been initialized correctly.

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

    Do not call this function directly, use ``drm_atomic_connector_set_property`` instead.

    This callback is optional if the driver does not support any driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic modesets, which can be aborted for any reason (including on userspace's request to just check whether a
    configuration would be possible). Drivers MUST NOT touch any persistent state (hardware or software) or data structures except the passed in ``state`` parameter.

    Also since userspace controls in which order properties are set this function must not do any input validation (since the state update is incomplete and hence likely
    inconsistent). Instead any such input validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't implemented by the driver (which shouldn't ever happen, the core only asks for properties attached to this
    connector). No other validation is allowed by the driver. The core already checks that the property value is within the range (integer, valid enum value, ...) the driver set
    when registering the property.

atomic_get_property
    Reads out the decoded driver-private property. This is used to implement the GETCONNECTOR IOCTL.

    Do not call this function directly, use ``drm_atomic_connector_get_property`` instead.

    This callback is optional if the driver does not support any driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the driver (which shouldn't ever happen, the core only asks for properties attached to this connector).


Description
===========

Each CRTC may have one or more connectors attached to it. The functions below allow the core DRM code to control connectors, enumerate available modes, etc.
