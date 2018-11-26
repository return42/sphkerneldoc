.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_kms.c

.. _`vc4-kms`:

VC4 KMS
=======

This is the general code for implementing KMS mode setting that
doesn't clearly associate with any of the other objects (plane,
crtc, HDMI encoder).

.. _`vc4_atomic_commit`:

vc4_atomic_commit
=================

.. c:function:: int vc4_atomic_commit(struct drm_device *dev, struct drm_atomic_state *state, bool nonblock)

    commit validated state object

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param state:
        the driver state object
    :type state: struct drm_atomic_state \*

    :param nonblock:
        nonblocking commit
    :type nonblock: bool

.. _`vc4_atomic_commit.description`:

Description
-----------

This function commits a with \ :c:func:`drm_atomic_helper_check`\  pre-validated state
object. This can still fail when e.g. the framebuffer reservation fails. For
now this doesn't implement asynchronous commits.

RETURNS
Zero for success or -errno.

.. This file was automatic generated / don't edit.

