.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_connector.h

.. _`drm_connector_status`:

enum drm_connector_status
=========================

.. c:type:: enum drm_connector_status

    status for a \ :c:type:`struct drm_connector <drm_connector>`\ 

.. _`drm_connector_status.definition`:

Definition
----------

.. code-block:: c

    enum drm_connector_status {
        connector_status_connected,
        connector_status_disconnected,
        connector_status_unknown
    };

.. _`drm_connector_status.constants`:

Constants
---------

connector_status_connected
    The connector is definitely connected toa sink device, and can be enabled.

connector_status_disconnected
    The connector isn't connected to asink device which can be autodetect. For digital outputs like DP or
    HDMI (which can be realiable probed) this means there's really
    nothing there. It is driver-dependent whether a connector with this
    status can be lit up or not.

connector_status_unknown
    The connector's status could not bereliably detected. This happens when probing would either cause
    flicker (like load-detection when the connector is in use), or when a
    hardware resource isn't available (like when load-detection needs a
    free CRTC). It should be possible to light up the connector with one
    of the listed fallback modes. For default configuration userspace
    should only try to light up connectors with unknown status when
    there's not connector with \ ``connector_status_connected``\ .

.. _`drm_connector_status.description`:

Description
-----------

This enum is used to track the connector status. There are no separate
#defines for the uapi!

.. _`drm_connector_registration_state`:

enum drm_connector_registration_state
=====================================

.. c:type:: enum drm_connector_registration_state

    userspace registration status for a \ :c:type:`struct drm_connector <drm_connector>`\ 

.. _`drm_connector_registration_state.definition`:

Definition
----------

.. code-block:: c

    enum drm_connector_registration_state {
        DRM_CONNECTOR_INITIALIZING,
        DRM_CONNECTOR_REGISTERED,
        DRM_CONNECTOR_UNREGISTERED
    };

.. _`drm_connector_registration_state.constants`:

Constants
---------

DRM_CONNECTOR_INITIALIZING
    The connector has just been created,but has yet to be exposed to userspace. There should be no
    additional restrictions to how the state of this connector may be
    modified.

DRM_CONNECTOR_REGISTERED
    The connector has been fully initializedand registered with sysfs, as such it has been exposed to
    userspace. There should be no additional restrictions to how the
    state of this connector may be modified.

DRM_CONNECTOR_UNREGISTERED
    The connector has either been exposedto userspace and has since been unregistered and removed from
    userspace, or the connector was unregistered before it had a chance
    to be exposed to userspace (e.g. still in the
    \ ``DRM_CONNECTOR_INITIALIZING``\  state). When a connector is
    unregistered, there are additional restrictions to how its state
    may be modified:

    - An unregistered connector may only have its DPMS changed from
      On->Off. Once DPMS is changed to Off, it may not be switched back
      to On.
    - Modesets are not allowed on unregistered connectors, unless they
      would result in disabling its assigned CRTCs. This means
      disabling a CRTC on an unregistered connector is OK, but enabling
      one is not.
    - Removing a CRTC from an unregistered connector is OK, but new
      CRTCs may never be assigned to an unregistered connector.

.. _`drm_connector_registration_state.description`:

Description
-----------

This enum is used to track the status of initializing a connector and
registering it with userspace, so that DRM can prevent bogus modesets on
connectors that no longer exist.

.. _`drm_scrambling`:

struct drm_scrambling
=====================

.. c:type:: struct drm_scrambling

    sink's scrambling support.

.. _`drm_scrambling.definition`:

Definition
----------

.. code-block:: c

    struct drm_scrambling {
        bool supported;
        bool low_rates;
    }

.. _`drm_scrambling.members`:

Members
-------

supported
    scrambling supported for rates > 340 Mhz.

low_rates
    scrambling supported for rates <= 340 Mhz.

.. _`drm_hdmi_info`:

struct drm_hdmi_info
====================

.. c:type:: struct drm_hdmi_info

    runtime information about the connected HDMI sink

.. _`drm_hdmi_info.definition`:

Definition
----------

.. code-block:: c

    struct drm_hdmi_info {
        struct drm_scdc scdc;
        unsigned long y420_vdb_modes[BITS_TO_LONGS(128)];
        unsigned long y420_cmdb_modes[BITS_TO_LONGS(128)];
        u64 y420_cmdb_map;
        u8 y420_dc_modes;
    }

.. _`drm_hdmi_info.members`:

Members
-------

scdc
    sink's scdc support and capabilities

y420_vdb_modes
    bitmap of modes which can support ycbcr420output only (not normal RGB/YCBCR444/422 outputs). There are total
    107 VICs defined by CEA-861-F spec, so the size is 128 bits to map
    upto 128 VICs;

y420_cmdb_modes
    bitmap of modes which can support ycbcr420output also, along with normal HDMI outputs. There are total 107
    VICs defined by CEA-861-F spec, so the size is 128 bits to map upto
    128 VICs;

