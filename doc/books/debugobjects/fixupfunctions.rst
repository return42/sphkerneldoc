.. -*- coding: utf-8; mode: rst -*-

.. _fixupfunctions:

===============
Fixup functions
===============


.. _debug_obj_descr:

Debug object type description structure
=======================================


.. toctree::
    :maxdepth: 1

    API-struct-debug-obj
    API-struct-debug-obj-descr


.. _fixup_init:

fixup_init
==========

This function is called from the debug code whenever a problem in
debug_object_init is detected. The function takes the address of the
object and the state which is currently recorded in the tracker.

Called from debug_object_init when the object state is:

-  ODEBUG_STATE_ACTIVE

The function returns 1 when the fixup was successful, otherwise 0. The
return value is used to update the statistics.

Note, that the function needs to call the debug_object_init() function
again, after the damage has been repaired in order to keep the state
consistent.


.. _fixup_activate:

fixup_activate
==============

This function is called from the debug code whenever a problem in
debug_object_activate is detected.

Called from debug_object_activate when the object state is:

-  ODEBUG_STATE_NOTAVAILABLE

-  ODEBUG_STATE_ACTIVE

The function returns 1 when the fixup was successful, otherwise 0. The
return value is used to update the statistics.

Note that the function needs to call the debug_object_activate()
function again after the damage has been repaired in order to keep the
state consistent.

The activation of statically initialized objects is a special case. When
debug_object_activate() has no tracked object for this object address
then fixup_activate() is called with object state
ODEBUG_STATE_NOTAVAILABLE. The fixup function needs to check whether
this is a legitimate case of a statically initialized object or not. In
case it is it calls debug_object_init() and debug_object_activate()
to make the object known to the tracker and marked active. In this case
the function should return 0 because this is not a real fixup.


.. _fixup_destroy:

fixup_destroy
=============

This function is called from the debug code whenever a problem in
debug_object_destroy is detected.

Called from debug_object_destroy when the object state is:

-  ODEBUG_STATE_ACTIVE

The function returns 1 when the fixup was successful, otherwise 0. The
return value is used to update the statistics.


.. _fixup_free:

fixup_free
==========

This function is called from the debug code whenever a problem in
debug_object_free is detected. Further it can be called from the debug
checks in kfree/vfree, when an active object is detected from the
debug_check_no_obj_freed() sanity checks.

Called from debug_object_free() or debug_check_no_obj_freed() when
the object state is:

-  ODEBUG_STATE_ACTIVE

The function returns 1 when the fixup was successful, otherwise 0. The
return value is used to update the statistics.


.. _fixup_assert_init:

fixup_assert_init
=================

This function is called from the debug code whenever a problem in
debug_object_assert_init is detected.

Called from debug_object_assert_init() with a hardcoded state
ODEBUG_STATE_NOTAVAILABLE when the object is not found in the debug
bucket.

The function returns 1 when the fixup was successful, otherwise 0. The
return value is used to update the statistics.

Note, this function should make sure debug_object_init() is called
before returning.

The handling of statically initialized objects is a special case. The
fixup function should check if this is a legitimate case of a statically
initialized object or not. In this case only debug_object_init()
should be called to make the object known to the tracker. Then the
function should return 0 because this is not a real fixup.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
