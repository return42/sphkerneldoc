.. -*- coding: utf-8; mode: rst -*-

==========
drm_crtc.h
==========

.. _`drm_framebuffer_funcs`:

struct drm_framebuffer_funcs
============================

.. c:type:: struct drm_framebuffer_funcs

    framebuffer hooks



Definition
----------

.. code-block:: c

  struct drm_framebuffer_funcs {
    void (* destroy) (struct drm_framebuffer *framebuffer);
    int (* create_handle) (struct drm_framebuffer *fb,struct drm_file *file_priv,unsigned int *handle);
    int (* dirty) (struct drm_framebuffer *framebuffer,struct drm_file *file_priv, unsigned flags,unsigned color, struct drm_clip_rect *clips,unsigned num_clips);
  };



Members
-------

:``destroy``:

    Clean up framebuffer resources, specifically also unreference the
    backing storage. The core guarantees to call this function for every
    framebuffer successfully created by ->:c:func:`fb_create` in
    :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`. Drivers must also call
    :c:func:`drm_framebuffer_cleanup` to release DRM core resources for this
    framebuffer.

:``create_handle``:

    Create a buffer handle in the driver-specific buffer manager (either
    GEM or TTM) valid for the passed-in struct :c:type:`struct drm_file <drm_file>`. This is used by
    the core to implement the GETFB IOCTL, which returns (for
    sufficiently priviledged user) also a native buffer handle. This can
    be used for seamless transitions between modesetting clients by
    copying the current screen contents to a private buffer and blending
    between that and the new contents.

    GEM based drivers should call :c:func:`drm_gem_handle_create` to create the
    handle.

    RETURNS:

    0 on success or a negative error code on failure.

:``dirty``:

    Optional callback for the dirty fb IOCTL.

    Userspace can notify the driver via this callback that an area of the
    framebuffer has changed and should be flushed to the display
    hardware. This can also be used internally, e.g. by the fbdev
    emulation, though that's not the case currently.

    See documentation in drm_mode.h for the struct drm_mode_fb_dirty_cmd
    for more information as all the semantics and arguments have a one to
    one mapping on this function.

    RETURNS:

    0 on success or a negative error code on failure.



.. _`drm_crtc_state`:

struct drm_crtc_state
=====================

.. c:type:: struct drm_crtc_state

    mutable CRTC state



Definition
----------

.. code-block:: c

  struct drm_crtc_state {
    struct drm_crtc * crtc;
    bool enable;
    bool active;
    bool planes_changed:1;
    bool mode_changed:1;
    bool active_changed:1;
    bool connectors_changed:1;
    bool color_mgmt_changed:1;
    u32 plane_mask;
    u32 connector_mask;
    u32 encoder_mask;
    u32 last_vblank_count;
    struct drm_display_mode adjusted_mode;
    struct drm_display_mode mode;
    struct drm_property_blob * degamma_lut;
    struct drm_property_blob * ctm;
    struct drm_property_blob * gamma_lut;
    struct drm_pending_vblank_event * event;
    struct drm_atomic_state * state;
  };



Members
-------

:``crtc``:
    backpointer to the CRTC

:``enable``:
    whether the CRTC should be enabled, gates all other state

:``active``:
    whether the CRTC is actively displaying (used for DPMS)

:``planes_changed``:
    planes on this crtc are updated

:``mode_changed``:
    crtc_state->mode or crtc_state->enable has been changed

:``active_changed``:
    crtc_state->active has been toggled.

:``connectors_changed``:
    connectors to this crtc have been updated

:``color_mgmt_changed``:
    color management properties have changed (degamma or
    gamma LUT or CSC matrix)

:``plane_mask``:
    bitmask of (1 << drm_plane_index(plane)) of attached planes

:``connector_mask``:
    bitmask of (1 << drm_connector_index(connector)) of attached connectors

:``encoder_mask``:
    bitmask of (1 << drm_encoder_index(encoder)) of attached encoders

:``last_vblank_count``:
    for helpers and drivers to capture the vblank of the
    update to ensure framebuffer cleanup isn't done too early

:``adjusted_mode``:
    for use by helpers and drivers to compute adjusted mode timings

:``mode``:
    current mode timings

:``degamma_lut``:
    Lookup table for converting framebuffer pixel data
    before apply the conversion matrix

:``ctm``:
    Transformation matrix

:``gamma_lut``:
    Lookup table for converting pixel data after the
    conversion matrix

:``event``:
    optional pointer to a DRM event to signal upon completion of the
    state update

:``state``:
    backpointer to global drm_atomic_state



Description
-----------

Note that the distinction between ``enable`` and ``active`` is rather subtile:
Flipping ``active`` while ``enable`` is set without changing anything else may
never return in a failure from the ->atomic_check callback. Userspace assumes
that a DPMS On will always succeed. In other words: ``enable`` controls resource
assignment, ``active`` controls the actual hardware state.


.. _`drm_crtc_funcs`:

struct drm_crtc_funcs
=====================

.. c:type:: struct drm_crtc_funcs

    control CRTCs for a given device



Definition
----------

.. code-block:: c

  struct drm_crtc_funcs {
    void (* reset) (struct drm_crtc *crtc);
    int (* cursor_set) (struct drm_crtc *crtc, struct drm_file *file_priv,uint32_t handle, uint32_t width, uint32_t height);
    int (* cursor_set2) (struct drm_crtc *crtc, struct drm_file *file_priv,uint32_t handle, uint32_t width, uint32_t height,int32_t hot_x, int32_t hot_y);
    int (* cursor_move) (struct drm_crtc *crtc, int x, int y);
    void (* gamma_set) (struct drm_crtc *crtc, u16 *r, u16 *g, u16 *b,uint32_t start, uint32_t size);
    void (* destroy) (struct drm_crtc *crtc);
    int (* set_config) (struct drm_mode_set *set);
    int (* page_flip) (struct drm_crtc *crtc,struct drm_framebuffer *fb,struct drm_pending_vblank_event *event,uint32_t flags);
    int (* set_property) (struct drm_crtc *crtc,struct drm_property *property, uint64_t val);
    struct drm_crtc_state *(* atomic_duplicate_state) (struct drm_crtc *crtc);
    void (* atomic_destroy_state) (struct drm_crtc *crtc,struct drm_crtc_state *state);
    int (* atomic_set_property) (struct drm_crtc *crtc,struct drm_crtc_state *state,struct drm_property *property,uint64_t val);
    int (* atomic_get_property) (struct drm_crtc *crtc,const struct drm_crtc_state *state,struct drm_property *property,uint64_t *val);
  };



Members
-------

:``reset``:

    Reset CRTC hardware and software state to off. This function isn't
    called by the core directly, only through :c:func:`drm_mode_config_reset`.
    It's not a helper hook only for historical reasons.

    Atomic drivers can use :c:func:`drm_atomic_helper_crtc_reset` to reset
    atomic state using this hook.

:``cursor_set``:

    Update the cursor image. The cursor position is relative to the CRTC
    and can be partially or fully outside of the visible area.

    Note that contrary to all other KMS functions the legacy cursor entry
    points don't take a framebuffer object, but instead take directly a
    raw buffer object id from the driver's buffer manager (which is
    either GEM or TTM for current drivers).

    This entry point is deprecated, drivers should instead implement
    universal plane support and register a proper cursor plane using
    :c:func:`drm_crtc_init_with_planes`.

    This callback is optional

    RETURNS:

    0 on success or a negative error code on failure.

:``cursor_set2``:

    Update the cursor image, including hotspot information. The hotspot
    must not affect the cursor position in CRTC coordinates, but is only
    meant as a hint for virtualized display hardware to coordinate the
    guests and hosts cursor position. The cursor hotspot is relative to
    the cursor image. Otherwise this works exactly like ``cursor_set``\ .

    This entry point is deprecated, drivers should instead implement
    universal plane support and register a proper cursor plane using
    :c:func:`drm_crtc_init_with_planes`.

    This callback is optional.

    RETURNS:

    0 on success or a negative error code on failure.

:``cursor_move``:

    Update the cursor position. The cursor does not need to be visible
    when this hook is called.

    This entry point is deprecated, drivers should instead implement
    universal plane support and register a proper cursor plane using
    :c:func:`drm_crtc_init_with_planes`.

    This callback is optional.

    RETURNS:

    0 on success or a negative error code on failure.

:``gamma_set``:

    Set gamma on the CRTC.

    This callback is optional.

    NOTE:

    Drivers that support gamma tables and also fbdev emulation through
    the provided helper library need to take care to fill out the gamma
    hooks for both. Currently there's a bit an unfortunate duplication
    going on, which should eventually be unified to just one set of
    hooks.

:``destroy``:

    Clean up plane resources. This is only called at driver unload time
    through :c:func:`drm_mode_config_cleanup` since a CRTC cannot be hotplugged
    in DRM.

:``set_config``:

    This is the main legacy entry point to change the modeset state on a
    CRTC. All the details of the desired configuration are passed in a
    struct :c:type:`struct drm_mode_set <drm_mode_set>` - see there for details.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_set_config` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

