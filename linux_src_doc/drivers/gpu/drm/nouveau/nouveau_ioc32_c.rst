.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nouveau_ioc32.c

.. _`nouveau_compat_ioctl`:

nouveau_compat_ioctl
====================

.. c:function:: long nouveau_compat_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    bit process running under a 64-bit kernel performs an ioctl on /dev/dri/card<n>.

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param cmd:
        *undescribed*
    :type cmd: unsigned int

    :param arg:
        *undescribed*
    :type arg: unsigned long

.. _`nouveau_compat_ioctl.description`:

Description
-----------

\param filp file pointer.
\param cmd command.
\param arg user argument.
\return zero on success or negative number on failure.

.. This file was automatic generated / don't edit.

