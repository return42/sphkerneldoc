.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-get-format-name:

===================
drm_get_format_name
===================

*man drm_get_format_name(9)*

*4.6.0-rc5*

return a string for drm fourcc format


Synopsis
========

.. c:function:: const char * drm_get_format_name( uint32_t format )

Arguments
=========

``format``
    format to compute name of


Description
===========

Note that the buffer used by this function is globally shared and owned
by the function itself.


FIXME
=====

This isn't really multithreading safe.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
