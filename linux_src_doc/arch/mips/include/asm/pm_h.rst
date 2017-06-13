.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/pm.h

.. _`mips_static_suspend_state`:

struct mips_static_suspend_state
================================

.. c:type:: struct mips_static_suspend_state

    Core saved CPU state across S2R.

.. _`mips_static_suspend_state.definition`:

Definition
----------

.. code-block:: c

    struct mips_static_suspend_state {
    #ifdef CONFIG_EVA
        unsigned long segctl;
    #endif
        unsigned long sp;
    }

.. _`mips_static_suspend_state.members`:

Members
-------

segctl
    CP0 Segment control registers.

sp
    Stack frame where GP register context is saved.

.. _`mips_static_suspend_state.description`:

Description
-----------

This structure contains minimal CPU state that must be saved in static kernel
data in order to be able to restore the rest of the state. This includes
segmentation configuration in the case of EVA being enabled, as they must be
restored prior to any kmalloc'd memory being referenced (even the stack
pointer).

.. This file was automatic generated / don't edit.

