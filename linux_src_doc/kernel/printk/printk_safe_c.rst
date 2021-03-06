.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/printk/printk_safe.c

.. _`printk_safe_flush`:

printk_safe_flush
=================

.. c:function:: void printk_safe_flush( void)

    flush all per-cpu nmi buffers.

    :param void:
        no arguments
    :type void: 

.. _`printk_safe_flush.description`:

Description
-----------

The buffers are flushed automatically via IRQ work. This function
is useful only when someone wants to be sure that all buffers have
been flushed at some point.

.. _`printk_safe_flush_on_panic`:

printk_safe_flush_on_panic
==========================

.. c:function:: void printk_safe_flush_on_panic( void)

    flush all per-cpu nmi buffers when the system goes down.

    :param void:
        no arguments
    :type void: 

.. _`printk_safe_flush_on_panic.description`:

Description
-----------

Similar to \ :c:func:`printk_safe_flush`\  but it can be called even in NMI context when
the system goes down. It does the best effort to get NMI messages into
the main ring buffer.

Note that it could try harder when there is only one CPU online.

.. This file was automatic generated / don't edit.

