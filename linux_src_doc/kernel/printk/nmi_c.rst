.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/printk/nmi.c

.. _`printk_nmi_flush`:

printk_nmi_flush
================

.. c:function:: void printk_nmi_flush( void)

    flush all per-cpu nmi buffers.

    :param  void:
        no arguments

.. _`printk_nmi_flush.description`:

Description
-----------

The buffers are flushed automatically via IRQ work. This function
is useful only when someone wants to be sure that all buffers have
been flushed at some point.

.. _`printk_nmi_flush_on_panic`:

printk_nmi_flush_on_panic
=========================

.. c:function:: void printk_nmi_flush_on_panic( void)

    flush all per-cpu nmi buffers when the system goes down.

    :param  void:
        no arguments

.. _`printk_nmi_flush_on_panic.description`:

Description
-----------

Similar to \ :c:func:`printk_nmi_flush`\  but it can be called even in NMI context when
the system goes down. It does the best effort to get NMI messages into
the main ring buffer.

Note that it could try harder when there is only one CPU online.

.. This file was automatic generated / don't edit.