y420_cmdb_map
    bitmap of SVD index, to extraxt vcb modes

y420_dc_modes
    bitmap of deep color support index

.. _`drm_hdmi_info.description`:

Description
-----------

Describes if a given display supports advanced HDMI 2.0 features.
This information is available in CEA-861-F extension blocks (like HF-VSDB).

.. _`drm_link_status`:

enum drm_link_status
====================

.. c:type:: enum drm_link_status

    connector's link_status property value

.. _`drm_link_status.definition`:

Definition
----------

.. code-block:: c

    enum drm_link_status {
        DRM_LINK_STATUS_GOOD,
        DRM_LINK_STATUS_BAD
    };

.. _`drm_link_status.constants`:

Constants
---------

DRM_LINK_STATUS_GOOD
    DP Link is Good as a result of successful
    link training

DRM_LINK_STATUS_BAD
    DP Link is BAD as a result of link training
    failure

.. _`drm_link_status.description`:

Description
-----------

This enum is used as the connector's link status property value.
It is set to the values defined in uapi.

.. _`drm_panel_orientation`:

enum drm_panel_orientation
==========================

.. c:type:: enum drm_panel_orientation

    panel_orientation info for \ :c:type:`struct drm_display_info <drm_display_info>`\ 

.. _`drm_panel_orientation.definition`:

Definition
----------

.. code-block:: c

    enum drm_panel_orientation {
        DRM_MODE_PANEL_ORIENTATION_UNKNOWN,
        DRM_MODE_PANEL_ORIENTATION_NORMAL,
        DRM_MODE_PANEL_ORIENTATION_BOTTOM_UP,
        DRM_MODE_PANEL_ORIENTATION_LEFT_UP,
        DRM_MODE_PANEL_ORIENTATION_RIGHT_UP
    };

.. _`drm_panel_orientation.constants`:

Constants
---------

DRM_MODE_PANEL_ORIENTATION_UNKNOWN
    The drm driver has not provided any
    panel orientation information (normal
    for non panels) in this case the "panel
    orientation" connector prop will not be
    attached.

DRM_MODE_PANEL_ORIENTATION_NORMAL
    The top side of the panel matches the
    top side of the device's casing.

DRM_MODE_PANEL_ORIENTATION_BOTTOM_UP
    The top side of the panel matches the
    bottom side of the device's casing, iow
    the panel is mounted upside-down.

DRM_MODE_PANEL_ORIENTATION_LEFT_UP
    The left side of the panel matches the
    top side of the device's casing.

DRM_MODE_PANEL_ORIENTATION_RIGHT_UP
    The right side of the panel matches the
    top side of the device's casing.

.. _`drm_panel_orientation.description`:

Description
-----------

This enum is used to track the (LCD) panel orientation. There are no
separate #defines for the uapi!

.. _`drm_display_info`:

struct drm_display_info
=======================

.. c:type:: struct drm_display_info

    runtime data about the connected sink

.. _`drm_display_info.definition`:

Definition
----------

.. code-block:: c

    struct drm_display_info {
        char name[DRM_DISPLAY_INFO_LEN];
        unsigned int width_mm;
        unsigned int height_mm;
        unsigned int pixel_clock;
        unsigned int bpc;
        enum subpixel_order subpixel_order;
    #define DRM_COLOR_FORMAT_RGB444 (1<<0)
    #define DRM_COLOR_FORMAT_YCRCB444 (1<<1)
    #define DRM_COLOR_FORMAT_YCRCB422 (1<<2)
    #define DRM_COLOR_FORMAT_YCRCB420 (1<<3)
        int panel_orientation;
        u32 color_formats;
        const u32 *bus_formats;
        unsigned int num_bus_formats;
    #define DRM_BUS_FLAG_DE_LOW (1<<0)
    #define DRM_BUS_FLAG_DE_HIGH (1<<1)
    #define DRM_BUS_FLAG_PIXDATA_POSEDGE (1<<2)
    #define DRM_BUS_FLAG_PIXDATA_NEGEDGE (1<<3)
    #define DRM_BUS_FLAG_DATA_MSB_TO_LSB (1<<4)
    #define DRM_BUS_FLAG_DATA_LSB_TO_MSB (1<<5)
    #define DRM_BUS_FLAG_SYNC_POSEDGE (1<<6)
    #define DRM_BUS_FLAG_SYNC_NEGEDGE (1<<7)
        u32 bus_flags;
        int max_tmds_clock;
        bool dvi_dual;
        bool has_hdmi_infoframe;
        u8 edid_hdmi_dc_modes;
        u8 cea_rev;
        struct drm_hdmi_info hdmi;
        bool non_desktop;
    }

.. _`drm_display_info.members`:

Members
-------

name
    Name of the display.

width_mm
    Physical width in mm.

height_mm
    Physical height in mm.

