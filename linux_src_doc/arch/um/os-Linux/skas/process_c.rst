.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/um/os-Linux/skas/process.c

.. _`userspace_tramp`:

userspace_tramp
===============

.. c:function:: int userspace_tramp(void *stack)

    userspace trampoline

    :param void \*stack:
        pointer to the new userspace stack page, can be NULL, if? FIXME:

.. _`userspace_tramp.description`:

Description
-----------

The userspace trampoline is used to setup a new userspace process in \ :c:func:`start_userspace`\  after it was \ :c:func:`clone`\ 'ed.
This function will run on a temporary stack page.
It \ :c:func:`ptrace`\ 'es itself, then

.. _`userspace_tramp.two-pages-are-mapped-into-the-userspace-address-space`:

Two pages are mapped into the userspace address space
-----------------------------------------------------

- STUB_CODE (with EXEC), which contains the skas stub code
- STUB_DATA (with R/W), which contains a data page that is used to transfer certain data between the UML userspace process and the UML kernel.
Also for the userspace process a SIGSEGV handler is installed to catch pagefaults in the userspace process.
And last the process stops itself to give control to the UML kernel for this userspace process.

.. _`userspace_tramp.return`:

Return
------

Always zero, otherwise the current userspace process is ended with non null \ :c:func:`exit`\  call

.. _`start_userspace`:

start_userspace
===============

.. c:function:: int start_userspace(unsigned long stub_stack)

    prepare a new userspace process

    :param unsigned long stub_stack:
        pointer to the stub stack. Can be NULL, if? FIXME:

.. _`start_userspace.description`:

Description
-----------

Setups a new temporary stack page that is used while \ :c:func:`userspace_tramp`\  runs
Clones the kernel process into a new userspace process, with FDs only.

.. _`start_userspace.return`:

Return
------

When positive: the process id of the new userspace process,
when negative: an error number.

.. _`start_userspace.fixme`:

FIXME
-----

can PIDs become negative?!

.. This file was automatic generated / don't edit.

