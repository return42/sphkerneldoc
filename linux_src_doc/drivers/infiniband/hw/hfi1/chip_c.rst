.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/chip.c

.. _`wait_logical_linkstate`:

wait_logical_linkstate
======================

.. c:function:: int wait_logical_linkstate(struct hfi1_pportdata *ppd, u32 state, int msecs)

    wait for an IB link state change to occur

    :param struct hfi1_pportdata \*ppd:
        port device

    :param u32 state:
        the state to wait for

    :param int msecs:
        the number of milliseconds to wait

.. _`wait_logical_linkstate.description`:

Description
-----------

Wait up to msecs milliseconds for IB link state change to occur.
For now, take the easy polling route.
Returns 0 if state reached, otherwise -ETIMEDOUT.

.. _`init_qpmap_table`:

init_qpmap_table
================

.. c:function:: void init_qpmap_table(struct hfi1_devdata *dd, u32 first_ctxt, u32 last_ctxt)

    @dd - device data \ ``first_ctxt``\  - first context \ ``last_ctxt``\  - first context

    :param struct hfi1_devdata \*dd:
        *undescribed*

    :param u32 first_ctxt:
        *undescribed*

    :param u32 last_ctxt:
        *undescribed*

.. _`init_qpmap_table.description`:

Description
-----------

This return sets the qpn mapping table that
is indexed by qpn[8:1].

The routine will round robin the 256 settings
from first_ctxt to last_ctxt.

The first/last looks ahead to having specialized
receive contexts for mgmt and bypass.  Normal
verbs traffic will assumed to be on a range
of receive contexts.

.. _`init_qos`:

init_qos
========

.. c:function:: void init_qos(struct hfi1_devdata *dd, struct rsm_map_table *rmt)

    init RX qos \ ``dd``\  - device data \ ``rmt``\  - RSM map table

    :param struct hfi1_devdata \*dd:
        *undescribed*

    :param struct rsm_map_table \*rmt:
        *undescribed*

.. _`init_qos.description`:

Description
-----------

This routine initializes Rule 0 and the RSM map table to implement
quality of service (qos).

If all of the limit tests succeed, qos is applied based on the array
interpretation of krcvqs where entry 0 is VL0.

The number of vl bits (n) and the number of qpn bits (m) are computed to
feed both the RSM map table and the single rule.

.. _`hfi1_init_dd`:

hfi1_init_dd
============

.. c:function:: struct hfi1_devdata *hfi1_init_dd(struct pci_dev *pdev, const struct pci_device_id *ent)

    :param struct pci_dev \*pdev:
        *undescribed*

    :param const struct pci_device_id \*ent:
        pci_device_id struct for this dev

.. _`hfi1_init_dd.description`:

Description
-----------

Also allocates, initializes, and returns the devdata struct for this
device instance

This is global, and is called directly at init to set up the
chip-specific function pointers for later use.

.. _`create_pbc`:

create_pbc
==========

.. c:function:: u64 create_pbc(struct hfi1_pportdata *ppd, u64 flags, int srate_mbs, u32 vl, u32 dw_len)

    build a pbc for transmission

    :param struct hfi1_pportdata \*ppd:
        *undescribed*

    :param u64 flags:
        special case flags or-ed in built pbc

    :param int srate_mbs:
        *undescribed*

    :param u32 vl:
        vl

    :param u32 dw_len:
        *undescribed*

.. _`create_pbc.description`:

Description
-----------

Create a PBC with the given flags, rate, VL, and length.

.. _`create_pbc.note`:

NOTE
----

The PBC created will not insert any HCRC - all callers but one are
for verbs, which does not use this PSM feature.  The lone other caller
is for the diagnostic interface which calls this if the user does not
supply their own PBC.

.. This file was automatic generated / don't edit.

