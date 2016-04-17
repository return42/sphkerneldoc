.. -*- coding: utf-8; mode: rst -*-

============
intel_bios.c
============


.. _`psb_intel_init_bios`:

psb_intel_init_bios
===================

.. c:function:: int psb_intel_init_bios (struct drm_device *dev)

    initialize VBIOS settings & find VBT

    :param struct drm_device \*dev:
        DRM device



.. _`psb_intel_init_bios.description`:

Description
-----------

Loads the Video BIOS and checks that the VBT exists.  Sets scratch registers
to appropriate values.

VBT existence is a sanity check that is relied on by other i830_bios.c code.
Note that it would be better to use a BIOS call to get the VBT, as BIOSes may
feed an updated VBT back through that, compared to what we'll fetch using
this method of groping around in the BIOS data.

Returns 0 on success, nonzero on failure.



.. _`psb_intel_destroy_bios`:

psb_intel_destroy_bios
======================

.. c:function:: void psb_intel_destroy_bios (struct drm_device *dev)

    :param struct drm_device \*dev:

        *undescribed*

