.. -*- coding: utf-8; mode: rst -*-

============
msm_atomic.c
============


.. _`msm_atomic_commit`:

msm_atomic_commit
=================

.. c:function:: int msm_atomic_commit (struct drm_device *dev, struct drm_atomic_state *state, bool async)

    commit validated state object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

    :param bool async:
        asynchronous commit



.. _`msm_atomic_commit.description`:

Description
-----------

This function commits a with :c:func:`drm_atomic_helper_check` pre-validated state
object. This can still fail when e.g. the framebuffer reservation fails. For
now this doesn't implement asynchronous commits.

RETURNS
Zero for success or -errno.

