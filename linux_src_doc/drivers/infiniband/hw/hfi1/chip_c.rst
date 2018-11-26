.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/chip.c

.. _`hfi1_addr_from_offset`:

hfi1_addr_from_offset
=====================

.. c:function:: void __iomem *hfi1_addr_from_offset(const struct hfi1_devdata *dd, u32 offset)

    return addr for readq/writeq \ ``dd``\  - the dd device \ ``offset``\  - the offset of the CSR within bar0

    :param dd:
        *undescribed*
    :type dd: const struct hfi1_devdata \*

    :param offset:
        *undescribed*
    :type offset: u32

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

    :param dd:
        *undescribed*
    :type dd: const struct hfi1_devdata \*

    :param offset:
        *undescribed*
    :type offset: u32

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

    :param dd:
        *undescribed*
    :type dd: const struct hfi1_devdata \*

    :param offset:
        *undescribed*
    :type offset: u32

    :param value:
        *undescribed*
    :type value: u64

.. _`get_csr_addr`:

get_csr_addr
============

.. c:function:: void __iomem *get_csr_addr(const struct hfi1_devdata *dd, u32 offset)

    return te iomem address for offset \ ``dd``\  - the dd device \ ``offset``\  - the offset of the CSR within bar0

    :param dd:
        *undescribed*
    :type dd: const struct hfi1_devdata \*

    :param offset:
        *undescribed*
    :type offset: u32

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

    :param ppd:
        info of physical Hfi port
    :type ppd: struct hfi1_pportdata \*

    :param link_width:
        new link width after link up or downgrade
    :type link_width: u16

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

    :param ppd:
        info of physical Hfi port
    :type ppd: struct hfi1_pportdata \*

    :param refresh_widths:
        True indicates link downgrade event
    :type refresh_widths: bool

.. _`apply_link_downgrade_policy.description`:

Description
-----------

Called when the enabled policy changes or the active link widths
change.
Refresh_widths indicates that a link downgrade occurred. The
link_downgraded variable is set by refresh_widths and
determines the success/failure of the policy application.

.. _`is_rcv_avail_int`:

is_rcv_avail_int
================

.. c:function:: void is_rcv_avail_int(struct hfi1_devdata *dd, unsigned int source)

    User receive context available IRQ handler

    :param dd:
        valid dd
    :type dd: struct hfi1_devdata \*

    :param source:
        logical IRQ source (offset from IS_RCVAVAIL_START)
    :type source: unsigned int

.. _`is_rcv_avail_int.description`:

Description
-----------

RX block receive available interrupt.  Source is < 160.

This is the general interrupt handler for user (PSM) receive contexts,
and can only be used for non-threaded IRQs.

.. _`is_rcv_urgent_int`:

is_rcv_urgent_int
=================

.. c:function:: void is_rcv_urgent_int(struct hfi1_devdata *dd, unsigned int source)

    User receive context urgent IRQ handler

    :param dd:
        valid dd
    :type dd: struct hfi1_devdata \*

    :param source:
        logical IRQ source (offset from IS_RCVURGENT_START)
    :type source: unsigned int

.. _`is_rcv_urgent_int.description`:

Description
-----------

RX block receive urgent interrupt.  Source is < 160.

.. _`is_rcv_urgent_int.note`:

NOTE
----

kernel receive contexts specifically do NOT enable this IRQ.

.. _`general_interrupt`:

general_interrupt
=================

.. c:function:: irqreturn_t general_interrupt(int irq, void *data)

    General interrupt handler

    :param irq:
        MSIx IRQ vector
    :type irq: int

    :param data:
        hfi1 devdata
    :type data: void \*

.. _`general_interrupt.description`:

Description
-----------

This is able to correctly handle all non-threaded interrupts.  Receive
context DATA IRQs are threaded and are not supported by this handler.

.. _`data_vls_operational`:

data_vls_operational
====================

.. c:function:: bool data_vls_operational(struct hfi1_pportdata *ppd)

    Verify if data VL BCT credits and MTU are both set.

    :param ppd:
        pointer to hfi1_pportdata structure
    :type ppd: struct hfi1_pportdata \*

