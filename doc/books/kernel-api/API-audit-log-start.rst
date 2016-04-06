
.. _API-audit-log-start:

===============
audit_log_start
===============

*man audit_log_start(9)*

*4.6.0-rc1*

obtain an audit buffer


Synopsis
========

.. c:function:: struct audit_buffer ⋆ audit_log_start( struct audit_context * ctx, gfp_t gfp_mask, int type )

Arguments
=========

``ctx``
    audit_context (may be NULL)

``gfp_mask``
    type of allocation

``type``
    audit message type


Description
===========

Returns audit_buffer pointer on success or NULL on error.

Obtain an audit buffer. This routine does locking to obtain the audit buffer, but then no locking is required for calls to audit_log_⋆format. If the task (ctx) is a task that is
currently in a syscall, then the syscall is marked as auditable and an audit record will be written at syscall exit. If there is no associated task, then task context (ctx) should
be NULL.
