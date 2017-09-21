.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/intel_rdt_sched.h

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
        u32 cur_rmid;
        u32 cur_closid;
        u32 default_rmid;
        u32 default_closid;
    }

.. _`intel_pqr_state.members`:

Members
-------

cur_rmid
    The cached Resource Monitoring ID

cur_closid
    The cached Class Of Service ID

default_rmid
    The user assigned Resource Monitoring ID

default_closid
    The user assigned cached Class Of Service ID

.. _`intel_pqr_state.description`:

Description
-----------

The upper 32 bits of IA32_PQR_ASSOC contain closid and the
lower 10 bits rmid. The update to IA32_PQR_ASSOC always
contains both parts, so we need to cache them. This also
stores the user configured per cpu CLOSID and RMID.

The cache also helps to avoid pointless updates if the value does
not change.

.. This file was automatic generated / don't edit.

