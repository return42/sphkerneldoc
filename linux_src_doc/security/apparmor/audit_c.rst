.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/audit.c

.. _`audit_pre`:

audit_pre
=========

.. c:function:: void audit_pre(struct audit_buffer *ab, void *ca)

    core AppArmor function.

    :param struct audit_buffer \*ab:
        audit buffer to fill (NOT NULL)

    :param void \*ca:
        audit structure containing data to audit (NOT NULL)

.. _`audit_pre.description`:

Description
-----------

Record common AppArmor audit data from \ ``sa``\ 

.. _`aa_audit_msg`:

aa_audit_msg
============

.. c:function:: void aa_audit_msg(int type, struct common_audit_data *sa, void (*cb)(struct audit_buffer *, void *))

    Log a message to the audit subsystem

    :param int type:
        *undescribed*

    :param struct common_audit_data \*sa:
        audit event structure (NOT NULL)

    :param void (\*cb)(struct audit_buffer \*, void \*):
        optional callback fn for type specific fields (MAYBE NULL)

.. _`aa_audit`:

aa_audit
========

.. c:function:: int aa_audit(int type, struct aa_profile *profile, gfp_t gfp, struct common_audit_data *sa, void (*cb)(struct audit_buffer *, void *))

    Log a profile based audit event to the audit subsystem

    :param int type:
        audit type for the message

    :param struct aa_profile \*profile:
        profile to check against (NOT NULL)

    :param gfp_t gfp:
        allocation flags to use

    :param struct common_audit_data \*sa:
        audit event (NOT NULL)

    :param void (\*cb)(struct audit_buffer \*, void \*):
        optional callback fn for type specific fields (MAYBE NULL)

.. _`aa_audit.description`:

Description
-----------

Handle default message switching based off of audit mode flags

.. _`aa_audit.return`:

Return
------

error on failure

.. This file was automatic generated / don't edit.

