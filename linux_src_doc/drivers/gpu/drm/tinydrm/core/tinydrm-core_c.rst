.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tinydrm/core/tinydrm-core.c

.. _`overview`:

overview
========

This library provides driver helpers for very simple display hardware.

It is based on \ :c:type:`struct drm_simple_display_pipe <drm_simple_display_pipe>`\  coupled with a \ :c:type:`struct drm_connector <drm_connector>`\  which
has only one fixed \ :c:type:`struct drm_display_mode <drm_display_mode>`\ . The framebuffers are backed by the
cma helper and have support for framebuffer flushing (dirty).
fbdev support is also included.

.. _`core`:

core
====

The driver allocates \ :c:type:`struct tinydrm_device <tinydrm_device>`\ , initializes it using
\ :c:func:`devm_tinydrm_init`\ , sets up the pipeline using \ :c:func:`tinydrm_display_pipe_init`\ 
and registers the DRM device using \ :c:func:`devm_tinydrm_register`\ .

.. _`tinydrm_gem_cma_prime_import_sg_table`:

tinydrm_gem_cma_prime_import_sg_table
=====================================

.. c:function:: struct drm_gem_object *tinydrm_gem_cma_prime_import_sg_table(struct drm_device *drm, struct dma_buf_attachment *attach, struct sg_table *sgt)

    Produce a CMA GEM object from another driver's scatter/gather table of pinned pages

    :param drm:
        DRM device to import into
    :type drm: struct drm_device \*

    :param attach:
        DMA-BUF attachment
    :type attach: struct dma_buf_attachment \*

    :param sgt:
        Scatter/gather table of pinned pages
    :type sgt: struct sg_table \*

.. _`tinydrm_gem_cma_prime_import_sg_table.description`:

Description
-----------

This function imports a scatter/gather table exported via DMA-BUF by
another driver using \ :c:func:`drm_gem_cma_prime_import_sg_table`\ . It sets the
kernel virtual address on the CMA object. Drivers should use this as their
\ :c:type:`drm_driver->gem_prime_import_sg_table <drm_driver>`\  callback if they need the virtual
address. \ :c:func:`tinydrm_gem_cma_free_object`\  should be used in combination with
this function.

.. _`tinydrm_gem_cma_prime_import_sg_table.return`:

Return
------

A pointer to a newly created GEM object or an ERR_PTR-encoded negative
error code on failure.

.. _`tinydrm_gem_cma_free_object`:

tinydrm_gem_cma_free_object
===========================

.. c:function:: void tinydrm_gem_cma_free_object(struct drm_gem_object *gem_obj)

    Free resources associated with a CMA GEM object

    :param gem_obj:
        GEM object to free
    :type gem_obj: struct drm_gem_object \*

.. _`tinydrm_gem_cma_free_object.description`:

Description
-----------

This function frees the backing memory of the CMA GEM object, cleans up the
GEM object state and frees the memory used to store the object itself using
\ :c:func:`drm_gem_cma_free_object`\ . It also handles PRIME buffers which has the kernel
virtual address set by \ :c:func:`tinydrm_gem_cma_prime_import_sg_table`\ . Drivers
can use this as their \ :c:type:`drm_driver->gem_free_object_unlocked <drm_driver>`\  callback.

.. _`devm_tinydrm_init`:

devm_tinydrm_init
=================

.. c:function:: int devm_tinydrm_init(struct device *parent, struct tinydrm_device *tdev, const struct drm_framebuffer_funcs *fb_funcs, struct drm_driver *driver)

    Initialize tinydrm device

    :param parent:
        Parent device object
    :type parent: struct device \*

    :param tdev:
        tinydrm device
    :type tdev: struct tinydrm_device \*

    :param fb_funcs:
        Framebuffer functions
    :type fb_funcs: const struct drm_framebuffer_funcs \*

    :param driver:
        DRM driver
    :type driver: struct drm_driver \*

.. _`devm_tinydrm_init.description`:

Description
-----------

This function initializes \ ``tdev``\ , the underlying DRM device and it's
mode_config. Resources will be automatically freed on driver detach (devres)
using \ :c:func:`drm_mode_config_cleanup`\  and \ :c:func:`drm_dev_put`\ .

.. _`devm_tinydrm_init.return`:

Return
------

Zero on success, negative error code on failure.

.. _`devm_tinydrm_register`:

devm_tinydrm_register
=====================

.. c:function:: int devm_tinydrm_register(struct tinydrm_device *tdev)

    Register tinydrm device

    :param tdev:
        tinydrm device
    :type tdev: struct tinydrm_device \*

.. _`devm_tinydrm_register.description`:

Description
-----------

This function registers the underlying DRM device and fbdev.
These resources will be automatically unregistered on driver detach (devres)
and the display pipeline will be disabled.

.. _`devm_tinydrm_register.return`:

Return
------

Zero on success, negative error code on failure.

.. _`tinydrm_shutdown`:

tinydrm_shutdown
================

.. c:function:: void tinydrm_shutdown(struct tinydrm_device *tdev)

    Shutdown tinydrm

    :param tdev:
        tinydrm device
    :type tdev: struct tinydrm_device \*

.. _`tinydrm_shutdown.description`:

Description
-----------

This function makes sure that the display pipeline is disabled.
Used by drivers in their shutdown callback to turn off the display
on machine shutdown and reboot.

.. This file was automatic generated / don't edit.

