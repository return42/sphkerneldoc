.. -*- coding: utf-8; mode: rst -*-

===========
drm_ioc32.c
===========


.. _`drm_compat_ioctl`:

drm_compat_ioctl
================

.. c:function:: long drm_compat_ioctl (struct file *filp, unsigned int cmd, unsigned long arg)

    bit process running under a 64-bit kernel performs an ioctl on /dev/drm.

    :param struct file \*filp:

        *undescribed*

    :param unsigned int cmd:

        *undescribed*

    :param unsigned long arg:

        *undescribed*



.. _`drm_compat_ioctl.description`:

Description
-----------


\param file_priv DRM file private.
\param cmd command.
\param arg user argument.
\return zero on success or negative number on failure.

