.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_kms.c

.. _`vc4_atomic_commit`:

vc4_atomic_commit
=================

.. c:function:: int vc4_atomic_commit(struct drm_device *dev, struct drm_atomic_state *state, bool nonblock)

    commit validated state object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

    :param bool nonblock:
        nonblocking commit

.. _`vc4_atomic_commit.description`:

Description
-----------

This function commits a with \ :c:func:`drm_atomic_helper_check`\  pre-validated state
object. This can still fail when e.g. the framebuffer reservation fails. For
now this doesn't implement asynchronous commits.

RETURNS
Zero for success or -errno.

.. This file was automatic generated / don't edit.

