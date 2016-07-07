.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_edid.h

.. _`drm_eld_mnl`:

drm_eld_mnl
===========

.. c:function:: int drm_eld_mnl(const uint8_t *eld)

    Get ELD monitor name length in bytes.

    :param const uint8_t \*eld:
        pointer to an eld memory structure with mnl set

.. _`drm_eld_sad`:

drm_eld_sad
===========

.. c:function:: const uint8_t *drm_eld_sad(const uint8_t *eld)

    Get ELD SAD structures.

    :param const uint8_t \*eld:
        pointer to an eld memory structure with sad_count set

.. _`drm_eld_sad_count`:

drm_eld_sad_count
=================

.. c:function:: int drm_eld_sad_count(const uint8_t *eld)

    Get ELD SAD count.

    :param const uint8_t \*eld:
        pointer to an eld memory structure with sad_count set

.. _`drm_eld_calc_baseline_block_size`:

drm_eld_calc_baseline_block_size
================================

.. c:function:: int drm_eld_calc_baseline_block_size(const uint8_t *eld)

    Calculate baseline block size in bytes

    :param const uint8_t \*eld:
        pointer to an eld memory structure with mnl and sad_count set

.. _`drm_eld_calc_baseline_block_size.description`:

Description
-----------

This is a helper for determining the payload size of the baseline block, in
bytes, for e.g. setting the Baseline_ELD_Len field in the ELD header block.

.. _`drm_eld_size`:

drm_eld_size
============

.. c:function:: int drm_eld_size(const uint8_t *eld)

    Get ELD size in bytes

    :param const uint8_t \*eld:
        pointer to a complete eld memory structure

.. _`drm_eld_size.description`:

Description
-----------

The returned value does not include the vendor block. It's vendor specific,
and comprises of the remaining bytes in the ELD memory buffer after
\ :c:func:`drm_eld_size`\  bytes of header and baseline block.

The returned value is guaranteed to be a multiple of 4.

.. _`drm_eld_get_conn_type`:

drm_eld_get_conn_type
=====================

.. c:function:: u8 drm_eld_get_conn_type(const uint8_t *eld)

    Get device type hdmi/dp connected

    :param const uint8_t \*eld:
        pointer to an ELD memory structure

.. _`drm_eld_get_conn_type.description`:

Description
-----------

The caller need to use \ ``DRM_ELD_CONN_TYPE_HDMI``\  or \ ``DRM_ELD_CONN_TYPE_DP``\  to
identify the display type connected.

.. This file was automatic generated / don't edit.

