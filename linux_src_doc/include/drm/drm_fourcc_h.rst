.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_fourcc.h

.. _`drm_format_info`:

struct drm_format_info
======================

.. c:type:: struct drm_format_info

    information about a DRM format

.. _`drm_format_info.definition`:

Definition
----------

.. code-block:: c

    struct drm_format_info {
        u32 format;
        u8 depth;
        u8 num_planes;
        u8 cpp[3];
        u8 hsub;
        u8 vsub;
    }

.. _`drm_format_info.members`:

Members
-------

format
    4CC format identifier (DRM_FORMAT_*)

depth
    Color depth (number of bits per pixel excluding padding bits),
    valid for a subset of RGB formats only. This is a legacy field, do not
    use in new code and set to 0 for new formats.

num_planes
    Number of color planes (1 to 3)

cpp
    Number of bytes per pixel (per plane)

hsub
    Horizontal chroma subsampling factor

vsub
    Vertical chroma subsampling factor

.. _`drm_format_name_buf`:

struct drm_format_name_buf
==========================

.. c:type:: struct drm_format_name_buf

    name of a DRM format

.. _`drm_format_name_buf.definition`:

Definition
----------

.. code-block:: c

    struct drm_format_name_buf {
        char str[32];
    }

.. _`drm_format_name_buf.members`:

Members
-------

str
    string buffer containing the format name

.. This file was automatic generated / don't edit.

