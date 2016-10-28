.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/groups.c

.. _`set_groups`:

set_groups
==========

.. c:function:: void set_groups(struct cred *new, struct group_info *group_info)

    Change a group subscription in a set of credentials

    :param struct cred \*new:
        The newly prepared set of credentials to alter

    :param struct group_info \*group_info:
        The group list to install

.. _`set_current_groups`:

set_current_groups
==================

.. c:function:: int set_current_groups(struct group_info *group_info)

    Change current's group subscription

    :param struct group_info \*group_info:
        The group list to impose

.. _`set_current_groups.description`:

Description
-----------

Validate a group subscription and, if valid, impose it upon current's task
security record.

.. This file was automatic generated / don't edit.

