.. -*- coding: utf-8; mode: rst -*-

=====
drm.h
=====

.. _`drm_client_cap_stereo_3d`:

DRM_CLIENT_CAP_STEREO_3D
========================

.. c:function:: DRM_CLIENT_CAP_STEREO_3D ()


.. _`drm_client_cap_stereo_3d.description`:

Description
-----------


if set to 1, the DRM core will expose the stereo 3D capabilities of the
monitor by advertising the supported 3D layouts in the flags of struct
drm_mode_modeinfo.


.. _`drm_client_cap_universal_planes`:

DRM_CLIENT_CAP_UNIVERSAL_PLANES
===============================

.. c:function:: DRM_CLIENT_CAP_UNIVERSAL_PLANES ()


.. _`drm_client_cap_universal_planes.description`:

Description
-----------


If set to 1, the DRM core will expose all planes (overlay, primary, and
cursor) to userspace.


.. _`drm_client_cap_atomic`:

DRM_CLIENT_CAP_ATOMIC
=====================

.. c:function:: DRM_CLIENT_CAP_ATOMIC ()


.. _`drm_client_cap_atomic.description`:

Description
-----------


If set to 1, the DRM core will expose atomic properties to userspace


.. _`drm_command_base`:

DRM_COMMAND_BASE
================

.. c:function:: DRM_COMMAND_BASE ()


.. _`drm_command_base.description`:

Description
-----------

The device specific ioctl range is from 0x40 to 0x9f.
Generic IOCTLS restart at 0xA0.

\sa :c:func:`drmCommandNone`, :c:func:`drmCommandRead`, :c:func:`drmCommandWrite`, and
:c:func:`drmCommandReadWrite`.

