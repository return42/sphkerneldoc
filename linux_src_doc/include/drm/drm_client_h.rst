.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_client.h

.. _`drm_client_funcs`:

struct drm_client_funcs
=======================

.. c:type:: struct drm_client_funcs

    DRM client callbacks

.. _`drm_client_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_client_funcs {
        struct module *owner;
        void (*unregister)(struct drm_client_dev *client);
        int (*restore)(struct drm_client_dev *client);
        int (*hotplug)(struct drm_client_dev *client);
    }

.. _`drm_client_funcs.members`:

Members
-------

owner
    The module owner

unregister

    Called when \ :c:type:`struct drm_device <drm_device>`\  is unregistered. The client should respond by
    releasing it's resources using \ :c:func:`drm_client_release`\ .

    This callback is optional.

restore

    Called on \ :c:func:`drm_lastclose`\ . The first client instance in the list that
    returns zero gets the privilege to restore and no more clients are
    called. This callback is not called after \ ``unregister``\  has been called.

    This callback is optional.

hotplug

    Called on \ :c:func:`drm_kms_helper_hotplug_event`\ .
    This callback is not called after \ ``unregister``\  has been called.

    This callback is optional.

.. _`drm_client_dev`:

struct drm_client_dev
=====================

.. c:type:: struct drm_client_dev

    DRM client instance

.. _`drm_client_dev.definition`:

Definition
----------

.. code-block:: c

    struct drm_client_dev {
        struct drm_device *dev;
        const char *name;
        struct list_head list;
        const struct drm_client_funcs *funcs;
        struct drm_file *file;
    }

.. _`drm_client_dev.members`:

Members
-------

dev
    DRM device

name
    Name of the client.

list

    List of all clients of a DRM device, linked into
    \ :c:type:`drm_device.clientlist <drm_device>`\ . Protected by \ :c:type:`drm_device.clientlist_mutex <drm_device>`\ .

funcs
    DRM client functions (optional)

file
    DRM file

.. _`drm_client_buffer`:

struct drm_client_buffer
========================

.. c:type:: struct drm_client_buffer

    DRM client buffer

.. _`drm_client_buffer.definition`:

Definition
----------

.. code-block:: c

    struct drm_client_buffer {
        struct drm_client_dev *client;
        u32 handle;
        u32 pitch;
        struct drm_gem_object *gem;
        void *vaddr;
        struct drm_framebuffer *fb;
    }

.. _`drm_client_buffer.members`:

Members
-------

client
    DRM client

handle
    Buffer handle

pitch
    Buffer pitch

gem
    GEM object backing this buffer

vaddr
    Virtual address for the buffer

fb
    DRM framebuffer

.. This file was automatic generated / don't edit.

