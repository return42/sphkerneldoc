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
        void (*printfn)(struct drm_printer *p, struct va_format *vaf);
        void *arg;
        const char *prefix;
    }

.. _`drm_printer.members`:

Members
-------

printfn
    *undescribed*

arg
    *undescribed*

prefix
    *undescribed*

.. _`drm_printer.description`:

Description
-----------

Do not use struct members directly.  Use \ :c:func:`drm_printer_seq_file`\ ,
\ :c:func:`drm_printer_info`\ , etc to initialize.  And \ :c:func:`drm_printf`\  for output.

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

.. This file was automatic generated / don't edit.

