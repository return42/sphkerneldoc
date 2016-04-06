
.. _API-drm-dp-dpcd-write:

=================
drm_dp_dpcd_write
=================

*man drm_dp_dpcd_write(9)*

*4.6.0-rc1*

write a series of bytes to the DPCD


Synopsis
========

.. c:function:: ssize_t drm_dp_dpcd_write( struct drm_dp_aux * aux, unsigned int offset, void * buffer, size_t size )

Arguments
=========

``aux``
    DisplayPort AUX channel

``offset``
    address of the (first) register to write

``buffer``
    buffer containing the values to write

``size``
    number of bytes in ``buffer``


Description
===========

Returns the number of bytes transferred on success, or a negative error code on failure. -EIO is returned if the request was NAKed by the sink or if the retry count was exceeded.
If not all bytes were transferred, this function returns -EPROTO. Errors from the underlying AUX channel transfer function, with the exception of -EBUSY (which causes the
transaction to be retried), are propagated to the caller.
