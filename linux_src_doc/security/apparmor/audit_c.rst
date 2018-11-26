.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/audit.c

.. _`audit_pre`:

audit_pre
=========

.. c:function:: void audit_pre(struct audit_buffer *ab, void *ca)

    core AppArmor function.

    :param ab:
        audit buffer to fill (NOT NULL)
    :type ab: struct audit_buffer \*

    :param ca:
        audit structure containing data to audit (NOT NULL)
    :type ca: void \*

.. _`audit_pre.description`:

Description
-----------

Record common AppArmor audit data from \ ``sa``\ 

.. _`aa_audit_msg`:

aa_audit_msg
============

.. c:function:: void aa_audit_msg(int type, struct common_audit_data *sa, void (*cb)(struct audit_buffer *, void *))

    Log a message to the audit subsystem

    :param type:
        *undescribed*
    :type type: int

    :param sa:
        audit event structure (NOT NULL)
    :type sa: struct common_audit_data \*

    :param void (\*cb)(struct audit_buffer \*, void \*):
        optional callback fn for type specific fields (MAYBE NULL)

.. _`aa_audit`:

aa_audit
========

.. c:function:: int aa_audit(int type, struct aa_profile *profile, struct common_audit_data *sa, void (*cb)(struct audit_buffer *, void *))

    Log a profile based audit event to the audit subsystem

    :param type:
        audit type for the message
    :type type: int

    :param profile:
        profile to check against (NOT NULL)
    :type profile: struct aa_profile \*

    :param sa:
        audit event (NOT NULL)
    :type sa: struct common_audit_data \*

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

