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

    :param p:
        the \ :c:type:`struct drm_printer <drm_printer>`\ 
    :type p: struct drm_printer \*

    :param fmt:
        format string
    :type fmt: const char \*

    :param va:
        the va_list
    :type va: va_list \*

.. _`drm_printf_indent`:

drm_printf_indent
=================

.. c:function::  drm_printf_indent( printer,  indent,  fmt,  ...)

    Print to a \ :c:type:`struct drm_printer <drm_printer>`\  stream with indentation

    :param printer:
        DRM printer
    :type printer: 

    :param indent:
        Tab indentation level (max 5)
    :type indent: 

    :param fmt:
        Format string
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_print_iterator`:

struct drm_print_iterator
=========================

.. c:type:: struct drm_print_iterator

    local struct used with drm_printer_coredump

.. _`drm_print_iterator.definition`:

Definition
----------

.. code-block:: c

    struct drm_print_iterator {
        void *data;
        ssize_t start;
        ssize_t remain;
    }

.. _`drm_print_iterator.members`:

Members
-------

data
    Pointer to the devcoredump output buffer

start
    The offset within the buffer to start writing

remain
    The number of bytes to write for this iteration

.. _`drm_coredump_printer`:

drm_coredump_printer
====================

.. c:function:: struct drm_printer drm_coredump_printer(struct drm_print_iterator *iter)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that can output to a buffer from the read function for devcoredump

    :param iter:
        A pointer to a struct drm_print_iterator for the read instance
    :type iter: struct drm_print_iterator \*

.. _`drm_coredump_printer.description`:

Description
-----------

This wrapper extends \ :c:func:`drm_printf`\  to work with a \ :c:func:`dev_coredumpm`\  callback
function. The passed in drm_print_iterator struct contains the buffer
pointer, size and offset as passed in from devcoredump.

For example::

     void coredump_read(char *buffer, loff_t offset, size_t count,
             void *data, size_t datalen)
     {
             struct drm_print_iterator iter;
             struct drm_printer p;

             iter.data = buffer;
             iter.start = offset;
             iter.remain = count;

             p = drm_coredump_printer(&iter);

             drm_printf(p, "foo=%d\n", foo);
     }

     void makecoredump(...)
     {
             ...
             dev_coredumpm(dev, THIS_MODULE, data, 0, GFP_KERNEL,
                     coredump_read, ...)
     }

.. _`drm_coredump_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_seq_file_printer`:

drm_seq_file_printer
====================

.. c:function:: struct drm_printer drm_seq_file_printer(struct seq_file *f)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that outputs to \ :c:type:`struct seq_file <seq_file>`\ 

    :param f:
        the \ :c:type:`struct seq_file <seq_file>`\  to output to
    :type f: struct seq_file \*

.. _`drm_seq_file_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_info_printer`:

drm_info_printer
================

.. c:function:: struct drm_printer drm_info_printer(struct device *dev)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that outputs to \ :c:func:`dev_printk`\ 

    :param dev:
        the \ :c:type:`struct device <device>`\  pointer
    :type dev: struct device \*

.. _`drm_info_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_debug_printer`:

drm_debug_printer
=================

.. c:function:: struct drm_printer drm_debug_printer(const char *prefix)

    construct a \ :c:type:`struct drm_printer <drm_printer>`\  that outputs to \ :c:func:`pr_debug`\ 

    :param prefix:
        debug output prefix
    :type prefix: const char \*

.. _`drm_debug_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. _`drm_dev_error`:

DRM_DEV_ERROR
=============

.. c:function::  DRM_DEV_ERROR( dev,  fmt,  ...)

    :param dev:
        device pointer
    :type dev: 

    :param fmt:
        \ :c:func:`printf`\  like format string.
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_dev_error_ratelimited`:

DRM_DEV_ERROR_RATELIMITED
=========================

.. c:function::  DRM_DEV_ERROR_RATELIMITED( dev,  fmt,  ...)

    :param dev:
        device pointer
    :type dev: 

    :param fmt:
        \ :c:func:`printf`\  like format string.
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_dev_debug`:

DRM_DEV_DEBUG
=============

.. c:function::  DRM_DEV_DEBUG( dev,  fmt,  ...)

    :param dev:
        device pointer
    :type dev: 

    :param fmt:
        \ :c:func:`printf`\  like format string.
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`drm_dev_debug_ratelimited`:

DRM_DEV_DEBUG_RATELIMITED
=========================

.. c:function::  DRM_DEV_DEBUG_RATELIMITED( dev,  fmt,  ...)

    :param dev:
        device pointer
    :type dev: 

    :param fmt:
        \ :c:func:`printf`\  like format string.
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. This file was automatic generated / don't edit.

