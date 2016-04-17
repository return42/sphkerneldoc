.. -*- coding: utf-8; mode: rst -*-

=====
msi.h
=====


.. _`msi_alloc_info`:

struct msi_alloc_info
=====================

.. c:type:: msi_alloc_info

    Default structure for MSI interrupt allocation.


.. _`msi_alloc_info.definition`:

Definition
----------

.. code-block:: c

  struct msi_alloc_info {
    struct msi_desc * desc;
    irq_hw_number_t hwirq;
    union scratchpad[NUM_MSI_ALLOC_SCRATCHPAD_REGS];
  };


.. _`msi_alloc_info.members`:

Members
-------

:``desc``:
    Pointer to msi descriptor

:``hwirq``:
    Associated hw interrupt number in the domain

:``scratchpad[NUM_MSI_ALLOC_SCRATCHPAD_REGS]``:
    Storage for implementation specific scratch data




.. _`msi_alloc_info.description`:

Description
-----------

Architectures can provide their own implementation by not including
asm-generic/msi.h into their arch specific header file.

