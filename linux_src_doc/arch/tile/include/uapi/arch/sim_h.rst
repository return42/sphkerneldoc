.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/uapi/arch/sim.h

.. _`sim_is_simulator`:

sim_is_simulator
================

.. c:function:: int sim_is_simulator( void)

    rather than on real hardware.  If running on hardware, other "sim_xxx()" calls have no useful effect.

    :param  void:
        no arguments

.. _`sim_checkpoint`:

sim_checkpoint
==============

.. c:function:: void sim_checkpoint( void)

    :param  void:
        no arguments

.. _`sim_checkpoint.description`:

Description
-----------

The checkpoint file name is either the default or the name specified
on the command line with "--checkpoint-file".

.. _`sim_get_tracing`:

sim_get_tracing
===============

.. c:function:: unsigned int sim_get_tracing( void)

    :param  void:
        no arguments

.. _`sim_get_tracing.description`:

Description
-----------

SIM_TRACE_CYCLES (--trace-cycles),
SIM_TRACE_ROUTER (--trace-router),
SIM_TRACE_REGISTER_WRITES (--trace-register-writes),
SIM_TRACE_DISASM (--trace-disasm),
SIM_TRACE_STALL_INFO (--trace-stall-info)
SIM_TRACE_MEMORY_CONTROLLER (--trace-memory-controller)
SIM_TRACE_L2_CACHE (--trace-l2)
SIM_TRACE_LINES (--trace-lines)

.. _`sim_set_tracing`:

sim_set_tracing
===============

.. c:function:: void sim_set_tracing(unsigned int mask)

    :param unsigned int mask:
        *undescribed*

.. _`sim_set_tracing.description`:

Description
-----------

SIM_TRACE_NONE (turns off tracing),
SIM_TRACE_ALL (turns on all possible tracing).

.. _`sim_set_tracing.or-the-bitwise-or-of-these-values`:

or the bitwise OR of these values
---------------------------------


SIM_TRACE_CYCLES (--trace-cycles),
SIM_TRACE_ROUTER (--trace-router),
SIM_TRACE_REGISTER_WRITES (--trace-register-writes),
SIM_TRACE_DISASM (--trace-disasm),
SIM_TRACE_STALL_INFO (--trace-stall-info)
SIM_TRACE_MEMORY_CONTROLLER (--trace-memory-controller)
SIM_TRACE_L2_CACHE (--trace-l2)
SIM_TRACE_LINES (--trace-lines)

.. _`sim_dump`:

sim_dump
========

.. c:function:: void sim_dump(unsigned int mask)

    :param unsigned int mask:
        *undescribed*

.. _`sim_dump.description`:

Description
-----------

SIM_DUMP_ALL (dump all known state)

.. _`sim_dump.or-the-bitwise-or-of-these-values`:

or the bitwise OR of these values
---------------------------------


SIM_DUMP_REGS (the register file),
SIM_DUMP_SPRS (the SPRs),
SIM_DUMP_ITLB (the iTLB),
SIM_DUMP_DTLB (the dTLB),
SIM_DUMP_L1I (the L1 I-cache),
SIM_DUMP_L1D (the L1 D-cache),
SIM_DUMP_L2 (the L2 cache),
SIM_DUMP_SNREGS (the switch register file),
SIM_DUMP_SNITLB (the switch iTLB),
SIM_DUMP_SNL1I (the switch L1 I-cache),
SIM_DUMP_BACKTRACE (the current backtrace)

.. _`sim_print`:

sim_print
=========

.. c:function:: void sim_print(const char*str)

    :param const char\*str:
        *undescribed*

.. _`sim_print.description`:

Description
-----------

\ ``param``\  str The string to be written.

.. _`sim_print_string`:

sim_print_string
================

.. c:function:: void sim_print_string(const char*str)

    :param const char\*str:
        *undescribed*

.. _`sim_print_string.description`:

Description
-----------

\ ``param``\  str The string to be written (a newline is automatically added).

.. _`sim_command`:

sim_command
===========

.. c:function:: void sim_command(const char*str)

    :param const char\*str:
        *undescribed*

.. _`sim_command.description`:

Description
-----------

Type 'sim help' at the tile-monitor prompt to learn what commands
are available.  Note the use of the tile-monitor "sim" command to
pass commands to the simulator.

The argument to \ :c:func:`sim_command`\  does not include the leading "sim"
prefix used at the tile-monitor prompt; for example, you might call
sim_command("trace disasm").

.. _`_sim_syscall0`:

\_sim_syscall0
==============

.. c:function:: long _sim_syscall0(int val)

    :param int val:
        *undescribed*

.. _`_sim_syscall0.description`:

Description
-----------

We use extra "and" instructions to ensure that all the values
we are passing to the simulator are actually valid in the registers
(i.e. returned from memory) prior to the SIM_CONTROL spr.

.. _`_sim_syscall`:

\_sim_syscall
=============

.. c:function::  _sim_syscall( syscall_num,  nr,  args...)

    simulation. This is used as the implementation of other functions and should not be used outside this file.

    :param  syscall_num:
        *undescribed*

    :param  nr:
        *undescribed*

