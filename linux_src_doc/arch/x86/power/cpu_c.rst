.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/power/cpu.c

.. _`__save_processor_state`:

__save_processor_state
======================

.. c:function:: void __save_processor_state(struct saved_context *ctxt)

    save CPU registers before creating a hibernation image and before restoring the memory state from it \ ``ctxt``\  - structure to store the registers contents in

    :param struct saved_context \*ctxt:
        *undescribed*

.. _`__save_processor_state.note`:

NOTE
----

If there is a CPU register the modification of which by the
boot kernel (ie. the kernel used for loading the hibernation image)
might affect the operations of the restored target kernel (ie. the one
saved in the hibernation image), then its contents must be saved by this
function.  In other words, if kernel A is hibernated and different
kernel B is used for loading the hibernation image into memory, the
kernel A's \__save_processor_state() function must save all registers
needed by kernel A, so that it can operate correctly after the resume
regardless of what kernel B does in the meantime.

.. _`__restore_processor_state`:

__restore_processor_state
=========================

.. c:function:: void notrace __restore_processor_state(struct saved_context *ctxt)

    restore the contents of CPU registers saved by \__save_processor_state() \ ``ctxt``\  - structure to load the registers contents from

    :param struct saved_context \*ctxt:
        *undescribed*

.. _`__restore_processor_state.description`:

Description
-----------

The asm code that gets us here will have restored a usable GDT, although
it will be pointing to the wrong alias.

.. This file was automatic generated / don't edit.

