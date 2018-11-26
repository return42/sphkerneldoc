.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_edid.c

.. _`drm_edid_header_is_valid`:

drm_edid_header_is_valid
========================

.. c:function:: int drm_edid_header_is_valid(const u8 *raw_edid)

    sanity check the header of the base EDID block

    :param raw_edid:
        pointer to raw base EDID block
    :type raw_edid: const u8 \*

.. _`drm_edid_header_is_valid.description`:

Description
-----------

Sanity check the header of the base EDID block.

.. _`drm_edid_header_is_valid.return`:

Return
------

8 if the header is perfect, down to 0 if it's totally wrong.

.. _`drm_edid_block_valid`:

drm_edid_block_valid
====================

.. c:function:: bool drm_edid_block_valid(u8 *raw_edid, int block, bool print_bad_edid, bool *edid_corrupt)

    Sanity check the EDID block (base or extension)

    :param raw_edid:
        pointer to raw EDID block
    :type raw_edid: u8 \*

    :param block:
        type of block to validate (0 for base, extension otherwise)
    :type block: int

    :param print_bad_edid:
        if true, dump bad EDID blocks to the console
    :type print_bad_edid: bool

    :param edid_corrupt:
        if true, the header or checksum is invalid
    :type edid_corrupt: bool \*

.. _`drm_edid_block_valid.description`:

Description
-----------

Validate a base or extension EDID block and optionally dump bad blocks to
the console.

.. _`drm_edid_block_valid.return`:

Return
------

True if the block is valid, false otherwise.

.. _`drm_edid_is_valid`:

drm_edid_is_valid
=================

.. c:function:: bool drm_edid_is_valid(struct edid *edid)

    sanity check EDID data

    :param edid:
        EDID data
    :type edid: struct edid \*

.. _`drm_edid_is_valid.description`:

Description
-----------

Sanity-check an entire EDID record (including extensions)

.. _`drm_edid_is_valid.return`:

Return
------

True if the EDID data is valid, false otherwise.

.. _`drm_do_probe_ddc_edid`:

drm_do_probe_ddc_edid
=====================

.. c:function:: int drm_do_probe_ddc_edid(void *data, u8 *buf, unsigned int block, size_t len)

    get EDID information via I2C

    :param data:
        I2C device adapter
    :type data: void \*

    :param buf:
        EDID data buffer to be filled
    :type buf: u8 \*

    :param block:
        128 byte EDID block to start fetching from
    :type block: unsigned int

    :param len:
        EDID data buffer length to fetch
    :type len: size_t

.. _`drm_do_probe_ddc_edid.description`:

Description
-----------

Try to fetch EDID information by calling I2C driver functions.

.. _`drm_do_probe_ddc_edid.return`:

Return
------

0 on success or -1 on failure.

.. _`drm_do_get_edid`:

drm_do_get_edid
===============

.. c:function:: struct edid *drm_do_get_edid(struct drm_connector *connector, int (*get_edid_block)(void *data, u8 *buf, unsigned int block, size_t len), void *data)

    get EDID data using a custom EDID block read function

    :param connector:
        connector we're probing
    :type connector: struct drm_connector \*

    :param int (\*get_edid_block)(void \*data, u8 \*buf, unsigned int block, size_t len):
        EDID block read function

    :param data:
        private data passed to the block read function
    :type data: void \*

.. _`drm_do_get_edid.description`:

Description
-----------

When the I2C adapter connected to the DDC bus is hidden behind a device that
exposes a different interface to read EDID blocks this function can be used
to get EDID data using a custom block read function.

As in the general case the DDC bus is accessible by the kernel at the I2C
level, drivers must make all reasonable efforts to expose it as an I2C
adapter and use \ :c:func:`drm_get_edid`\  instead of abusing this function.

The EDID may be overridden using debugfs override_edid or firmare EDID
(drm_load_edid_firmware() and drm.edid_firmware parameter), in this priority
order. Having either of them bypasses actual EDID reads.

.. _`drm_do_get_edid.return`:

Return
------

Pointer to valid EDID or NULL if we couldn't find any.

.. _`drm_probe_ddc`:

drm_probe_ddc
=============

.. c:function:: bool drm_probe_ddc(struct i2c_adapter *adapter)

    probe DDC presence

    :param adapter:
        I2C adapter to probe
    :type adapter: struct i2c_adapter \*

.. _`drm_probe_ddc.return`:

Return
------

True on success, false on failure.