.. _`_sim_syscall.description`:

Description
-----------

\ ``param``\  syscall_num The simulator syscall number.
\ ``param``\  nr The number of additional arguments provided.

\ ``return``\  Varies by syscall.

.. _`sim_set_shaping`:

sim_set_shaping
===============

.. c:function:: int sim_set_shaping(unsigned shim, unsigned type, unsigned units, unsigned rate)

    :param unsigned shim:
        *undescribed*

    :param unsigned type:
        *undescribed*

    :param unsigned units:
        *undescribed*

    :param unsigned rate:
        *undescribed*

.. _`sim_set_shaping.description`:

Description
-----------

\ ``param``\  type The type of shaping. This should be the same type of
shaping that is already in place on the shim. One of:
SIM_CONTROL_SHAPING_MULTIPLIER
SIM_CONTROL_SHAPING_PPS
SIM_CONTROL_SHAPING_BPS

\ ``param``\  rate The rate to which to change it. This must fit in
SIM_CONTROL_SHAPING_RATE_BITS bits or a warning is issued and
the shaping is not changed.

\ ``return``\  0 if no problems were detected in the arguments to sim_set_shaping
or 1 if problems were detected (for example, rate does not fit in 17 bits).

.. _`sim_profiler_enable`:

sim_profiler_enable
===================

.. c:function:: void sim_profiler_enable( void)

    :param  void:
        no arguments

.. _`sim_profiler_enable.description`:

Description
-----------

Note that this has no effect if run in an environment without
profiling support (thus, the proper flags to the simulator must
be supplied).

.. _`sim_profiler_set_enabled`:

sim_profiler_set_enabled
========================

.. c:function:: void sim_profiler_set_enabled(int enabled)

    :param int enabled:
        *undescribed*

.. _`sim_profiler_set_enabled.description`:

Description
-----------

\ ``param``\  enabled If true, turns on profiling. If false, turns it off.

Note that this has no effect if run in an environment without
profiling support (thus, the proper flags to the simulator must
be supplied).

.. _`sim_profiler_is_enabled`:

sim_profiler_is_enabled
=======================

.. c:function:: int sim_profiler_is_enabled( void)

    for the current task.

    :param  void:
        no arguments

.. _`sim_profiler_is_enabled.description`:

Description
-----------

This returns false even if \ :c:func:`sim_profiler_enable`\  was called
if the current execution environment does not support profiling.

.. _`sim_profiler_clear`:

sim_profiler_clear
==================

.. c:function:: void sim_profiler_clear( void)

    :param  void:
        no arguments

.. _`sim_profiler_clear.description`:

Description
-----------

Resetting can be done while profiling is enabled.  It does not affect
the chip-wide profiling counters.

.. _`sim_profiler_chip_enable`:

sim_profiler_chip_enable
========================

.. c:function:: void sim_profiler_chip_enable(unsigned int mask)

    level profiling counters.

    :param unsigned int mask:
        *undescribed*

.. _`sim_profiler_chip_enable.description`:

Description
-----------

Does not affect the per-task profiling counters.

SIM_CHIP_ALL (enables all chip-level components).

.. _`sim_profiler_chip_enable.or-the-bitwise-or-of-these-values`:

or the bitwise OR of these values
---------------------------------


SIM_CHIP_MEMCTL (enable all memory controllers)
SIM_CHIP_XAUI (enable all XAUI controllers)
SIM_CHIP_MPIPE (enable all MPIPE controllers)

.. _`sim_profiler_chip_disable`:

sim_profiler_chip_disable
=========================

.. c:function:: void sim_profiler_chip_disable(unsigned int mask)

    level profiling counters.

    :param unsigned int mask:
        *undescribed*

.. _`sim_profiler_chip_disable.description`:

Description
-----------

Does not affect the per-task profiling counters.

SIM_CHIP_ALL (disables all chip-level components).

.. _`sim_profiler_chip_disable.or-the-bitwise-or-of-these-values`:

or the bitwise OR of these values
---------------------------------


SIM_CHIP_MEMCTL (disable all memory controllers)
SIM_CHIP_XAUI (disable all XAUI controllers)
SIM_CHIP_MPIPE (disable all MPIPE controllers)

.. _`sim_profiler_chip_clear`:

sim_profiler_chip_clear
=======================

.. c:function:: void sim_profiler_chip_clear(unsigned int mask)

    level profiling counters to zero.

    :param unsigned int mask:
        *undescribed*

.. _`sim_profiler_chip_clear.description`:

Description
-----------

Does not affect the per-task profiling counters.

SIM_CHIP_ALL (clears all chip-level components).

.. _`sim_profiler_chip_clear.or-the-bitwise-or-of-these-values`:

or the bitwise OR of these values
---------------------------------


SIM_CHIP_MEMCTL (clear all memory controllers)
SIM_CHIP_XAUI (clear all XAUI controllers)
SIM_CHIP_MPIPE (clear all MPIPE controllers)

.. This file was automatic generated / don't edit.

