.. -*- coding: utf-8; mode: rst -*-

.. _API-edd-show-raw-data:

=================
edd_show_raw_data
=================

*man edd_show_raw_data(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