.. _`drm_get_edid`:

drm_get_edid
============

.. c:function:: struct edid *drm_get_edid(struct drm_connector *connector, struct i2c_adapter *adapter)

    get EDID data, if available

    :param connector:
        connector we're probing
    :type connector: struct drm_connector \*

    :param adapter:
        I2C adapter to use for DDC
    :type adapter: struct i2c_adapter \*

.. _`drm_get_edid.description`:

Description
-----------

Poke the given I2C channel to grab EDID data if possible.  If found,
attach it to the connector.

.. _`drm_get_edid.return`:

Return
------

Pointer to valid EDID or NULL if we couldn't find any.

.. _`drm_get_edid_switcheroo`:

drm_get_edid_switcheroo
=======================

.. c:function:: struct edid *drm_get_edid_switcheroo(struct drm_connector *connector, struct i2c_adapter *adapter)

    get EDID data for a vga_switcheroo output

    :param connector:
        connector we're probing
    :type connector: struct drm_connector \*

    :param adapter:
        I2C adapter to use for DDC
    :type adapter: struct i2c_adapter \*

.. _`drm_get_edid_switcheroo.description`:

Description
-----------

Wrapper around \ :c:func:`drm_get_edid`\  for laptops with dual GPUs using one set of
outputs. The wrapper adds the requisite vga_switcheroo calls to temporarily
switch DDC to the GPU which is retrieving EDID.

.. _`drm_get_edid_switcheroo.return`:

Return
------

Pointer to valid EDID or \ ``NULL``\  if we couldn't find any.

.. _`drm_edid_duplicate`:

drm_edid_duplicate
==================

.. c:function:: struct edid *drm_edid_duplicate(const struct edid *edid)

    duplicate an EDID and the extensions

    :param edid:
        EDID to duplicate
    :type edid: const struct edid \*

.. _`drm_edid_duplicate.return`:

Return
------

Pointer to duplicated EDID or NULL on allocation failure.

.. _`edid_vendor`:

edid_vendor
===========

.. c:function:: bool edid_vendor(const struct edid *edid, const char *vendor)

    match a string against EDID's obfuscated vendor field

    :param edid:
        EDID to match
    :type edid: const struct edid \*

    :param vendor:
        vendor string
    :type vendor: const char \*

.. _`edid_vendor.description`:

Description
-----------

Returns true if \ ``vendor``\  is in \ ``edid``\ , false otherwise

.. _`edid_get_quirks`:

edid_get_quirks
===============

.. c:function:: u32 edid_get_quirks(const struct edid *edid)

    return quirk flags for a given EDID

    :param edid:
        EDID to process
    :type edid: const struct edid \*

.. _`edid_get_quirks.description`:

Description
-----------

This tells subsequent routines what fixes they need to apply.

.. _`edid_fixup_preferred`:

edid_fixup_preferred
====================

.. c:function:: void edid_fixup_preferred(struct drm_connector *connector, u32 quirks)

    set preferred modes based on quirk list

    :param connector:
        has mode list to fix up
    :type connector: struct drm_connector \*

    :param quirks:
        quirks list
    :type quirks: u32

.. _`edid_fixup_preferred.description`:

Description
-----------

Walk the mode list for \ ``connector``\ , clearing the preferred status
on existing modes and setting it anew for the right mode ala \ ``quirks``\ .

.. _`standard_timing_level`:

standard_timing_level
=====================

.. c:function:: int standard_timing_level(struct edid *edid)

    get std. timing level(CVT/GTF/DMT)

    :param edid:
        EDID block to scan
    :type edid: struct edid \*

.. _`drm_mode_std`:

drm_mode_std
============

.. c:function:: struct drm_display_mode *drm_mode_std(struct drm_connector *connector, struct edid *edid, struct std_timing *t)

    convert standard mode info (width, height, refresh) into mode

    :param connector:
        connector of for the EDID block
    :type connector: struct drm_connector \*

    :param edid:
        EDID block to scan
    :type edid: struct edid \*

    :param t:
        standard timing params
    :type t: struct std_timing \*

.. _`drm_mode_std.description`:

Description
-----------

Take the standard timing params (in this case width, aspect, and refresh)
and convert them into a real mode using CVT/GTF/DMT.

.. _`drm_mode_detailed`:

drm_mode_detailed
=================

