.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_ioc32.c

.. _`radeon_compat_ioctl`:

radeon_compat_ioctl
===================

.. c:function:: long radeon_compat_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    bit process running under a 64-bit kernel performs an ioctl on /dev/dri/card<n>.

    :param struct file \*filp:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`radeon_compat_ioctl.description`:

Description
-----------

\param filp file pointer.
\param cmd command.
\param arg user argument.
\return zero on success or negative number on failure.

.. This file was automatic generated / don't edit.