:``page_flip``:

    Legacy entry point to schedule a flip to the given framebuffer.

    Page flipping is a synchronization mechanism that replaces the frame
    buffer being scanned out by the CRTC with a new frame buffer during
    vertical blanking, avoiding tearing (except when requested otherwise
    through the DRM_MODE_PAGE_FLIP_ASYNC flag). When an application
    requests a page flip the DRM core verifies that the new frame buffer
    is large enough to be scanned out by the CRTC in the currently
    configured mode and then calls the CRTC ->:c:func:`page_flip` operation with a
    pointer to the new frame buffer.

    The driver must wait for any pending rendering to the new framebuffer
    to complete before executing the flip. It should also wait for any
    pending rendering from other drivers if the underlying buffer is a
    shared dma-buf.

    An application can request to be notified when the page flip has
    completed. The drm core will supply a struct :c:type:`struct drm_event <drm_event>` in the event
    parameter in this case. This can be handled by the
    :c:func:`drm_crtc_send_vblank_event` function, which the driver should call on
    the provided event upon completion of the flip. Note that if
    the driver supports vblank signalling and timestamping the vblank
    counters and timestamps must agree with the ones returned from page
    flip events. With the current vblank helper infrastructure this can
    be achieved by holding a vblank reference while the page flip is
    pending, acquired through :c:func:`drm_crtc_vblank_get` and released with
    :c:func:`drm_crtc_vblank_put`. Drivers are free to implement their own vblank
    counter and timestamp tracking though, e.g. if they have accurate
    timestamp registers in hardware.

    FIXME:

    Up to that point drivers need to manage events themselves and can use
    even->base.list freely for that. Specifically they need to ensure
    that they don't send out page flip (or vblank) events for which the
    corresponding drm file has been closed already. The drm core
    unfortunately does not (yet) take care of that. Therefore drivers
    currently must clean up and release pending events in their
    ->preclose driver function.

    This callback is optional.

    NOTE:

    Very early versions of the KMS ABI mandated that the driver must
    block (but not reject) any rendering to the old framebuffer until the
    flip operation has completed and the old framebuffer is no longer
    visible. This requirement has been lifted, and userspace is instead
    expected to request delivery of an event and wait with recycling old
    buffers until such has been received.

    RETURNS:

    0 on success or a negative error code on failure. Note that if a
    ->:c:func:`page_flip` operation is already pending the callback should return
    -EBUSY. Pageflips on a disabled CRTC (either by setting a NULL mode
    or just runtime disabled through DPMS respectively the new atomic
    "ACTIVE" state) should result in an -EINVAL error code. Note that
    :c:func:`drm_atomic_helper_page_flip` checks this already for atomic drivers.

:``set_property``:

    This is the legacy entry point to update a property attached to the
    CRTC.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_crtc_set_property` to implement this hook.

    This callback is optional if the driver does not support any legacy
    driver-private properties.

    RETURNS:

    0 on success or a negative error code on failure.

:``atomic_duplicate_state``:

    Duplicate the current atomic state for this CRTC and return it.
    The core and helpers gurantee that any atomic state duplicated with
    this hook and still owned by the caller (i.e. not transferred to the
    driver by calling ->:c:func:`atomic_commit` from struct
    :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`) will be cleaned up by calling the
    ``atomic_destroy_state`` hook in this structure.

    Atomic drivers which don't subclass struct :c:type:`struct drm_crtc <drm_crtc>` should use
    :c:func:`drm_atomic_helper_crtc_duplicate_state`. Drivers that subclass the
    state structure to extend it with driver-private state should use
    :c:func:`__drm_atomic_helper_crtc_duplicate_state` to make sure shared state is
    duplicated in a consistent fashion across drivers.

    It is an error to call this hook before crtc->state has been
    initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook must
    acquire a reference for each of them. The driver must release these
    references again in ``atomic_destroy_state``\ .

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

:``atomic_destroy_state``:

    Destroy a state duplicated with ``atomic_duplicate_state`` and release
    or unreference all resources it references

:``atomic_set_property``:

    Decode a driver-private property value and store the decoded value
    into the passed-in state structure. Since the atomic core decodes all
    standardized properties (even for extensions beyond the core set of
    properties which might not be implemented by all drivers) this
    requires drivers to subclass the state structure.

    Such driver-private properties should really only be implemented for
    truly hardware/vendor specific state. Instead it is preferred to
    standardize atomic extension and decode the properties used to expose
    such an extension in the core.

    Do not call this function directly, use
    :c:func:`drm_atomic_crtc_set_property` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic
    modesets, which can be aborted for any reason (including on
    userspace's request to just check whether a configuration would be
    possible). Drivers MUST NOT touch any persistent state (hardware or
    software) or data structures except the passed in ``state`` parameter.

    Also since userspace controls in which order properties are set this
    function must not do any input validation (since the state update is
    incomplete and hence likely inconsistent). Instead any such input
    validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't
    implemented by the driver (which should never happen, the core only
    asks for properties attached to this CRTC). No other validation is
    allowed by the driver. The core already checks that the property
    value is within the range (integer, valid enum value, ...) the driver
    set when registering the property.

:``atomic_get_property``:

    Reads out the decoded driver-private property. This is used to
    implement the GETCRTC IOCTL.

    Do not call this function directly, use
    :c:func:`drm_atomic_crtc_get_property` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the
    driver (which should never happen, the core only asks for
    properties attached to this CRTC).



Description
-----------


The drm_crtc_funcs structure is the central CRTC management structure
in the DRM.  Each CRTC controls one or more connectors (note that the name
CRTC is simply historical, a CRTC may control LVDS, VGA, DVI, TV out, etc.
connectors, not just CRTs).

Each driver is responsible for filling out this structure at startup time,
in addition to providing other modesetting features, like i2c and DDC
bus accessors.


.. _`drm_crtc`:

struct drm_crtc
===============

.. c:type:: struct drm_crtc

    central CRTC control structure



Definition
----------