pixel_clock
    Maximum pixel clock supported by the sink, in units of100Hz. This mismatches the clock in \ :c:type:`struct drm_display_mode <drm_display_mode>`\  (which is in
    kHZ), because that's what the EDID uses as base unit.

bpc
    Maximum bits per color channel. Used by HDMI and DP outputs.

subpixel_order
    Subpixel order of LCD panels.

panel_orientation
    Read only connector property for built-in panels,indicating the orientation of the panel vs the device's casing.
    \ :c:func:`drm_connector_init`\  sets this to DRM_MODE_PANEL_ORIENTATION_UNKNOWN.
    When not UNKNOWN this gets used by the drm_fb_helpers to rotate the
    fb to compensate and gets exported as prop to userspace.

color_formats
    HDMI Color formats, selects between RGB and YCrCbmodes. Used DRM_COLOR_FORMAT\_ defines, which are _not_ the same ones
    as used to describe the pixel format in framebuffers, and also don't
    match the formats in \ ``bus_formats``\  which are shared with v4l.

bus_formats
    Pixel data format on the wire, somewhat redundant with@color_formats. Array of size \ ``num_bus_formats``\  encoded using
    MEDIA_BUS_FMT\_ defines shared with v4l and media drivers.

num_bus_formats
    Size of \ ``bus_formats``\  array.

bus_flags
    Additional information (like pixel signal polarity) forthe pixel data on the bus, using DRM_BUS_FLAGS\_ defines.

max_tmds_clock
    Maximum TMDS clock rate supported by thesink in kHz. 0 means undefined.

dvi_dual
    Dual-link DVI sink?

has_hdmi_infoframe
    Does the sink support the HDMI infoframe?

edid_hdmi_dc_modes
    Mask of supported hdmi deep color modes. Evenmore stuff redundant with \ ``bus_formats``\ .

cea_rev
    CEA revision of the HDMI sink.

hdmi
    advance features of a HDMI sink.

non_desktop
    Non desktop display (HMD).

.. _`drm_display_info.description`:

Description
-----------

Describes a given display (e.g. CRT or flat panel) and its limitations. For
fixed display sinks like built-in panels there's not much difference between
this and \ :c:type:`struct drm_connector <drm_connector>`\ . But for sinks with a real cable this
structure is meant to describe all the things at the other end of the cable.

For sinks which provide an EDID this can be filled out by calling
\ :c:func:`drm_add_edid_modes`\ .

.. _`drm_tv_connector_state`:

struct drm_tv_connector_state
=============================

.. c:type:: struct drm_tv_connector_state

    TV connector related states

.. _`drm_tv_connector_state.definition`:

Definition
----------

.. code-block:: c

    struct drm_tv_connector_state {
        enum drm_mode_subconnector subconnector;
        struct {
            unsigned int left;
            unsigned int right;
            unsigned int top;
            unsigned int bottom;
        } margins;
        unsigned int mode;
        unsigned int brightness;
        unsigned int contrast;
        unsigned int flicker_reduction;
        unsigned int overscan;
        unsigned int saturation;
        unsigned int hue;
    }

.. _`drm_tv_connector_state.members`:

Members
-------

subconnector
    selected subconnector

margins
    margins

margins.left
    left margin

margins.right
    right margin

margins.top
    top margin

margins.bottom
    bottom margin

mode
    TV mode

brightness
    brightness in percent

contrast
    contrast in percent

flicker_reduction
    flicker reduction in percent

overscan
    overscan in percent

saturation
    saturation in percent

hue
    hue in percent

.. _`drm_connector_state`:

struct drm_connector_state
==========================

.. c:type:: struct drm_connector_state

    mutable connector state

.. _`drm_connector_state.definition`:

Definition
----------

.. code-block:: c

    struct drm_connector_state {
        struct drm_connector *connector;
        struct drm_crtc *crtc;
        struct drm_encoder *best_encoder;
        enum drm_link_status link_status;
        struct drm_atomic_state *state;
        struct drm_crtc_commit *commit;
        struct drm_tv_connector_state tv;
        enum hdmi_picture_aspect picture_aspect_ratio;
        unsigned int content_type;
        unsigned int scaling_mode;
        unsigned int content_protection;
        struct drm_writeback_job *writeback_job;
    }

.. _`drm_connector_state.members`:

Members
-------

connector
    backpointer to the connector

crtc
    CRTC to connect connector to, NULL if disabled.
    Do not change this directly, use \ :c:func:`drm_atomic_set_crtc_for_connector`\ 
    instead.

best_encoder

    Used by the atomic helpers to select the encoder, through the
    \ :c:type:`drm_connector_helper_funcs.atomic_best_encoder <drm_connector_helper_funcs>`\  or
    \ :c:type:`drm_connector_helper_funcs.best_encoder <drm_connector_helper_funcs>`\  callbacks.

link_status
    Connector link_status to keep track of whether link isGOOD or BAD to notify userspace if retraining is necessary.

