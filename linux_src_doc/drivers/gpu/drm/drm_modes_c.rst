.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_modes.c

.. _`drm_mode_debug_printmodeline`:

drm_mode_debug_printmodeline
============================

.. c:function:: void drm_mode_debug_printmodeline(const struct drm_display_mode *mode)

    print a mode to dmesg

    :param const struct drm_display_mode \*mode:
        mode to print

.. _`drm_mode_debug_printmodeline.description`:

Description
-----------

Describe \ ``mode``\  using DRM_DEBUG.

.. _`drm_mode_create`:

drm_mode_create
===============

.. c:function:: struct drm_display_mode *drm_mode_create(struct drm_device *dev)

    create a new display mode

    :param struct drm_device \*dev:
        DRM device

.. _`drm_mode_create.description`:

Description
-----------

Create a new, cleared drm_display_mode with kzalloc, allocate an ID for it
and return it.

.. _`drm_mode_create.return`:

Return
------

Pointer to new mode on success, NULL on error.

.. _`drm_mode_destroy`:

drm_mode_destroy
================

.. c:function:: void drm_mode_destroy(struct drm_device *dev, struct drm_display_mode *mode)

    remove a mode

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_display_mode \*mode:
        mode to remove

.. _`drm_mode_destroy.description`:

Description
-----------

Release \ ``mode``\ 's unique ID, then free it \ ``mode``\  structure itself using kfree.

.. _`drm_mode_probed_add`:

drm_mode_probed_add
===================

.. c:function:: void drm_mode_probed_add(struct drm_connector *connector, struct drm_display_mode *mode)

    add a mode to a connector's probed_mode list

    :param struct drm_connector \*connector:
        connector the new mode

    :param struct drm_display_mode \*mode:
        mode data

.. _`drm_mode_probed_add.description`:

Description
-----------

Add \ ``mode``\  to \ ``connector``\ 's probed_mode list for later use. This list should
then in a second step get filtered and all the modes actually supported by
the hardware moved to the \ ``connector``\ 's modes list.

.. _`drm_cvt_mode`:

drm_cvt_mode
============

.. c:function:: struct drm_display_mode *drm_cvt_mode(struct drm_device *dev, int hdisplay, int vdisplay, int vrefresh, bool reduced, bool interlaced, bool margins)

    create a modeline based on the CVT algorithm

    :param struct drm_device \*dev:
        drm device

    :param int hdisplay:
        hdisplay size

    :param int vdisplay:
        vdisplay size

    :param int vrefresh:
        vrefresh rate

    :param bool reduced:
        whether to use reduced blanking

    :param bool interlaced:
        whether to compute an interlaced mode

    :param bool margins:
        whether to add margins (borders)

.. _`drm_cvt_mode.description`:

Description
-----------

This function is called to generate the modeline based on CVT algorithm
according to the hdisplay, vdisplay, vrefresh.
It is based from the VESA(TM) Coordinated Video Timing Generator by
Graham Loveridge April 9, 2003 available at
http://www.elo.utfsm.cl/~elo212/docs/CVTd6r1.xls

And it is copied from xf86CVTmode in xserver/hw/xfree86/modes/xf86cvt.c.
What I have done is to translate it by using integer calculation.

.. _`drm_cvt_mode.return`:

Return
------

The modeline based on the CVT algorithm stored in a drm_display_mode object.
The display mode object is allocated with \ :c:func:`drm_mode_create`\ . Returns NULL
when no mode could be allocated.

.. _`drm_gtf_mode_complex`:

drm_gtf_mode_complex
====================

.. c:function:: struct drm_display_mode *drm_gtf_mode_complex(struct drm_device *dev, int hdisplay, int vdisplay, int vrefresh, bool interlaced, int margins, int GTF_M, int GTF_2C, int GTF_K, int GTF_2J)

    create the modeline based on the full GTF algorithm

    :param struct drm_device \*dev:
        drm device

    :param int hdisplay:
        hdisplay size

    :param int vdisplay:
        vdisplay size

    :param int vrefresh:
        vrefresh rate.

    :param bool interlaced:
        whether to compute an interlaced mode

    :param int margins:
        desired margin (borders) size

    :param int GTF_M:
        extended GTF formula parameters

    :param int GTF_2C:
        extended GTF formula parameters

    :param int GTF_K:
        extended GTF formula parameters

    :param int GTF_2J:
        extended GTF formula parameters

