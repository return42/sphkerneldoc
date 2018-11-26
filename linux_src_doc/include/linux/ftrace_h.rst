.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ftrace.h

.. _`stack_tracer_disable`:

stack_tracer_disable
====================

.. c:function:: void stack_tracer_disable( void)

    temporarily disable the stack tracer

    :param void:
        no arguments
    :type void: 

.. _`stack_tracer_disable.description`:

Description
-----------

There's a few locations (namely in RCU) where stack tracing
cannot be executed. This function is used to disable stack
tracing during those critical sections.

This function must be called with preemption or interrupts
disabled and \ :c:func:`stack_tracer_enable`\  must be called shortly after
while preemption or interrupts are still disabled.

.. _`stack_tracer_enable`:

stack_tracer_enable
===================

.. c:function:: void stack_tracer_enable( void)

    re-enable the stack tracer

    :param void:
        no arguments
    :type void: 

.. _`stack_tracer_enable.description`:

Description
-----------

After \ :c:func:`stack_tracer_disable`\  is called, \ :c:func:`stack_tracer_enable`\ 
must be called shortly afterward.

.. _`ftrace_make_nop`:

ftrace_make_nop
===============

.. c:function:: int ftrace_make_nop(struct module *mod, struct dyn_ftrace *rec, unsigned long addr)

    convert code into nop

    :param mod:
        module structure if called by module load initialization
    :type mod: struct module \*

    :param rec:
        the mcount call site record
    :type rec: struct dyn_ftrace \*

    :param addr:
        the address that the call site should be calling
    :type addr: unsigned long

.. _`ftrace_make_nop.description`:

Description
-----------

This is a very sensitive operation and great care needs
to be taken by the arch.  The operation should carefully
read the location, check to see if what is read is indeed
what we expect it to be, and then on success of the compare,
it should write to the location.

The code segment at \ ``rec->ip``\  should be a caller to \ ``addr``\ 

.. _`ftrace_make_nop.return-must-be`:

Return must be
--------------

0 on success
-EFAULT on error reading the location
-EINVAL on a failed compare of the contents
-EPERM  on error writing to the location
Any other value will be considered a failure.

.. _`ftrace_make_call`:

ftrace_make_call
================

.. c:function:: int ftrace_make_call(struct dyn_ftrace *rec, unsigned long addr)

    convert a nop call site into a call to addr

    :param rec:
        the mcount call site record
    :type rec: struct dyn_ftrace \*

    :param addr:
        the address that the call site should call
    :type addr: unsigned long

.. _`ftrace_make_call.description`:

Description
-----------

This is a very sensitive operation and great care needs
to be taken by the arch.  The operation should carefully
read the location, check to see if what is read is indeed
what we expect it to be, and then on success of the compare,
it should write to the location.

The code segment at \ ``rec->ip``\  should be a nop

.. _`ftrace_make_call.return-must-be`:

Return must be
--------------

0 on success
-EFAULT on error reading the location
-EINVAL on a failed compare of the contents
-EPERM  on error writing to the location
Any other value will be considered a failure.

.. _`ftrace_modify_call`:

ftrace_modify_call
==================

.. c:function:: int ftrace_modify_call(struct dyn_ftrace *rec, unsigned long old_addr, unsigned long addr)

    convert from one addr to another (no nop)

    :param rec:
        the mcount call site record
    :type rec: struct dyn_ftrace \*

    :param old_addr:
        the address expected to be currently called to
    :type old_addr: unsigned long

    :param addr:
        the address to change to
    :type addr: unsigned long

.. _`ftrace_modify_call.description`:

Description
-----------

This is a very sensitive operation and great care needs
to be taken by the arch.  The operation should carefully
read the location, check to see if what is read is indeed
what we expect it to be, and then on success of the compare,
it should write to the location.

The code segment at \ ``rec->ip``\  should be a caller to \ ``old_addr``\ 

.. _`ftrace_modify_call.return-must-be`:

Return must be
--------------

0 on success
-EFAULT on error reading the location
-EINVAL on a failed compare of the contents
-EPERM  on error writing to the location
Any other value will be considered a failure.

.. This file was automatic generated / don't edit.

