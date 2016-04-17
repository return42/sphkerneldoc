.. -*- coding: utf-8; mode: rst -*-

========
vc4_bo.c
========


.. _`vc4_create_object`:

vc4_create_object
=================

.. c:function:: struct drm_gem_object *vc4_create_object (struct drm_device *dev, size_t size)

    Implementation of driver->gem_create_object.

    :param struct drm_device \*dev:

        *undescribed*

    :param size_t size:

        *undescribed*



.. _`vc4_create_object.description`:

Description
-----------


This lets the CMA helpers allocate object structs for us, and keep
our BO stats correct.

