.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/livepatch/patch.h

.. _`klp_ops`:

struct klp_ops
==============

.. c:type:: struct klp_ops

    structure for tracking registered ftrace ops structs

.. _`klp_ops.definition`:

Definition
----------

.. code-block:: c

    struct klp_ops {
        struct list_head node;
        struct list_head func_stack;
        struct ftrace_ops fops;
    }

.. _`klp_ops.members`:

Members
-------

node
    node for the global klp_ops list

func_stack
    list head for the stack of klp_func's (active func is on top)

fops
    registered ftrace ops struct

.. _`klp_ops.description`:

Description
-----------

A single ftrace_ops is shared between all enabled replacement functions
(klp_func structs) which have the same old_addr.  This allows the switch
between function versions to happen instantaneously by updating the klp_ops
struct's func_stack list.  The winner is the klp_func at the top of the
func_stack (front of the list).

.. This file was automatic generated / don't edit.

