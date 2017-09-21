.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/migration.c

.. _`irq_fixup_move_pending`:

irq_fixup_move_pending
======================

.. c:function:: bool irq_fixup_move_pending(struct irq_desc *desc, bool force_clear)

    Cleanup irq move pending from a dying CPU

    :param struct irq_desc \*desc:
        Interrupt descpriptor to clean up

    :param bool force_clear:
        If set clear the move pending bit unconditionally.
        If not set, clear it only when the dying CPU is the
        last one in the pending mask.

.. _`irq_fixup_move_pending.description`:

Description
-----------

Returns true if the pending bit was set and the pending mask contains an
online CPU other than the dying CPU.

.. This file was automatic generated / don't edit.