.. code-block:: c

  struct drm_crtc {
    struct drm_device * dev;
    struct device_node * port;
    struct list_head head;
    struct drm_modeset_lock mutex;
    struct drm_mode_object base;
    struct drm_plane * primary;
    struct drm_plane * cursor;
    int cursor_x;
    int cursor_y;
    bool enabled;
    struct drm_display_mode mode;
    struct drm_display_mode hwmode;
    int x;
    int y;
    const struct drm_crtc_funcs * funcs;
    uint32_t gamma_size;
    uint16_t * gamma_store;
    const struct drm_crtc_helper_funcs * helper_private;
    struct drm_object_properties properties;
    struct drm_crtc_state * state;
    struct drm_modeset_acquire_ctx * acquire_ctx;
  };



Members
-------

:``dev``:
    parent DRM device

:``port``:
    OF node used by :c:func:`drm_of_find_possible_crtcs`

:``head``:
    list management

:``mutex``:
    per-CRTC locking

:``base``:
    base KMS object for ID tracking etc.

:``primary``:
    primary plane for this CRTC

:``cursor``:
    cursor plane for this CRTC

:``cursor_x``:
    current x position of the cursor, used for universal cursor planes

:``cursor_y``:
    current y position of the cursor, used for universal cursor planes

:``enabled``:
    is this CRTC enabled?

:``mode``:
    current mode timings

:``hwmode``:
    mode timings as programmed to hw regs

:``x``:
    x position on screen

:``y``:
    y position on screen

:``funcs``:
    CRTC control functions

:``gamma_size``:
    size of gamma ramp

:``gamma_store``:
    gamma ramp values

:``helper_private``:
    mid-layer private data

:``properties``:
    property tracking for this CRTC

:``state``:
    current atomic state for this CRTC

:``acquire_ctx``:
    per-CRTC implicit acquire context used by atomic drivers for
    legacy IOCTLs



Description
-----------

Each CRTC may have one or more connectors associated with it.  This structure
allows the CRTC to be controlled.


.. _`drm_connector_state`:

struct drm_connector_state
==========================

.. c:type:: struct drm_connector_state

    mutable connector state



Definition
----------

.. code-block:: c

  struct drm_connector_state {
    struct drm_connector * connector;
    struct drm_crtc * crtc;
    struct drm_encoder * best_encoder;
    struct drm_atomic_state * state;
  };



Members
-------

:``connector``:
    backpointer to the connector

:``crtc``:
    CRTC to connect connector to, NULL if disabled

:``best_encoder``:
    can be used by helpers and drivers to select the encoder

:``state``:
    backpointer to global drm_atomic_state



.. _`drm_connector_funcs`:

struct drm_connector_funcs
==========================

.. c:type:: struct drm_connector_funcs

    control connectors on a given device



Definition
----------

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
-------

:``dpms``:

    Legacy entry point to set the per-connector DPMS state. Legacy DPMS
    is exposed as a standard property on the connector, but diverted to
    this callback in the drm core. Note that atomic drivers don't
    implement the 4 level DPMS support on the connector any more, but
    instead only have an on/off "ACTIVE" property on the CRTC object.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_connector_dpms` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

:``reset``:

    Reset connector hardware and software state to off. This function isn't
    called by the core directly, only through :c:func:`drm_mode_config_reset`.
    It's not a helper hook only for historical reasons.

    Atomic drivers can use :c:func:`drm_atomic_helper_connector_reset` to reset
    atomic state using this hook.

:``detect``:

    Check to see if anything is attached to the connector. The parameter
    force is set to false whilst polling, true when checking the
    connector due to a user request. force can be used by the driver to
    avoid expensive, destructive operations during automated probing.

    FIXME:

    Note that this hook is only called by the probe helper. It's not in
    the helper library vtable purely for historical reasons. The only DRM
    core        entry point to probe connector state is ``fill_modes``\ .

    RETURNS:

    drm_connector_status indicating the connector's status.

:``force``:

    This function is called to update internal encoder state when the
    connector is forced to a certain state by userspace, either through
    the sysfs interfaces or on the kernel cmdline. In that case the
    ``detect`` callback isn't called.

    FIXME:

    Note that this hook is only called by the probe helper. It's not in
    the helper library vtable purely for historical reasons. The only DRM
    core        entry point to probe connector state is ``fill_modes``\ .

:``fill_modes``:

    Entry point for output detection and basic mode validation. The
    driver should reprobe the output if needed (e.g. when hotplug
    handling is unreliable), add all detected modes to connector->modes
    and filter out any the device can't support in any configuration. It
    also needs to filter out any modes wider or higher than the
    parameters max_width and max_height indicate.

    The drivers must also prune any modes no longer valid from
    connector->modes. Furthermore it must update connector->status and
    connector->edid.  If no EDID has been received for this output
    connector->edid must be NULL.

    Drivers using the probe helpers should use
    :c:func:`drm_helper_probe_single_connector_modes` or
    :c:func:`drm_helper_probe_single_connector_modes_nomerge` to implement this
    function.

    RETURNS:

    The number of modes detected and filled into connector->modes.

:``set_property``:

    This is the legacy entry point to update a property attached to the
    connector.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_connector_set_property` to implement this hook.

    This callback is optional if the driver does not support any legacy
    driver-private properties.

    RETURNS:

    0 on success or a negative error code on failure.

:``destroy``:

    Clean up connector resources. This is called at driver unload time
    through :c:func:`drm_mode_config_cleanup`. It can also be called at runtime
    when a connector is being hot-unplugged for drivers that support
    connector hotplugging (e.g. DisplayPort MST).

