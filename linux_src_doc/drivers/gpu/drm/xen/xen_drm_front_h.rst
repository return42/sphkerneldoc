.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/xen/xen_drm_front.h

.. _`driver-modes-of-operation-in-terms-of-display-buffers-used`:

Driver modes of operation in terms of display buffers used
==========================================================

Depending on the requirements for the para-virtualized environment, namely
requirements dictated by the accompanying DRM/(v)GPU drivers running in both
host and guest environments, display buffers can be allocated by either
frontend driver or backend.

.. _`buffers-allocated-by-the-frontend-driver`:

Buffers allocated by the frontend driver
========================================

In this mode of operation driver allocates buffers from system memory.

Note! If used with accompanying DRM/(v)GPU drivers this mode of operation
may require IOMMU support on the platform, so accompanying DRM/vGPU
hardware can still reach display buffer memory while importing PRIME
buffers from the frontend driver.

.. _`buffers-allocated-by-the-backend`:

Buffers allocated by the backend
================================

This mode of operation is run-time configured via guest domain configuration
through XenStore entries.

For systems which do not provide IOMMU support, but having specific
requirements for display buffers it is possible to allocate such buffers
at backend side and share those with the frontend.
For example, if host domain is 1:1 mapped and has DRM/GPU hardware expecting
physically contiguous memory, this allows implementing zero-copying
use-cases.

Note, while using this scenario the following should be considered:

#. If guest domain dies then pages/grants received from the backend
   cannot be claimed back

#. Misbehaving guest may send too many requests to the
   backend exhausting its grant references and memory
   (consider this from security POV)

.. _`driver-limitations`:

Driver limitations
==================

#. Only primary plane without additional properties is supported.

#. Only one video mode per connector supported which is configured
   via XenStore.

#. All CRTCs operate at fixed frequency of 60Hz.

.. This file was automatic generated / don't edit.

