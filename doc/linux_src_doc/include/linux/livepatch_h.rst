.. -*- coding: utf-8; mode: rst -*-

===========
livepatch.h
===========


.. _`klp_func`:

struct klp_func
===============

.. c:type:: klp_func

    function structure for live patching


.. _`klp_func.definition`:

Definition
----------

.. code-block:: c

  struct klp_func {
    const char * old_name;
    void * new_func;
    unsigned long old_sympos;
    unsigned long old_addr;
    struct kobject kobj;
    enum klp_state state;
    struct list_head stack_node;
  };


.. _`klp_func.members`:

Members
-------

:``old_name``:
    name of the function to be patched

:``new_func``:
    pointer to the patched function code

:``old_sympos``:
    a hint indicating which symbol position the old function
    can be found (optional)

:``old_addr``:
    the address of the function being patched

:``kobj``:
    kobject for sysfs resources

:``state``:
    tracks function-level patch application state

:``stack_node``:
    list node for klp_ops func_stack list




.. _`klp_reloc`:

struct klp_reloc
================

.. c:type:: klp_reloc

    relocation structure for live patching


.. _`klp_reloc.definition`:

Definition
----------

.. code-block:: c

  struct klp_reloc {
    unsigned long loc;
    unsigned long sympos;
    unsigned long type;
    const char * name;
    int addend;
    int external;
  };


.. _`klp_reloc.members`:

Members
-------

:``loc``:
    address where the relocation will be written

:``sympos``:
    position in kallsyms to disambiguate symbols (optional)

:``type``:
    ELF relocation type

:``name``:
    name of the referenced symbol (for lookup/verification)

:``addend``:
    offset from the referenced symbol

:``external``:
    symbol is either exported or within the live patch module itself




.. _`klp_object`:

struct klp_object
=================

.. c:type:: klp_object

    kernel object structure for live patching


.. _`klp_object.definition`:

Definition
----------

.. code-block:: c

  struct klp_object {
    const char * name;
    struct klp_reloc * relocs;
    struct klp_func * funcs;
    struct kobject kobj;
    struct module * mod;
    enum klp_state state;
  };


.. _`klp_object.members`:

Members
-------

:``name``:
    module name (or NULL for vmlinux)

:``relocs``:
    relocation entries to be applied at load time

:``funcs``:
    function entries for functions to be patched in the object

:``kobj``:
    kobject for sysfs resources

:``mod``:
    kernel module associated with the patched object
    (NULL for vmlinux)

:``state``:
    tracks object-level patch application state




.. _`klp_patch`:

struct klp_patch
================

.. c:type:: klp_patch

    patch structure for live patching


.. _`klp_patch.definition`:

Definition
----------

.. code-block:: c

  struct klp_patch {
    struct module * mod;
    struct klp_object * objs;
    struct list_head list;
    struct kobject kobj;
    enum klp_state state;
  };


.. _`klp_patch.members`:

Members
-------

:``mod``:
    reference to the live patch module

:``objs``:
    object entries for kernel objects to be patched

:``list``:
    list node for global list of registered patches

:``kobj``:
    kobject for sysfs resources

:``state``:
    tracks patch-level application state


