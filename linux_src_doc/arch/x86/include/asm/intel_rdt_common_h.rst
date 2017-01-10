.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/intel_rdt_common.h

.. _`intel_pqr_state`:

struct intel_pqr_state
======================

.. c:type:: struct intel_pqr_state

    State cache for the PQR MSR

.. _`intel_pqr_state.definition`:

Definition
----------

.. code-block:: c

    struct intel_pqr_state {
        u32 rmid;
        u32 closid;
        int rmid_usecnt;
    }

.. _`intel_pqr_state.members`:

Members
-------

rmid
    The cached Resource Monitoring ID

closid
    The cached Class Of Service ID

rmid_usecnt
    The usage counter for rmid

.. _`intel_pqr_state.description`:

Description
-----------

The upper 32 bits of MSR_IA32_PQR_ASSOC contain closid and the
lower 10 bits rmid. The update to MSR_IA32_PQR_ASSOC always
contains both parts, so we need to cache them.

The cache also helps to avoid pointless updates if the value does
not change.

.. This file was automatic generated / don't edit.

