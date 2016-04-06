
.. _API-drm-dp-dpcd-read:

================
drm_dp_dpcd_read
================

*man drm_dp_dpcd_read(9)*

*4.6.0-rc1*

read a series of bytes from the DPCD


Synopsis
========

.. c:function:: ssize_t drm_dp_dpcd_read( struct drm_dp_aux * aux, unsigned int offset, void * buffer, size_t size )

Arguments
=========

``aux``
    DisplayPort AUX channel

``offset``
    address of the (first) register to read

``buffer``
    buffer to store the register values

``size``
    number of bytes in ``buffer``


Description
===========

Returns the number of bytes transferred on success, or a negative error code on failure. -EIO is returned if the request was NAKed by the sink or if the retry count was exceeded.
If not all bytes were transferred, this function returns -EPROTO. Errors from the underlying AUX channel transfer function, with the exception of -EBUSY (which causes the
transaction to be retried), are propagated to the caller.
