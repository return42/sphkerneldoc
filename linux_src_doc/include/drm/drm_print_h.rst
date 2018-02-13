.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_print.h

.. _`print`:

print
=====

A simple wrapper for \ :c:func:`dev_printk`\ , \ :c:func:`seq_printf`\ , etc.  Allows same
debug code to be used for both debugfs and printk logging.

For example::

    void log_some_info(struct drm_printer *p)
    {
            drm_printf(p, "foo=%d\n", foo);
            drm_printf(p, "bar=%d\n", bar);
    }

    #ifdef CONFIG_DEBUG_FS
    void debugfs_show(struct seq_file *f)
    {
            struct drm_printer p = drm_seq_file_printer(f);
            log_some_info(&p);
    }
    #endif

    void some_other_function(...)
    {
            struct drm_printer p = drm_info_printer(drm->dev);
            log_some_info(&p);
    }

.. _`drm_printer`:

struct drm_printer
==================

.. c:type:: struct drm_printer

    drm output "stream"

.. _`drm_printer.definition`:

Definition
----------

.. code-block:: c

    struct drm_printer {
    }

.. _`drm_printer.members`:

Members
-------

void
    no arguments

.. _`drm_printer.description`:

Description
-----------

Do not use struct members directly.  Use \ :c:func:`drm_printer_seq_file`\ ,
\ :c:func:`drm_printer_info`\ , etc to initialize.  And \ :c:func:`drm_printf`\  for output.

.. _`drm_vprintf`:

drm_vprintf
===========

.. c:function:: void drm_vprintf(struct drm_printer *p, const char *fmt, va_list *va)

    print to a \ :c:type:`struct drm_printer <drm_printer>`\  stream

    :param struct drm_printer \*p:
        the \ :c:type:`struct drm_printer <drm_printer>`\ 

    :param const char \*fmt:
        format string

    :param va_list \*va:
        the va_list

.. _`drm_printf_indent`:

drm_printf_indent
=================

.. c:function::  drm_printf_indent( printer,  indent,  fmt,  ...)

    Print to a \ :c:type:`struct drm_printer <drm_printer>`\  stream with indentation

    :param  printer:
        DRM printer

    :param  indent:
        Tab indentation level (max 5)

    :param  fmt:
        Format string

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_seq_file_printer`:

drm_seq_file_printer
====================

.. c:function:: struct drm_printer drm_seq_file_printer(struct seq_file *f)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that outputs to \ :c:type:`struct seq_file <seq_file>`\ 

    :param struct seq_file \*f:
        the \ :c:type:`struct seq_file <seq_file>`\  to output to

.. _`drm_seq_file_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_info_printer`:

drm_info_printer
================

.. c:function:: struct drm_printer drm_info_printer(struct device *dev)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that outputs to \ :c:func:`dev_printk`\ 

    :param struct device \*dev:
        the \ :c:type:`struct device <device>`\  pointer

.. _`drm_info_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_debug_printer`:

drm_debug_printer
=================

.. c:function:: struct drm_printer drm_debug_printer(const char *prefix)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that outputs to \ :c:func:`pr_debug`\ 

    :param const char \*prefix:
        debug output prefix

.. _`drm_debug_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_dev_error`:

DRM_DEV_ERROR
=============

.. c:function::  DRM_DEV_ERROR( dev,  fmt,  ...)

    :param  dev:
        device pointer

    :param  fmt:
        printf() like format string.

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_dev_error_ratelimited`:

DRM_DEV_ERROR_RATELIMITED
=========================

.. c:function::  DRM_DEV_ERROR_RATELIMITED( dev,  fmt,  ...)

    :param  dev:
        device pointer

    :param  fmt:
        printf() like format string.

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_dev_debug`:

DRM_DEV_DEBUG
=============

.. c:function::  DRM_DEV_DEBUG( dev,  fmt,  args...)

    :param  dev:
        device pointer

    :param  fmt:
        printf() like format string.

.. _`drm_dev_debug_ratelimited`:

DRM_DEV_DEBUG_RATELIMITED
=========================

.. c:function::  DRM_DEV_DEBUG_RATELIMITED( dev,  fmt,  args...)

    :param  dev:
        device pointer

    :param  fmt:
        printf() like format string.

.. This file was automatic generated / don't edit.

