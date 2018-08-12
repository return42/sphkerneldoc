.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/uapi/drm/drm.h

.. _`drm_drawable_info_type_t`:

typedef drm_drawable_info_type_t
================================

.. c:type:: typedef drm_drawable_info_type_t


.. _`drm_client_cap_stereo_3d`:

DRM_CLIENT_CAP_STEREO_3D
========================

.. c:function::  DRM_CLIENT_CAP_STEREO_3D()

.. _`drm_client_cap_stereo_3d.description`:

Description
-----------

if set to 1, the DRM core will expose the stereo 3D capabilities of the
monitor by advertising the supported 3D layouts in the flags of struct
drm_mode_modeinfo.

.. _`drm_client_cap_universal_planes`:

DRM_CLIENT_CAP_UNIVERSAL_PLANES
===============================

.. c:function::  DRM_CLIENT_CAP_UNIVERSAL_PLANES()

.. _`drm_client_cap_universal_planes.description`:

Description
-----------

If set to 1, the DRM core will expose all planes (overlay, primary, and
cursor) to userspace.

.. _`drm_client_cap_atomic`:

DRM_CLIENT_CAP_ATOMIC
=====================

.. c:function::  DRM_CLIENT_CAP_ATOMIC()

.. _`drm_client_cap_atomic.description`:

Description
-----------

If set to 1, the DRM core will expose atomic properties to userspace

.. _`drm_client_cap_aspect_ratio`:

DRM_CLIENT_CAP_ASPECT_RATIO
===========================

.. c:function::  DRM_CLIENT_CAP_ASPECT_RATIO()

.. _`drm_client_cap_aspect_ratio.description`:

Description
-----------

If set to 1, the DRM core will provide aspect ratio information in modes.

.. _`drm_command_base`:

DRM_COMMAND_BASE
================

.. c:function::  DRM_COMMAND_BASE()

    The device specific ioctl range is from 0x40 to 0x9f. Generic IOCTLS restart at 0xA0.

.. _`drm_command_base.description`:

Description
-----------

\sa \ :c:func:`drmCommandNone`\ , \ :c:func:`drmCommandRead`\ , \ :c:func:`drmCommandWrite`\ , and
\ :c:func:`drmCommandReadWrite`\ .

.. This file was automatic generated / don't edit.

