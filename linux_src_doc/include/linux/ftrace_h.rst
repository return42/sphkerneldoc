.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ftrace.h

.. _`ftrace_function_local_enable`:

ftrace_function_local_enable
============================

.. c:function:: void ftrace_function_local_enable(struct ftrace_ops *ops)

    enable ftrace_ops on current cpu

    :param struct ftrace_ops \*ops:
        *undescribed*

.. _`ftrace_function_local_enable.description`:

Description
-----------

This function enables tracing on current cpu by decreasing
the per cpu control variable.
It must be called with preemption disabled and only on ftrace_ops
registered with FTRACE_OPS_FL_PER_CPU. If called without preemption
disabled, this_cpu_ptr will complain when CONFIG_DEBUG_PREEMPT is enabled.

.. _`ftrace_function_local_disable`:

ftrace_function_local_disable
=============================

.. c:function:: void ftrace_function_local_disable(struct ftrace_ops *ops)

    disable ftrace_ops on current cpu

    :param struct ftrace_ops \*ops:
        *undescribed*

.. _`ftrace_function_local_disable.description`:

Description
-----------

This function disables tracing on current cpu by increasing
the per cpu control variable.
It must be called with preemption disabled and only on ftrace_ops
registered with FTRACE_OPS_FL_PER_CPU. If called without preemption
disabled, this_cpu_ptr will complain when CONFIG_DEBUG_PREEMPT is enabled.

.. _`ftrace_function_local_disabled`:

ftrace_function_local_disabled
==============================

.. c:function:: int ftrace_function_local_disabled(struct ftrace_ops *ops)

    returns ftrace_ops disabled value on current cpu

    :param struct ftrace_ops \*ops:
        *undescribed*

.. _`ftrace_function_local_disabled.description`:

Description
-----------

This function returns value of ftrace_ops::disabled on current cpu.
It must be called with preemption disabled and only on ftrace_ops
registered with FTRACE_OPS_FL_PER_CPU. If called without preemption
disabled, this_cpu_ptr will complain when CONFIG_DEBUG_PREEMPT is enabled.

.. _`ftrace_make_nop`:

ftrace_make_nop
===============

.. c:function:: int ftrace_make_nop(struct module *mod, struct dyn_ftrace *rec, unsigned long addr)

    convert code into nop

    :param struct module \*mod:
        module structure if called by module load initialization

    :param struct dyn_ftrace \*rec:
        the mcount call site record

    :param unsigned long addr:
        the address that the call site should be calling

.. _`ftrace_make_nop.description`:

Description
-----------

This is a very sensitive operation and great care needs
to be taken by the arch.  The operation should carefully
read the location, check to see if what is read is indeed
what we expect it to be, and then on success of the compare,
it should write to the location.

The code segment at \ ``rec``\ ->ip should be a caller to \ ``addr``\ 

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

    :param struct dyn_ftrace \*rec:
        the mcount call site record

    :param unsigned long addr:
        the address that the call site should call

.. _`ftrace_make_call.description`:

Description
-----------

This is a very sensitive operation and great care needs
to be taken by the arch.  The operation should carefully
read the location, check to see if what is read is indeed
what we expect it to be, and then on success of the compare,
it should write to the location.

The code segment at \ ``rec``\ ->ip should be a nop

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

    :param struct dyn_ftrace \*rec:
        the mcount call site record

    :param unsigned long old_addr:
        the address expected to be currently called to

    :param unsigned long addr:
        the address to change to

.. _`ftrace_modify_call.description`:

Description
-----------

This is a very sensitive operation and great care needs
to be taken by the arch.  The operation should carefully
read the location, check to see if what is read is indeed
what we expect it to be, and then on success of the compare,
it should write to the location.

The code segment at \ ``rec``\ ->ip should be a caller to \ ``old_addr``\ 

.. _`ftrace_modify_call.return-must-be`:

Return must be
--------------

0 on success
-EFAULT on error reading the location
-EINVAL on a failed compare of the contents
-EPERM  on error writing to the location
Any other value will be considered a failure.

.. This file was automatic generated / don't edit.

