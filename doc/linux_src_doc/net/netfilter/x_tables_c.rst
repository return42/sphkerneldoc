.. -*- coding: utf-8; mode: rst -*-

==========
x_tables.c
==========


.. _`xt_hook_ops_alloc`:

xt_hook_ops_alloc
=================

.. c:function:: struct nf_hook_ops *xt_hook_ops_alloc (const struct xt_table *table, nf_hookfn *fn)

    set up hooks for a new table

    :param const struct xt_table \*table:
        table with metadata needed to set up hooks

    :param nf_hookfn \*fn:
        Hook function



.. _`xt_hook_ops_alloc.description`:

Description
-----------

This function will create the nf_hook_ops that the x_table needs
to hand to :c:func:`xt_hook_link_net`.