.. c:function:: struct drm_display_mode *drm_mode_detailed(struct drm_device *dev, struct edid *edid, struct detailed_timing *timing, u32 quirks)

    create a new mode from an EDID detailed timing section

    :param dev:
        DRM device (needed to create new mode)
    :type dev: struct drm_device \*

    :param edid:
        EDID block
    :type edid: struct edid \*

    :param timing:
        EDID detailed timing info
    :type timing: struct detailed_timing \*

    :param quirks:
        quirks to apply
    :type quirks: u32

.. _`drm_mode_detailed.description`:

Description
-----------

An EDID detailed timing block contains enough info for us to create and
return a new struct drm_display_mode.

.. _`add_established_modes`:

add_established_modes
=====================

.. c:function:: int add_established_modes(struct drm_connector *connector, struct edid *edid)

    get est. modes from EDID and add them

    :param connector:
        connector to add mode(s) to
    :type connector: struct drm_connector \*

    :param edid:
        EDID block to scan
    :type edid: struct edid \*

.. _`add_established_modes.description`:

Description
-----------

Each EDID block contains a bitmap of the supported "established modes" list
(defined above).  Tease them out and add them to the global modes list.

.. _`add_standard_modes`:

add_standard_modes
==================

.. c:function:: int add_standard_modes(struct drm_connector *connector, struct edid *edid)

    get std. modes from EDID and add them

    :param connector:
        connector to add mode(s) to
    :type connector: struct drm_connector \*

    :param edid:
        EDID block to scan
    :type edid: struct edid \*

.. _`add_standard_modes.description`:

Description
-----------