:``atomic_duplicate_state``:

    Duplicate the current atomic state for this connector and return it.
    The core and helpers gurantee that any atomic state duplicated with
    this hook and still owned by the caller (i.e. not transferred to the
    driver by calling ->:c:func:`atomic_commit` from struct
    :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`) will be cleaned up by calling the
    ``atomic_destroy_state`` hook in this structure.

    Atomic drivers which don't subclass struct :c:type:`struct drm_connector_state <drm_connector_state>` should use
    :c:func:`drm_atomic_helper_connector_duplicate_state`. Drivers that subclass the
    state structure to extend it with driver-private state should use
    :c:func:`__drm_atomic_helper_connector_duplicate_state` to make sure shared state is
    duplicated in a consistent fashion across drivers.

    It is an error to call this hook before connector->state has been
    initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook must
    acquire a reference for each of them. The driver must release these
    references again in ``atomic_destroy_state``\ .

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

:``atomic_destroy_state``:

    Destroy a state duplicated with ``atomic_duplicate_state`` and release
    or unreference all resources it references

:``atomic_set_property``:

    Decode a driver-private property value and store the decoded value
    into the passed-in state structure. Since the atomic core decodes all
    standardized properties (even for extensions beyond the core set of
    properties which might not be implemented by all drivers) this
    requires drivers to subclass the state structure.

    Such driver-private properties should really only be implemented for
    truly hardware/vendor specific state. Instead it is preferred to
    standardize atomic extension and decode the properties used to expose
    such an extension in the core.

    Do not call this function directly, use
    :c:func:`drm_atomic_connector_set_property` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic
    modesets, which can be aborted for any reason (including on
    userspace's request to just check whether a configuration would be
    possible). Drivers MUST NOT touch any persistent state (hardware or
    software) or data structures except the passed in ``state`` parameter.

    Also since userspace controls in which order properties are set this
    function must not do any input validation (since the state update is
    incomplete and hence likely inconsistent). Instead any such input
    validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't
    implemented by the driver (which shouldn't ever happen, the core only
    asks for properties attached to this connector). No other validation
    is allowed by the driver. The core already checks that the property
    value is within the range (integer, valid enum value, ...) the driver
    set when registering the property.

:``atomic_get_property``:

    Reads out the decoded driver-private property. This is used to
    implement the GETCONNECTOR IOCTL.

    Do not call this function directly, use
    :c:func:`drm_atomic_connector_get_property` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the
    driver (which shouldn't ever happen, the core only asks for
    properties attached to this connector).



Description
-----------


Each CRTC may have one or more connectors attached to it.  The functions
below allow the core DRM code to control connectors, enumerate available modes,
etc.


.. _`drm_encoder_funcs`:

struct drm_encoder_funcs
========================

.. c:type:: struct drm_encoder_funcs

    encoder controls



Definition
----------

.. code-block:: c

  struct drm_encoder_funcs {
    void (* reset) (struct drm_encoder *encoder);
    void (* destroy) (struct drm_encoder *encoder);
  };



Members
-------

:``reset``:

    Reset encoder hardware and software state to off. This function isn't
    called by the core directly, only through :c:func:`drm_mode_config_reset`.
    It's not a helper hook only for historical reasons.

:``destroy``:

    Clean up encoder resources. This is only called at driver unload time
    through :c:func:`drm_mode_config_cleanup` since an encoder cannot be
    hotplugged in DRM.



Description
-----------


Encoders sit between CRTCs and connectors.


.. _`drm_encoder`:

struct drm_encoder
==================

.. c:type:: struct drm_encoder

    central DRM encoder structure



Definition
----------

.. code-block:: c

  struct drm_encoder {
    struct drm_device * dev;
    struct list_head head;
    struct drm_mode_object base;
    char * name;
    int encoder_type;
    uint32_t possible_crtcs;
    uint32_t possible_clones;
    struct drm_crtc * crtc;
    struct drm_bridge * bridge;
    const struct drm_encoder_funcs * funcs;
    const struct drm_encoder_helper_funcs * helper_private;
  };



Members
-------

:``dev``:
    parent DRM device

:``head``:
    list management

:``base``:
    base KMS object

:``name``:
    encoder name

:``encoder_type``:
    one of the ``DRM_MODE_ENCODER_``\ <foo> types in drm_mode.h

:``possible_crtcs``:
    bitmask of potential CRTC bindings

:``possible_clones``:
    bitmask of potential sibling encoders for cloning

:``crtc``:
    currently bound CRTC

:``bridge``:
    bridge associated to the encoder

:``funcs``:
    control functions

:``helper_private``:
    mid-layer private data



Description
-----------

CRTCs drive pixels to encoders, which convert them into signals
appropriate for a given connector or set of connectors.


.. _`drm_connector`:

struct drm_connector
====================

.. c:type:: struct drm_connector

    central DRM connector control structure



Definition
----------

.. code-block:: c

  struct drm_connector {
    struct drm_device * dev;
    struct device * kdev;
    struct device_attribute * attr;
    struct list_head head;
    struct drm_mode_object base;
    char * name;
    int connector_type;
    int connector_type_id;
    bool interlace_allowed;
    bool doublescan_allowed;
    bool stereo_allowed;
    struct list_head modes;
    enum drm_connector_status status;
    struct list_head probed_modes;
    struct drm_display_info display_info;
    const struct drm_connector_funcs * funcs;
    struct drm_property_blob * edid_blob_ptr;
    struct drm_object_properties properties;
    struct drm_property_blob * path_blob_ptr;
    uint8_t polled;
    int dpms;
    const struct drm_connector_helper_funcs * helper_private;
    struct drm_cmdline_mode cmdline_mode;
    enum drm_connector_force force;
    bool override_edid;
    uint32_t encoder_ids[DRM_CONNECTOR_MAX_ENCODER];
    struct drm_encoder * encoder;
    uint8_t eld[MAX_ELD_BYTES];
    bool dvi_dual;
    int max_tmds_clock;
    bool latency_present[2];
    int video_latency[2];
    int audio_latency[2];
    int null_edid_counter;
    unsigned bad_edid_counter;
    bool edid_corrupt;
    struct dentry * debugfs_entry;
    struct drm_connector_state * state;
    bool has_tile;
    struct drm_tile_group * tile_group;
    bool tile_is_single_monitor;
    uint8_t num_h_tile;
    uint8_t num_v_tile;
    uint8_t tile_h_loc;
    uint8_t tile_v_loc;
    uint16_t tile_h_size;
    uint16_t tile_v_size;
  };



Members
-------

:``dev``:
    parent DRM device

:``kdev``:
    kernel device for sysfs attributes

:``attr``:
    sysfs attributes

:``head``:
    list management

:``base``:
    base KMS object

:``name``:
    connector name

:``connector_type``:
    one of the ``DRM_MODE_CONNECTOR_``\ <foo> types from drm_mode.h

:``connector_type_id``:
    index into connector type enum

:``interlace_allowed``:
    can this connector handle interlaced modes?

:``doublescan_allowed``:
    can this connector handle doublescan?

:``stereo_allowed``:
    can this connector handle stereo modes?

:``modes``:
    modes available on this connector (from :c:func:`fill_modes` + user)

:``status``:
    one of the drm_connector_status enums (connected, not, or unknown)

:``probed_modes``:
    list of modes derived directly from the display

:``display_info``:
    information about attached display (e.g. from EDID)

:``funcs``:
    connector control functions

:``edid_blob_ptr``:
    DRM property containing EDID if present

:``properties``:
    property tracking for this connector

:``path_blob_ptr``:
    DRM blob property data for the DP MST path property

:``polled``:
    a ``DRM_CONNECTOR_POLL_``\ <foo> value for core driven polling

:``dpms``:
    current dpms state

:``helper_private``:
    mid-layer private data

:``cmdline_mode``:
    mode line parsed from the kernel cmdline for this connector

:``force``:
    a ``DRM_FORCE_``\ <foo> state for forced mode sets

:``override_edid``:
    has the EDID been overwritten through debugfs for testing?

:``encoder_ids[DRM_CONNECTOR_MAX_ENCODER]``:
    valid encoders for this connector

:``encoder``:
    encoder driving this connector, if any

:``eld[MAX_ELD_BYTES]``:
    EDID-like data, if present

:``dvi_dual``:
    dual link DVI, if found

:``max_tmds_clock``:
    max clock rate, if found

:``latency_present[2]``:
    AV delay info from ELD, if found

:``video_latency[2]``:
    video latency info from ELD, if found

:``audio_latency[2]``:
    audio latency info from ELD, if found

:``null_edid_counter``:
    track sinks that give us all zeros for the EDID

:``bad_edid_counter``:
    track sinks that give us an EDID with invalid checksum

:``edid_corrupt``:
    indicates whether the last read EDID was corrupt

:``debugfs_entry``:
    debugfs directory for this connector

:``state``:
    current atomic state for this connector

:``has_tile``:
    is this connector connected to a tiled monitor

:``tile_group``:
    tile group for the connected monitor

:``tile_is_single_monitor``:
    whether the tile is one monitor housing

:``num_h_tile``:
    number of horizontal tiles in the tile group

:``num_v_tile``:
    number of vertical tiles in the tile group

:``tile_h_loc``:
    horizontal location of this tile

:``tile_v_loc``:
    vertical location of this tile

:``tile_h_size``:
    horizontal size of this tile.

:``tile_v_size``:
    vertical size of this tile.



Description
-----------

Each connector may be connected to one or more CRTCs, or may be clonable by
another connector if they can share a CRTC.  Each connector also has a specific
position in the broader display (referred to as a 'screen' though it could
span multiple monitors).


.. _`drm_plane_state`:

struct drm_plane_state
======================

.. c:type:: struct drm_plane_state

    mutable plane state



Definition
----------

.. code-block:: c

  struct drm_plane_state {
    struct drm_plane * plane;
    struct drm_crtc * crtc;
    struct drm_framebuffer * fb;
    struct fence * fence;
    int32_t crtc_x;
    int32_t crtc_y;
    uint32_t crtc_w;
    uint32_t crtc_h;
    uint32_t src_x;
    uint32_t src_y;
    uint32_t src_h;
    uint32_t src_w;
    struct drm_atomic_state * state;
  };



Members
-------

:``plane``:
    backpointer to the plane

:``crtc``:
    currently bound CRTC, NULL if disabled

:``fb``:
    currently bound framebuffer

:``fence``:
    optional fence to wait for before scanning out ``fb``

:``crtc_x``:
    left position of visible portion of plane on crtc

:``crtc_y``:
    upper position of visible portion of plane on crtc

:``crtc_w``:
    width of visible portion of plane on crtc

:``crtc_h``:
    height of visible portion of plane on crtc

:``src_x``:
    left position of visible portion of plane within
    plane (in 16.16)

:``src_y``:
    upper position of visible portion of plane within
    plane (in 16.16)

:``src_h``:
    height of visible portion of plane (in 16.16)

:``src_w``:
    width of visible portion of plane (in 16.16)

:``state``:
    backpointer to global drm_atomic_state



.. _`drm_plane_funcs`:

struct drm_plane_funcs
======================

.. c:type:: struct drm_plane_funcs

    driver plane control functions



Definition
----------

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
-------

:``update_plane``:

    This is the legacy entry point to enable and configure the plane for
    the given CRTC and framebuffer. It is never called to disable the
    plane, i.e. the passed-in crtc and fb paramters are never NULL.

    The source rectangle in frame buffer memory coordinates is given by
    the src_x, src_y, src_w and src_h parameters (as 16.16 fixed point
    values). Devices that don't support subpixel plane coordinates can
    ignore the fractional part.

    The destination rectangle in CRTC coordinates is given by the
    crtc_x, crtc_y, crtc_w and crtc_h parameters (as integer values).
    Devices scale the source rectangle to the destination rectangle. If
    scaling is not supported, and the source rectangle size doesn't match
    the destination rectangle size, the driver must return a
    -<errorname>EINVAL</errorname> error.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_update_plane` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

:``disable_plane``:

    This is the legacy entry point to disable the plane. The DRM core
    calls this method in response to a DRM_IOCTL_MODE_SETPLANE IOCTL call
    with the frame buffer ID set to 0.  Disabled planes must not be
    processed by the CRTC.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_disable_plane` to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

:``destroy``:

    Clean up plane resources. This is only called at driver unload time
    through :c:func:`drm_mode_config_cleanup` since a plane cannot be hotplugged
    in DRM.

:``reset``:

    Reset plane hardware and software state to off. This function isn't
    called by the core directly, only through :c:func:`drm_mode_config_reset`.
    It's not a helper hook only for historical reasons.

    Atomic drivers can use :c:func:`drm_atomic_helper_plane_reset` to reset
    atomic state using this hook.

:``set_property``:

    This is the legacy entry point to update a property attached to the
    plane.

    Drivers implementing atomic modeset should use
    :c:func:`drm_atomic_helper_plane_set_property` to implement this hook.

    This callback is optional if the driver does not support any legacy
    driver-private properties.

    RETURNS:

    0 on success or a negative error code on failure.

:``atomic_duplicate_state``:

    Duplicate the current atomic state for this plane and return it.
    The core and helpers gurantee that any atomic state duplicated with
    this hook and still owned by the caller (i.e. not transferred to the
    driver by calling ->:c:func:`atomic_commit` from struct
    :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`) will be cleaned up by calling the
    ``atomic_destroy_state`` hook in this structure.

    Atomic drivers which don't subclass struct :c:type:`struct drm_plane_state <drm_plane_state>` should use
    :c:func:`drm_atomic_helper_plane_duplicate_state`. Drivers that subclass the
    state structure to extend it with driver-private state should use
    :c:func:`__drm_atomic_helper_plane_duplicate_state` to make sure shared state is
    duplicated in a consistent fashion across drivers.

    It is an error to call this hook before plane->state has been
    initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook must
    acquire a reference for each of them. The driver must release these
    references again in ``atomic_destroy_state``\ .

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

