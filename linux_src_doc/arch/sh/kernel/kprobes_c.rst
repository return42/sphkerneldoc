.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/kprobes.c

.. _`kprobe_handle_illslot`:

kprobe_handle_illslot
=====================

.. c:function:: int __kprobes kprobe_handle_illslot(unsigned long pc)

    containing a kprobe, remove the probe.

    :param pc:
        *undescribed*
    :type pc: unsigned long

.. _`kprobe_handle_illslot.description`:

Description
-----------

Returns 0 if the exception was handled successfully, 1 otherwise.

.. This file was automatic generated / don't edit.