.. _`drm_gtf_mode_complex.description`:

Description
-----------

GTF feature blocks specify C and J in multiples of 0.5, so we pass them
in here multiplied by two.  For a C of 40, pass in 80.

.. _`drm_gtf_mode_complex.return`:

Return
------

The modeline based on the full GTF algorithm stored in a drm_display_mode object.
The display mode object is allocated with \ :c:func:`drm_mode_create`\ . Returns NULL
when no mode could be allocated.

.. _`drm_gtf_mode`:

drm_gtf_mode
============

.. c:function:: struct drm_display_mode *drm_gtf_mode(struct drm_device *dev, int hdisplay, int vdisplay, int vrefresh, bool interlaced, int margins)

    create the modeline based on the GTF algorithm

    :param struct drm_device \*dev:
        drm device

    :param int hdisplay:
        hdisplay size

    :param int vdisplay:
        vdisplay size

    :param int vrefresh:
        vrefresh rate.

    :param bool interlaced:
        whether to compute an interlaced mode

    :param int margins:
        desired margin (borders) size

.. _`drm_gtf_mode.description`:

Description
-----------

return the modeline based on GTF algorithm

This function is to create the modeline based on the GTF algorithm.

.. _`drm_gtf_mode.generalized-timing-formula-is-derived-from`:

Generalized Timing Formula is derived from
------------------------------------------


     GTF Spreadsheet by Andy Morrish (1/5/97)
     available at http://www.vesa.org

And it is copied from the file of xserver/hw/xfree86/modes/xf86gtf.c.
What I have done is to translate it by using integer calculation.
I also refer to the function of fb_get_mode in the file of
drivers/video/fbmon.c

Standard GTF parameters::

    M = 600
    C = 40
    K = 128
    J = 20

.. _`drm_gtf_mode.return`:

Return
------

The modeline based on the GTF algorithm stored in a drm_display_mode object.
The display mode object is allocated with \ :c:func:`drm_mode_create`\ . Returns NULL
when no mode could be allocated.

.. _`drm_display_mode_from_videomode`:

drm_display_mode_from_videomode
===============================

.. c:function:: void drm_display_mode_from_videomode(const struct videomode *vm, struct drm_display_mode *dmode)

    fill in \ ``dmode``\  using \ ``vm``\ ,

    :param const struct videomode \*vm:
        videomode structure to use as source

    :param struct drm_display_mode \*dmode:
        drm_display_mode structure to use as destination

.. _`drm_display_mode_from_videomode.description`:

Description
-----------

Fills out \ ``dmode``\  using the display mode specified in \ ``vm``\ .

.. _`drm_display_mode_to_videomode`:

drm_display_mode_to_videomode
=============================

.. c:function:: void drm_display_mode_to_videomode(const struct drm_display_mode *dmode, struct videomode *vm)

    fill in \ ``vm``\  using \ ``dmode``\ ,

    :param const struct drm_display_mode \*dmode:
        drm_display_mode structure to use as source

    :param struct videomode \*vm:
        videomode structure to use as destination

.. _`drm_display_mode_to_videomode.description`:

Description
-----------

Fills out \ ``vm``\  using the display mode specified in \ ``dmode``\ .

.. _`drm_bus_flags_from_videomode`:

drm_bus_flags_from_videomode
============================

.. c:function:: void drm_bus_flags_from_videomode(const struct videomode *vm, u32 *bus_flags)

    extract information about pixelclk and DE polarity from videomode and store it in a separate variable

    :param const struct videomode \*vm:
        videomode structure to use

    :param u32 \*bus_flags:
        information about pixelclk and DE polarity will be stored here

.. _`drm_bus_flags_from_videomode.description`:

Description
-----------

