.. -*- coding: utf-8; mode: rst -*-

=========
vc4_kms.c
=========


.. _`vc4-kms`:

VC4 KMS
=======

This is the general code for implementing KMS mode setting that
doesn't clearly associate with any of the other objects (plane,
crtc, HDMI encoder).



.. _`vc4_atomic_commit`:

vc4_atomic_commit
=================

.. c:function:: int vc4_atomic_commit (struct drm_device *dev, struct drm_atomic_state *state, bool async)

    commit validated state object

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        the driver state object

    :param bool async:
        asynchronous commit



.. _`vc4_atomic_commit.description`:

Description
-----------

This function commits a with :c:func:`drm_atomic_helper_check` pre-validated state
object. This can still fail when e.g. the framebuffer reservation fails. For
now this doesn't implement asynchronous commits.

RETURNS
Zero for success or -errno.

