.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/arch/x86/tests/insn-x86.c

.. _`test__insn_x86`:

test__insn_x86
==============

.. c:function:: int test__insn_x86(int subtest __maybe_unused, int subtest __maybe_unused)

    test x86 instruction decoder - new instructions.

    :param int subtest __maybe_unused:
        *undescribed*

    :param int subtest __maybe_unused:
        *undescribed*

.. _`test__insn_x86.description`:

Description
-----------

This function implements a test that decodes a selection of instructions and
checks the results.  The Intel PT function that further categorizes
instructions (i.e. \ :c:func:`intel_pt_get_insn`\ ) is also checked.

The instructions are originally in insn-x86-dat-src.c which has been
processed by scripts gen-insn-x86-dat.sh and gen-insn-x86-dat.awk to produce
insn-x86-dat-32.c and insn-x86-dat-64.c which are included into this program.
i.e. to add new instructions to the test, edit insn-x86-dat-src.c, run the
gen-insn-x86-dat.sh script, make perf, and then run the test.

If the test passes \ ``0``\  is returned, otherwise \ ``-1``\  is returned.  Use the
verbose (-v) option to see all the instructions and whether or not they
decoded successfuly.

.. This file was automatic generated / don't edit.

