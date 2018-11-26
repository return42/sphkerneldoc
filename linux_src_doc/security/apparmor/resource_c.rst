.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/resource.c

.. _`audit_resource`:

audit_resource
==============

.. c:function:: int audit_resource(struct aa_profile *profile, unsigned int resource, unsigned long value, struct aa_label *peer, const char *info, int error)

    audit setting resource limit

    :param profile:
        profile being enforced  (NOT NULL)
    :type profile: struct aa_profile \*

    :param resource:
        rlimit being auditing
    :type resource: unsigned int

    :param value:
        value being set
    :type value: unsigned long

    :param peer:
        *undescribed*
    :type peer: struct aa_label \*

    :param info:
        *undescribed*
    :type info: const char \*

    :param error:
        error value
    :type error: int

.. _`audit_resource.return`:

Return
------

0 or sa->error else other error code on failure

.. _`aa_map_resource`:

aa_map_resource
===============

.. c:function:: int aa_map_resource(int resource)

    map compiled policy resource to internal #

    :param resource:
        flattened policy resource number
    :type resource: int

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

    :param label:
        *undescribed*
    :type label: struct aa_label \*

    :param task:
        *undescribed*
    :type task: struct task_struct \*

    :param resource:
        *undescribed*
    :type resource: unsigned int

    :param new_rlim:
        *undescribed*
    :type new_rlim: struct rlimit \*

.. _`aa_task_setrlimit.description`:

Description
-----------

Control raising the processes hard limit.

.. _`aa_task_setrlimit.return`:

Return
------

0 or error code if setting resource failed

.. _`__aa_transition_rlimits`:

\__aa_transition_rlimits
========================

.. c:function:: void __aa_transition_rlimits(struct aa_label *old_l, struct aa_label *new_l)

    apply new profile rlimits

    :param old_l:
        old label on task  (NOT NULL)
    :type old_l: struct aa_label \*

    :param new_l:
        new label with rlimits to apply  (NOT NULL)
    :type new_l: struct aa_label \*

.. This file was automatic generated / don't edit.

