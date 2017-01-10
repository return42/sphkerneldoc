.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_print.h

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
    }

.. _`drm_printer.members`:

Members
-------

printfn
    actual output fxn

arg
    output fxn specific data

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
        the struct \ :c:type:`struct seq_file <seq_file>`\  to output to

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
        the struct \ :c:type:`struct device <device>`\  pointer

.. _`drm_info_printer.return`:

Return
------

The \ :c:type:`struct drm_printer <drm_printer>`\  object

.. This file was automatic generated / don't edit.

