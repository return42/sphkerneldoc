.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_debugfs_crc.c

.. _`crc-abi`:

CRC ABI
=======

DRM device drivers can provide to userspace CRC information of each frame as
it reached a given hardware component (a CRC sampling "source").

Userspace can control generation of CRCs in a given CRTC by writing to the
file dri/0/crtc-N/crc/control in debugfs, with N being the index of the CRTC.
Accepted values are source names (which are driver-specific) and the "auto"
keyword, which will let the driver select a default source of frame CRCs
for this CRTC.

Once frame CRC generation is enabled, userspace can capture them by reading
the dri/0/crtc-N/crc/data file. Each line in that file contains the frame
number in the first field and then a number of unsigned integer fields
containing the CRC data. Fields are separated by a single space and the number
of CRC fields is source-specific.

Note that though in some cases the CRC is computed in a specified way and on
the frame contents as supplied by userspace (eDP 1.3), in general the CRC
computation is performed in an unspecified way and on frame contents that have
been already processed in also an unspecified way and thus userspace cannot
rely on being able to generate matching CRC values for the frame contents that
it submits. In this general case, the maximum userspace can do is to compare
the reported CRCs of frames that should have the same contents.

On the driver side the implementation effort is minimal, drivers only need to
implement \ :c:type:`drm_crtc_funcs.set_crc_source <drm_crtc_funcs>`\ . The debugfs files are automatically
set up if that vfunc is set. CRC samples need to be captured in the driver by
calling \ :c:func:`drm_crtc_add_crc_entry`\ .

.. _`drm_crtc_add_crc_entry`:

drm_crtc_add_crc_entry
======================

.. c:function:: int drm_crtc_add_crc_entry(struct drm_crtc *crtc, bool has_frame, uint32_t frame, uint32_t *crcs)

    Add entry with CRC information for a frame

    :param struct drm_crtc \*crtc:
        CRTC to which the frame belongs

    :param bool has_frame:
        whether this entry has a frame number to go with

    :param uint32_t frame:
        number of the frame these CRCs are about

    :param uint32_t \*crcs:
        array of CRC values, with length matching #drm_crtc_crc.values_cnt

.. _`drm_crtc_add_crc_entry.description`:

Description
-----------

For each frame, the driver polls the source of CRCs for new data and calls
this function to add them to the buffer from where userspace reads.

.. This file was automatic generated / don't edit.