:``atomic_destroy_state``:

    Destroy a state duplicated with ``atomic_duplicate_state`` and release
    or unreference all resources it references

:``atomic_set_property``:

    Decode a driver-private property value and store the decoded value
    into the passed-in state structure. Since the atomic core decodes all
    standardized properties (even for extensions beyond the core set of
    properties which might not be implemented by all drivers) this
    requires drivers to subclass the state structure.

    Such driver-private properties should really only be implemented for
    truly hardware/vendor specific state. Instead it is preferred to
    standardize atomic extension and decode the properties used to expose
    such an extension in the core.

    Do not call this function directly, use
    :c:func:`drm_atomic_plane_set_property` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic
    modesets, which can be aborted for any reason (including on
    userspace's request to just check whether a configuration would be
    possible). Drivers MUST NOT touch any persistent state (hardware or
    software) or data structures except the passed in ``state`` parameter.

    Also since userspace controls in which order properties are set this
    function must not do any input validation (since the state update is
    incomplete and hence likely inconsistent). Instead any such input
    validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't
    implemented by the driver (which shouldn't ever happen, the core only
    asks for properties attached to this plane). No other validation is
    allowed by the driver. The core already checks that the property
    value is within the range (integer, valid enum value, ...) the driver
    set when registering the property.

:``atomic_get_property``:

    Reads out the decoded driver-private property. This is used to
    implement the GETPLANE IOCTL.

    Do not call this function directly, use
    :c:func:`drm_atomic_plane_get_property` instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the
    driver (which should never happen, the core only asks for
    properties attached to this plane).



.. _`drm_plane`:

struct drm_plane
================

.. c:type:: struct drm_plane

    central DRM plane control structure



Definition
----------

.. code-block:: c

  struct drm_plane {
    struct drm_device * dev;
    struct list_head head;
    struct drm_mode_object base;
    uint32_t possible_crtcs;
    uint32_t * format_types;
    unsigned int format_count;
    bool format_default;
    struct drm_crtc * crtc;
    struct drm_framebuffer * fb;
    struct drm_framebuffer * old_fb;
    const struct drm_plane_funcs * funcs;
    struct drm_object_properties properties;
    enum drm_plane_type type;
    struct drm_plane_state * state;
  };



Members
-------

:``dev``:
    DRM device this plane belongs to

:``head``:
    for list management

:``base``:
    base mode object

:``possible_crtcs``:
    pipes this plane can be bound to

:``format_types``:
    array of formats supported by this plane

:``format_count``:
    number of formats supported

:``format_default``:
    driver hasn't supplied supported formats for the plane

:``crtc``:
    currently bound CRTC

:``fb``:
    currently bound fb

:``old_fb``:
    Temporary tracking of the old fb while a modeset is ongoing. Used by
    :c:func:`drm_mode_set_config_internal` to implement correct refcounting.

:``funcs``:
    helper functions

:``properties``:
    property tracking for this plane

:``type``:
    type of plane (overlay, primary, cursor)

:``state``:
    current atomic state for this plane



.. _`drm_bridge_funcs`:

struct drm_bridge_funcs
=======================

.. c:type:: struct drm_bridge_funcs

    drm_bridge control functions



Definition
----------

