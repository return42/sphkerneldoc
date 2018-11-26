.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/include/avc.h

.. _`avc_audit`:

avc_audit
=========

.. c:function:: int avc_audit(struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass, u32 requested, struct av_decision *avd, int result, struct common_audit_data *a, int flags)

    Audit the granting or denial of permissions.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param requested:
        requested permissions
    :type requested: u32

    :param avd:
        access vector decisions
    :type avd: struct av_decision \*

    :param result:
        result from avc_has_perm_noaudit
    :type result: int

    :param a:
        auxiliary audit data
    :type a: struct common_audit_data \*

    :param flags:
        VFS walk flags
    :type flags: int

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

