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

    :param ellipsis ellipsis:
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

    :param ellipsis ellipsis:
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

.. _`drm_dev_debug_ratelimited.description`:

Description
-----------

\param fmt \ :c:func:`printf`\  like format string.
\param arg arguments

.. _`drm_drv_uses_atomic_modeset`:

drm_drv_uses_atomic_modeset
===========================

.. c:function:: bool drm_drv_uses_atomic_modeset(struct drm_device *dev)

    check if the driver implements \ :c:func:`atomic_commit`\ 

    :param struct drm_device \*dev:
        DRM device

.. _`drm_drv_uses_atomic_modeset.description`:

Description
-----------

This check is useful if drivers do not have DRIVER_ATOMIC set but
have atomic modesetting internally implemented.

.. This file was automatic generated / don't edit.

