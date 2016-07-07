.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/debugobjects.h

.. _`debug_obj`:

struct debug_obj
================

.. c:type:: struct debug_obj

    representaion of an tracked object

.. _`debug_obj.definition`:

Definition
----------

.. code-block:: c

    struct debug_obj {
        struct hlist_node node;
        enum debug_obj_state state;
        unsigned int astate;
        void *object;
        struct debug_obj_descr *descr;
    }

.. _`debug_obj.members`:

Members
-------

node
    hlist node to link the object into the tracker list

state
    tracked object state

astate
    current active state

object
    pointer to the real object

descr
    pointer to an object type specific debug description structure

.. _`debug_obj_descr`:

struct debug_obj_descr
======================

.. c:type:: struct debug_obj_descr

    object type specific debug description structure

.. _`debug_obj_descr.definition`:

Definition
----------

.. code-block:: c

    struct debug_obj_descr {
        const char *name;
        void *(* debug_hint) (void *addr);
        bool (* is_static_object) (void *addr);
        bool (* fixup_init) (void *addr, enum debug_obj_state state);
        bool (* fixup_activate) (void *addr, enum debug_obj_state state);
        bool (* fixup_destroy) (void *addr, enum debug_obj_state state);
        bool (* fixup_free) (void *addr, enum debug_obj_state state);
        bool (* fixup_assert_init) (void *addr, enum debug_obj_state state);
    }

.. _`debug_obj_descr.members`:

Members
-------

name
    name of the object typee

debug_hint
    function returning address, which have associated
    kernel symbol, to allow identify the object
    \ ``is_static_object``\     return true if the obj is static, otherwise return false

is_static_object
    *undescribed*

fixup_init
    fixup function, which is called when the init check
    fails. All fixup functions must return true if fixup
    was successful, otherwise return false

fixup_activate
    fixup function, which is called when the activate check
    fails

fixup_destroy
    fixup function, which is called when the destroy check
    fails

fixup_free
    fixup function, which is called when the free check
    fails

fixup_assert_init
    fixup function, which is called when the assert_init
    check fails

.. This file was automatic generated / don't edit.

