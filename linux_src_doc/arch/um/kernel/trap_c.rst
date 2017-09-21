.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/um/kernel/trap.c

.. _`segv_handler`:

segv_handler
============

.. c:function:: void segv_handler(int sig, struct siginfo *unused_si, struct uml_pt_regs *regs)

    the SIGSEGV handler

    :param int sig:
        the signal number

    :param struct siginfo \*unused_si:
        the signal info struct; unused in this handler

    :param struct uml_pt_regs \*regs:
        the ptrace register information

.. _`segv_handler.description`:

Description
-----------

The handler first extracts the faultinfo from the UML ptrace regs struct.
If the userfault did not happen in an UML userspace process, bad_segv is called.
Otherwise the signal did happen in a cloned userspace process, handle it.

.. This file was automatic generated / don't edit.

