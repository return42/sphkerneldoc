
.. _API-struct-drm-connector:

====================
struct drm_connector
====================

*man struct drm_connector(9)*

*4.6.0-rc1*

central DRM connector control structure


Synopsis
========

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
=======

dev
    parent DRM device

kdev
    kernel device for sysfs attributes

attr
    sysfs attributes

head
    list management

base
    base KMS object

name
    connector name

connector_type
    one of the ``DRM_MODE_CONNECTOR_`` <foo> types from drm_mode.h

connector_type_id
    index into connector type enum

interlace_allowed
    can this connector handle interlaced modes?

doublescan_allowed
    can this connector handle doublescan?

stereo_allowed
    can this connector handle stereo modes?

modes
    modes available on this connector (from ``fill_modes`` + user)

status
    one of the drm_connector_status enums (connected, not, or unknown)

probed_modes
    list of modes derived directly from the display

display_info
    information about attached display (e.g. from EDID)

funcs
    connector control functions

edid_blob_ptr
    DRM property containing EDID if present

properties
    property tracking for this connector

path_blob_ptr
    DRM blob property data for the DP MST path property

polled
    a ``DRM_CONNECTOR_POLL_``\ <foo> value for core driven polling

dpms
    current dpms state

helper_private
    mid-layer private data

cmdline_mode
    mode line parsed from the kernel cmdline for this connector

force
    a ``DRM_FORCE_``\ <foo> state for forced mode sets

override_edid
    has the EDID been overwritten through debugfs for testing?

encoder_ids[DRM_CONNECTOR_MAX_ENCODER]
    valid encoders for this connector

encoder
    encoder driving this connector, if any

eld[MAX_ELD_BYTES]
    EDID-like data, if present

dvi_dual
    dual link DVI, if found

max_tmds_clock
    max clock rate, if found

latency_present[2]
    AV delay info from ELD, if found

video_latency[2]
    video latency info from ELD, if found

audio_latency[2]
    audio latency info from ELD, if found

null_edid_counter
    track sinks that give us all zeros for the EDID

bad_edid_counter
    track sinks that give us an EDID with invalid checksum

edid_corrupt
    indicates whether the last read EDID was corrupt

debugfs_entry
    debugfs directory for this connector

state
    current atomic state for this connector

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


Description
===========

Each connector may be connected to one or more CRTCs, or may be clonable by another connector if they can share a CRTC. Each connector also has a specific position in the broader
display (referred to as a 'screen' though it could span multiple monitors).
