.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/capability.c

.. _`audit_cb`:

audit_cb
========

.. c:function:: void audit_cb(struct audit_buffer *ab, void *va)

    call back for capability components of audit struct \ ``ab``\  - audit buffer   (NOT NULL) \ ``va``\  - audit struct to audit data from  (NOT NULL)

    :param ab:
        *undescribed*
    :type ab: struct audit_buffer \*

    :param va:
        *undescribed*
    :type va: void \*

.. _`audit_caps`:

audit_caps
==========

.. c:function:: int audit_caps(struct common_audit_data *sa, struct aa_profile *profile, int cap, int error)

    audit a capability

    :param sa:
        audit data
    :type sa: struct common_audit_data \*

    :param profile:
        profile being tested for confinement (NOT NULL)
    :type profile: struct aa_profile \*

    :param cap:
        capability tested
    :type cap: int

    :param error:
        error code returned by test
    :type error: int

.. _`audit_caps.description`:

Description
-----------

Do auditing of capability and handle, audit/complain/kill modes switching
and duplicate message elimination.

.. _`audit_caps.return`:

Return
------

0 or sa->error on success,  error code on failure

.. _`profile_capable`:

profile_capable
===============

.. c:function:: int profile_capable(struct aa_profile *profile, int cap, int audit, struct common_audit_data *sa)

    test if profile allows use of capability \ ``cap``\ 

    :param profile:
        profile being enforced    (NOT NULL, NOT unconfined)
    :type profile: struct aa_profile \*

    :param cap:
        capability to test if allowed
    :type cap: int

    :param audit:
        whether an audit record should be generated
    :type audit: int

    :param sa:
        audit data (MAY BE NULL indicating no auditing)
    :type sa: struct common_audit_data \*

.. _`profile_capable.return`:

Return
------

0 if allowed else -EPERM

.. _`aa_capable`:

aa_capable
==========

.. c:function:: int aa_capable(struct aa_label *label, int cap, int audit)

    test permission to use capability

    :param label:
        label being tested for capability (NOT NULL)
    :type label: struct aa_label \*

    :param cap:
        capability to be tested
    :type cap: int

    :param audit:
        whether an audit record should be generated
    :type audit: int

.. _`aa_capable.description`:

Description
-----------

Look up capability in profile capability set.

.. _`aa_capable.return`:

Return
------

0 on success, or else an error code.

.. This file was automatic generated / don't edit.

