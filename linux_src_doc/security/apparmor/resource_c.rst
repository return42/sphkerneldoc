.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/resource.c

.. _`audit_resource`:

audit_resource
==============

.. c:function:: int audit_resource(struct aa_profile *profile, unsigned int resource, unsigned long value, struct aa_label *peer, const char *info, int error)

    audit setting resource limit

    :param struct aa_profile \*profile:
        profile being enforced  (NOT NULL)

    :param unsigned int resource:
        rlimit being auditing

    :param unsigned long value:
        value being set

    :param struct aa_label \*peer:
        *undescribed*

    :param const char \*info:
        *undescribed*

    :param int error:
        error value

.. _`audit_resource.return`:

Return
------

0 or sa->error else other error code on failure

.. _`aa_map_resource`:

aa_map_resource
===============

.. c:function:: int aa_map_resource(int resource)

    map compiled policy resource to internal #

    :param int resource:
        flattened policy resource number

.. _`aa_map_resource.return`:

Return
------

resource # for the current architecture.

rlimit resource can vary based on architecture, map the compiled policy
resource # to the internal representation for the architecture.

.. _`aa_task_setrlimit`:

aa_task_setrlimit
=================

.. c:function:: int aa_task_setrlimit(struct aa_label *label, struct task_struct *task, unsigned int resource, struct rlimit *new_rlim)

    test permission to set an rlimit \ ``label``\  - label confining the task  (NOT NULL) \ ``task``\  - task the resource is being set on \ ``resource``\  - the resource being set \ ``new_rlim``\  - the new resource limit  (NOT NULL)

    :param struct aa_label \*label:
        *undescribed*

    :param struct task_struct \*task:
        *undescribed*

    :param unsigned int resource:
        *undescribed*

    :param struct rlimit \*new_rlim:
        *undescribed*

.. _`aa_task_setrlimit.description`:

Description
-----------

Control raising the processes hard limit.

.. _`aa_task_setrlimit.return`:

Return
------

0 or error code if setting resource failed

.. _`__aa_transition_rlimits`:

__aa_transition_rlimits
=======================

.. c:function:: void __aa_transition_rlimits(struct aa_label *old_l, struct aa_label *new_l)

    apply new profile rlimits

    :param struct aa_label \*old_l:
        old label on task  (NOT NULL)

    :param struct aa_label \*new_l:
        new label with rlimits to apply  (NOT NULL)

.. This file was automatic generated / don't edit.

