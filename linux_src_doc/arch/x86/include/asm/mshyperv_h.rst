.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/mshyperv.h

.. _`hv_cpu_number_to_vp_number`:

hv_cpu_number_to_vp_number
==========================

.. c:function:: int hv_cpu_number_to_vp_number(int cpu_number)

    Map CPU to VP.

    :param int cpu_number:
        CPU number in Linux terms

.. _`hv_cpu_number_to_vp_number.description`:

Description
-----------

This function returns the mapping between the Linux processor
number and the hypervisor's virtual processor number, useful
in making hypercalls and such that talk about specific
processors.

.. _`hv_cpu_number_to_vp_number.return`:

Return
------

Virtual processor number in Hyper-V terms

.. This file was automatic generated / don't edit.

