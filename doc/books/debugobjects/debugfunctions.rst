.. -*- coding: utf-8; mode: rst -*-

.. _debugfunctions:

***************
Debug functions
***************


.. _prototypes:

Debug object function reference
===============================


.. kernel-doc:: lib/debugobjects.c
    :export:

.. _debug_object_init:

debug_object_init
=================

This function is called whenever the initialization function of a real
object is called.

When the real object is already tracked by debugobjects it is checked,
whether the object can be initialized. Initializing is not allowed for
active and destroyed objects. When debugobjects detects an error, then
it calls the fixup_init function of the object type description
structure if provided by the caller. The fixup function can correct the
problem before the real initialization of the object happens. E.g. it
can deactivate an active object in order to prevent damage to the
subsystem.

When the real object is not yet tracked by debugobjects, debugobjects
allocates a tracker object for the real object and sets the tracker
object state to ODEBUG_STATE_INIT. It verifies that the object is not
on the callers stack. If it is on the callers stack then a limited
number of warnings including a full stack trace is printk'ed. The
calling code must use debug_object_init_on_stack() and remove the
object before leaving the function which allocated it. See next section.


.. _debug_object_init_on_stack:

debug_object_init_on_stack
==========================

This function is called whenever the initialization function of a real
object which resides on the stack is called.

When the real object is already tracked by debugobjects it is checked,
whether the object can be initialized. Initializing is not allowed for
active and destroyed objects. When debugobjects detects an error, then
it calls the fixup_init function of the object type description
structure if provided by the caller. The fixup function can correct the
problem before the real initialization of the object happens. E.g. it
can deactivate an active object in order to prevent damage to the
subsystem.

When the real object is not yet tracked by debugobjects debugobjects
allocates a tracker object for the real object and sets the tracker
object state to ODEBUG_STATE_INIT. It verifies that the object is on
the callers stack.

An object which is on the stack must be removed from the tracker by
calling debug_object_free() before the function which allocates the
object returns. Otherwise we keep track of stale objects.


.. _debug_object_activate:

debug_object_activate
=====================

This function is called whenever the activation function of a real
object is called.

When the real object is already tracked by debugobjects it is checked,
whether the object can be activated. Activating is not allowed for
active and destroyed objects. When debugobjects detects an error, then
it calls the fixup_activate function of the object type description
structure if provided by the caller. The fixup function can correct the
problem before the real activation of the object happens. E.g. it can
deactivate an active object in order to prevent damage to the subsystem.

When the real object is not yet tracked by debugobjects then the
fixup_activate function is called if available. This is necessary to
allow the legitimate activation of statically allocated and initialized
objects. The fixup function checks whether the object is valid and calls
the debug_objects_init() function to initialize the tracking of this
object.

When the activation is legitimate, then the state of the associated
tracker object is set to ODEBUG_STATE_ACTIVE.


.. _debug_object_deactivate:

debug_object_deactivate
=======================

This function is called whenever the deactivation function of a real
object is called.

When the real object is tracked by debugobjects it is checked, whether
the object can be deactivated. Deactivating is not allowed for untracked
or destroyed objects.

When the deactivation is legitimate, then the state of the associated
tracker object is set to ODEBUG_STATE_INACTIVE.


.. _debug_object_destroy:

debug_object_destroy
====================

This function is called to mark an object destroyed. This is useful to
prevent the usage of invalid objects, which are still available in
memory: either statically allocated objects or objects which are freed
later.

When the real object is tracked by debugobjects it is checked, whether
the object can be destroyed. Destruction is not allowed for active and
destroyed objects. When debugobjects detects an error, then it calls the
fixup_destroy function of the object type description structure if
provided by the caller. The fixup function can correct the problem
before the real destruction of the object happens. E.g. it can
deactivate an active object in order to prevent damage to the subsystem.

When the destruction is legitimate, then the state of the associated
tracker object is set to ODEBUG_STATE_DESTROYED.


.. _debug_object_free:

debug_object_free
=================

This function is called before an object is freed.

When the real object is tracked by debugobjects it is checked, whether
the object can be freed. Free is not allowed for active objects. When
debugobjects detects an error, then it calls the fixup_free function of
the object type description structure if provided by the caller. The
fixup function can correct the problem before the real free of the
object happens. E.g. it can deactivate an active object in order to
prevent damage to the subsystem.

Note that debug_object_free removes the object from the tracker. Later
usage of the object is detected by the other debug checks.


.. _debug_object_assert_init:

debug_object_assert_init
========================

This function is called to assert that an object has been initialized.

When the real object is not tracked by debugobjects, it calls
fixup_assert_init of the object type description structure provided by
the caller, with the hardcoded object state ODEBUG_NOT_AVAILABLE. The
fixup function can correct the problem by calling debug_object_init
and other specific initializing functions.

When the real object is already tracked by debugobjects it is ignored.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