state
    backpointer to global drm_atomic_state

commit
    Tracks the pending commit to prevent use-after-free conditions.
    Is only set when \ ``crtc``\  is NULL.

tv
    TV connector state

picture_aspect_ratio
    Connector property to control theHDMI infoframe aspect ratio setting.

    The \ ``DRM_MODE_PICTURE_ASPECT_``\ \* values much match the
    values for \ :c:type:`enum hdmi_picture_aspect <hdmi_picture_aspect>`\ 

content_type
    Connector property to control theHDMI infoframe content type setting.
    The \ ``DRM_MODE_CONTENT_TYPE_``\ \* values much
    match the values.

scaling_mode
    Connector property to control theupscaling, mostly used for built-in panels.

content_protection
    Connector property to request contentprotection. This is most commonly used for HDCP.

writeback_job
    Writeback job for writeback connectors
    Holds the framebuffer and out-fence for a writeback connector. As
    the writeback completion may be asynchronous to the normal commit
    cycle, the writeback job lifetime is managed separately from the
    normal atomic state by this object.

    See also: \ :c:func:`drm_writeback_queue_job`\  and
    \ :c:func:`drm_writeback_signal_completion`\ 

.. _`drm_connector_funcs`:

struct drm_connector_funcs
==========================

.. c:type:: struct drm_connector_funcs

    control connectors on a given device

