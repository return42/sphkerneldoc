.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_file.h

.. _`drm_minor`:

struct drm_minor
================

.. c:type:: struct drm_minor

    DRM device minor structure

.. _`drm_minor.definition`:

Definition
----------

.. code-block:: c

    struct drm_minor {
    }

.. _`drm_minor.members`:

Members
-------

void
    no arguments

.. _`drm_minor.description`:

Description
-----------

This structure represents a DRM minor number for device nodes in /dev.
Entirely opaque to drivers and should never be inspected directly by drivers.
Drivers instead should only interact with \ :c:type:`struct drm_file <drm_file>`\  and of course
\ :c:type:`struct drm_device <drm_device>`\ , which is also where driver-private data and resources can
be attached to.

.. _`drm_pending_event`:

struct drm_pending_event
========================

.. c:type:: struct drm_pending_event

    Event queued up for userspace to read

.. _`drm_pending_event.definition`:

Definition
----------

.. code-block:: c

    struct drm_pending_event {
        struct completion *completion;
        void (*completion_release)(struct completion *completion);
        struct drm_event *event;
        struct dma_fence *fence;
        struct drm_file *file_priv;
        struct list_head link;
        struct list_head pending_link;
    }

.. _`drm_pending_event.members`:

Members
-------

completion

    Optional pointer to a kernel internal completion signalled when
    \ :c:func:`drm_send_event`\  is called, useful to internally synchronize with
    nonblocking operations.

completion_release

    Optional callback currently only used by the atomic modeset helpers
    to clean up the reference count for the structure \ ``completion``\  is
    stored in.

event

    Pointer to the actual event that should be sent to userspace to be
    read using \ :c:func:`drm_read`\ . Can be optional, since nowadays events are
    also used to signal kernel internal threads with \ ``completion``\  or DMA
    transactions using \ ``fence``\ .

fence

    Optional DMA fence to unblock other hardware transactions which
    depend upon the nonblocking DRM operation this event represents.

file_priv

    \ :c:type:`struct drm_file <drm_file>`\  where \ ``event``\  should be delivered to. Only set when
    \ ``event``\  is set.

link

    Double-linked list to keep track of this event. Can be used by the
    driver up to the point when it calls \ :c:func:`drm_send_event`\ , after that
    this list entry is owned by the core for its own book-keeping.

pending_link

    Entry on \ :c:type:`drm_file.pending_event_list <drm_file>`\ , to keep track of all pending
    events for \ ``file_priv``\ , to allow correct unwinding of them when
    userspace closes the file before the event is delivered.

.. _`drm_pending_event.description`:

Description
-----------

This represents a DRM event. Drivers can use this as a generic completion
mechanism, which supports kernel-internal \ :c:type:`struct completion <completion>`\ , \ :c:type:`struct dma_fence <dma_fence>`\ 
and also the DRM-specific \ :c:type:`struct drm_event <drm_event>`\  delivery mechanism.

.. _`drm_file`:

struct drm_file
===============

.. c:type:: struct drm_file

    DRM file private data

.. _`drm_file.definition`:

Definition
----------

.. code-block:: c

    struct drm_file {
        unsigned authenticated :1;
        unsigned stereo_allowed :1;
        unsigned universal_planes:1;
        unsigned atomic:1;
        unsigned aspect_ratio_allowed:1;
        unsigned writeback_connectors:1;
        unsigned is_master:1;
        struct drm_master *master;
        struct pid *pid;
        drm_magic_t magic;
        struct list_head lhead;
        struct drm_minor *minor;
        struct idr object_idr;
        spinlock_t table_lock;
        struct idr syncobj_idr;
        spinlock_t syncobj_table_lock;
        struct file *filp;
        void *driver_priv;
        struct list_head fbs;
        struct mutex fbs_lock;
        struct list_head blobs;
        wait_queue_head_t event_wait;
        struct list_head pending_event_list;
        struct list_head event_list;
        int event_space;
        struct mutex event_read_lock;
        struct drm_prime_file_private prime;
    }

.. _`drm_file.members`:

Members
-------

authenticated

    Whether the client is allowed to submit rendering, which for legacy
    nodes means it must be authenticated.

    See also the :ref:`section on primary nodes and authentication
    <drm_primary_node>`.

stereo_allowed

    True when the client has asked us to expose stereo 3D mode flags.

universal_planes

    True if client understands CRTC primary planes and cursor planes
    in the plane list. Automatically set when \ ``atomic``\  is set.

atomic
    True if client understands atomic properties.

