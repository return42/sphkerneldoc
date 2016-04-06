
.. _API-drm-read:

========
drm_read
========

*man drm_read(9)*

*4.6.0-rc1*

read method for DRM file


Synopsis
========

.. c:function:: ssize_t drm_read( struct file * filp, char __user * buffer, size_t count, loff_t * offset )

Arguments
=========

``filp``
    file pointer

``buffer``
    userspace destination pointer for the read

``count``
    count in bytes to read

``offset``
    offset to read


Description
===========

This function must be used by drivers as their . ``read`` #file_operations method iff they use DRM events for asynchronous signalling to userspace. Since events are used by the
KMS API for vblank and page flip completion this means all modern display drivers must use it.

``offset`` is ignore, DRM events are read like a pipe. Therefore drivers also must set the . ``llseek`` #file_operation to ``no_llseek``. Polling support is provided by
``drm_poll``.

This function will only ever read a full event. Therefore userspace must supply a big enough buffer to fit any event to ensure forward progress. Since the maximum event space is
currently 4K it's recommended to just use that for safety.


RETURNS
=======

Number of bytes read (always aligned to full events, and can be 0) or a negative error code on failure.
