.. -*- coding: utf-8; mode: rst -*-

==============
debugobjects.h
==============

.. _`debug_obj`:

struct debug_obj
================

.. c:type:: struct debug_obj

    representaion of an tracked object



Definition
----------

.. code-block:: c

  struct debug_obj {
    struct hlist_node node;
    enum debug_obj_state state;
    unsigned int astate;
    void * object;
    struct debug_obj_descr * descr;
  };



Members
-------

:``node``:
    hlist node to link the object into the tracker list

:``state``:
    tracked object state

:``astate``:
    current active state

:``object``:
    pointer to the real object

:``descr``:
    pointer to an object type specific debug description structure



.. _`debug_obj_descr`:

struct debug_obj_descr
======================

.. c:type:: struct debug_obj_descr

    object type specific debug description structure



Definition
----------

.. code-block:: c

  struct debug_obj_descr {
    const char * name;
    void *(* debug_hint) (void *addr);
    int (* fixup_init) (void *addr, enum debug_obj_state state);
    int (* fixup_activate) (void *addr, enum debug_obj_state state);
    int (* fixup_destroy) (void *addr, enum debug_obj_state state);
    int (* fixup_free) (void *addr, enum debug_obj_state state);
    int (* fixup_assert_init) (void *addr, enum debug_obj_state state);
  };



Members
-------

:``name``:
    name of the object typee

:``debug_hint``:
    function returning address, which have associated
    kernel symbol, to allow identify the object

:``fixup_init``:
    fixup function, which is called when the init check
    fails

:``fixup_activate``:
    fixup function, which is called when the activate check
    fails

:``fixup_destroy``:
    fixup function, which is called when the destroy check
    fails

:``fixup_free``:
    fixup function, which is called when the free check
    fails

:``fixup_assert_init``:
    fixup function, which is called when the assert_init
    check fails


