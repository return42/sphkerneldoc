.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/omap_drv.c

.. _`dev_lastclose`:

dev_lastclose
=============

.. c:function:: void dev_lastclose(struct drm_device *dev)

    clean up after all DRM clients have exited

    :param struct drm_device \*dev:
        DRM device

.. _`dev_lastclose.description`:

Description
-----------

Take care of cleaning up after all DRM clients have exited.  In the
mode setting case, we want to restore the kernel's initial mode (just
in case the last client left us in a bad state).

.. This file was automatic generated / don't edit.

