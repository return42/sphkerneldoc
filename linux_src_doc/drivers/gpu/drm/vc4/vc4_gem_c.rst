.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_gem.c

.. _`vc4_cl_lookup_bos`:

vc4_cl_lookup_bos
=================

.. c:function:: int vc4_cl_lookup_bos(struct drm_device *dev, struct drm_file *file_priv, struct vc4_exec_info *exec)

    Sets up exec->bo[] with the GEM objects referenced by the job.

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        DRM file for this fd

    :param struct vc4_exec_info \*exec:
        V3D job being set up

.. _`vc4_cl_lookup_bos.description`:

Description
-----------

The command validator needs to reference BOs by their index within
the submitted job's BO list.  This does the validation of the job's
BO list and reference counting for the lifetime of the job.

Note that this function doesn't need to unreference the BOs on
failure, because that will happen at \ :c:func:`vc4_complete_exec`\  time.

.. _`vc4_submit_cl_ioctl`:

vc4_submit_cl_ioctl
===================

.. c:function:: int vc4_submit_cl_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Submits a job (frame) to the VC4.

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl argument

    :param struct drm_file \*file_priv:
        DRM file for this fd

.. _`vc4_submit_cl_ioctl.description`:

Description
-----------

This is the main entrypoint for userspace to submit a 3D frame to
the GPU.  Userspace provides the binner command list (if
applicable), and the kernel sets up the render command list to draw
to the framebuffer described in the ioctl, using the command lists
that the 3D engine's binner will produce.

.. This file was automatic generated / don't edit.