.. code-block:: c

  struct drm_bridge_funcs {
    int (* attach) (struct drm_bridge *bridge);
    bool (* mode_fixup) (struct drm_bridge *bridge,const struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
    void (* disable) (struct drm_bridge *bridge);
    void (* post_disable) (struct drm_bridge *bridge);
    void (* mode_set) (struct drm_bridge *bridge,struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
    void (* pre_enable) (struct drm_bridge *bridge);
    void (* enable) (struct drm_bridge *bridge);
  };



Members
-------

:``attach``:
    Called during drm_bridge_attach

:``mode_fixup``:

    This callback is used to validate and adjust a mode. The paramater
    mode is the display mode that should be fed to the next element in
    the display chain, either the final :c:type:`struct drm_connector <drm_connector>` or the next
    :c:type:`struct drm_bridge <drm_bridge>`. The parameter adjusted_mode is the input mode the bridge
    requires. It can be modified by this callback and does not need to
    match mode.

    This is the only hook that allows a bridge to reject a modeset. If
    this function passes all other callbacks must succeed for this
    configuration.

    NOTE:

    This function is called in the check phase of atomic modesets, which
    can be aborted for any reason (including on userspace's request to
    just check whether a configuration would be possible). Drivers MUST
    NOT touch any persistent state (hardware or software) or data
    structures except the passed in ``state`` parameter.

    RETURNS:

    True if an acceptable configuration is possible, false if the modeset
    operation should be rejected.

:``disable``:

    This callback should disable the bridge. It is called right before
    the preceding element in the display pipe is disabled. If the
    preceding element is a bridge this means it's called before that
    bridge's ->:c:func:`disable` function. If the preceding element is a
    :c:type:`struct drm_encoder <drm_encoder>` it's called right before the encoder's ->:c:func:`disable`,
    ->:c:func:`prepare` or ->:c:func:`dpms` hook from struct :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>`.

    The bridge can assume that the display pipe (i.e. clocks and timing
    signals) feeding it is still running when this callback is called.

    The disable callback is optional.

:``post_disable``:

    This callback should disable the bridge. It is called right after
    the preceding element in the display pipe is disabled. If the
    preceding element is a bridge this means it's called after that
    bridge's ->:c:func:`post_disable` function. If the preceding element is a
    :c:type:`struct drm_encoder <drm_encoder>` it's called right after the encoder's ->:c:func:`disable`,
    ->:c:func:`prepare` or ->:c:func:`dpms` hook from struct :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>`.

    The bridge must assume that the display pipe (i.e. clocks and timing
    singals) feeding it is no longer running when this callback is
    called.

    The post_disable callback is optional.

:``mode_set``:

    This callback should set the given mode on the bridge. It is called
    after the ->:c:func:`mode_set` callback for the preceding element in the
    display pipeline has been called already. The display pipe (i.e.
    clocks and timing signals) is off when this function is called.

:``pre_enable``:

    This callback should enable the bridge. It is called right before
    the preceding element in the display pipe is enabled. If the
    preceding element is a bridge this means it's called before that
    bridge's ->:c:func:`pre_enable` function. If the preceding element is a
    :c:type:`struct drm_encoder <drm_encoder>` it's called right before the encoder's ->:c:func:`enable`,
    ->:c:func:`commit` or ->:c:func:`dpms` hook from struct :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>`.

    The display pipe (i.e. clocks and timing signals) feeding this bridge
    will not yet be running when this callback is called. The bridge must
    not enable the display link feeding the next bridge in the chain (if
    there is one) when this callback is called.

    The pre_enable callback is optional.

:``enable``:

    This callback should enable the bridge. It is called right after
    the preceding element in the display pipe is enabled. If the
    preceding element is a bridge this means it's called after that
    bridge's ->:c:func:`enable` function. If the preceding element is a
    :c:type:`struct drm_encoder <drm_encoder>` it's called right after the encoder's ->:c:func:`enable`,
    ->:c:func:`commit` or ->:c:func:`dpms` hook from struct :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>`.

    The bridge can assume that the display pipe (i.e. clocks and timing
    signals) feeding it is running when this callback is called. This
    callback must enable the display link feeding the next bridge in the
    chain if there is one.

    The enable callback is optional.



.. _`drm_bridge`:

struct drm_bridge
=================

.. c:type:: struct drm_bridge

    central DRM bridge control structure



Definition
----------

.. code-block:: c

  struct drm_bridge {
    struct drm_device * dev;
    struct drm_encoder * encoder;
    struct drm_bridge * next;
    #ifdef CONFIG_OF
    struct device_node * of_node;
    #endif
    struct list_head list;
    const struct drm_bridge_funcs * funcs;
    void * driver_private;
  };



Members
-------

:``dev``:
    DRM device this bridge belongs to

:``encoder``:
    encoder to which this bridge is connected

:``next``:
    the next bridge in the encoder chain

:``of_node``:
    device node pointer to the bridge

:``list``:
    to keep track of all added bridges

:``funcs``:
    control functions

:``driver_private``:
    pointer to the bridge driver's internal context



.. _`drm_atomic_state`:

struct drm_atomic_state
=======================

.. c:type:: struct drm_atomic_state

    the global state object for atomic updates



Definition
----------

.. code-block:: c

  struct drm_atomic_state {
    struct drm_device * dev;
    bool allow_modeset:1;
    bool legacy_cursor_update:1;
    bool legacy_set_config:1;
    struct drm_plane ** planes;
    struct drm_plane_state ** plane_states;
    struct drm_crtc ** crtcs;
    struct drm_crtc_state ** crtc_states;
    int num_connector;
    struct drm_connector ** connectors;
    struct drm_connector_state ** connector_states;
    struct drm_modeset_acquire_ctx * acquire_ctx;
  };



Members
-------

:``dev``:
    parent DRM device

:``allow_modeset``:
    allow full modeset

:``legacy_cursor_update``:
    hint to enforce legacy cursor IOCTL semantics

:``legacy_set_config``:
    Disable conflicting encoders instead of failing with -EINVAL.

:``planes``:
    pointer to array of plane pointers

:``plane_states``:
    pointer to array of plane states pointers

:``crtcs``:
    pointer to array of CRTC pointers

:``crtc_states``:
    pointer to array of CRTC states pointers

:``num_connector``:
    size of the ``connectors`` and ``connector_states`` arrays

:``connectors``:
    pointer to array of connector pointers

:``connector_states``:
    pointer to array of connector states pointers

:``acquire_ctx``:
    acquire context for this atomic modeset state update



.. _`drm_mode_set`:

struct drm_mode_set
===================

.. c:type:: struct drm_mode_set

    new values for a CRTC config change



Definition
----------

.. code-block:: c

  struct drm_mode_set {
    struct drm_framebuffer * fb;
    struct drm_crtc * crtc;
    struct drm_display_mode * mode;
    uint32_t x;
    uint32_t y;
    struct drm_connector ** connectors;
    size_t num_connectors;
  };



Members
-------

:``fb``:
    framebuffer to use for new config

:``crtc``:
    CRTC whose configuration we're about to change

:``mode``:
    mode timings to use

:``x``:
    position of this CRTC relative to ``fb``

:``y``:
    position of this CRTC relative to ``fb``

:``connectors``:
    array of connectors to drive with this CRTC if possible

:``num_connectors``:
    size of ``connectors`` array



Description
-----------

Represents a single crtc the connectors that it drives with what mode
and from which framebuffer it scans out from.

This is used to set modes.


.. _`drm_mode_config_funcs`:

struct drm_mode_config_funcs
============================

.. c:type:: struct drm_mode_config_funcs

    basic driver provided mode setting functions



Definition
----------

.. code-block:: c

  struct drm_mode_config_funcs {
    struct drm_framebuffer *(* fb_create) (struct drm_device *dev,struct drm_file *file_priv,const struct drm_mode_fb_cmd2 *mode_cmd);
    void (* output_poll_changed) (struct drm_device *dev);
    int (* atomic_check) (struct drm_device *dev,struct drm_atomic_state *state);
    int (* atomic_commit) (struct drm_device *dev,struct drm_atomic_state *state,bool async);
    struct drm_atomic_state *(* atomic_state_alloc) (struct drm_device *dev);
    void (* atomic_state_clear) (struct drm_atomic_state *state);
    void (* atomic_state_free) (struct drm_atomic_state *state);
  };



Members
-------

:``fb_create``:

    Create a new framebuffer object. The core does basic checks on the
    requested metadata, but most of that is left to the driver. See
    struct :c:type:`struct drm_mode_fb_cmd2 <drm_mode_fb_cmd2>` for details.

    If the parameters are deemed valid and the backing storage objects in
    the underlying memory manager all exist, then the driver allocates
    a new :c:type:`struct drm_framebuffer <drm_framebuffer>` structure, subclassed to contain
    driver-specific information (like the internal native buffer object
    references). It also needs to fill out all relevant metadata, which
    should be done by calling :c:func:`drm_helper_mode_fill_fb_struct`.

    The initialization is finalized by calling :c:func:`drm_framebuffer_init`,
    which registers the framebuffer and makes it accessible to other
    threads.

    RETURNS:

    A new framebuffer with an initial reference count of 1 or a negative
    error code encoded with :c:func:`ERR_PTR`.

:``output_poll_changed``:

    Callback used by helpers to inform the driver of output configuration
    changes.

    Drivers implementing fbdev emulation with the helpers can call
    drm_fb_helper_hotplug_changed from this hook to inform the fbdev
    helper of output changes.

    FIXME:

    Except that there's no vtable for device-level helper callbacks
    there's no reason this is a core function.

:``atomic_check``:

    This is the only hook to validate an atomic modeset update. This
    function must reject any modeset and state changes which the hardware
    or driver doesn't support. This includes but is of course not limited
    to::

     - Checking that the modes, framebuffers, scaling and placement
       requirements and so on are within the limits of the hardware.

     - Checking that any hidden shared resources are not oversubscribed.
       This can be shared PLLs, shared lanes, overall memory bandwidth,
       display fifo space (where shared between planes or maybe even
       CRTCs).

     - Checking that virtualized resources exported to userspace are not
       oversubscribed. For various reasons it can make sense to expose
       more planes, crtcs or encoders than which are physically there. One
       example is dual-pipe operations (which generally should be hidden
       from userspace if when lockstepped in hardware, exposed otherwise),
       where a plane might need 1 hardware plane (if it's just on one
       pipe), 2 hardware planes (when it spans both pipes) or maybe even
       shared a hardware plane with a 2nd plane (if there's a compatible
       plane requested on the area handled by the other pipe).

     - Check that any transitional state is possible and that if
       requested, the update can indeed be done in the vblank period
       without temporarily disabling some functions.

     - Check any other constraints the driver or hardware might have.

     - This callback also needs to correctly fill out the :c:type:`struct drm_crtc_state <drm_crtc_state>`
       in this update to make sure that :c:func:`drm_atomic_crtc_needs_modeset`
       reflects the nature of the possible update and returns true if and
       only if the update cannot be applied without tearing within one
       vblank on that CRTC. The core uses that information to reject
       updates which require a full modeset (i.e. blanking the screen, or
       at least pausing updates for a substantial amount of time) if
       userspace has disallowed that in its request.

     - The driver also does not need to repeat basic input validation
       like done for the corresponding legacy entry points. The core does
       that before calling this hook.

    See the documentation of ``atomic_commit`` for an exhaustive list of
    error conditions which don't have to be checked at the
    ->:c:func:`atomic_check` stage?

    See the documentation for struct :c:type:`struct drm_atomic_state <drm_atomic_state>` for how exactly
    an atomic modeset update is described.

    Drivers using the atomic helpers can implement this hook using
    :c:func:`drm_atomic_helper_check`, or one of the exported sub-functions of
    it.

    RETURNS:

    0 on success or one of the below negative error codes:

     - -EINVAL, if any of the above constraints are violated.

     - -EDEADLK, when returned from an attempt to acquire an additional
       :c:type:`struct drm_modeset_lock <drm_modeset_lock>` through :c:func:`drm_modeset_lock`.

     - -ENOMEM, if allocating additional state sub-structures failed due
       to lack of memory.

     - -EINTR, -EAGAIN or -ERESTARTSYS, if the IOCTL should be restarted.
       This can either be due to a pending signal, or because the driver
       needs to completely bail out to recover from an exceptional
       situation like a GPU hang. From a userspace point all errors are
       treated equally.

:``atomic_commit``:

    This is the only hook to commit an atomic modeset update. The core
    guarantees that ``atomic_check`` has been called successfully before
    calling this function, and that nothing has been changed in the
    interim.

    See the documentation for struct :c:type:`struct drm_atomic_state <drm_atomic_state>` for how exactly
    an atomic modeset update is described.

    Drivers using the atomic helpers can implement this hook using
    :c:func:`drm_atomic_helper_commit`, or one of the exported sub-functions of
    it.

    Asynchronous commits (as indicated with the async parameter) must
    do any preparatory work which might result in an unsuccessful commit
    in the context of this callback. The only exceptions are hardware
    errors resulting in -EIO. But even in that case the driver must
    ensure that the display pipe is at least running, to avoid
    compositors crashing when pageflips don't work. Anything else,
    specifically committing the update to the hardware, should be done
    without blocking the caller. For updates which do not require a
    modeset this must be guaranteed.

    The driver must wait for any pending rendering to the new
    framebuffers to complete before executing the flip. It should also
    wait for any pending rendering from other drivers if the underlying
    buffer is a shared dma-buf. Asynchronous commits must not wait for
    rendering in the context of this callback.

    An application can request to be notified when the atomic commit has
    completed. These events are per-CRTC and can be distinguished by the
    CRTC index supplied in :c:type:`struct drm_event <drm_event>` to userspace.

    The drm core will supply a struct :c:type:`struct drm_event <drm_event>` in the event
    member of each CRTC's :c:type:`struct drm_crtc_state <drm_crtc_state>` structure. This can be handled by the
    :c:func:`drm_crtc_send_vblank_event` function, which the driver should call on
    the provided event upon completion of the atomic commit. Note that if
    the driver supports vblank signalling and timestamping the vblank
    counters and timestamps must agree with the ones returned from page
    flip events. With the current vblank helper infrastructure this can
    be achieved by holding a vblank reference while the page flip is
    pending, acquired through :c:func:`drm_crtc_vblank_get` and released with
    :c:func:`drm_crtc_vblank_put`. Drivers are free to implement their own vblank
    counter and timestamp tracking though, e.g. if they have accurate
    timestamp registers in hardware.

    NOTE:

    Drivers are not allowed to shut down any display pipe successfully
    enabled through an atomic commit on their own. Doing so can result in
    compositors crashing if a page flip is suddenly rejected because the
    pipe is off.

    RETURNS:

    0 on success or one of the below negative error codes:

     - -EBUSY, if an asynchronous updated is requested and there is
       an earlier updated pending. Drivers are allowed to support a queue
       of outstanding updates, but currently no driver supports that.
       Note that drivers must wait for preceding updates to complete if a
       synchronous update is requested, they are not allowed to fail the
       commit in that case.

     - -ENOMEM, if the driver failed to allocate memory. Specifically
       this can happen when trying to pin framebuffers, which must only
       be done when committing the state.

     - -ENOSPC, as a refinement of the more generic -ENOMEM to indicate
       that the driver has run out of vram, iommu space or similar GPU
       address space needed for framebuffer.

     - -EIO, if the hardware completely died.

     - -EINTR, -EAGAIN or -ERESTARTSYS, if the IOCTL should be restarted.
       This can either be due to a pending signal, or because the driver
       needs to completely bail out to recover from an exceptional
       situation like a GPU hang. From a userspace point of view all errors are
       treated equally.

    This list is exhaustive. Specifically this hook is not allowed to
    return -EINVAL (any invalid requests should be caught in
    ``atomic_check``\ ) or -EDEADLK (this function must not acquire
    additional modeset locks).

:``atomic_state_alloc``:

    This optional hook can be used by drivers that want to subclass struct
    :c:type:`struct drm_atomic_state <drm_atomic_state>` to be able to track their own driver-private global
    state easily. If this hook is implemented, drivers must also
    implement ``atomic_state_clear`` and ``atomic_state_free``\ .

    RETURNS:

    A new :c:type:`struct drm_atomic_state <drm_atomic_state>` on success or NULL on failure.

:``atomic_state_clear``:

    This hook must clear any driver private state duplicated into the
    passed-in :c:type:`struct drm_atomic_state <drm_atomic_state>`. This hook is called when the caller
    encountered a :c:type:`struct drm_modeset_lock <drm_modeset_lock>` deadlock and needs to drop all
    already acquired locks as part of the deadlock avoidance dance
    implemented in :c:func:`drm_modeset_lock_backoff`.

    Any duplicated state must be invalidated since a concurrent atomic
    update might change it, and the drm atomic interfaces always apply
    updates as relative changes to the current state.

    Drivers that implement this must call :c:func:`drm_atomic_state_default_clear`
    to clear common state.

:``atomic_state_free``:

    This hook needs driver private resources and the :c:type:`struct drm_atomic_state <drm_atomic_state>`
    itself. Note that the core first calls :c:func:`drm_atomic_state_clear` to
    avoid code duplicate between the clear and free hooks.

    Drivers that implement this must call :c:func:`drm_atomic_state_default_free`
    to release common resources.



Description
-----------


Some global (i.e. not per-CRTC, connector, etc) mode setting functions that
involve drivers.


.. _`drm_mode_config`:

struct drm_mode_config
======================

.. c:type:: struct drm_mode_config

    Mode configuration control structure



Definition
----------

.. code-block:: c

  struct drm_mode_config {
    struct mutex mutex;
    struct drm_modeset_lock connection_mutex;
    struct drm_modeset_acquire_ctx * acquire_ctx;
    struct mutex idr_mutex;
    struct idr crtc_idr;
    struct mutex fb_lock;
    int num_fb;
    struct list_head fb_list;
    int num_connector;
    struct list_head connector_list;
    int num_encoder;
    struct list_head encoder_list;
    int num_overlay_plane;
    int num_total_plane;
    struct list_head plane_list;
    int num_crtc;
    struct list_head crtc_list;
    struct list_head property_list;
    int min_width;
    int min_height;
    int max_width;
    int max_height;
    const struct drm_mode_config_funcs * funcs;
    resource_size_t fb_base;
    bool poll_enabled;
    bool poll_running;
    struct delayed_work output_poll_work;
    struct mutex blob_lock;
    struct list_head property_blob_list;
    struct drm_property * degamma_lut_property;
    struct drm_property * degamma_lut_size_property;
    struct drm_property * ctm_property;
    struct drm_property * gamma_lut_property;
    struct drm_property * gamma_lut_size_property;
    uint32_t preferred_depth;
    uint32_t prefer_shadow;
    bool async_page_flip;
    uint32_t cursor_width;
    uint32_t cursor_height;
  };



Members
-------

:``mutex``:
    mutex protecting KMS related lists and structures

:``connection_mutex``:
    ww mutex protecting connector state and routing

:``acquire_ctx``:
    global implicit acquire context used by atomic drivers for
    legacy IOCTLs

:``idr_mutex``:
    mutex for KMS ID allocation and management

:``crtc_idr``:
    main KMS ID tracking object

:``fb_lock``:
    mutex to protect fb state and lists

:``num_fb``:
    number of fbs available

:``fb_list``:
    list of framebuffers available

:``num_connector``:
    number of connectors on this device

:``connector_list``:
    list of connector objects

:``num_encoder``:
    number of encoders on this device

:``encoder_list``:
    list of encoder objects

:``num_overlay_plane``:
    number of overlay planes on this device

:``num_total_plane``:
    number of universal (i.e. with primary/curso) planes on this device

:``plane_list``:
    list of plane objects

:``num_crtc``:
    number of CRTCs on this device

:``crtc_list``:
    list of CRTC objects

:``property_list``:
    list of property objects

:``min_width``:
    minimum pixel width on this device

:``min_height``:
    minimum pixel height on this device

:``max_width``:
    maximum pixel width on this device

:``max_height``:
    maximum pixel height on this device

:``funcs``:
    core driver provided mode setting functions

:``fb_base``:
    base address of the framebuffer

:``poll_enabled``:
    track polling support for this device

:``poll_running``:
    track polling status for this device

:``output_poll_work``:
    delayed work for polling in process context

:``blob_lock``:
    mutex for blob property allocation and management
    @\*_property: core property tracking

:``property_blob_list``:
    list of all the blob property objects

:``degamma_lut_property``:
    LUT used to convert the framebuffer's colors to linear
    gamma

:``degamma_lut_size_property``:
    size of the degamma LUT as supported by the
    driver (read-only)

:``ctm_property``:
    Matrix used to convert colors after the lookup in the
    degamma LUT

:``gamma_lut_property``:
    LUT used to convert the colors, after the CSC matrix, to
    the gamma space of the connected screen (read-only)

:``gamma_lut_size_property``:
    size of the gamma LUT as supported by the driver

:``preferred_depth``:
    preferred RBG pixel depth, used by fb helpers

:``prefer_shadow``:
    hint to userspace to prefer shadow-fb rendering

:``async_page_flip``:
    does this device support async flips on the primary plane?

:``cursor_width``:
    hint to userspace for max cursor width

:``cursor_height``:
    hint to userspace for max cursor height



Description
-----------

Core mode resource tracking structure.  All CRTC, encoders, and connectors
enumerated by the driver are added here, as are global properties.  Some
global restrictions are also here, e.g. dimension restrictions.


.. _`drm_for_each_plane_mask`:

drm_for_each_plane_mask
=======================

.. c:function:: drm_for_each_plane_mask ( plane,  dev,  plane_mask)

    iterate over planes specified by bitmask

    :param plane:
        the loop cursor

    :param dev:
        the DRM device

    :param plane_mask:
        bitmask of plane indices


.. _`drm_for_each_plane_mask.description`:

Description
-----------

Iterate over all planes specified by bitmask.


.. _`drm_for_each_encoder_mask`:

drm_for_each_encoder_mask
=========================

.. c:function:: drm_for_each_encoder_mask ( encoder,  dev,  encoder_mask)

    iterate over encoders specified by bitmask

    :param encoder:
        the loop cursor

    :param dev:
        the DRM device

    :param encoder_mask:
        bitmask of encoder indices


.. _`drm_for_each_encoder_mask.description`:

Description
-----------

Iterate over all encoders specified by bitmask.


.. _`drm_crtc_mask`:

drm_crtc_mask
=============

.. c:function:: uint32_t drm_crtc_mask (struct drm_crtc *crtc)

    find the mask of a registered CRTC

    :param struct drm_crtc \*crtc:
        CRTC to find mask for


.. _`drm_crtc_mask.description`:

Description
-----------

Given a registered CRTC, return the mask bit of that CRTC for an
encoder's possible_crtcs field.


.. _`drm_encoder_crtc_ok`:

drm_encoder_crtc_ok
===================

.. c:function:: bool drm_encoder_crtc_ok (struct drm_encoder *encoder, struct drm_crtc *crtc)

    can a given crtc drive a given encoder?

    :param struct drm_encoder \*encoder:
        encoder to test

    :param struct drm_crtc \*crtc:
        crtc to test


.. _`drm_encoder_crtc_ok.description`:

Description
-----------

Return false if ``encoder`` can't be driven by ``crtc``\ , true otherwise.

