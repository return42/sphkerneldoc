
.. _API-audit-set-loginuid:

==================
audit_set_loginuid
==================

*man audit_set_loginuid(9)*

*4.6.0-rc1*

set current task's audit_context loginuid


Synopsis
========

.. c:function:: int audit_set_loginuid( kuid_t loginuid )

Arguments
=========

``loginuid``
    loginuid value


Description
===========

Returns 0.

Called (set) from fs/proc/base.c::\ ``proc_loginuid_write``.
