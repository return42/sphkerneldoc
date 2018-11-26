.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_print.c

.. _`drm_puts`:

drm_puts
========

.. c:function:: void drm_puts(struct drm_printer *p, const char *str)

    print a const string to a \ :c:type:`struct drm_printer <drm_printer>`\  stream

    :param p:
        the \ :c:type:`struct drm <drm>`\  printer
    :type p: struct drm_printer \*

    :param str:
        const string
    :type str: const char \*

.. _`drm_puts.description`:

Description
-----------

Allow \ :c:type:`struct drm_printer <drm_printer>`\  types that have a constant string
option to use it.

.. _`drm_printf`:

drm_printf
==========

.. c:function:: void drm_printf(struct drm_printer *p, const char *f,  ...)

    print to a \ :c:type:`struct drm_printer <drm_printer>`\  stream

    :param p:
        the \ :c:type:`struct drm_printer <drm_printer>`\ 
    :type p: struct drm_printer \*

    :param f:
        format string
    :type f: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. This file was automatic generated / don't edit.