.. _`data_vls_operational.return`:

Return
------

true - Ok, false -otherwise.

.. _`update_statusp`:

update_statusp
==============

.. c:function:: void update_statusp(struct hfi1_pportdata *ppd, u32 state)

    Update userspace status flag

    :param ppd:
        Port data structure
    :type ppd: struct hfi1_pportdata \*

    :param state:
        port state information
    :type state: u32

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

    :param ppd:
        port device
    :type ppd: struct hfi1_pportdata \*

    :param state:
        the state to wait for
    :type state: u32

    :param msecs:
        the number of milliseconds to wait
    :type msecs: int

.. _`wait_logical_linkstate.description`:

Description
-----------

Wait up to msecs milliseconds for IB link state change to occur.
For now, take the easy polling route.
Returns 0 if state reached, otherwise -ETIMEDOUT.

.. _`read_mod_write`:

read_mod_write
==============

.. c:function:: void read_mod_write(struct hfi1_devdata *dd, u16 src, u64 bits, bool set)

    Calculate the IRQ register index and set/clear the bits

    :param dd:
        valid devdata
    :type dd: struct hfi1_devdata \*

    :param src:
        IRQ source to determine register index from
    :type src: u16

    :param bits:
        the bits to set or clear
    :type bits: u64

    :param set:
        true == set the bits, false == clear the bits
    :type set: bool

.. _`set_intr_bits`:

set_intr_bits
=============

.. c:function:: int set_intr_bits(struct hfi1_devdata *dd, u16 first, u16 last, bool set)

    Enable/disable a range (one or more) IRQ sources

    :param dd:
        valid devdata
    :type dd: struct hfi1_devdata \*

    :param first:
        first IRQ source to set/clear
    :type first: u16

    :param last:
        last IRQ source (inclusive) to set/clear
    :type last: u16

    :param set:
        true == set the bits, false == clear the bits
    :type set: bool

.. _`set_intr_bits.description`:

Description
-----------

If first == last, set the exact source.

.. _`set_up_interrupts`:

set_up_interrupts
=================

.. c:function:: int set_up_interrupts(struct hfi1_devdata *dd)

    Initialize the IRQ resources and state

    :param dd:
        valid devdata
    :type dd: struct hfi1_devdata \*

.. _`init_qpmap_table`:

init_qpmap_table
================

.. c:function:: void init_qpmap_table(struct hfi1_devdata *dd, u32 first_ctxt, u32 last_ctxt)

    \ ``dd``\  - device data \ ``first_ctxt``\  - first context \ ``last_ctxt``\  - first context

    :param dd:
        *undescribed*
    :type dd: struct hfi1_devdata \*

    :param first_ctxt:
        *undescribed*
    :type first_ctxt: u32

    :param last_ctxt:
        *undescribed*
    :type last_ctxt: u32

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

    :param dd:
        *undescribed*
    :type dd: struct hfi1_devdata \*

    :param rmt:
        *undescribed*
    :type rmt: struct rsm_map_table \*

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

.. c:function:: int hfi1_init_dd(struct hfi1_devdata *dd)

    Initialize most of the dd structure.

    :param dd:
        *undescribed*
    :type dd: struct hfi1_devdata \*

.. _`hfi1_init_dd.description`:

Description
-----------

This is global, and is called directly at init to set up the
chip-specific function pointers for later use.

.. _`create_pbc`:

create_pbc
==========

.. c:function:: u64 create_pbc(struct hfi1_pportdata *ppd, u64 flags, int srate_mbs, u32 vl, u32 dw_len)

    build a pbc for transmission

    :param ppd:
        *undescribed*
    :type ppd: struct hfi1_pportdata \*

    :param flags:
        special case flags or-ed in built pbc
    :type flags: u64

    :param srate_mbs:
        *undescribed*
    :type srate_mbs: int

    :param vl:
        vl
    :type vl: u32

    :param dw_len:
        *undescribed*
    :type dw_len: u32

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

