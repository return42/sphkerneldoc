.. -*- coding: utf-8; mode: rst -*-

==========
drm_fops.c
==========



.. _xref_drm_open:

drm_open
========

.. c:function:: int drm_open (struct inode * inode, struct file * filp)

    open method for DRM file

    :param struct inode * inode:
        device inode

    :param struct file * filp:
        file pointer.



Description
-----------

This function must be used by drivers as their .:c:func:`open` #file_operations
method. It looks up the correct DRM device and instantiates all the per-file
resources for it.



RETURNS
-------



0 on success or negative errno value on falure.




.. _xref_drm_release:

drm_release
===========

.. c:function:: int drm_release (struct inode * inode, struct file * filp)

    release method for DRM file

    :param struct inode * inode:
        device inode

    :param struct file * filp:
        file pointer.



Description
-----------

This function must be used by drivers as their .:c:func:`release` #file_operations
method. It frees any resources associated with the open file, and if this is
the last open file for the DRM device also proceeds to call :c:func:`drm_lastclose`.



RETURNS
-------



Always succeeds and returns 0.




.. _xref_drm_read:

drm_read
========

.. c:function:: ssize_t drm_read (struct file * filp, char __user * buffer, size_t count, loff_t * offset)

    read method for DRM file

    :param struct file * filp:
        file pointer

    :param char __user * buffer:
        userspace destination pointer for the read

    :param size_t count:
        count in bytes to read

    :param loff_t * offset:
        offset to read



Description
-----------

This function must be used by drivers as their .:c:func:`read` #file_operations
method iff they use DRM events for asynchronous signalling to userspace.
Since events are used by the KMS API for vblank and page flip completion this
means all modern display drivers must use it.


**offset** is ignore, DRM events are read like a pipe. Therefore drivers also
must set the .:c:func:`llseek` #file_operation to :c:func:`no_llseek`. Polling support is
provided by :c:func:`drm_poll`.


This function will only ever read a full event. Therefore userspace must
supply a big enough buffer to fit any event to ensure forward progress. Since
the maximum event space is currently 4K it's recommended to just use that for
safety.



RETURNS
-------



Number of bytes read (always aligned to full events, and can be 0) or a
negative error code on failure.




.. _xref_drm_poll:

drm_poll
========

.. c:function:: unsigned int drm_poll (struct file * filp, struct poll_table_struct * wait)

    poll method for DRM file

    :param struct file * filp:
        file pointer

    :param struct poll_table_struct * wait:
        poll waiter table



Description
-----------

This function must be used by drivers as their .:c:func:`read` #file_operations
method iff they use DRM events for asynchronous signalling to userspace.
Since events are used by the KMS API for vblank and page flip completion this
means all modern display drivers must use it.


See also :c:func:`drm_read`.



RETURNS
-------



Mask of POLL flags indicating the current status of the file.




.. _xref_drm_event_reserve_init_locked:

drm_event_reserve_init_locked
=============================

.. c:function:: int drm_event_reserve_init_locked (struct drm_device * dev, struct drm_file * file_priv, struct drm_pending_event * p, struct drm_event * e)

    init a DRM event and reserve space for it

    :param struct drm_device * dev:
        DRM device

    :param struct drm_file * file_priv:
        DRM file private data

    :param struct drm_pending_event * p:
        tracking structure for the pending event

    :param struct drm_event * e:
        actual event data to deliver to userspace



Description
-----------

This function prepares the passed in event for eventual delivery. If the event
doesn't get delivered (because the IOCTL fails later on, before queuing up
anything) then the even must be cancelled and freed using
:c:func:`drm_event_cancel_free`. Successfully initialized events should be sent out
using :c:func:`drm_send_event` or :c:func:`drm_send_event_locked` to signal completion of the
asynchronous event to userspace.


If callers embedded **p** into a larger structure it must be allocated with
kmalloc and **p** must be the first member element.


This is the locked version of :c:func:`drm_event_reserve_init` for callers which
already hold dev->event_lock.



RETURNS
-------



0 on success or a negative error code on failure.




.. _xref_drm_event_reserve_init:

drm_event_reserve_init
======================

.. c:function:: int drm_event_reserve_init (struct drm_device * dev, struct drm_file * file_priv, struct drm_pending_event * p, struct drm_event * e)

    init a DRM event and reserve space for it

    :param struct drm_device * dev:
        DRM device

    :param struct drm_file * file_priv:
        DRM file private data

    :param struct drm_pending_event * p:
        tracking structure for the pending event

    :param struct drm_event * e:
        actual event data to deliver to userspace



Description
-----------

This function prepares the passed in event for eventual delivery. If the event
doesn't get delivered (because the IOCTL fails later on, before queuing up
anything) then the even must be cancelled and freed using
:c:func:`drm_event_cancel_free`. Successfully initialized events should be sent out
using :c:func:`drm_send_event` or :c:func:`drm_send_event_locked` to signal completion of the
asynchronous event to userspace.


If callers embedded **p** into a larger structure it must be allocated with
kmalloc and **p** must be the first member element.


Callers which already hold dev->event_lock should use
:c:func:`drm_event_reserve_init` instead.



RETURNS
-------



0 on success or a negative error code on failure.




.. _xref_drm_event_cancel_free:

drm_event_cancel_free
=====================

.. c:function:: void drm_event_cancel_free (struct drm_device * dev, struct drm_pending_event * p)

    free a DRM event and release it's space

    :param struct drm_device * dev:
        DRM device

    :param struct drm_pending_event * p:
        tracking structure for the pending event



Description
-----------

This function frees the event **p** initialized with :c:func:`drm_event_reserve_init`
and releases any allocated space.




.. _xref_drm_send_event_locked:

drm_send_event_locked
=====================

.. c:function:: void drm_send_event_locked (struct drm_device * dev, struct drm_pending_event * e)

    send DRM event to file descriptor

    :param struct drm_device * dev:
        DRM device

    :param struct drm_pending_event * e:
        DRM event to deliver



Description
-----------

This function sends the event **e**, initialized with :c:func:`drm_event_reserve_init`,
to its associated userspace DRM file. Callers must already hold
dev->event_lock, see :c:func:`drm_send_event` for the unlocked version.


Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.




.. _xref_drm_send_event:

drm_send_event
==============

.. c:function:: void drm_send_event (struct drm_device * dev, struct drm_pending_event * e)

    send DRM event to file descriptor

    :param struct drm_device * dev:
        DRM device

    :param struct drm_pending_event * e:
        DRM event to deliver



Description
-----------

This function sends the event **e**, initialized with :c:func:`drm_event_reserve_init`,
to its associated userspace DRM file. This function acquires dev->event_lock,
see :c:func:`drm_send_event_locked` for callers which already hold this lock.


Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.