aspect_ratio_allowed

    True, if client can handle picture aspect ratios, and has requested
    to pass this information along with the mode.

writeback_connectors

    True if client understands writeback connectors

is_master

    This client is the creator of \ ``master``\ . Protected by struct
    \ :c:type:`drm_device.master_mutex <drm_device>`\ .

    See also the :ref:`section on primary nodes and authentication
    <drm_primary_node>`.

master

    Master this node is currently associated with. Only relevant if
    \ :c:func:`drm_is_primary_client`\  returns true. Note that this only
    matches \ :c:type:`drm_device.master <drm_device>`\  if the master is the currently active one.

    See also \ ``authentication``\  and \ ``is_master``\  and the :ref:`section on
    primary nodes and authentication <drm_primary_node>`.

pid
    Process that opened this file.

magic
    Authentication magic, see \ ``authenticated``\ .

lhead

    List of all open files of a DRM device, linked into
    \ :c:type:`drm_device.filelist <drm_device>`\ . Protected by \ :c:type:`drm_device.filelist_mutex <drm_device>`\ .

minor
    \ :c:type:`struct drm_minor <drm_minor>`\  for this file.

object_idr

    Mapping of mm object handles to object pointers. Used by the GEM
    subsystem. Protected by \ ``table_lock``\ .

table_lock
    Protects \ ``object_idr``\ .

syncobj_idr
    Mapping of sync object handles to object pointers.

syncobj_table_lock
    Protects \ ``syncobj_idr``\ .

filp
    Pointer to the core file structure.

driver_priv

    Optional pointer for driver private data. Can be allocated in
    \ :c:type:`drm_driver.open <drm_driver>`\  and should be freed in \ :c:type:`drm_driver.postclose <drm_driver>`\ .

fbs

    List of \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  associated with this file, using the
    \ :c:type:`drm_framebuffer.filp_head <drm_framebuffer>`\  entry.

    Protected by \ ``fbs_lock``\ . Note that the \ ``fbs``\  list holds a reference on
    the framebuffer object to prevent it from untimely disappearing.

fbs_lock
    Protects \ ``fbs``\ .

blobs

    User-created blob properties; this retains a reference on the
    property.

    Protected by \ ``drm_mode_config.blob_lock``\ ;

event_wait
    Waitqueue for new events added to \ ``event_list``\ .

pending_event_list

    List of pending \ :c:type:`struct drm_pending_event <drm_pending_event>`\ , used to clean up pending
    events in case this file gets closed before the event is signalled.
    Uses the \ :c:type:`drm_pending_event.pending_link <drm_pending_event>`\  entry.

    Protect by \ :c:type:`drm_device.event_lock <drm_device>`\ .

event_list

    List of \ :c:type:`struct drm_pending_event <drm_pending_event>`\ , ready for delivery to userspace
    through \ :c:func:`drm_read`\ . Uses the \ :c:type:`drm_pending_event.link <drm_pending_event>`\  entry.

    Protect by \ :c:type:`drm_device.event_lock <drm_device>`\ .

event_space

    Available event space to prevent userspace from
    exhausting kernel memory. Currently limited to the fairly arbitrary
    value of 4KB.

event_read_lock
    Serializes \ :c:func:`drm_read`\ .

prime

    Per-file buffer caches used by the PRIME buffer sharing code.

.. _`drm_file.description`:

Description
-----------

This structure tracks DRM state per open file descriptor.

.. _`drm_is_primary_client`:

drm_is_primary_client
=====================

.. c:function:: bool drm_is_primary_client(const struct drm_file *file_priv)

    is this an open file of the primary node

    :param file_priv:
        DRM file
    :type file_priv: const struct drm_file \*

.. _`drm_is_primary_client.description`:

Description
-----------

Returns true if this is an open file of the primary node, i.e.
\ :c:type:`drm_file.minor <drm_file>`\  of \ ``file_priv``\  is a primary minor.

See also the :ref:`section on primary nodes and authentication
<drm_primary_node>`.

.. _`drm_is_render_client`:

drm_is_render_client
====================

.. c:function:: bool drm_is_render_client(const struct drm_file *file_priv)

    is this an open file of the render node

    :param file_priv:
        DRM file
    :type file_priv: const struct drm_file \*

.. _`drm_is_render_client.description`:

Description
-----------

Returns true if this is an open file of the render node, i.e.
\ :c:type:`drm_file.minor <drm_file>`\  of \ ``file_priv``\  is a render minor.

See also the :ref:`section on render nodes <drm_render_node>`.

.. This file was automatic generated / don't edit.

