.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/seccomp.h

.. _`seccomp`:

struct seccomp
==============

.. c:type:: struct seccomp

    the state of a seccomp'ed process

.. _`seccomp.definition`:

Definition
----------

.. code-block:: c

    struct seccomp {
        int mode;
        struct seccomp_filter *filter;
    }

.. _`seccomp.members`:

Members
-------

mode
    indicates one of the valid values above for controlled
    system calls available to a process.

filter
    must always point to a valid seccomp-filter or NULL as it is
    accessed without locking during system call entry.

.. _`seccomp.description`:

Description
-----------

@filter must only be accessed from the context of current as there
is no read locking.

.. This file was automatic generated / don't edit.

