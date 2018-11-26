.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kvm/book3s_hv_builtin.c

.. _`kvm_cma_reserve`:

kvm_cma_reserve
===============

.. c:function:: void kvm_cma_reserve( void)

    reserve area for kvm hash pagetable

    :param void:
        no arguments
    :type void: 

.. _`kvm_cma_reserve.description`:

Description
-----------

This function reserves memory from early allocator. It should be
called by arch specific code once the memblock allocator
has been activated and all other subsystems have already allocated/reserved
memory.

.. This file was automatic generated / don't edit.

