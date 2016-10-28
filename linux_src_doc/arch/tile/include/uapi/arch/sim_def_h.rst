.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/uapi/arch/sim_def.h

.. _`_sim_control_operator_bits`:

_SIM_CONTROL_OPERATOR_BITS
==========================

.. c:function::  _SIM_CONTROL_OPERATOR_BITS()

    the low bits of the SIM_CONTROL\_\* SPR values specify the operation to perform, and the remaining bits are an operation-specific parameter (often unused).

.. _`sim_control_set_tracing`:

SIM_CONTROL_SET_TRACING
=======================

.. c:function::  SIM_CONTROL_SET_TRACING()

    sets the tracing mask to the given mask. See "\ :c:func:`sim_set_tracing`\ ".

.. _`sim_control_dump`:

SIM_CONTROL_DUMP
================

.. c:function::  SIM_CONTROL_DUMP()

    dumps the requested items of machine state to the log.

.. _`sim_control_enable_functional_barrier`:

SIM_CONTROL_ENABLE_FUNCTIONAL_BARRIER
=====================================

.. c:function::  SIM_CONTROL_ENABLE_FUNCTIONAL_BARRIER()

    level functional mode. All tiles must perform this write for functional mode to be enabled. Ignored in naked boot mode unless --functional is specified.

.. _`sim_control_enable_functional_barrier.warning`:

WARNING
-------

Only the hypervisor startup code should use this!

.. _`sim_control_putc`:

SIM_CONTROL_PUTC
================

.. c:function::  SIM_CONTROL_PUTC()

    writes a string directly to the simulator output.  Written to once for each character in the string, plus a final NUL.  Instead of NUL, you can also use "SIM_PUTC_FLUSH_STRING" or "SIM_PUTC_FLUSH_BINARY".

.. _`sim_control_grinder_clear`:

SIM_CONTROL_GRINDER_CLEAR
=========================

.. c:function::  SIM_CONTROL_GRINDER_CLEAR()

    -grind-coherence state for this core.  This is intended to be used before a loop that will invalidate the cache by loading new data and evicting all current data. Generally speaking, this API should only be used by system code.

.. _`sim_control_os_fork`:

SIM_CONTROL_OS_FORK
===================

.. c:function::  SIM_CONTROL_OS_FORK()

    indicates that a fork syscall just created the given process.

.. _`sim_control_os_exit`:

SIM_CONTROL_OS_EXIT
===================

.. c:function::  SIM_CONTROL_OS_EXIT()

    indicates that an exit syscall was just executed by the given process.

.. _`sim_control_os_switch`:

SIM_CONTROL_OS_SWITCH
=====================

.. c:function::  SIM_CONTROL_OS_SWITCH()

    indicates that the OS just switched to the given process.

.. _`sim_control_os_exec`:

SIM_CONTROL_OS_EXEC
===================

.. c:function::  SIM_CONTROL_OS_EXEC()

    indicates that an exec syscall was just executed. Written to once for each character in the executable name, plus a final NUL.

.. _`sim_control_os_interp`:

SIM_CONTROL_OS_INTERP
=====================

.. c:function::  SIM_CONTROL_OS_INTERP()

    indicates that an interpreter (PT_INTERP) was loaded.  Written to once for each character in "ADDR:PATH", plus a final NUL, where "ADDR" is a hex load address starting with "0x", and "PATH" is the executable name.

.. _`sim_control_dlopen`:

SIM_CONTROL_DLOPEN
==================

.. c:function::  SIM_CONTROL_DLOPEN()

    indicates that a dll was loaded.  Written to once for each character in "ADDR:PATH", plus a final NUL, where "ADDR" is a hexadecimal load address starting with "0x", and "PATH" is the executable name.

.. _`sim_control_dlclose`:

SIM_CONTROL_DLCLOSE
===================

.. c:function::  SIM_CONTROL_DLCLOSE()

    indicates that a dll was unloaded.  Written to once for each character in "ADDR", plus a final NUL, where "ADDR" is a hexadecimal load address starting with "0x".

