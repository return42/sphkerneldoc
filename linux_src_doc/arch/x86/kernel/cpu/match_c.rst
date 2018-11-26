.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/match.c

.. _`x86_match_cpu`:

x86_match_cpu
=============

.. c:function:: const struct x86_cpu_id *x86_match_cpu(const struct x86_cpu_id *match)

    match current CPU again an array of x86_cpu_ids

    :param match:
        Pointer to array of x86_cpu_ids. Last entry terminated with
        {}.
    :type match: const struct x86_cpu_id \*

.. _`x86_match_cpu.description`:

Description
-----------

Return the entry if the current CPU matches the entries in the
passed x86_cpu_id match table. Otherwise NULL.  The match table
contains vendor (X86_VENDOR\_\*), family, model and feature bits or
respective wildcard entries.

A typical table entry would be to match a specific CPU
{ X86_VENDOR_INTEL, 6, 0x12 }
or to match a specific CPU feature
{ X86_FEATURE_MATCH(X86_FEATURE_FOOBAR) }

Fields can be wildcarded with \ ``X86_VENDOR_ANY``\ , \ ``X86_FAMILY_ANY``\ ,
\ ``X86_MODEL_ANY``\ , \ ``X86_FEATURE_ANY``\  or 0 (except for vendor)

Arrays used to match for this should also be declared using
MODULE_DEVICE_TABLE(x86cpu, ...)

This always matches against the boot cpu, assuming models and features are
consistent over all CPUs.

.. This file was automatic generated / don't edit.

