.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/chip.c

.. _`hfi1_addr_from_offset`:

hfi1_addr_from_offset
=====================

.. c:function:: void __iomem *hfi1_addr_from_offset(const struct hfi1_devdata *dd, u32 offset)

    return addr for readq/writeq \ ``dd``\  - the dd device \ ``offset``\  - the offset of the CSR within bar0

    :param const struct hfi1_devdata \*dd:
        *undescribed*

    :param u32 offset:
        *undescribed*

.. _`hfi1_addr_from_offset.description`:

Description
-----------

This routine selects the appropriate base address
based on the indicated offset.

.. _`read_csr`:

read_csr
========

.. c:function:: u64 read_csr(const struct hfi1_devdata *dd, u32 offset)

    read CSR at the indicated offset \ ``dd``\  - the dd device \ ``offset``\  - the offset of the CSR within bar0

    :param const struct hfi1_devdata \*dd:
        *undescribed*

    :param u32 offset:
        *undescribed*

.. _`read_csr.return`:

Return
------

the value read or all FF's if there
is no mapping

.. _`write_csr`:

write_csr
=========

.. c:function:: void write_csr(const struct hfi1_devdata *dd, u32 offset, u64 value)

    write CSR at the indicated offset \ ``dd``\  - the dd device \ ``offset``\  - the offset of the CSR within bar0 \ ``value``\  - value to write

    :param const struct hfi1_devdata \*dd:
        *undescribed*

    :param u32 offset:
        *undescribed*

    :param u64 value:
        *undescribed*

.. _`get_csr_addr`:

get_csr_addr
============

.. c:function:: void __iomem *get_csr_addr(const struct hfi1_devdata *dd, u32 offset)

    return te iomem address for offset \ ``dd``\  - the dd device \ ``offset``\  - the offset of the CSR within bar0

    :param const struct hfi1_devdata \*dd:
        *undescribed*

    :param u32 offset:
        *undescribed*

.. _`get_csr_addr.return`:

Return
------

The iomem address to use in subsequent
writeq/readq operations.

.. _`update_xmit_counters`:

update_xmit_counters
====================

.. c:function:: void update_xmit_counters(struct hfi1_pportdata *ppd, u16 link_width)

    update PortXmitWait/PortVlXmitWait counters.

    :param struct hfi1_pportdata \*ppd:
        info of physical Hfi port

    :param u16 link_width:
        new link width after link up or downgrade

.. _`update_xmit_counters.description`:

Description
-----------

Update the PortXmitWait and PortVlXmitWait counters after
a link up or downgrade event to reflect a link width change.

.. _`apply_link_downgrade_policy`:

apply_link_downgrade_policy
===========================

.. c:function:: bool apply_link_downgrade_policy(struct hfi1_pportdata *ppd, bool refresh_widths)

    Apply the link width downgrade enabled policy against the current active link widths.

    :param struct hfi1_pportdata \*ppd:
        info of physical Hfi port

    :param bool refresh_widths:
        True indicates link downgrade event

.. _`apply_link_downgrade_policy.description`:

Description
-----------

Called when the enabled policy changes or the active link widths
change.
Refresh_widths indicates that a link downgrade occurred. The
link_downgraded variable is set by refresh_widths and
determines the success/failure of the policy application.

.. _`update_statusp`:

update_statusp
==============

.. c:function:: void update_statusp(struct hfi1_pportdata *ppd, u32 state)

    Update userspace status flag

    :param struct hfi1_pportdata \*ppd:
        Port data structure

    :param u32 state:
        port state information

.. _`update_statusp.description`:

Description
-----------

Actual port status is determined by the host_link_state value
in the ppd.

host_link_state MUST be updated before updating the user space
statusp.

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

.. _`get_int_mask`:

get_int_mask
============

.. c:function:: u64 get_int_mask(struct hfi1_devdata *dd, u32 i)

    get 64 bit int mask \ ``dd``\  - the devdata \ ``i``\  - the csr (relative to CCE_INT_MASK)

    :param struct hfi1_devdata \*dd:
        *undescribed*

    :param u32 i:
        *undescribed*

.. _`get_int_mask.description`:

Description
-----------

Returns the mask with the urgent interrupt mask
bit clear for kernel receive contexts.

.. _`hfi1_clean_up_interrupts`:

hfi1_clean_up_interrupts
========================

.. c:function:: void hfi1_clean_up_interrupts(struct hfi1_devdata *dd)

    Free all IRQ resources

    :param struct hfi1_devdata \*dd:
        valid device data data structure

.. _`hfi1_clean_up_interrupts.description`:

Description
-----------

Free the MSI or INTx IRQs and assoicated PCI resources,
if they have been allocated.

.. _`init_qpmap_table`:

init_qpmap_table
================

.. c:function:: void init_qpmap_table(struct hfi1_devdata *dd, u32 first_ctxt, u32 last_ctxt)

    \ ``dd``\  - device data \ ``first_ctxt``\  - first context \ ``last_ctxt``\  - first context

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

