.. -*- coding: utf-8; mode: rst -*-

.. _howto:

**********************
Howto use debugobjects
**********************

A kernel subsystem needs to provide a data structure which describes the
object type and add calls into the debug code at appropriate places. The
data structure to describe the object type needs at minimum the name of
the object type. Optional functions can and should be provided to fixup
detected problems so the kernel can continue to work and the debug
information can be retrieved from a live system instead of hard core
debugging with serial consoles and stack trace transcripts from the
monitor.

The debug calls provided by debugobjects are:

-  debug_object_init

-  debug_object_init_on_stack

-  debug_object_activate

-  debug_object_deactivate

-  debug_object_destroy

-  debug_object_free

-  debug_object_assert_init

Each of these functions takes the address of the real object and a
pointer to the object type specific debug description structure.

Each detected error is reported in the statistics and a limited number
of errors are printk'ed including a full stack trace.

The statistics are available via /sys/kernel/debug/debug_objects/stats.
They provide information about the number of warnings and the number of
successful fixups along with information about the usage of the internal
tracking objects and the state of the internal tracking objects pool.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