Sets DRM_BUS_FLAG_DE_(LOW|HIGH) and DRM_BUS_FLAG_PIXDATA_(POS|NEG)EDGE
in \ ``bus_flags``\  according to DISPLAY_FLAGS found in \ ``vm``\ 

.. _`of_get_drm_display_mode`:

of_get_drm_display_mode
=======================

.. c:function:: int of_get_drm_display_mode(struct device_node *np, struct drm_display_mode *dmode, u32 *bus_flags, int index)

    get a drm_display_mode from devicetree

    :param struct device_node \*np:
        device_node with the timing specification

    :param struct drm_display_mode \*dmode:
        will be set to the return value

    :param u32 \*bus_flags:
        information about pixelclk and DE polarity

    :param int index:
        index into the list of display timings in devicetree

.. _`of_get_drm_display_mode.description`:

Description
-----------

This function is expensive and should only be used, if only one mode is to be
read from DT. To get multiple modes start with of_get_display_timings and
work with that instead.

.. _`of_get_drm_display_mode.return`:

Return
------

0 on success, a negative errno code when no of videomode node was found.

.. _`drm_mode_set_name`:

drm_mode_set_name
=================

.. c:function:: void drm_mode_set_name(struct drm_display_mode *mode)

    set the name on a mode

    :param struct drm_display_mode \*mode:
        name will be set in this mode

.. _`drm_mode_set_name.description`:

Description
-----------

Set the name of \ ``mode``\  to a standard format which is <hdisplay>x<vdisplay>
with an optional 'i' suffix for interlaced modes.

.. _`drm_mode_hsync`:

drm_mode_hsync
==============

.. c:function:: int drm_mode_hsync(const struct drm_display_mode *mode)

    get the hsync of a mode

    :param const struct drm_display_mode \*mode:
        mode

.. _`drm_mode_hsync.return`:

Return
------

\ ``modes``\ 's hsync rate in kHz, rounded to the nearest integer. Calculates the
value first if it is not yet set.

.. _`drm_mode_vrefresh`:

drm_mode_vrefresh
=================

.. c:function:: int drm_mode_vrefresh(const struct drm_display_mode *mode)

    get the vrefresh of a mode

    :param const struct drm_display_mode \*mode:
        mode

.. _`drm_mode_vrefresh.return`:

Return
------

\ ``modes``\ 's vrefresh rate in Hz, rounded to the nearest integer. Calculates the
value first if it is not yet set.

.. _`drm_mode_get_hv_timing`:

drm_mode_get_hv_timing
======================

.. c:function:: void drm_mode_get_hv_timing(const struct drm_display_mode *mode, int *hdisplay, int *vdisplay)

    Fetches hdisplay/vdisplay for given mode

    :param const struct drm_display_mode \*mode:
        mode to query

    :param int \*hdisplay:
        hdisplay value to fill in

    :param int \*vdisplay:
        vdisplay value to fill in

.. _`drm_mode_get_hv_timing.description`:

Description
-----------

The vdisplay value will be doubled if the specified mode is a stereo mode of
the appropriate layout.

.. _`drm_mode_set_crtcinfo`:

drm_mode_set_crtcinfo
=====================

.. c:function:: void drm_mode_set_crtcinfo(struct drm_display_mode *p, int adjust_flags)

    set CRTC modesetting timing parameters

    :param struct drm_display_mode \*p:
        mode

    :param int adjust_flags:
        a combination of adjustment flags

.. _`drm_mode_set_crtcinfo.description`:

Description
-----------

Setup the CRTC modesetting timing parameters for \ ``p``\ , adjusting if necessary.

- The CRTC_INTERLACE_HALVE_V flag can be used to halve vertical timings of
  interlaced modes.
- The CRTC_STEREO_DOUBLE flag can be used to compute the timings for
  buffers containing two eyes (only adjust the timings when needed, eg. for
  "frame packing" or "side by side full").
- The CRTC_NO_DBLSCAN and CRTC_NO_VSCAN flags request that adjustment *not*
  be performed for doublescan and vscan > 1 modes respectively.

.. _`drm_mode_copy`:

