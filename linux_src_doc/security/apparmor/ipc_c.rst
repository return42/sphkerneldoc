.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/ipc.c

.. _`audit_ptrace_mask`:

audit_ptrace_mask
=================

.. c:function:: void audit_ptrace_mask(struct audit_buffer *ab, u32 mask)

    convert mask to permission string

    :param struct audit_buffer \*ab:
        *undescribed*

    :param u32 mask:
        permission mask to convert

.. _`aa_may_ptrace`:

aa_may_ptrace
=============

.. c:function:: int aa_may_ptrace(struct aa_label *tracer, struct aa_label *tracee, u32 request)

    test if tracer task can trace the tracee

    :param struct aa_label \*tracer:
        label of the task doing the tracing  (NOT NULL)

    :param struct aa_label \*tracee:
        task label to be traced

    :param u32 request:
        permission request

.. _`aa_may_ptrace.return`:

Return
------

%0 else error code if permission denied or error

.. This file was automatic generated / don't edit.

