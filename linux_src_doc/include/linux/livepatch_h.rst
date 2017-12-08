.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/livepatch.h

.. _`klp_func`:

struct klp_func
===============

.. c:type:: struct klp_func

    function structure for live patching

.. _`klp_func.definition`:

Definition
----------

.. code-block:: c

    struct klp_func {
        const char *old_name;
        void *new_func;
        unsigned long old_sympos;
        bool immediate;
        unsigned long old_addr;
        struct kobject kobj;
        struct list_head stack_node;
        unsigned long old_size, new_size;
        bool patched;
        bool transition;
    }

.. _`klp_func.members`:

Members
-------

old_name
    name of the function to be patched

new_func
    pointer to the patched function code

old_sympos
    a hint indicating which symbol position the old function
    can be found (optional)

immediate
    patch the func immediately, bypassing safety mechanisms

old_addr
    the address of the function being patched

kobj
    kobject for sysfs resources

stack_node
    list node for klp_ops func_stack list

old_size
    size of the old function

new_size
    size of the new function

patched
    the func has been added to the klp_ops list

transition
    the func is currently being applied or reverted

.. _`klp_func.description`:

Description
-----------

The patched and transition variables define the func's patching state.  When
patching, a func is always in one of the following states:

patched=0 transition=0: unpatched
patched=0 transition=1: unpatched, temporary starting state
patched=1 transition=1: patched, may be visible to some tasks
patched=1 transition=0: patched, visible to all tasks

And when unpatching, it goes in the reverse order:

patched=1 transition=0: patched, visible to all tasks
patched=1 transition=1: patched, may be visible to some tasks
patched=0 transition=1: unpatched, temporary ending state
patched=0 transition=0: unpatched

.. _`klp_callbacks`:

struct klp_callbacks
====================

.. c:type:: struct klp_callbacks

    pre/post live-(un)patch callback structure

.. _`klp_callbacks.definition`:

Definition
----------

.. code-block:: c

    struct klp_callbacks {
        int (*pre_patch)(struct klp_object *obj);
        void (*post_patch)(struct klp_object *obj);
        void (*pre_unpatch)(struct klp_object *obj);
        void (*post_unpatch)(struct klp_object *obj);
        bool post_unpatch_enabled;
    }

.. _`klp_callbacks.members`:

Members
-------

pre_patch
    executed before code patching

post_patch
    executed after code patching

pre_unpatch
    executed before code unpatching

post_unpatch
    executed after code unpatching

post_unpatch_enabled
    flag indicating if post-unpatch callback
    should run

.. _`klp_callbacks.description`:

Description
-----------

All callbacks are optional.  Only the pre-patch callback, if provided,
will be unconditionally executed.  If the parent klp_object fails to
patch for any reason, including a non-zero error status returned from
the pre-patch callback, no further callbacks will be executed.

.. _`klp_object`:

struct klp_object
=================

.. c:type:: struct klp_object

    kernel object structure for live patching

.. _`klp_object.definition`:

Definition
----------

.. code-block:: c

    struct klp_object {
        const char *name;
        struct klp_func *funcs;
        struct klp_callbacks callbacks;
        struct kobject kobj;
        struct module *mod;
        bool patched;
    }

.. _`klp_object.members`:

Members
-------

name
    module name (or NULL for vmlinux)

funcs
    function entries for functions to be patched in the object

callbacks
    functions to be executed pre/post (un)patching

kobj
    kobject for sysfs resources

mod
    kernel module associated with the patched object
    (NULL for vmlinux)

patched
    the object's funcs have been added to the klp_ops list

.. _`klp_patch`:

struct klp_patch
================

.. c:type:: struct klp_patch

    patch structure for live patching

.. _`klp_patch.definition`:

Definition
----------

.. code-block:: c

    struct klp_patch {
        struct module *mod;
        struct klp_object *objs;
        bool immediate;
        struct list_head list;
        struct kobject kobj;
        bool enabled;
        struct completion finish;
    }

.. _`klp_patch.members`:

Members
-------

mod
    reference to the live patch module

objs
    object entries for kernel objects to be patched

immediate
    patch all funcs immediately, bypassing safety mechanisms

list
    list node for global list of registered patches

kobj
    kobject for sysfs resources

enabled
    the patch is enabled (but operation may be incomplete)

finish
    for waiting till it is safe to remove the patch module

.. This file was automatic generated / don't edit.