drm_mode_copy
=============

.. c:function:: void drm_mode_copy(struct drm_display_mode *dst, const struct drm_display_mode *src)

    copy the mode

    :param struct drm_display_mode \*dst:
        mode to overwrite

    :param const struct drm_display_mode \*src:
        mode to copy

.. _`drm_mode_copy.description`:

Description
-----------

Copy an existing mode into another mode, preserving the object id and
list head of the destination mode.

.. _`drm_mode_duplicate`:

drm_mode_duplicate
==================

.. c:function:: struct drm_display_mode *drm_mode_duplicate(struct drm_device *dev, const struct drm_display_mode *mode)

    allocate and duplicate an existing mode

    :param struct drm_device \*dev:
        drm_device to allocate the duplicated mode for

    :param const struct drm_display_mode \*mode:
        mode to duplicate

.. _`drm_mode_duplicate.description`:

Description
-----------

Just allocate a new mode, copy the existing mode into it, and return
a pointer to it.  Used to create new instances of established modes.

.. _`drm_mode_duplicate.return`:

Return
------

Pointer to duplicated mode on success, NULL on error.

.. _`drm_mode_equal`:

drm_mode_equal
==============

.. c:function:: bool drm_mode_equal(const struct drm_display_mode *mode1, const struct drm_display_mode *mode2)

    test modes for equality

    :param const struct drm_display_mode \*mode1:
        first mode

    :param const struct drm_display_mode \*mode2:
        second mode

.. _`drm_mode_equal.description`:

Description
-----------

Check to see if \ ``mode1``\  and \ ``mode2``\  are equivalent.

.. _`drm_mode_equal.return`:

Return
------

True if the modes are equal, false otherwise.

.. _`drm_mode_equal_no_clocks`:

drm_mode_equal_no_clocks
========================

.. c:function:: bool drm_mode_equal_no_clocks(const struct drm_display_mode *mode1, const struct drm_display_mode *mode2)

    test modes for equality

    :param const struct drm_display_mode \*mode1:
        first mode

    :param const struct drm_display_mode \*mode2:
        second mode

.. _`drm_mode_equal_no_clocks.description`:

Description
-----------

Check to see if \ ``mode1``\  and \ ``mode2``\  are equivalent, but
don't check the pixel clocks.

.. _`drm_mode_equal_no_clocks.return`:

Return
------

True if the modes are equal, false otherwise.

.. _`drm_mode_equal_no_clocks_no_stereo`:

drm_mode_equal_no_clocks_no_stereo
==================================

.. c:function:: bool drm_mode_equal_no_clocks_no_stereo(const struct drm_display_mode *mode1, const struct drm_display_mode *mode2)

    test modes for equality

    :param const struct drm_display_mode \*mode1:
        first mode

    :param const struct drm_display_mode \*mode2:
        second mode

.. _`drm_mode_equal_no_clocks_no_stereo.description`:

Description
-----------

Check to see if \ ``mode1``\  and \ ``mode2``\  are equivalent, but
don't check the pixel clocks nor the stereo layout.

.. _`drm_mode_equal_no_clocks_no_stereo.return`:

Return
------

True if the modes are equal, false otherwise.

.. _`drm_mode_validate_basic`:

drm_mode_validate_basic
=======================

.. c:function:: enum drm_mode_status drm_mode_validate_basic(const struct drm_display_mode *mode)

    make sure the mode is somewhat sane

    :param const struct drm_display_mode \*mode:
        mode to check

.. _`drm_mode_validate_basic.description`:

Description
-----------

Check that the mode timings are at least somewhat reasonable.
Any hardware specific limits are left up for each driver to check.

.. _`drm_mode_validate_basic.return`:

Return
------

The mode status

.. _`drm_mode_validate_size`:

drm_mode_validate_size
======================

.. c:function:: enum drm_mode_status drm_mode_validate_size(const struct drm_display_mode *mode, int maxX, int maxY)

    make sure modes adhere to size constraints

    :param const struct drm_display_mode \*mode:
        mode to check

    :param int maxX:
        maximum width

    :param int maxY:
        maximum height

