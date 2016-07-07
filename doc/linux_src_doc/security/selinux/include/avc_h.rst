.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/include/avc.h

.. _`avc_audit`:

avc_audit
=========

.. c:function:: int avc_audit(u32 ssid, u32 tsid, u16 tclass, u32 requested, struct av_decision *avd, int result, struct common_audit_data *a, int flags)

    Audit the granting or denial of permissions.

    :param u32 ssid:
        source security identifier

    :param u32 tsid:
        target security identifier

    :param u16 tclass:
        target security class

    :param u32 requested:
        requested permissions

    :param struct av_decision \*avd:
        access vector decisions

    :param int result:
        result from avc_has_perm_noaudit

    :param struct common_audit_data \*a:
        auxiliary audit data

    :param int flags:
        VFS walk flags

.. _`avc_audit.description`:

Description
-----------

Audit the granting or denial of permissions in accordance
with the policy.  This function is typically called by
\ :c:func:`avc_has_perm`\  after a permission check, but can also be
called directly by callers who use \ :c:func:`avc_has_perm_noaudit`\ 
in order to separate the permission check from the auditing.
For example, this separation is useful when the permission check must
be performed under a lock, to allow the lock to be released
before calling the auditing code.

.. This file was automatic generated / don't edit.

