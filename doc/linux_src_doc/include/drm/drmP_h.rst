.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drmP.h

.. _`drm_error`:

DRM_ERROR
=========

.. c:function::  DRM_ERROR( fmt,  ...)

    :param  fmt:
        *undescribed*

    :param ... :
        variable arguments

.. _`drm_error.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_error_ratelimited`:

DRM_ERROR_RATELIMITED
=====================

.. c:function::  DRM_ERROR_RATELIMITED( fmt,  ...)

    :param  fmt:
        *undescribed*

    :param ... :
        variable arguments

.. _`drm_error_ratelimited.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_debug`:

DRM_DEBUG
=========

.. c:function::  DRM_DEBUG( fmt,  args...)

    :param  fmt:
        *undescribed*

    :param  args...:
        variable arguments

.. _`drm_debug.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_ioctl_t`:

drm_ioctl_t
===========

.. c:function:: typedef int drm_ioctl_t(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`drm_ioctl_t.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private pointer.
\param cmd command.
\param arg argument.

.. _`drm_ioctl_def_drv`:

DRM_IOCTL_DEF_DRV
=================

.. c:function::  DRM_IOCTL_DEF_DRV( ioctl,  _func,  _flags)

    ioctl, for use by \ :c:func:`drm_ioctl`\ .

    :param  ioctl:
        *undescribed*

    :param  _func:
        *undescribed*

    :param  _flags:
        *undescribed*

.. _`drm_crtc_vblank_waitqueue`:

drm_crtc_vblank_waitqueue
=========================

.. c:function:: wait_queue_head_t *drm_crtc_vblank_waitqueue(struct drm_crtc *crtc)

    get vblank waitqueue for the CRTC

    :param struct drm_crtc \*crtc:
        which CRTC's vblank waitqueue to retrieve

.. _`drm_crtc_vblank_waitqueue.description`:

Description
-----------

This function returns a pointer to the vblank waitqueue for the CRTC.
Drivers can use this to implement vblank waits using \ :c:func:`wait_event`\  & co.

.. This file was automatic generated / don't edit.