.. _`drm_mode_validate_size.description`:

Description
-----------

This function is a helper which can be used to validate modes against size
limitations of the DRM device/connector. If a mode is too big its status
member is updated with the appropriate validation failure code. The list
itself is not changed.

.. _`drm_mode_validate_size.return`:

Return
------

The mode status

.. _`drm_mode_validate_ycbcr420`:

drm_mode_validate_ycbcr420
==========================

.. c:function:: enum drm_mode_status drm_mode_validate_ycbcr420(const struct drm_display_mode *mode, struct drm_connector *connector)

    add 'ycbcr420-only' modes only when allowed

    :param const struct drm_display_mode \*mode:
        mode to check

    :param struct drm_connector \*connector:
        drm connector under action

.. _`drm_mode_validate_ycbcr420.description`:

Description
-----------

This function is a helper which can be used to filter out any YCBCR420
only mode, when the source doesn't support it.

.. _`drm_mode_validate_ycbcr420.return`:

Return
------

The mode status

.. _`drm_mode_prune_invalid`:

drm_mode_prune_invalid
======================

.. c:function:: void drm_mode_prune_invalid(struct drm_device *dev, struct list_head *mode_list, bool verbose)

    remove invalid modes from mode list

    :param struct drm_device \*dev:
        DRM device

    :param struct list_head \*mode_list:
        list of modes to check

    :param bool verbose:
        be verbose about it

.. _`drm_mode_prune_invalid.description`:

Description
-----------

This helper function can be used to prune a display mode list after
validation has been completed. All modes who's status is not MODE_OK will be
removed from the list, and if \ ``verbose``\  the status code and mode name is also
printed to dmesg.

.. _`drm_mode_compare`:

drm_mode_compare
================

.. c:function:: int drm_mode_compare(void *priv, struct list_head *lh_a, struct list_head *lh_b)

    compare modes for favorability

    :param void \*priv:
        unused

    :param struct list_head \*lh_a:
        list_head for first mode

    :param struct list_head \*lh_b:
        list_head for second mode

.. _`drm_mode_compare.description`:

Description
-----------

Compare two modes, given by \ ``lh_a``\  and \ ``lh_b``\ , returning a value indicating
which is better.

.. _`drm_mode_compare.return`:

Return
------

Negative if \ ``lh_a``\  is better than \ ``lh_b``\ , zero if they're equivalent, or
positive if \ ``lh_b``\  is better than \ ``lh_a``\ .

.. _`drm_mode_sort`:

drm_mode_sort
=============

.. c:function:: void drm_mode_sort(struct list_head *mode_list)

    sort mode list

    :param struct list_head \*mode_list:
        list of drm_display_mode structures to sort

.. _`drm_mode_sort.description`:

Description
-----------

Sort \ ``mode_list``\  by favorability, moving good modes to the head of the list.

.. _`drm_mode_connector_list_update`:

drm_mode_connector_list_update
==============================

.. c:function:: void drm_mode_connector_list_update(struct drm_connector *connector)

    update the mode list for the connector

    :param struct drm_connector \*connector:
        the connector to update

.. _`drm_mode_connector_list_update.description`:

Description
-----------

This moves the modes from the \ ``connector``\  probed_modes list
to the actual mode list. It compares the probed mode against the current
list and only adds different/new modes.

This is just a helper functions doesn't validate any modes itself and also
doesn't prune any invalid modes. Callers need to do that themselves.

.. _`drm_mode_parse_command_line_for_connector`:

drm_mode_parse_command_line_for_connector
=========================================

.. c:function:: bool drm_mode_parse_command_line_for_connector(const char *mode_option, struct drm_connector *connector, struct drm_cmdline_mode *mode)

    parse command line modeline for connector

    :param const char \*mode_option:
        optional per connector mode option

    :param struct drm_connector \*connector:
        connector to parse modeline for

    :param struct drm_cmdline_mode \*mode:
        preallocated drm_cmdline_mode structure to fill out

.. _`drm_mode_parse_command_line_for_connector.description`:

