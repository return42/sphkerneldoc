.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/device_cgroup.c

.. _`dev_exception_clean`:

dev_exception_clean
===================

.. c:function:: void dev_exception_clean(struct dev_cgroup *dev_cgroup)

    frees all entries of the exception list

    :param dev_cgroup:
        dev_cgroup with the exception list to be cleaned
    :type dev_cgroup: struct dev_cgroup \*

.. _`dev_exception_clean.description`:

Description
-----------

called under devcgroup_mutex

.. _`devcgroup_online`:

devcgroup_online
================

.. c:function:: int devcgroup_online(struct cgroup_subsys_state *css)

    initializes devcgroup's behavior and exceptions based on parent's

    :param css:
        css getting online
        returns 0 in case of success, error code otherwise
    :type css: struct cgroup_subsys_state \*

.. _`match_exception`:

match_exception
===============

.. c:function:: bool match_exception(struct list_head *exceptions, short type, u32 major, u32 minor, short access)

    iterates the exception list trying to find a complete match

    :param exceptions:
        list of exceptions
    :type exceptions: struct list_head \*

    :param type:
        device type (DEVCG_DEV_BLOCK or DEVCG_DEV_CHAR)
    :type type: short

    :param major:
        device file major number, ~0 to match all
    :type major: u32

    :param minor:
        device file minor number, ~0 to match all
    :type minor: u32

    :param access:
        permission mask (DEVCG_ACC_READ, DEVCG_ACC_WRITE, DEVCG_ACC_MKNOD)
    :type access: short

.. _`match_exception.description`:

Description
-----------

It is considered a complete match if an exception is found that will
contain the entire range of provided parameters.

.. _`match_exception.return`:

Return
------

true in case it matches an exception completely

.. _`match_exception_partial`:

match_exception_partial
=======================

.. c:function:: bool match_exception_partial(struct list_head *exceptions, short type, u32 major, u32 minor, short access)

    iterates the exception list trying to find a partial match

    :param exceptions:
        list of exceptions
    :type exceptions: struct list_head \*

    :param type:
        device type (DEVCG_DEV_BLOCK or DEVCG_DEV_CHAR)
    :type type: short

    :param major:
        device file major number, ~0 to match all
    :type major: u32

    :param minor:
        device file minor number, ~0 to match all
    :type minor: u32

    :param access:
        permission mask (DEVCG_ACC_READ, DEVCG_ACC_WRITE, DEVCG_ACC_MKNOD)
    :type access: short

.. _`match_exception_partial.description`:

Description
-----------

It is considered a partial match if an exception's range is found to
contain \*any\* of the devices specified by provided parameters. This is
used to make sure no extra access is being granted that is forbidden by
any of the exception list.

.. _`match_exception_partial.return`:

Return
------

true in case the provided range mat matches an exception completely

.. _`verify_new_ex`:

verify_new_ex
=============

.. c:function:: bool verify_new_ex(struct dev_cgroup *dev_cgroup, struct dev_exception_item *refex, enum devcg_behavior behavior)

    verifies if a new exception is allowed by parent cgroup's permissions

    :param dev_cgroup:
        dev cgroup to be tested against
    :type dev_cgroup: struct dev_cgroup \*

    :param refex:
        new exception
    :type refex: struct dev_exception_item \*

    :param behavior:
        behavior of the exception's dev_cgroup
    :type behavior: enum devcg_behavior

.. _`verify_new_ex.description`:

Description
-----------

This is used to make sure a child cgroup won't have more privileges
than its parent

.. _`parent_allows_removal`:

parent_allows_removal
=====================

.. c:function:: bool parent_allows_removal(struct dev_cgroup *childcg, struct dev_exception_item *ex)

    verify if it's ok to remove an exception

    :param childcg:
        child cgroup from where the exception will be removed
    :type childcg: struct dev_cgroup \*

    :param ex:
        exception being removed
    :type ex: struct dev_exception_item \*

.. _`parent_allows_removal.description`:

Description
-----------

When removing an exception in cgroups with default ALLOW policy, it must
be checked if removing it will give the child cgroup more access than the
parent.

.. _`parent_allows_removal.return`:

Return
------

true if it's ok to remove exception, false otherwise

.. _`may_allow_all`:

may_allow_all
=============

.. c:function:: int may_allow_all(struct dev_cgroup *parent)

    checks if it's possible to change the behavior to allow based on parent's rules.

    :param parent:
        device cgroup's parent
    :type parent: struct dev_cgroup \*

.. _`may_allow_all.return`:

Return
------

!= 0 in case it's allowed, 0 otherwise

.. _`revalidate_active_exceptions`:

revalidate_active_exceptions
============================

.. c:function:: void revalidate_active_exceptions(struct dev_cgroup *devcg)

    walks through the active exception list and revalidates the exceptions based on parent's behavior and exceptions. The exceptions that are no longer valid will be removed. Called with devcgroup_mutex held.

    :param devcg:
        cgroup which exceptions will be checked
    :type devcg: struct dev_cgroup \*

.. _`revalidate_active_exceptions.description`:

Description
-----------

This is one of the three key functions for hierarchy implementation.
This function is responsible for re-evaluating all the cgroup's active
exceptions due to a parent's exception change.
Refer to Documentation/cgroup-v1/devices.txt for more details.

.. _`propagate_exception`:

propagate_exception
===================

.. c:function:: int propagate_exception(struct dev_cgroup *devcg_root, struct dev_exception_item *ex)

    propagates a new exception to the children

    :param devcg_root:
        device cgroup that added a new exception
    :type devcg_root: struct dev_cgroup \*

    :param ex:
        new exception to be propagated
    :type ex: struct dev_exception_item \*

.. _`propagate_exception.return`:

Return
------

0 in case of success, != 0 in case of error

.. _`__devcgroup_check_permission`:

\__devcgroup_check_permission
=============================

.. c:function:: int __devcgroup_check_permission(short type, u32 major, u32 minor, short access)

    checks if an inode operation is permitted

    :param type:
        device type
    :type type: short

    :param major:
        device major number
    :type major: u32

    :param minor:
        device minor number
    :type minor: u32

    :param access:
        combination of DEVCG_ACC_WRITE, DEVCG_ACC_READ and DEVCG_ACC_MKNOD
    :type access: short

.. _`__devcgroup_check_permission.description`:

Description
-----------

returns 0 on success, -EPERM case the operation is not permitted

.. This file was automatic generated / don't edit.

