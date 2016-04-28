.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-debug-obj-descr:

======================
struct debug_obj_descr
======================

*man struct debug_obj_descr(9)*

*4.6.0-rc5*

object type specific debug description structure


Synopsis
========

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
=======

name
    name of the object typee

debug_hint
    function returning address, which have associated kernel symbol, to
    allow identify the object

fixup_init
    fixup function, which is called when the init check fails

fixup_activate
    fixup function, which is called when the activate check fails

fixup_destroy
    fixup function, which is called when the destroy check fails

fixup_free
    fixup function, which is called when the free check fails

fixup_assert_init
    fixup function, which is called when the assert_init check fails


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
