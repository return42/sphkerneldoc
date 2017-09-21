.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/capability.c

.. _`audit_cb`:

audit_cb
========

.. c:function:: void audit_cb(struct audit_buffer *ab, void *va)

    call back for capability components of audit struct \ ``ab``\  - audit buffer   (NOT NULL) \ ``va``\  - audit struct to audit data from  (NOT NULL)

    :param struct audit_buffer \*ab:
        *undescribed*

    :param void \*va:
        *undescribed*

.. _`audit_caps`:

audit_caps
==========

.. c:function:: int audit_caps(struct common_audit_data *sa, struct aa_profile *profile, int cap, int error)

    audit a capability

    :param struct common_audit_data \*sa:
        audit data

    :param struct aa_profile \*profile:
        profile being tested for confinement (NOT NULL)

    :param int cap:
        capability tested

    :param int error:
        error code returned by test

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

    :param struct aa_profile \*profile:
        profile being enforced    (NOT NULL, NOT unconfined)

    :param int cap:
        capability to test if allowed

    :param int audit:
        whether an audit record should be generated

    :param struct common_audit_data \*sa:
        audit data (MAY BE NULL indicating no auditing)

.. _`profile_capable.return`:

Return
------

0 if allowed else -EPERM

.. _`aa_capable`:

aa_capable
==========

.. c:function:: int aa_capable(struct aa_label *label, int cap, int audit)

    test permission to use capability

    :param struct aa_label \*label:
        label being tested for capability (NOT NULL)

    :param int cap:
        capability to be tested

    :param int audit:
        whether an audit record should be generated

.. _`aa_capable.description`:

Description
-----------

Look up capability in profile capability set.

.. _`aa_capable.return`:

Return
------

0 on success, or else an error code.

.. This file was automatic generated / don't edit.

