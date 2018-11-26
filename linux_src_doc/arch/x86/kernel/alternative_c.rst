.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/alternative.c

.. _`text_poke_early`:

text_poke_early
===============

.. c:function:: void *text_poke_early(void *addr, const void *opcode, size_t len)

    Update instructions on a live kernel at boot time

    :param addr:
        address to modify
    :type addr: void \*

    :param opcode:
        source of the copy
    :type opcode: const void \*

    :param len:
        length to copy
    :type len: size_t

.. _`text_poke_early.description`:

Description
-----------

When you use this code to patch more than one byte of an instruction
you need to make sure that other CPUs cannot execute this code in parallel.
Also no thread must be currently preempted in the middle of these
instructions. And on the local CPU you need to be protected again NMI or MCE
handlers seeing an inconsistent instruction while you patch.

.. _`text_poke`:

text_poke
=========

.. c:function:: void *text_poke(void *addr, const void *opcode, size_t len)

    Update instructions on a live kernel

    :param addr:
        address to modify
    :type addr: void \*

    :param opcode:
        source of the copy
    :type opcode: const void \*

    :param len:
        length to copy
    :type len: size_t

.. _`text_poke.description`:

Description
-----------

Only atomic text poke/set should be allowed when not doing early patching.
It means the size must be writable atomically and the address must be aligned
in a way that permits an atomic write. It also makes sure we fit on a single
page.

.. _`text_poke_bp`:

text_poke_bp
============

.. c:function:: void *text_poke_bp(void *addr, const void *opcode, size_t len, void *handler)

    - update instructions on live kernel on SMP

    :param addr:
        address to patch
    :type addr: void \*

    :param opcode:
        opcode of new instruction
    :type opcode: const void \*

    :param len:
        length to copy
    :type len: size_t

    :param handler:
        address to jump to when the temporary breakpoint is hit
    :type handler: void \*

.. _`text_poke_bp.description`:

Description
-----------

Modify multi-byte instruction by using int3 breakpoint on SMP.
We completely avoid \ :c:func:`stop_machine`\  here, and achieve the
synchronization using int3 breakpoint.

.. _`text_poke_bp.the-way-it-is-done`:

The way it is done
------------------

- add a int3 trap to the address that will be patched
- sync cores
- update all but the first byte of the patched range
- sync cores
- replace the first byte (int3) by the first byte of
replacing opcode
- sync cores

.. This file was automatic generated / don't edit.

