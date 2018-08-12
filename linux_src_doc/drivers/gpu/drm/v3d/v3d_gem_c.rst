.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_gem.c

.. _`v3d_cl_lookup_bos`:

v3d_cl_lookup_bos
=================

.. c:function:: int v3d_cl_lookup_bos(struct drm_device *dev, struct drm_file *file_priv, struct drm_v3d_submit_cl *args, struct v3d_exec_info *exec)

    Sets up exec->bo[] with the GEM objects referenced by the job.

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        DRM file for this fd

    :param struct drm_v3d_submit_cl \*args:
        *undescribed*

    :param struct v3d_exec_info \*exec:
        V3D job being set up

.. _`v3d_cl_lookup_bos.description`:

Description
-----------

The command validator needs to reference BOs by their index within
the submitted job's BO list.  This does the validation of the job's
BO list and reference counting for the lifetime of the job.

Note that this function doesn't need to unreference the BOs on
failure, because that will happen at \ :c:func:`v3d_exec_cleanup`\  time.

.. _`v3d_submit_cl_ioctl`:

v3d_submit_cl_ioctl
===================

.. c:function:: int v3d_submit_cl_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Submits a job (frame) to the V3D.

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl argument

    :param struct drm_file \*file_priv:
        DRM file for this fd

.. _`v3d_submit_cl_ioctl.description`:

Description
-----------

This is the main entrypoint for userspace to submit a 3D frame to
the GPU.  Userspace provides the binner command list (if
applicable), and the kernel sets up the render command list to draw
to the framebuffer described in the ioctl, using the command lists
that the 3D engine's binner will produce.

.. This file was automatic generated / don't edit.

