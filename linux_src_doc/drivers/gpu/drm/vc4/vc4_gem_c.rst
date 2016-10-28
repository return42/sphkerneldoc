.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_gem.c

.. _`vc4_cl_lookup_bos`:

vc4_cl_lookup_bos
=================

.. c:function:: int vc4_cl_lookup_bos(struct drm_device *dev, struct drm_file *file_priv, struct vc4_exec_info *exec)

    use in the command validator that actually writes relocated addresses pointing to them.

    :param struct drm_device \*dev:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

    :param struct vc4_exec_info \*exec:
        *undescribed*

.. _`vc4_submit_cl_ioctl`:

vc4_submit_cl_ioctl
===================

.. c:function:: int vc4_submit_cl_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`vc4_submit_cl_ioctl.description`:

Description
-----------

This is what is called batchbuffer emitting on other hardware.

.. This file was automatic generated / don't edit.