.. _`sim_control_allow_multiple_caching`:

SIM_CONTROL_ALLOW_MULTIPLE_CACHING
==================================

.. c:function::  SIM_CONTROL_ALLOW_MULTIPLE_CACHING()

    indicates whether to allow data reads to remotely-cached dirty cache lines to be cached locally without grinder warnings or assertions (used by Linux kernel fast memcpy).

.. _`sim_control_shaping`:

SIM_CONTROL_SHAPING
===================

.. c:function::  SIM_CONTROL_SHAPING()

    the gbe or xgbe shims. Must specify the shim id, the type, the units, and the rate, as defined in SIM_SHAPING_SPR_ARG.

.. _`sim_control_command`:

SIM_CONTROL_COMMAND
===================

.. c:function::  SIM_CONTROL_COMMAND()

    requests that a simulator command be executed.  Written to once for each character in the command, plus a final NUL.

.. _`sim_control_panic`:

SIM_CONTROL_PANIC
=================

.. c:function::  SIM_CONTROL_PANIC()

    is panicking, to allow debugging via --debug-on-panic.

.. _`sim_control_syscall`:

SIM_CONTROL_SYSCALL
===================

.. c:function::  SIM_CONTROL_SYSCALL()

    See "\ :c:func:`sim_syscall`\ " for more info.

.. _`sim_control_os_fork_parent`:

SIM_CONTROL_OS_FORK_PARENT
==========================

.. c:function::  SIM_CONTROL_OS_FORK_PARENT()

    provides the pid that subsequent SIM_CONTROL_OS_FORK writes should use as the pid, rather than the default previous SIM_CONTROL_OS_SWITCH.

.. _`sim_control_clear_mpipe_magic_bytes`:

SIM_CONTROL_CLEAR_MPIPE_MAGIC_BYTES
===================================

.. c:function::  SIM_CONTROL_CLEAR_MPIPE_MAGIC_BYTES()

    (shifted by 8), clears the pending magic data section.  The cleared pending magic data section and any subsequently appended magic bytes will only take effect when the classifier blast programmer is run.

.. _`sim_control_append_mpipe_magic_byte`:

SIM_CONTROL_APPEND_MPIPE_MAGIC_BYTE
===================================

.. c:function::  SIM_CONTROL_APPEND_MPIPE_MAGIC_BYTE()

    (shifted by 8) and a byte of data (shifted by 16), appends that byte to the shim's pending magic data section.  The pending magic data section takes effect when the classifier blast programmer is run.

.. _`sim_control_enable_mpipe_link_magic_byte`:

SIM_CONTROL_ENABLE_MPIPE_LINK_MAGIC_BYTE
========================================

.. c:function::  SIM_CONTROL_ENABLE_MPIPE_LINK_MAGIC_BYTE()

    (shifted by 8), an enable=1/disable=0 bit (shifted by 16), and a mask of links (shifted by 32), enable or disable the corresponding mPIPE links.

.. _`sim_syscall_validate_lines_evicted`:

SIM_SYSCALL_VALIDATE_LINES_EVICTED
==================================

.. c:function::  SIM_SYSCALL_VALIDATE_LINES_EVICTED()

    bit PA is passed as the second argument to \ :c:func:`sim_syscall`\ , and over a range passed as the third argument, are no longer in cache. The simulator raises an error if this is not the case.

.. _`sim_trace_flag_mask`:

SIM_TRACE_FLAG_MASK
===================

.. c:function::  SIM_TRACE_FLAG_MASK()

    (SIM_TRACE_xxx values).

.. _`sim_putc_flush_string`:

SIM_PUTC_FLUSH_STRING
=====================

.. c:function::  SIM_PUTC_FLUSH_STRING()

    flush, including coordinate/cycle prefix and newline.

.. _`sim_putc_flush_binary`:

SIM_PUTC_FLUSH_BINARY
=====================

.. c:function::  SIM_PUTC_FLUSH_BINARY()

    data-flush, which skips the prefix and does not append a newline.

.. This file was automatic generated / don't edit.

