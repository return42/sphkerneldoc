.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drmP.h

.. _`drm_dev_error`:

DRM_DEV_ERROR
=============

.. c:function::  DRM_DEV_ERROR( dev,  fmt,  ...)

    :param  dev:
        *undescribed*

    :param  fmt:
        *undescribed*

    :param ... :
        variable arguments

.. _`drm_dev_error.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_dev_error_ratelimited`:

DRM_DEV_ERROR_RATELIMITED
=========================

.. c:function::  DRM_DEV_ERROR_RATELIMITED( dev,  fmt,  ...)

    :param  dev:
        *undescribed*

    :param  fmt:
        *undescribed*

    :param ... :
        variable arguments

.. _`drm_dev_error_ratelimited.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_dev_debug`:

DRM_DEV_DEBUG
=============

.. c:function::  DRM_DEV_DEBUG( dev,  fmt,  args...)

    :param  dev:
        *undescribed*

    :param  fmt:
        *undescribed*

    :param  args...:
        variable arguments

.. _`drm_dev_debug.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_dev_debug_ratelimited`:

DRM_DEV_DEBUG_RATELIMITED
=========================

.. c:function::  DRM_DEV_DEBUG_RATELIMITED( dev,  fmt,  args...)

    :param  dev:
        *undescribed*

    :param  fmt:
        *undescribed*

    :param  args...:
        variable arguments

.. _`drm_dev_debug_ratelimited.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_ioctl_t`:

drm_ioctl_t
===========

.. c:function:: int drm_ioctl_t(struct drm_device *dev, void *data, struct drm_file *file_priv)

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

.. This file was automatic generated / don't edit.