Description
-----------

This parses \ ``mode_option``\  command line modeline for modes and options to
configure the connector. If \ ``mode_option``\  is NULL the default command line
modeline in fb_mode_option will be parsed instead.

This uses the same parameters as the fb modedb.c, except for an extra
force-enable, force-enable-digital and force-disable bit at the end:

<xres>x<yres>[M][R][-<bpp>][@<refresh>][i][m][eDd]

The intermediate drm_cmdline_mode structure is required to store additional
options from the command line modline like the force-enable/disable flag.

.. _`drm_mode_parse_command_line_for_connector.return`:

Return
------

True if a valid modeline has been parsed, false otherwise.

.. _`drm_mode_create_from_cmdline_mode`:

drm_mode_create_from_cmdline_mode
=================================

.. c:function:: struct drm_display_mode *drm_mode_create_from_cmdline_mode(struct drm_device *dev, struct drm_cmdline_mode *cmd)

    convert a command line modeline into a DRM display mode

    :param struct drm_device \*dev:
        DRM device to create the new mode for

    :param struct drm_cmdline_mode \*cmd:
        input command line modeline

.. _`drm_mode_create_from_cmdline_mode.return`:

Return
------

Pointer to converted mode on success, NULL on error.

.. _`drm_mode_convert_to_umode`:

drm_mode_convert_to_umode
=========================

.. c:function:: void drm_mode_convert_to_umode(struct drm_mode_modeinfo *out, const struct drm_display_mode *in)

    convert a drm_display_mode into a modeinfo

    :param struct drm_mode_modeinfo \*out:
        drm_mode_modeinfo struct to return to the user

    :param const struct drm_display_mode \*in:
        drm_display_mode to use

.. _`drm_mode_convert_to_umode.description`:

Description
-----------

Convert a drm_display_mode into a drm_mode_modeinfo structure to return to
the user.

.. _`drm_mode_convert_umode`:

drm_mode_convert_umode
======================

.. c:function:: int drm_mode_convert_umode(struct drm_display_mode *out, const struct drm_mode_modeinfo *in)

    convert a modeinfo into a drm_display_mode

    :param struct drm_display_mode \*out:
        drm_display_mode to return to the user

    :param const struct drm_mode_modeinfo \*in:
        drm_mode_modeinfo to use

.. _`drm_mode_convert_umode.description`:

Description
-----------

Convert a drm_mode_modeinfo into a drm_display_mode structure to return to
the caller.

.. _`drm_mode_convert_umode.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_is_420_only`:

drm_mode_is_420_only
====================

.. c:function:: bool drm_mode_is_420_only(const struct drm_display_info *display, const struct drm_display_mode *mode)

    if a given videomode can be only supported in YCBCR420 output format

    :param const struct drm_display_info \*display:
        display under action

    :param const struct drm_display_mode \*mode:
        video mode to be tested.

.. _`drm_mode_is_420_only.return`:

Return
------

true if the mode can be supported in YCBCR420 format
false if not.

.. _`drm_mode_is_420_also`:

drm_mode_is_420_also
====================

.. c:function:: bool drm_mode_is_420_also(const struct drm_display_info *display, const struct drm_display_mode *mode)

    if a given videomode can be supported in YCBCR420 output format also (along with RGB/YCBCR444/422)

    :param const struct drm_display_info \*display:
        display under action.

    :param const struct drm_display_mode \*mode:
        video mode to be tested.

.. _`drm_mode_is_420_also.return`:

Return
------

true if the mode can be support YCBCR420 format
false if not.

.. _`drm_mode_is_420`:

drm_mode_is_420
===============

.. c:function:: bool drm_mode_is_420(const struct drm_display_info *display, const struct drm_display_mode *mode)

    if a given videomode can be supported in YCBCR420 output format

    :param const struct drm_display_info \*display:
        display under action.

    :param const struct drm_display_mode \*mode:
        video mode to be tested.

.. _`drm_mode_is_420.return`:

Return
------

true if the mode can be supported in YCBCR420 format
false if not.

.. This file was automatic generated / don't edit.