Standard modes can be calculated using the appropriate standard (DMT,
GTF or CVT. Grab them from \ ``edid``\  and add them to the list.

.. _`drm_match_cea_mode`:

drm_match_cea_mode
==================

.. c:function:: u8 drm_match_cea_mode(const struct drm_display_mode *to_match)

    look for a CEA mode matching given mode

    :param to_match:
        display mode
    :type to_match: const struct drm_display_mode \*

.. _`drm_match_cea_mode.return`:

Return
------

The CEA Video ID (VIC) of the mode or 0 if it isn't a CEA-861
mode.

.. _`drm_get_cea_aspect_ratio`:

drm_get_cea_aspect_ratio
========================

.. c:function:: enum hdmi_picture_aspect drm_get_cea_aspect_ratio(const u8 video_code)

    get the picture aspect ratio corresponding to the input VIC from the CEA mode list

    :param video_code:
        ID given to each of the CEA modes
    :type video_code: const u8

.. _`drm_get_cea_aspect_ratio.description`:

Description
-----------

Returns picture aspect ratio

.. _`drm_edid_get_monitor_name`:

drm_edid_get_monitor_name
=========================

.. c:function:: void drm_edid_get_monitor_name(struct edid *edid, char *name, int bufsize)

    fetch the monitor name from the edid

    :param edid:
        monitor EDID information
    :type edid: struct edid \*

    :param name:
        pointer to a character array to hold the name of the monitor
    :type name: char \*

    :param bufsize:
        The size of the name buffer (should be at least 14 chars.)
    :type bufsize: int

.. _`drm_edid_to_sad`:

drm_edid_to_sad
===============

.. c:function:: int drm_edid_to_sad(struct edid *edid, struct cea_sad **sads)

    extracts SADs from EDID

    :param edid:
        EDID to parse
    :type edid: struct edid \*

    :param sads:
        pointer that will be set to the extracted SADs
    :type sads: struct cea_sad \*\*

.. _`drm_edid_to_sad.description`:

Description
-----------

Looks for CEA EDID block and extracts SADs (Short Audio Descriptors) from it.

.. _`drm_edid_to_sad.note`:

Note
----

The returned pointer needs to be freed using \ :c:func:`kfree`\ .

.. _`drm_edid_to_sad.return`:

Return
------

The number of found SADs or negative number on error.

.. _`drm_edid_to_speaker_allocation`:

drm_edid_to_speaker_allocation
==============================

.. c:function:: int drm_edid_to_speaker_allocation(struct edid *edid, u8 **sadb)

    extracts Speaker Allocation Data Blocks from EDID

    :param edid:
        EDID to parse
    :type edid: struct edid \*

    :param sadb:
        pointer to the speaker block
    :type sadb: u8 \*\*

.. _`drm_edid_to_speaker_allocation.description`:

Description
-----------

Looks for CEA EDID block and extracts the Speaker Allocation Data Block from it.

.. _`drm_edid_to_speaker_allocation.note`:

Note
----

The returned pointer needs to be freed using \ :c:func:`kfree`\ .

.. _`drm_edid_to_speaker_allocation.return`:

Return
------

The number of found Speaker Allocation Blocks or negative number on
error.

.. _`drm_av_sync_delay`:

drm_av_sync_delay
=================

.. c:function:: int drm_av_sync_delay(struct drm_connector *connector, const struct drm_display_mode *mode)

    compute the HDMI/DP sink audio-video sync delay

    :param connector:
        connector associated with the HDMI/DP sink
    :type connector: struct drm_connector \*

    :param mode:
        the display mode
    :type mode: const struct drm_display_mode \*

.. _`drm_av_sync_delay.return`:

Return
------

The HDMI/DP sink's audio-video sync delay in milliseconds or 0 if
the sink doesn't support audio or video.

.. _`drm_detect_hdmi_monitor`:

drm_detect_hdmi_monitor
=======================

.. c:function:: bool drm_detect_hdmi_monitor(struct edid *edid)

    detect whether monitor is HDMI

    :param edid:
        monitor EDID information
    :type edid: struct edid \*

.. _`drm_detect_hdmi_monitor.description`:

Description
-----------

Parse the CEA extension according to CEA-861-B.

.. _`drm_detect_hdmi_monitor.return`:

Return
------

True if the monitor is HDMI, false if not or unknown.

.. _`drm_detect_monitor_audio`:

drm_detect_monitor_audio
========================

.. c:function:: bool drm_detect_monitor_audio(struct edid *edid)

    check monitor audio capability

    :param edid:
        EDID block to scan
    :type edid: struct edid \*

.. _`drm_detect_monitor_audio.description`:

Description
-----------

Monitor should have CEA extension block.
If monitor has 'basic audio', but no CEA audio blocks, it's 'basic
audio' only. If there is any audio extension block and supported
audio format, assume at least 'basic audio' support, even if 'basic
audio' is not defined in EDID.

.. _`drm_detect_monitor_audio.return`:

Return
------

True if the monitor supports audio, false otherwise.

.. _`drm_rgb_quant_range_selectable`:

drm_rgb_quant_range_selectable
==============================

.. c:function:: bool drm_rgb_quant_range_selectable(struct edid *edid)

    is RGB quantization range selectable?

    :param edid:
        EDID block to scan
    :type edid: struct edid \*

.. _`drm_rgb_quant_range_selectable.description`:

Description
-----------

Check whether the monitor reports the RGB quantization range selection
as supported. The AVI infoframe can then be used to inform the monitor
which quantization range (full or limited) is used.

.. _`drm_rgb_quant_range_selectable.return`:

Return
------

True if the RGB quantization range is selectable, false otherwise.

.. _`drm_default_rgb_quant_range`:

drm_default_rgb_quant_range
===========================

.. c:function:: enum hdmi_quantization_range drm_default_rgb_quant_range(const struct drm_display_mode *mode)

    default RGB quantization range

    :param mode:
        display mode
    :type mode: const struct drm_display_mode \*

.. _`drm_default_rgb_quant_range.description`:

Description
-----------

Determine the default RGB quantization range for the mode,
as specified in CEA-861.

.. _`drm_default_rgb_quant_range.return`:

Return
------

The default RGB quantization range for the mode

.. _`drm_add_edid_modes`:

drm_add_edid_modes
==================

.. c:function:: int drm_add_edid_modes(struct drm_connector *connector, struct edid *edid)

    add modes from EDID data, if available

    :param connector:
        connector we're probing
    :type connector: struct drm_connector \*

    :param edid:
        EDID data
    :type edid: struct edid \*

.. _`drm_add_edid_modes.description`:

Description
-----------

Add the specified modes to the connector's mode list. Also fills out the
\ :c:type:`struct drm_display_info <drm_display_info>`\  structure and ELD in \ ``connector``\  with any information which
can be derived from the edid.

.. _`drm_add_edid_modes.return`:

Return
------

The number of modes added or 0 if we couldn't find any.

.. _`drm_add_modes_noedid`:

drm_add_modes_noedid
====================

.. c:function:: int drm_add_modes_noedid(struct drm_connector *connector, int hdisplay, int vdisplay)

    add modes for the connectors without EDID

    :param connector:
        connector we're probing
    :type connector: struct drm_connector \*

    :param hdisplay:
        the horizontal display limit
    :type hdisplay: int

    :param vdisplay:
        the vertical display limit
    :type vdisplay: int

.. _`drm_add_modes_noedid.description`:

Description
-----------

Add the specified modes to the connector's mode list. Only when the
hdisplay/vdisplay is not beyond the given limit, it will be added.

.. _`drm_add_modes_noedid.return`:

Return
------

The number of modes added or 0 if we couldn't find any.

.. _`drm_set_preferred_mode`:

drm_set_preferred_mode
======================

.. c:function:: void drm_set_preferred_mode(struct drm_connector *connector, int hpref, int vpref)

    Sets the preferred mode of a connector

    :param connector:
        connector whose mode list should be processed
    :type connector: struct drm_connector \*

    :param hpref:
        horizontal resolution of preferred mode
    :type hpref: int

    :param vpref:
        vertical resolution of preferred mode
    :type vpref: int

.. _`drm_set_preferred_mode.description`:

Description
-----------

Marks a mode as preferred if it matches the resolution specified by \ ``hpref``\ 
and \ ``vpref``\ .

.. _`drm_hdmi_avi_infoframe_from_display_mode`:

drm_hdmi_avi_infoframe_from_display_mode
========================================

.. c:function:: int drm_hdmi_avi_infoframe_from_display_mode(struct hdmi_avi_infoframe *frame, const struct drm_display_mode *mode, bool is_hdmi2_sink)

    fill an HDMI AVI infoframe with data from a DRM display mode

    :param frame:
        HDMI AVI infoframe
    :type frame: struct hdmi_avi_infoframe \*

    :param mode:
        DRM display mode
    :type mode: const struct drm_display_mode \*

    :param is_hdmi2_sink:
        Sink is HDMI 2.0 compliant
    :type is_hdmi2_sink: bool

.. _`drm_hdmi_avi_infoframe_from_display_mode.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_hdmi_avi_infoframe_quant_range`:

drm_hdmi_avi_infoframe_quant_range
==================================

.. c:function:: void drm_hdmi_avi_infoframe_quant_range(struct hdmi_avi_infoframe *frame, const struct drm_display_mode *mode, enum hdmi_quantization_range rgb_quant_range, bool rgb_quant_range_selectable, bool is_hdmi2_sink)

    fill the HDMI AVI infoframe quantization range information

    :param frame:
        HDMI AVI infoframe
    :type frame: struct hdmi_avi_infoframe \*

    :param mode:
        DRM display mode
    :type mode: const struct drm_display_mode \*

    :param rgb_quant_range:
        RGB quantization range (Q)
    :type rgb_quant_range: enum hdmi_quantization_range

    :param rgb_quant_range_selectable:
        Sink support selectable RGB quantization range (QS)
    :type rgb_quant_range_selectable: bool

    :param is_hdmi2_sink:
        HDMI 2.0 sink, which has different default recommendations
    :type is_hdmi2_sink: bool

.. _`drm_hdmi_avi_infoframe_quant_range.description`:

Description
-----------

Note that \ ``is_hdmi2_sink``\  can be derived by looking at the
\ :c:type:`drm_scdc.supported <drm_scdc>`\  flag stored in \ :c:type:`drm_hdmi_info.scdc <drm_hdmi_info>`\ ,
\ :c:type:`drm_display_info.hdmi <drm_display_info>`\ , which can be found in \ :c:type:`drm_connector.display_info <drm_connector>`\ .

.. _`drm_hdmi_vendor_infoframe_from_display_mode`:

drm_hdmi_vendor_infoframe_from_display_mode
===========================================

.. c:function:: int drm_hdmi_vendor_infoframe_from_display_mode(struct hdmi_vendor_infoframe *frame, struct drm_connector *connector, const struct drm_display_mode *mode)

    fill an HDMI infoframe with data from a DRM display mode

    :param frame:
        HDMI vendor infoframe
    :type frame: struct hdmi_vendor_infoframe \*

    :param connector:
        the connector
    :type connector: struct drm_connector \*

    :param mode:
        DRM display mode
    :type mode: const struct drm_display_mode \*

.. _`drm_hdmi_vendor_infoframe_from_display_mode.description`:

Description
-----------

Note that there's is a need to send HDMI vendor infoframes only when using a
4k or stereoscopic 3D mode. So when giving any other mode as input this
function will return -EINVAL, error that can be safely ignored.

.. _`drm_hdmi_vendor_infoframe_from_display_mode.return`:

Return
------

0 on success or a negative error code on failure.

.. This file was automatic generated / don't edit.

