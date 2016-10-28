.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/livepatch/core.c

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

.. _`klp_disable_patch`:

klp_disable_patch
=================

.. c:function:: int klp_disable_patch(struct klp_patch *patch)

    disables a registered patch

    :param struct klp_patch \*patch:
        The registered, enabled patch to be disabled

.. _`klp_disable_patch.description`:

Description
-----------

Unregisters the patched functions from ftrace.

.. _`klp_disable_patch.return`:

Return
------

0 on success, otherwise error

.. _`klp_enable_patch`:

klp_enable_patch
================

.. c:function:: int klp_enable_patch(struct klp_patch *patch)

    enables a registered patch

    :param struct klp_patch \*patch:
        The registered, disabled patch to be enabled

.. _`klp_enable_patch.description`:

Description
-----------

Performs the needed symbol lookups and code relocations,
then registers the patched functions with ftrace.

.. _`klp_enable_patch.return`:

Return
------

0 on success, otherwise error

.. _`klp_unregister_patch`:

klp_unregister_patch
====================

.. c:function:: int klp_unregister_patch(struct klp_patch *patch)

    unregisters a patch

    :param struct klp_patch \*patch:
        Disabled patch to be unregistered

.. _`klp_unregister_patch.description`:

Description
-----------

Frees the data structures and removes the sysfs interface.

.. _`klp_unregister_patch.return`:

Return
------

0 on success, otherwise error

.. _`klp_register_patch`:

klp_register_patch
==================

.. c:function:: int klp_register_patch(struct klp_patch *patch)

    registers a patch

    :param struct klp_patch \*patch:
        Patch to be registered

.. _`klp_register_patch.description`:

Description
-----------

Initializes the data structure associated with the patch and
creates the sysfs interface.

.. _`klp_register_patch.return`:

Return
------

0 on success, otherwise error

.. This file was automatic generated / don't edit.

