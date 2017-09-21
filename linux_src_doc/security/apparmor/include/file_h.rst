.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/file.h

.. _`aa_alloc_file_ctx`:

aa_alloc_file_ctx
=================

.. c:function:: struct aa_file_ctx *aa_alloc_file_ctx(struct aa_label *label, gfp_t gfp)

    allocate file_ctx

    :param struct aa_label \*label:
        initial label of task creating the file

    :param gfp_t gfp:
        gfp flags for allocation

.. _`aa_alloc_file_ctx.return`:

Return
------

file_ctx or NULL on failure

.. _`aa_free_file_ctx`:

aa_free_file_ctx
================

.. c:function:: void aa_free_file_ctx(struct aa_file_ctx *ctx)

    free a file_ctx

    :param struct aa_file_ctx \*ctx:
        file_ctx to free  (MAYBE_NULL)

.. _`aa_file_rules`:

struct aa_file_rules
====================

.. c:type:: struct aa_file_rules

    components used for file rule permissions

.. _`aa_file_rules.definition`:

Definition
----------

.. code-block:: c

    struct aa_file_rules {
        unsigned int start;
        struct aa_dfa *dfa;
        struct aa_domain trans;
    }

.. _`aa_file_rules.members`:

Members
-------

start
    *undescribed*

dfa
    dfa to match path names and conditionals against

trans
    transition table for indexed by named x transitions

.. _`aa_file_rules.description`:

Description
-----------

File permission are determined by matching a path against \ ``dfa``\  and then
then using the value of the accept entry for the matching state as
an index into \ ``perms``\ .  If a named exec transition is required it is
looked up in the transition table.

.. _`aa_map_file_to_perms`:

aa_map_file_to_perms
====================

.. c:function:: u32 aa_map_file_to_perms(struct file *file)

    map file flags to AppArmor permissions

    :param struct file \*file:
        open file to map flags to AppArmor permissions

.. _`aa_map_file_to_perms.return`:

Return
------

apparmor permission set for the file

.. This file was automatic generated / don't edit.

