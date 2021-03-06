.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_file.c

.. _`file-operations`:

file operations
===============

Drivers must define the file operations structure that forms the DRM
userspace API entry point, even though most of those operations are
implemented in the DRM core. The resulting \ :c:type:`struct file_operations <file_operations>`\  must be
stored in the \ :c:type:`drm_driver.fops <drm_driver>`\  field. The mandatory functions are \ :c:func:`drm_open`\ ,
\ :c:func:`drm_read`\ , \ :c:func:`drm_ioctl`\  and \ :c:func:`drm_compat_ioctl`\  if CONFIG_COMPAT is enabled
Note that drm_compat_ioctl will be NULL if CONFIG_COMPAT=n, so there's no
need to sprinkle #ifdef into the code. Drivers which implement private ioctls
that require 32/64 bit compatibility support must provide their own
\ :c:type:`file_operations.compat_ioctl <file_operations>`\  handler that processes private ioctls and calls
\ :c:func:`drm_compat_ioctl`\  for core ioctls.

In addition \ :c:func:`drm_read`\  and \ :c:func:`drm_poll`\  provide support for DRM events. DRM
events are a generic and extensible means to send asynchronous events to
userspace through the file descriptor. They are used to send vblank event and
page flip completions by the KMS API. But drivers can also use it for their
own needs, e.g. to signal completion of rendering.

For the driver-side event interface see \ :c:func:`drm_event_reserve_init`\  and
\ :c:func:`drm_send_event`\  as the main starting points.

The memory mapping implementation will vary depending on how the driver
manages memory. Legacy drivers will use the deprecated \ :c:func:`drm_legacy_mmap`\ 
function, modern drivers should use one of the provided memory-manager
specific implementations. For GEM-based drivers this is \ :c:func:`drm_gem_mmap`\ , and
for drivers which use the CMA GEM helpers it's \ :c:func:`drm_gem_cma_mmap`\ .

No other file operations are supported by the DRM userspace API. Overall the
following is an example \ :c:type:`struct file_operations <file_operations>`\  structure::

    static const example_drm_fops = {
            .owner = THIS_MODULE,
            .open = drm_open,
            .release = drm_release,
            .unlocked_ioctl = drm_ioctl,
            .compat_ioctl = drm_compat_ioctl, // NULL if CONFIG_COMPAT=n
            .poll = drm_poll,
            .read = drm_read,
            .llseek = no_llseek,
            .mmap = drm_gem_mmap,
    };

For plain GEM based drivers there is the \ :c:func:`DEFINE_DRM_GEM_FOPS`\  macro, and for
CMA based drivers there is the \ :c:func:`DEFINE_DRM_GEM_CMA_FOPS`\  macro to make this
simpler.

The driver's \ :c:type:`struct file_operations <file_operations>`\  must be stored in \ :c:type:`drm_driver.fops <drm_driver>`\ .

For driver-private IOCTL handling see the more detailed discussion in
:ref:`IOCTL support in the userland interfaces chapter<drm_driver_ioctl>`.

.. _`drm_file_alloc`:

drm_file_alloc
==============

.. c:function:: struct drm_file *drm_file_alloc(struct drm_minor *minor)

    allocate file context

    :param minor:
        minor to allocate on
    :type minor: struct drm_minor \*

.. _`drm_file_alloc.description`:

Description
-----------

This allocates a new DRM file context. It is not linked into any context and
can be used by the caller freely. Note that the context keeps a pointer to
\ ``minor``\ , so it must be freed before \ ``minor``\  is.

.. _`drm_file_alloc.return`:

Return
------

Pointer to newly allocated context, ERR_PTR on failure.

.. _`drm_file_free`:

drm_file_free
=============

.. c:function:: void drm_file_free(struct drm_file *file)

    free file context

    :param file:
        context to free, or NULL
    :type file: struct drm_file \*

.. _`drm_file_free.description`:

Description
-----------

This destroys and deallocates a DRM file context previously allocated via
\ :c:func:`drm_file_alloc`\ . The caller must make sure to unlink it from any contexts
before calling this.

If NULL is passed, this is a no-op.

.. _`drm_file_free.return`:

Return
------

0 on success, or error code on failure.

.. _`drm_open`:

drm_open
========

.. c:function:: int drm_open(struct inode *inode, struct file *filp)

    open method for DRM file

    :param inode:
        device inode
    :type inode: struct inode \*

    :param filp:
        file pointer.
    :type filp: struct file \*

.. _`drm_open.description`:

Description
-----------

This function must be used by drivers as their \ :c:type:`file_operations.open <file_operations>`\  method.
It looks up the correct DRM device and instantiates all the per-file
resources for it. It also calls the \ :c:type:`drm_driver.open <drm_driver>`\  driver callback.

.. _`drm_open.return`:

Return
------


0 on success or negative errno value on falure.

.. _`drm_release`:

drm_release
===========

.. c:function:: int drm_release(struct inode *inode, struct file *filp)

    release method for DRM file

    :param inode:
        device inode
    :type inode: struct inode \*

    :param filp:
        file pointer.
    :type filp: struct file \*

.. _`drm_release.description`:

Description
-----------

This function must be used by drivers as their \ :c:type:`file_operations.release <file_operations>`\ 
method. It frees any resources associated with the open file, and calls the
\ :c:type:`drm_driver.postclose <drm_driver>`\  driver callback. If this is the last open file for the
DRM device also proceeds to call the \ :c:type:`drm_driver.lastclose <drm_driver>`\  driver callback.

.. _`drm_release.return`:

Return
------


Always succeeds and returns 0.

.. _`drm_read`:

drm_read
========

.. c:function:: ssize_t drm_read(struct file *filp, char __user *buffer, size_t count, loff_t *offset)

    read method for DRM file

    :param filp:
        file pointer
    :type filp: struct file \*

    :param buffer:
        userspace destination pointer for the read
    :type buffer: char __user \*

    :param count:
        count in bytes to read
    :type count: size_t

    :param offset:
        offset to read
    :type offset: loff_t \*

.. _`drm_read.description`:

Description
-----------

This function must be used by drivers as their \ :c:type:`file_operations.read <file_operations>`\ 
method iff they use DRM events for asynchronous signalling to userspace.
Since events are used by the KMS API for vblank and page flip completion this
means all modern display drivers must use it.

\ ``offset``\  is ignored, DRM events are read like a pipe. Therefore drivers also
must set the \ :c:type:`file_operation.llseek <file_operation>`\  to \ :c:func:`no_llseek`\ . Polling support is
provided by \ :c:func:`drm_poll`\ .

This function will only ever read a full event. Therefore userspace must
supply a big enough buffer to fit any event to ensure forward progress. Since
the maximum event space is currently 4K it's recommended to just use that for
safety.

.. _`drm_read.return`:

Return
------


Number of bytes read (always aligned to full events, and can be 0) or a
negative error code on failure.

.. _`drm_poll`:

drm_poll
========

.. c:function:: __poll_t drm_poll(struct file *filp, struct poll_table_struct *wait)

    poll method for DRM file

    :param filp:
        file pointer
    :type filp: struct file \*

    :param wait:
        poll waiter table
    :type wait: struct poll_table_struct \*

.. _`drm_poll.description`:

Description
-----------

This function must be used by drivers as their \ :c:type:`file_operations.read <file_operations>`\  method
iff they use DRM events for asynchronous signalling to userspace.  Since
events are used by the KMS API for vblank and page flip completion this means
all modern display drivers must use it.

See also \ :c:func:`drm_read`\ .

.. _`drm_poll.return`:

Return
------


Mask of POLL flags indicating the current status of the file.

.. _`drm_event_reserve_init_locked`:

drm_event_reserve_init_locked
=============================

.. c:function:: int drm_event_reserve_init_locked(struct drm_device *dev, struct drm_file *file_priv, struct drm_pending_event *p, struct drm_event *e)

    init a DRM event and reserve space for it

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param file_priv:
        DRM file private data
    :type file_priv: struct drm_file \*

    :param p:
        tracking structure for the pending event
    :type p: struct drm_pending_event \*

    :param e:
        actual event data to deliver to userspace
    :type e: struct drm_event \*

.. _`drm_event_reserve_init_locked.description`:

