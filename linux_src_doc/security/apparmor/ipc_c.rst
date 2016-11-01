.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/ipc.c

.. _`aa_audit_ptrace`:

aa_audit_ptrace
===============

.. c:function:: int aa_audit_ptrace(struct aa_profile *profile, struct aa_profile *target, int error)

    do auditing for ptrace

    :param struct aa_profile \*profile:
        profile being enforced  (NOT NULL)

    :param struct aa_profile \*target:
        profile being traced (NOT NULL)

    :param int error:
        error condition

.. _`aa_audit_ptrace.return`:

Return
------

%0 or error code

.. _`aa_may_ptrace`:

aa_may_ptrace
=============

.. c:function:: int aa_may_ptrace(struct aa_profile *tracer, struct aa_profile *tracee, unsigned int mode)

    test if tracer task can trace the tracee

    :param struct aa_profile \*tracer:
        profile of the task doing the tracing  (NOT NULL)

    :param struct aa_profile \*tracee:
        task to be traced

    :param unsigned int mode:
        whether PTRACE_MODE_READ \|\| PTRACE_MODE_ATTACH

.. _`aa_may_ptrace.return`:

Return
------

%0 else error code if permission denied or error

.. _`aa_ptrace`:

aa_ptrace
=========

.. c:function:: int aa_ptrace(struct task_struct *tracer, struct task_struct *tracee, unsigned int mode)

    do ptrace permission check and auditing

    :param struct task_struct \*tracer:
        task doing the tracing (NOT NULL)

    :param struct task_struct \*tracee:
        task being traced (NOT NULL)

    :param unsigned int mode:
        ptrace mode either PTRACE_MODE_READ \|\| PTRACE_MODE_ATTACH

.. _`aa_ptrace.return`:

Return
------

%0 else error code if permission denied or error

.. This file was automatic generated / don't edit.

