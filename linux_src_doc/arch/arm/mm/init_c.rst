.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mm/init.c

.. _`update_sections_early`:

update_sections_early
=====================

.. c:function:: void update_sections_early(struct section_perm perms, int n)

    framework and executed by only one CPU while all other CPUs will spin and wait, so no locking is required in this function.

    :param perms:
        *undescribed*
    :type perms: struct section_perm

    :param n:
        *undescribed*
    :type n: int

.. This file was automatic generated / don't edit.