Description
-----------

This function prepares the passed in event for eventual delivery. If the event
doesn't get delivered (because the IOCTL fails later on, before queuing up
anything) then the even must be cancelled and freed using
\ :c:func:`drm_event_cancel_free`\ . Successfully initialized events should be sent out
using \ :c:func:`drm_send_event`\  or \ :c:func:`drm_send_event_locked`\  to signal completion of the
asynchronous event to userspace.

If callers embedded \ ``p``\  into a larger structure it must be allocated with
kmalloc and \ ``p``\  must be the first member element.

This is the locked version of \ :c:func:`drm_event_reserve_init`\  for callers which
already hold \ :c:type:`drm_device.event_lock <drm_device>`\ .

.. _`drm_event_reserve_init_locked.return`:

Return
------


0 on success or a negative error code on failure.

.. _`drm_event_reserve_init`:

drm_event_reserve_init
======================

.. c:function:: int drm_event_reserve_init(struct drm_device *dev, struct drm_file *file_priv, struct drm_pending_event *p, struct drm_event *e)

    init a DRM event and reserve space for it

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param file_priv:
        DRM file private data
    :type file_priv: struct drm_file \*

    :param p:
        tracking structure for the pending event
    :type p: struct drm_pending_event \*

    :param e:
        actual event data to deliver to userspace
    :type e: struct drm_event \*

.. _`drm_event_reserve_init.description`:

Description
-----------

This function prepares the passed in event for eventual delivery. If the event
doesn't get delivered (because the IOCTL fails later on, before queuing up
anything) then the even must be cancelled and freed using
\ :c:func:`drm_event_cancel_free`\ . Successfully initialized events should be sent out
using \ :c:func:`drm_send_event`\  or \ :c:func:`drm_send_event_locked`\  to signal completion of the
asynchronous event to userspace.

If callers embedded \ ``p``\  into a larger structure it must be allocated with
kmalloc and \ ``p``\  must be the first member element.

Callers which already hold \ :c:type:`drm_device.event_lock <drm_device>`\  should use
\ :c:func:`drm_event_reserve_init_locked`\  instead.

.. _`drm_event_reserve_init.return`:

Return
------


0 on success or a negative error code on failure.

.. _`drm_event_cancel_free`:

drm_event_cancel_free
=====================

.. c:function:: void drm_event_cancel_free(struct drm_device *dev, struct drm_pending_event *p)

    free a DRM event and release it's space

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param p:
        tracking structure for the pending event
    :type p: struct drm_pending_event \*

.. _`drm_event_cancel_free.description`:

Description
-----------

This function frees the event \ ``p``\  initialized with \ :c:func:`drm_event_reserve_init`\ 
and releases any allocated space. It is used to cancel an event when the
nonblocking operation could not be submitted and needed to be aborted.

.. _`drm_send_event_locked`:

drm_send_event_locked
=====================

.. c:function:: void drm_send_event_locked(struct drm_device *dev, struct drm_pending_event *e)

    send DRM event to file descriptor

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param e:
        DRM event to deliver
    :type e: struct drm_pending_event \*

.. _`drm_send_event_locked.description`:

Description
-----------

This function sends the event \ ``e``\ , initialized with \ :c:func:`drm_event_reserve_init`\ ,
to its associated userspace DRM file. Callers must already hold
\ :c:type:`drm_device.event_lock <drm_device>`\ , see \ :c:func:`drm_send_event`\  for the unlocked version.

Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.

.. _`drm_send_event`:

drm_send_event
==============

.. c:function:: void drm_send_event(struct drm_device *dev, struct drm_pending_event *e)

    send DRM event to file descriptor

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param e:
        DRM event to deliver
    :type e: struct drm_pending_event \*

.. _`drm_send_event.description`:

Description
-----------

This function sends the event \ ``e``\ , initialized with \ :c:func:`drm_event_reserve_init`\ ,
to its associated userspace DRM file. This function acquires
\ :c:type:`drm_device.event_lock <drm_device>`\ , see \ :c:func:`drm_send_event_locked`\  for callers which already
hold this lock.

Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.

.. This file was automatic generated / don't edit.

