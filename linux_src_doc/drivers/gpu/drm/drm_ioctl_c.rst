.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_ioctl.c

.. _`drm_noop`:

drm_noop
========

.. c:function:: int drm_noop(struct drm_device *dev, void *data, struct drm_file *file_priv)

    DRM no-op ioctl implemntation

    :param struct drm_device \*dev:
        DRM device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        DRM file for the ioctl call

.. _`drm_noop.description`:

Description
-----------

This no-op implementation for drm ioctls is useful for deprecated
functionality where we can't return a failure code because existing userspace
checks the result of the ioctl, but doesn't care about the action.

Always returns successfully with 0.

.. _`drm_invalid_op`:

drm_invalid_op
==============

.. c:function:: int drm_invalid_op(struct drm_device *dev, void *data, struct drm_file *file_priv)

    DRM invalid ioctl implemntation

    :param struct drm_device \*dev:
        DRM device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        DRM file for the ioctl call

.. _`drm_invalid_op.description`:

Description
-----------

This no-op implementation for drm ioctls is useful for deprecated
functionality where we really don't want to allow userspace to call the ioctl
any more. This is the case for old ums interfaces for drivers that
transitioned to kms gradually and so kept the old legacy tables around. This
only applies to radeon and i915 kms drivers, other drivers shouldn't need to
use this function.

Always fails with a return value of -EINVAL.

.. _`drm_ioctl`:

drm_ioctl
=========

.. c:function:: long drm_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    ioctl callback implementation for DRM drivers

    :param struct file \*filp:
        file this ioctl is called on

    :param unsigned int cmd:
        ioctl cmd number

    :param unsigned long arg:
        user argument

.. _`drm_ioctl.description`:

Description
-----------

Looks up the ioctl function in the ::ioctls table, checking for root
previleges if so required, and dispatches to the respective function.

.. _`drm_ioctl.return`:

Return
------

Zero on success, negative error code on failure.

.. _`drm_ioctl_flags`:

drm_ioctl_flags
===============

.. c:function:: bool drm_ioctl_flags(unsigned int nr, unsigned int *flags)

    Check for core ioctl and return ioctl permission flags

    :param unsigned int nr:
        ioctl number

    :param unsigned int \*flags:
        where to return the ioctl permission flags

.. _`drm_ioctl_flags.description`:

Description
-----------

This ioctl is only used by the vmwgfx driver to augment the access checks
done by the drm core and insofar a pretty decent layering violation. This
shouldn't be used by any drivers.

.. _`drm_ioctl_flags.return`:

Return
------

True if the \ ``nr``\  corresponds to a DRM core ioctl number, false otherwise.

.. This file was automatic generated / don't edit.

