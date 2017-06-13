.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_debugfs_crc.c

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

