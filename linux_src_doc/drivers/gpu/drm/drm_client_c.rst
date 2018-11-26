.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_client.c

.. _`overview`:

overview
========

This library provides support for clients running in the kernel like fbdev and bootsplash.
Currently it's only partially implemented, just enough to support fbdev.

GEM drivers which provide a GEM based dumb buffer with a virtual address are supported.

.. _`drm_client_init`:

drm_client_init
===============

.. c:function:: int drm_client_init(struct drm_device *dev, struct drm_client_dev *client, const char *name, const struct drm_client_funcs *funcs)

    Initialise a DRM client

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param client:
        DRM client
    :type client: struct drm_client_dev \*

    :param name:
        Client name
    :type name: const char \*

    :param funcs:
        DRM client functions (optional)
    :type funcs: const struct drm_client_funcs \*

.. _`drm_client_init.description`:

Description
-----------

This initialises the client and opens a \ :c:type:`struct drm_file <drm_file>`\ . Use \ :c:func:`drm_client_add`\  to complete the process.
The caller needs to hold a reference on \ ``dev``\  before calling this function.
The client is freed when the \ :c:type:`struct drm_device <drm_device>`\  is unregistered. See \ :c:func:`drm_client_release`\ .

.. _`drm_client_init.return`:

Return
------

Zero on success or negative error code on failure.

.. _`drm_client_add`:

drm_client_add
==============

.. c:function:: void drm_client_add(struct drm_client_dev *client)

    Add client to the device list

    :param client:
        DRM client
    :type client: struct drm_client_dev \*

.. _`drm_client_add.description`:

Description
-----------

Add the client to the \ :c:type:`struct drm_device <drm_device>`\  client list to activate its callbacks.
\ ``client``\  must be initialized by a call to \ :c:func:`drm_client_init`\ . After
\ :c:func:`drm_client_add`\  it is no longer permissible to call \ :c:func:`drm_client_release`\ 
directly (outside the unregister callback), instead cleanup will happen
automatically on driver unload.

.. _`drm_client_release`:

drm_client_release
==================

.. c:function:: void drm_client_release(struct drm_client_dev *client)

    Release DRM client resources

    :param client:
        DRM client
    :type client: struct drm_client_dev \*

.. _`drm_client_release.description`:

Description
-----------

Releases resources by closing the \ :c:type:`struct drm_file <drm_file>`\  that was opened by \ :c:func:`drm_client_init`\ .
It is called automatically if the \ :c:type:`drm_client_funcs.unregister <drm_client_funcs>`\  callback is _not_ set.

This function should only be called from the unregister callback. An exception
is fbdev which cannot free the buffer if userspace has open file descriptors.

.. _`drm_client_release.note`:

Note
----

Clients cannot initiate a release by themselves. This is done to keep the code simple.
The driver has to be unloaded before the client can be unloaded.

.. _`drm_client_dev_hotplug`:

drm_client_dev_hotplug
======================

.. c:function:: void drm_client_dev_hotplug(struct drm_device *dev)

    Send hotplug event to clients

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_client_dev_hotplug.description`:

Description
-----------

This function calls the \ :c:type:`drm_client_funcs.hotplug <drm_client_funcs>`\  callback on the attached clients.

\ :c:func:`drm_kms_helper_hotplug_event`\  calls this function, so drivers that use it
don't need to call this function themselves.

.. _`drm_client_framebuffer_create`:

drm_client_framebuffer_create
=============================

.. c:function:: struct drm_client_buffer *drm_client_framebuffer_create(struct drm_client_dev *client, u32 width, u32 height, u32 format)

    Create a client framebuffer

    :param client:
        DRM client
    :type client: struct drm_client_dev \*

    :param width:
        Framebuffer width
    :type width: u32

    :param height:
        Framebuffer height
    :type height: u32

    :param format:
        Buffer format
    :type format: u32

.. _`drm_client_framebuffer_create.description`:

Description
-----------

This function creates a \ :c:type:`struct drm_client_buffer <drm_client_buffer>`\  which consists of a
\ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  backed by a dumb buffer.
Call \ :c:func:`drm_client_framebuffer_delete`\  to free the buffer.

.. _`drm_client_framebuffer_create.return`:

Return
------

Pointer to a client buffer or an error pointer on failure.

.. _`drm_client_framebuffer_delete`:

drm_client_framebuffer_delete
=============================

.. c:function:: void drm_client_framebuffer_delete(struct drm_client_buffer *buffer)

    Delete a client framebuffer

    :param buffer:
        DRM client buffer (can be NULL)
    :type buffer: struct drm_client_buffer \*

.. This file was automatic generated / don't edit.

