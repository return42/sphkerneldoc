.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/ipc.c

.. _`audit_ptrace_mask`:

audit_ptrace_mask
=================

.. c:function:: void audit_ptrace_mask(struct audit_buffer *ab, u32 mask)

    convert mask to permission string

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param mask:
        permission mask to convert
    :type mask: u32

.. _`aa_may_ptrace`:

aa_may_ptrace
=============

.. c:function:: int aa_may_ptrace(struct aa_label *tracer, struct aa_label *tracee, u32 request)

    test if tracer task can trace the tracee

    :param tracer:
        label of the task doing the tracing  (NOT NULL)
    :type tracer: struct aa_label \*

    :param tracee:
        task label to be traced
    :type tracee: struct aa_label \*

    :param request:
        permission request
    :type request: u32

.. _`aa_may_ptrace.return`:

Return
------

\ ``0``\  else error code if permission denied or error

.. _`audit_signal_mask`:

audit_signal_mask
=================

.. c:function:: void audit_signal_mask(struct audit_buffer *ab, u32 mask)

    convert mask to permission string

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param mask:
        permission mask to convert
    :type mask: u32

.. _`audit_signal_cb`:

audit_signal_cb
===============

.. c:function:: void audit_signal_cb(struct audit_buffer *ab, void *va)

    call back for signal specific audit fields

    :param ab:
        audit_buffer  (NOT NULL)
    :type ab: struct audit_buffer \*

    :param va:
        audit struct to audit values of  (NOT NULL)
    :type va: void \*

.. This file was automatic generated / don't edit.

