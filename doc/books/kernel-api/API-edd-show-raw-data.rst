
.. _API-edd-show-raw-data:

=================
edd_show_raw_data
=================

*man edd_show_raw_data(9)*

*4.6.0-rc1*

copies raw data to buffer for userspace to parse


Synopsis
========

.. c:function:: ssize_t edd_show_raw_data( struct edd_device * edev, char * buf )

Arguments
=========

``edev``
    target edd_device

``buf``
    output buffer


Returns
=======

number of bytes written, or -EINVAL on failure
