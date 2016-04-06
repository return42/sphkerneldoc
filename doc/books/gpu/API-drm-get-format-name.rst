
.. _API-drm-get-format-name:

===================
drm_get_format_name
===================

*man drm_get_format_name(9)*

*4.6.0-rc1*

return a string for drm fourcc format


Synopsis
========

.. c:function:: const char ⋆ drm_get_format_name( uint32_t format )

Arguments
=========

``format``
    format to compute name of


Description
===========

Note that the buffer used by this function is globally shared and owned by the function itself.


FIXME
=====

This isn't really multithreading safe.