.. _`drm_connector_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_connector_funcs {
        int (*dpms)(struct drm_connector *connector, int mode);
        void (*reset)(struct drm_connector *connector);
        enum drm_connector_status (*detect)(struct drm_connector *connector, bool force);
        void (*force)(struct drm_connector *connector);
        int (*fill_modes)(struct drm_connector *connector, uint32_t max_width, uint32_t max_height);
        int (*set_property)(struct drm_connector *connector, struct drm_property *property, uint64_t val);
        int (*late_register)(struct drm_connector *connector);
        void (*early_unregister)(struct drm_connector *connector);
        void (*destroy)(struct drm_connector *connector);
        struct drm_connector_state *(*atomic_duplicate_state)(struct drm_connector *connector);
        void (*atomic_destroy_state)(struct drm_connector *connector, struct drm_connector_state *state);
        int (*atomic_set_property)(struct drm_connector *connector,struct drm_connector_state *state,struct drm_property *property, uint64_t val);
        int (*atomic_get_property)(struct drm_connector *connector,const struct drm_connector_state *state,struct drm_property *property, uint64_t *val);
        void (*atomic_print_state)(struct drm_printer *p, const struct drm_connector_state *state);
    }

.. _`drm_connector_funcs.members`:

Members
-------

dpms

    Legacy entry point to set the per-connector DPMS state. Legacy DPMS
    is exposed as a standard property on the connector, but diverted to
    this callback in the drm core. Note that atomic drivers don't
    implement the 4 level DPMS support on the connector any more, but
    instead only have an on/off "ACTIVE" property on the CRTC object.

    This hook is not used by atomic drivers, remapping of the legacy DPMS
    property is entirely handled in the DRM core.

    RETURNS:

    0 on success or a negative error code on failure.

reset

    Reset connector hardware and software state to off. This function isn't
    called by the core directly, only through \ :c:func:`drm_mode_config_reset`\ .
    It's not a helper hook only for historical reasons.

    Atomic drivers can use \ :c:func:`drm_atomic_helper_connector_reset`\  to reset
    atomic state using this hook.

detect

    Check to see if anything is attached to the connector. The parameter
    force is set to false whilst polling, true when checking the
    connector due to a user request. force can be used by the driver to
    avoid expensive, destructive operations during automated probing.

    This callback is optional, if not implemented the connector will be
    considered as always being attached.

    FIXME:

    Note that this hook is only called by the probe helper. It's not in
    the helper library vtable purely for historical reasons. The only DRM
    core entry point to probe connector state is \ ``fill_modes``\ .

    Note that the helper library will already hold
    \ :c:type:`drm_mode_config.connection_mutex <drm_mode_config>`\ . Drivers which need to grab additional
    locks to avoid races with concurrent modeset changes need to use
    \ :c:type:`drm_connector_helper_funcs.detect_ctx <drm_connector_helper_funcs>`\  instead.

    RETURNS:

    drm_connector_status indicating the connector's status.

force

    This function is called to update internal encoder state when the
    connector is forced to a certain state by userspace, either through
    the sysfs interfaces or on the kernel cmdline. In that case the
    \ ``detect``\  callback isn't called.

    FIXME:

    Note that this hook is only called by the probe helper. It's not in
    the helper library vtable purely for historical reasons. The only DRM
    core entry point to probe connector state is \ ``fill_modes``\ .

fill_modes

    Entry point for output detection and basic mode validation. The
    driver should reprobe the output if needed (e.g. when hotplug
    handling is unreliable), add all detected modes to \ :c:type:`drm_connector.modes <drm_connector>`\ 
    and filter out any the device can't support in any configuration. It
    also needs to filter out any modes wider or higher than the
    parameters max_width and max_height indicate.

    The drivers must also prune any modes no longer valid from
    \ :c:type:`drm_connector.modes <drm_connector>`\ . Furthermore it must update
    \ :c:type:`drm_connector.status <drm_connector>`\  and \ :c:type:`drm_connector.edid <drm_connector>`\ .  If no EDID has been
    received for this output connector->edid must be NULL.

    Drivers using the probe helpers should use
    \ :c:func:`drm_helper_probe_single_connector_modes`\  to implement this
    function.

    RETURNS:

    The number of modes detected and filled into \ :c:type:`drm_connector.modes <drm_connector>`\ .

set_property

    This is the legacy entry point to update a property attached to the
    connector.

    This callback is optional if the driver does not support any legacy
    driver-private properties. For atomic drivers it is not used because
    property handling is done entirely in the DRM core.

    RETURNS:

    0 on success or a negative error code on failure.

late_register

    This optional hook can be used to register additional userspace
    interfaces attached to the connector, light backlight control, i2c,
    DP aux or similar interfaces. It is called late in the driver load
    sequence from \ :c:func:`drm_connector_register`\  when registering all the
    core drm connector interfaces. Everything added from this callback
    should be unregistered in the early_unregister callback.

    This is called while holding \ :c:type:`drm_connector.mutex <drm_connector>`\ .

    Returns:

    0 on success, or a negative error code on failure.

early_unregister

    This optional hook should be used to unregister the additional
    userspace interfaces attached to the connector from
    \ :c:func:`late_register`\ . It is called from \ :c:func:`drm_connector_unregister`\ ,
    early in the driver unload sequence to disable userspace access
    before data structures are torndown.

    This is called while holding \ :c:type:`drm_connector.mutex <drm_connector>`\ .

destroy

    Clean up connector resources. This is called at driver unload time
    through \ :c:func:`drm_mode_config_cleanup`\ . It can also be called at runtime
    when a connector is being hot-unplugged for drivers that support
    connector hotplugging (e.g. DisplayPort MST).

atomic_duplicate_state

    Duplicate the current atomic state for this connector and return it.
    The core and helpers guarantee that any atomic state duplicated with
    this hook and still owned by the caller (i.e. not transferred to the
    driver by calling \ :c:type:`drm_mode_config_funcs.atomic_commit <drm_mode_config_funcs>`\ ) will be
    cleaned up by calling the \ ``atomic_destroy_state``\  hook in this
    structure.

    This callback is mandatory for atomic drivers.

    Atomic drivers which don't subclass \ :c:type:`struct drm_connector_state <drm_connector_state>`\  should use
    \ :c:func:`drm_atomic_helper_connector_duplicate_state`\ . Drivers that subclass the
    state structure to extend it with driver-private state should use
    \ :c:func:`__drm_atomic_helper_connector_duplicate_state`\  to make sure shared state is
    duplicated in a consistent fashion across drivers.

    It is an error to call this hook before \ :c:type:`drm_connector.state <drm_connector>`\  has been
    initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook must
    acquire a reference for each of them. The driver must release these
    references again in \ ``atomic_destroy_state``\ .

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

atomic_destroy_state

    Destroy a state duplicated with \ ``atomic_duplicate_state``\  and release
    or unreference all resources it references

    This callback is mandatory for atomic drivers.

atomic_set_property

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
    \ :c:func:`drm_atomic_connector_set_property`\  instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic
    modesets, which can be aborted for any reason (including on
    userspace's request to just check whether a configuration would be
    possible). Drivers MUST NOT touch any persistent state (hardware or
    software) or data structures except the passed in \ ``state``\  parameter.

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

atomic_get_property

    Reads out the decoded driver-private property. This is used to
    implement the GETCONNECTOR IOCTL.

    Do not call this function directly, use
    \ :c:func:`drm_atomic_connector_get_property`\  instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the
    driver (which shouldn't ever happen, the core only asks for
    properties attached to this connector).

atomic_print_state

    If driver subclasses \ :c:type:`struct drm_connector_state <drm_connector_state>`\ , it should implement
    this optional hook for printing additional driver specific state.

    Do not call this directly, use \ :c:func:`drm_atomic_connector_print_state`\ 
    instead.

.. _`drm_connector_funcs.description`:

Description
-----------

Each CRTC may have one or more connectors attached to it.  The functions
below allow the core DRM code to control connectors, enumerate available modes,
etc.

.. _`drm_connector`:

struct drm_connector
====================

.. c:type:: struct drm_connector

    central DRM connector control structure

.. _`drm_connector.definition`:

Definition
----------

.. code-block:: c

    struct drm_connector {
        struct drm_device *dev;
        struct device *kdev;
        struct device_attribute *attr;
        struct list_head head;
        struct drm_mode_object base;
        char *name;
        struct mutex mutex;
        unsigned index;
        int connector_type;
        int connector_type_id;
        bool interlace_allowed;
        bool doublescan_allowed;
        bool stereo_allowed;
        bool ycbcr_420_allowed;
        enum drm_connector_registration_state registration_state;
        struct list_head modes;
        enum drm_connector_status status;
        struct list_head probed_modes;
        struct drm_display_info display_info;
        const struct drm_connector_funcs *funcs;
        struct drm_property_blob *edid_blob_ptr;
        struct drm_object_properties properties;
        struct drm_property *scaling_mode_property;
        struct drm_property *content_protection_property;
        struct drm_property_blob *path_blob_ptr;
    #define DRM_CONNECTOR_POLL_HPD (1 << 0)
    #define DRM_CONNECTOR_POLL_CONNECT (1 << 1)
    #define DRM_CONNECTOR_POLL_DISCONNECT (1 << 2)
        uint8_t polled;
        int dpms;
        const struct drm_connector_helper_funcs *helper_private;
        struct drm_cmdline_mode cmdline_mode;
        enum drm_connector_force force;
        bool override_edid;
    #define DRM_CONNECTOR_MAX_ENCODER 3
        uint32_t encoder_ids[DRM_CONNECTOR_MAX_ENCODER];
        struct drm_encoder *encoder;
    #define MAX_ELD_BYTES 128
        uint8_t eld[MAX_ELD_BYTES];
        bool latency_present[2];
        int video_latency[2];
        int audio_latency[2];
        int null_edid_counter;
        unsigned bad_edid_counter;
        bool edid_corrupt;
        struct dentry *debugfs_entry;
        struct drm_connector_state *state;
        struct drm_property_blob *tile_blob_ptr;
        bool has_tile;
        struct drm_tile_group *tile_group;
        bool tile_is_single_monitor;
        uint8_t num_h_tile, num_v_tile;
        uint8_t tile_h_loc, tile_v_loc;
        uint16_t tile_h_size, tile_v_size;
        struct llist_node free_node;
    }

.. _`drm_connector.members`:

Members
-------

dev
    parent DRM device

kdev
    kernel device for sysfs attributes

attr
    sysfs attributes

head

    List of all connectors on a \ ``dev``\ , linked from
    \ :c:type:`drm_mode_config.connector_list <drm_mode_config>`\ . Protected by
    \ :c:type:`drm_mode_config.connector_list_lock <drm_mode_config>`\ , but please only use
    \ :c:type:`struct drm_connector_list_iter <drm_connector_list_iter>`\  to walk this list.

base
    base KMS object

name
    human readable name, can be overwritten by the driver

mutex
    Lock for general connector state, but currently only protects@registered. Most of the connector state is still protected by
    \ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ .

index
    Compacted connector index, which matches the position insidethe mode_config.list for drivers not supporting hot-add/removing. Can
    be used as an array index. It is invariant over the lifetime of the
    connector.

connector_type
    one of the DRM_MODE_CONNECTOR_<foo> types from drm_mode.h

connector_type_id
    index into connector type enum

interlace_allowed
    Can this connector handle interlaced modes? Only used by
    \ :c:func:`drm_helper_probe_single_connector_modes`\  for mode filtering.

doublescan_allowed
    Can this connector handle doublescan? Only used by
    \ :c:func:`drm_helper_probe_single_connector_modes`\  for mode filtering.

stereo_allowed
    Can this connector handle stereo modes? Only used by
    \ :c:func:`drm_helper_probe_single_connector_modes`\  for mode filtering.

ycbcr_420_allowed
    This bool indicates if this connector iscapable of handling YCBCR 420 output. While parsing the EDID
    blocks, its very helpful to know, if the source is capable of
    handling YCBCR 420 outputs.

registration_state
    Is this connector initializing, exposed(registered) with userspace, or unregistered?

    Protected by \ ``mutex``\ .

modes
    Modes available on this connector (from \ :c:func:`fill_modes`\  + user).
    Protected by \ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ .

status
    One of the drm_connector_status enums (connected, not, or unknown).
    Protected by \ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ .

probed_modes
    These are modes added by probing with DDC or the BIOS, before
    filtering is applied. Used by the probe helpers. Protected by
    \ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ .

display_info
    Display information is filled from EDID informationwhen a display is detected. For non hot-pluggable displays such as
    flat panels in embedded systems, the driver should initialize the
    \ :c:type:`drm_display_info.width_mm <drm_display_info>`\  and \ :c:type:`drm_display_info.height_mm <drm_display_info>`\  fields
    with the physical size of the display.

    Protected by \ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ .

funcs
    connector control functions

edid_blob_ptr
    DRM property containing EDID if present. Protected by&drm_mode_config.mutex. This should be updated only by calling
    \ :c:func:`drm_connector_update_edid_property`\ .

properties
    property tracking for this connector

scaling_mode_property
    Optional atomic property to control theupscaling. See \ :c:func:`drm_connector_attach_content_protection_property`\ .

content_protection_property
    DRM ENUM property for contentprotection. See \ :c:func:`drm_connector_attach_content_protection_property`\ .

path_blob_ptr

    DRM blob property data for the DP MST path property. This should only
    be updated by calling \ :c:func:`drm_connector_set_path_property`\ .

polled

    Connector polling mode, a combination of

    DRM_CONNECTOR_POLL_HPD
        The connector generates hotplug events and doesn't need to be
        periodically polled. The CONNECT and DISCONNECT flags must not
        be set together with the HPD flag.

    DRM_CONNECTOR_POLL_CONNECT
        Periodically poll the connector for connection.

    DRM_CONNECTOR_POLL_DISCONNECT
        Periodically poll the connector for disconnection, without
        causing flickering even when the connector is in use. DACs should
        rarely do this without a lot of testing.

    Set to 0 for connectors that don't support connection status
    discovery.

dpms
    Current dpms state. For legacy drivers the&drm_connector_funcs.dpms callback must update this. For atomic
    drivers, this is handled by the core atomic code, and drivers must
    only take \ :c:type:`drm_crtc_state.active <drm_crtc_state>`\  into account.

helper_private
    mid-layer private data

cmdline_mode
    mode line parsed from the kernel cmdline for this connector

force
    a DRM_FORCE_<foo> state for forced mode sets

override_edid
    has the EDID been overwritten through debugfs for testing?

encoder_ids
    Valid encoders for this connector. Please only \ :c:func:`usedrm_connector_for_each_possible_encoder`\  to enumerate these.

encoder
    Currently bound encoder driving this connector, if any.Only really meaningful for non-atomic drivers. Atomic drivers should
    instead look at \ :c:type:`drm_connector_state.best_encoder <drm_connector_state>`\ , and in case they
    need the CRTC driving this output, \ :c:type:`drm_connector_state.crtc <drm_connector_state>`\ .

eld
    EDID-like data, if present

latency_present
    AV delay info from ELD, if found

video_latency
    Video latency info from ELD, if found.[0]: progressive, [1]: interlaced

audio_latency
    audio latency info from ELD, if found[0]: progressive, [1]: interlaced

null_edid_counter
    track sinks that give us all zeros for the EDID.Needed to workaround some HW bugs where we get all 0s

bad_edid_counter
    track sinks that give us an EDID with invalid checksum

edid_corrupt
    Indicates whether the last read EDID was corrupt. Usedin Displayport compliance testing - Displayport Link CTS Core 1.2
    rev1.1 4.2.2.6

debugfs_entry
    debugfs directory for this connector

state

    Current atomic state for this connector.

    This is protected by \ :c:type:`drm_mode_config.connection_mutex <drm_mode_config>`\ . Note that
    nonblocking atomic commits access the current connector state without
    taking locks. Either by going through the \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\ 
    pointers, see \ :c:func:`for_each_oldnew_connector_in_state`\ ,
    \ :c:func:`for_each_old_connector_in_state`\  and
    \ :c:func:`for_each_new_connector_in_state`\ . Or through careful ordering of
    atomic commit operations as implemented in the atomic helpers, see
    \ :c:type:`struct drm_crtc_commit <drm_crtc_commit>`\ .

tile_blob_ptr

    DRM blob property data for the tile property (used mostly by DP MST).
    This is meant for screens which are driven through separate display
    pipelines represented by \ :c:type:`struct drm_crtc <drm_crtc>`\ , which might not be running with
    genlocked clocks. For tiled panels which are genlocked, like
    dual-link LVDS or dual-link DSI, the driver should try to not expose
    the tiling and virtualize both \ :c:type:`struct drm_crtc <drm_crtc>`\  and \ :c:type:`struct drm_plane <drm_plane>`\  if needed.

    This should only be updated by calling
    \ :c:func:`drm_connector_set_tile_property`\ .

has_tile
    is this connector connected to a tiled monitor

tile_group
    tile group for the connected monitor

tile_is_single_monitor
    whether the tile is one monitor housing

num_h_tile
    number of horizontal tiles in the tile group

num_v_tile
    number of vertical tiles in the tile group

tile_h_loc
    horizontal location of this tile

tile_v_loc
    vertical location of this tile

tile_h_size
    horizontal size of this tile.

tile_v_size
    vertical size of this tile.

free_node

    List used only by \ :c:type:`struct drm_connector_list_iter <drm_connector_list_iter>`\  to be able to clean up a
    connector from any context, in conjunction with
    \ :c:type:`drm_mode_config.connector_free_work <drm_mode_config>`\ .

.. _`drm_connector.description`:

Description
-----------

Each connector may be connected to one or more CRTCs, or may be clonable by
another connector if they can share a CRTC.  Each connector also has a specific
position in the broader display (referred to as a 'screen' though it could
span multiple monitors).

.. _`drm_connector_lookup`:

drm_connector_lookup
====================

.. c:function:: struct drm_connector *drm_connector_lookup(struct drm_device *dev, struct drm_file *file_priv, uint32_t id)

    lookup connector object

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param file_priv:
        drm file to check for lease against.
    :type file_priv: struct drm_file \*

    :param id:
        connector object id
    :type id: uint32_t

.. _`drm_connector_lookup.description`:

Description
-----------

This function looks up the connector object specified by id
add takes a reference to it.

.. _`drm_connector_get`:

drm_connector_get
=================

.. c:function:: void drm_connector_get(struct drm_connector *connector)

    acquire a connector reference

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`drm_connector_get.description`:

Description
-----------

This function increments the connector's refcount.

.. _`drm_connector_put`:

drm_connector_put
=================

.. c:function:: void drm_connector_put(struct drm_connector *connector)

    release a connector reference

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`drm_connector_put.description`:

Description
-----------

This function decrements the connector's reference count and frees the
object if the reference count drops to zero.

.. _`drm_connector_reference`:

drm_connector_reference
=======================

.. c:function:: void drm_connector_reference(struct drm_connector *connector)

    acquire a connector reference

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`drm_connector_reference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_connector_get`\  and should not be
used by new code.

.. _`drm_connector_unreference`:

drm_connector_unreference
=========================

.. c:function:: void drm_connector_unreference(struct drm_connector *connector)

    release a connector reference

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`drm_connector_unreference.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_connector_put`\  and should not be
used by new code.

.. _`drm_connector_is_unregistered`:

drm_connector_is_unregistered
=============================

.. c:function:: bool drm_connector_is_unregistered(struct drm_connector *connector)

    has the connector been unregistered from userspace?

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`drm_connector_is_unregistered.description`:

Description
-----------

Checks whether or not \ ``connector``\  has been unregistered from userspace.

.. _`drm_connector_is_unregistered.return`:

Return
------

True if the connector was unregistered, false if the connector is
registered or has not yet been registered with userspace.

.. _`drm_tile_group`:

struct drm_tile_group
=====================

.. c:type:: struct drm_tile_group

    Tile group metadata

.. _`drm_tile_group.definition`:

Definition
----------

.. code-block:: c

    struct drm_tile_group {
        struct kref refcount;
        struct drm_device *dev;
        int id;
        u8 group_data[8];
    }

.. _`drm_tile_group.members`:

Members
-------

refcount
    reference count

dev
    DRM device

id
    tile group id exposed to userspace

group_data
    Sink-private data identifying this group

.. _`drm_tile_group.description`:

Description
-----------

\ ``group_data``\  corresponds to displayid vend/prod/serial for external screens
with an EDID.

.. _`drm_connector_list_iter`:

struct drm_connector_list_iter
==============================

.. c:type:: struct drm_connector_list_iter

    connector_list iterator

.. _`drm_connector_list_iter.definition`:

Definition
----------

.. code-block:: c

    struct drm_connector_list_iter {
    }

.. _`drm_connector_list_iter.members`:

Members
-------

void
    no arguments

.. _`drm_connector_list_iter.description`:

Description
-----------

This iterator tracks state needed to be able to walk the connector_list
within struct drm_mode_config. Only use together with
\ :c:func:`drm_connector_list_iter_begin`\ , \ :c:func:`drm_connector_list_iter_end`\  and
\ :c:func:`drm_connector_list_iter_next`\  respectively the convenience macro
\ :c:func:`drm_for_each_connector_iter`\ .

.. _`drm_for_each_connector_iter`:

drm_for_each_connector_iter
===========================

.. c:function::  drm_for_each_connector_iter( connector,  iter)

    connector_list iterator macro

    :param connector:
        \ :c:type:`struct drm_connector <drm_connector>`\  pointer used as cursor
    :type connector: 

    :param iter:
        \ :c:type:`struct drm_connector_list_iter <drm_connector_list_iter>`\ 
    :type iter: 

.. _`drm_for_each_connector_iter.description`:

Description
-----------

Note that \ ``connector``\  is only valid within the list body, if you want to use
\ ``connector``\  after calling \ :c:func:`drm_connector_list_iter_end`\  then you need to grab
your own reference first using \ :c:func:`drm_connector_get`\ .

.. _`drm_connector_for_each_possible_encoder`:

drm_connector_for_each_possible_encoder
=======================================

.. c:function::  drm_connector_for_each_possible_encoder( connector,  encoder,  __i)

    iterate connector's possible encoders

    :param connector:
        \ :c:type:`struct drm_connector <drm_connector>`\  pointer
    :type connector: 

    :param encoder:
        \ :c:type:`struct drm_encoder <drm_encoder>`\  pointer used as cursor
    :type encoder: 

    :param __i:
        int iteration cursor, for macro-internal use
    :type __i: 

.. This file was automatic generated / don't edit.

