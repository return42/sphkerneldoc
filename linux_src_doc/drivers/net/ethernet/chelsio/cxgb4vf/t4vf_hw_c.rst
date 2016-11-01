.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/t4vf_hw.c

.. _`t4vf_record_mbox`:

t4vf_record_mbox
================

.. c:function:: void t4vf_record_mbox(struct adapter *adapter, const __be64 *cmd, int size, int access, int execute)

    record a Firmware Mailbox Command/Reply in the log

    :param struct adapter \*adapter:
        the adapter

    :param const __be64 \*cmd:
        the Firmware Mailbox Command or Reply

    :param int size:
        command length in bytes

    :param int access:
        the time (ms) needed to access the Firmware Mailbox

    :param int execute:
        the time (ms) the command spent being executed

.. _`t4vf_wr_mbox_core`:

t4vf_wr_mbox_core
=================

.. c:function:: int t4vf_wr_mbox_core(struct adapter *adapter, const void *cmd, int size, void *rpl, bool sleep_ok)

    send a command to FW through the mailbox

    :param struct adapter \*adapter:
        the adapter

    :param const void \*cmd:
        the command to write

    :param int size:
        command length in bytes

    :param void \*rpl:
        where to optionally store the reply

    :param bool sleep_ok:
        if true we may sleep while awaiting command completion

.. _`t4vf_wr_mbox_core.description`:

Description
-----------

Sends the given command to FW through the mailbox and waits for the
FW to execute the command.  If \ ``rpl``\  is not \ ``NULL``\  it is used to store
the FW's reply to the command.  The command and its optional reply
are of the same length.  FW can take up to 500 ms to respond.
\ ``sleep_ok``\  determines whether we may sleep while awaiting the response.
If sleeping is allowed we use progressive backoff otherwise we spin.

The return value is 0 on success or a negative errno on failure.  A
failure can happen either because we are not able to execute the
command or FW executes it but signals an error.  In the latter case
the return value is the error code indicated by FW (negated).

.. _`init_link_config`:

init_link_config
================

.. c:function:: void init_link_config(struct link_config *lc, unsigned int caps)

    initialize a link's SW state

    :param struct link_config \*lc:
        structure holding the link state

    :param unsigned int caps:
        link capabilities

.. _`init_link_config.description`:

Description
-----------

Initializes the SW state maintained for each link, including the link's
capabilities and default speed/flow-control/autonegotiation settings.

.. _`t4vf_port_init`:

t4vf_port_init
==============

.. c:function:: int t4vf_port_init(struct adapter *adapter, int pidx)

    initialize port hardware/software state

    :param struct adapter \*adapter:
        the adapter

    :param int pidx:
        the adapter port index

.. _`t4vf_fw_reset`:

t4vf_fw_reset
=============

.. c:function:: int t4vf_fw_reset(struct adapter *adapter)

    issue a reset to FW

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_fw_reset.description`:

Description
-----------

Issues a reset command to FW.  For a Physical Function this would
result in the Firmware resetting all of its state.  For a Virtual
Function this just resets the state associated with the VF.

.. _`t4vf_query_params`:

t4vf_query_params
=================

.. c:function:: int t4vf_query_params(struct adapter *adapter, unsigned int nparams, const u32 *params, u32 *vals)

    query FW or device parameters

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int nparams:
        the number of parameters

    :param const u32 \*params:
        the parameter names

    :param u32 \*vals:
        the parameter values

.. _`t4vf_query_params.description`:

Description
-----------

Reads the values of firmware or device parameters.  Up to 7 parameters
can be queried at once.

.. _`t4vf_set_params`:

t4vf_set_params
===============

.. c:function:: int t4vf_set_params(struct adapter *adapter, unsigned int nparams, const u32 *params, const u32 *vals)

    sets FW or device parameters

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int nparams:
        the number of parameters

    :param const u32 \*params:
        the parameter names

    :param const u32 \*vals:
        the parameter values

.. _`t4vf_set_params.description`:

Description
-----------

Sets the values of firmware or device parameters.  Up to 7 parameters
can be specified at once.

.. _`t4vf_fl_pkt_align`:

t4vf_fl_pkt_align
=================

.. c:function:: int t4vf_fl_pkt_align(struct adapter *adapter)

    return the fl packet alignment

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_fl_pkt_align.description`:

Description
-----------

T4 has a single field to specify the packing and padding boundary.
T5 onwards has separate fields for this and hence the alignment for
next packet offset is maximum of these two.  And T6 changes the
Ingress Padding Boundary Shift, so it's all a mess and it's best
if we put this in low-level Common Code ...

.. _`t4vf_bar2_sge_qregs`:

t4vf_bar2_sge_qregs
===================

.. c:function:: int t4vf_bar2_sge_qregs(struct adapter *adapter, unsigned int qid, enum t4_bar2_qtype qtype, u64 *pbar2_qoffset, unsigned int *pbar2_qid)

    return BAR2 SGE Queue register information

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int qid:
        the Queue ID

    :param enum t4_bar2_qtype qtype:
        the Ingress or Egress type for \ ``qid``\ 

    :param u64 \*pbar2_qoffset:
        BAR2 Queue Offset

    :param unsigned int \*pbar2_qid:
        BAR2 Queue ID or 0 for Queue ID inferred SGE Queues

.. _`t4vf_bar2_sge_qregs.description`:

Description
-----------

Returns the BAR2 SGE Queue Registers information associated with the
indicated Absolute Queue ID.  These are passed back in return value
pointers.  \ ``qtype``\  should be T4_BAR2_QTYPE_EGRESS for Egress Queue
and T4_BAR2_QTYPE_INGRESS for Ingress Queues.

This may return an error which indicates that BAR2 SGE Queue
registers aren't available.  If an error is not returned, then the

.. _`t4vf_bar2_sge_qregs.following-values-are-returned`:

following values are returned
-----------------------------


\*@pbar2_qoffset: the BAR2 Offset of the \ ``qid``\  Registers
\*@pbar2_qid: the BAR2 SGE Queue ID or 0 of \ ``qid``\ 

If the returned BAR2 Queue ID is 0, then BAR2 SGE registers which
require the "Inferred Queue ID" ability may be used.  E.g. the
Write Combining Doorbell Buffer. If the BAR2 Queue ID is not 0,
then these "Inferred Queue ID" register may not be used.

.. _`t4vf_get_sge_params`:

t4vf_get_sge_params
===================

.. c:function:: int t4vf_get_sge_params(struct adapter *adapter)

    retrieve adapter Scatter gather Engine parameters

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_get_sge_params.description`:

Description
-----------

Retrieves various core SGE parameters in the form of hardware SGE
register values.  The caller is responsible for decoding these as
needed.  The SGE parameters are stored in \ ``adapter``\ ->params.sge.

.. _`t4vf_get_vpd_params`:

t4vf_get_vpd_params
===================

.. c:function:: int t4vf_get_vpd_params(struct adapter *adapter)

    retrieve device VPD paremeters

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_get_vpd_params.description`:

Description
-----------

Retrives various device Vital Product Data parameters.  The parameters
are stored in \ ``adapter``\ ->params.vpd.

.. _`t4vf_get_dev_params`:

t4vf_get_dev_params
===================

.. c:function:: int t4vf_get_dev_params(struct adapter *adapter)

    retrieve device paremeters

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_get_dev_params.description`:

Description
-----------

Retrives various device parameters.  The parameters are stored in
\ ``adapter``\ ->params.dev.

.. _`t4vf_get_rss_glb_config`:

t4vf_get_rss_glb_config
=======================

.. c:function:: int t4vf_get_rss_glb_config(struct adapter *adapter)

    retrieve adapter RSS Global Configuration

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_get_rss_glb_config.description`:

Description
-----------

Retrieves global RSS mode and parameters with which we have to live
and stores them in the \ ``adapter``\ 's RSS parameters.

.. _`t4vf_get_vfres`:

t4vf_get_vfres
==============

.. c:function:: int t4vf_get_vfres(struct adapter *adapter)

    retrieve VF resource limits

    :param struct adapter \*adapter:
        the adapter

.. _`t4vf_get_vfres.description`:

Description
-----------

Retrieves configured resource limits and capabilities for a virtual
function.  The results are stored in \ ``adapter``\ ->vfres.

.. _`t4vf_read_rss_vi_config`:

t4vf_read_rss_vi_config
=======================

.. c:function:: int t4vf_read_rss_vi_config(struct adapter *adapter, unsigned int viid, union rss_vi_config *config)

    read a VI's RSS configuration

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        Virtual Interface ID

    :param union rss_vi_config \*config:
        pointer to host-native VI RSS Configuration buffer

.. _`t4vf_read_rss_vi_config.description`:

Description
-----------

Reads the Virtual Interface's RSS configuration information and
translates it into CPU-native format.

.. _`t4vf_write_rss_vi_config`:

t4vf_write_rss_vi_config
========================

.. c:function:: int t4vf_write_rss_vi_config(struct adapter *adapter, unsigned int viid, union rss_vi_config *config)

    write a VI's RSS configuration

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        Virtual Interface ID

    :param union rss_vi_config \*config:
        pointer to host-native VI RSS Configuration buffer

.. _`t4vf_write_rss_vi_config.description`:

Description
-----------

Write the Virtual Interface's RSS configuration information
(translating it into firmware-native format before writing).

.. _`t4vf_config_rss_range`:

t4vf_config_rss_range
=====================

.. c:function:: int t4vf_config_rss_range(struct adapter *adapter, unsigned int viid, int start, int n, const u16 *rspq, int nrspq)

    configure a portion of the RSS mapping table

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        Virtual Interface of RSS Table Slice

    :param int start:
        starting entry in the table to write

    :param int n:
        how many table entries to write

    :param const u16 \*rspq:
        values for the "Response Queue" (Ingress Queue) lookup table

    :param int nrspq:
        number of values in \ ``rspq``\ 

.. _`t4vf_config_rss_range.description`:

Description
-----------

Programs the selected part of the VI's RSS mapping table with the
provided values.  If \ ``nrspq``\  < \ ``n``\  the supplied values are used repeatedly
until the full table range is populated.

The caller must ensure the values in \ ``rspq``\  are in the range 0..1023.

.. _`t4vf_alloc_vi`:

t4vf_alloc_vi
=============

.. c:function:: int t4vf_alloc_vi(struct adapter *adapter, int port_id)

    allocate a virtual interface on a port

    :param struct adapter \*adapter:
        the adapter

    :param int port_id:
        physical port associated with the VI

.. _`t4vf_alloc_vi.description`:

Description
-----------

Allocate a new Virtual Interface and bind it to the indicated
physical port.  Return the new Virtual Interface Identifier on
success, or a [negative] error number on failure.

.. _`t4vf_free_vi`:

t4vf_free_vi
============

.. c:function:: int t4vf_free_vi(struct adapter *adapter, int viid)

    - free a virtual interface

    :param struct adapter \*adapter:
        the adapter

    :param int viid:
        the virtual interface identifier

.. _`t4vf_free_vi.description`:

Description
-----------

Free a previously allocated Virtual Interface.  Return an error on
failure.

.. _`t4vf_enable_vi`:

t4vf_enable_vi
==============

.. c:function:: int t4vf_enable_vi(struct adapter *adapter, unsigned int viid, bool rx_en, bool tx_en)

    enable/disable a virtual interface

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the Virtual Interface ID

    :param bool rx_en:
        1=enable Rx, 0=disable Rx

    :param bool tx_en:
        1=enable Tx, 0=disable Tx

.. _`t4vf_enable_vi.description`:

Description
-----------

Enables/disables a virtual interface.

.. _`t4vf_identify_port`:

t4vf_identify_port
==================

.. c:function:: int t4vf_identify_port(struct adapter *adapter, unsigned int viid, unsigned int nblinks)

    identify a VI's port by blinking its LED

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the Virtual Interface ID

    :param unsigned int nblinks:
        how many times to blink LED at 2.5 Hz

.. _`t4vf_identify_port.description`:

Description
-----------

Identifies a VI's port by blinking its LED.

.. _`t4vf_set_rxmode`:

t4vf_set_rxmode
===============

.. c:function:: int t4vf_set_rxmode(struct adapter *adapter, unsigned int viid, int mtu, int promisc, int all_multi, int bcast, int vlanex, bool sleep_ok)

    set Rx properties of a virtual interface

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the VI id

    :param int mtu:
        the new MTU or -1 for no change

    :param int promisc:
        1 to enable promiscuous mode, 0 to disable it, -1 no change

    :param int all_multi:
        1 to enable all-multi mode, 0 to disable it, -1 no change

    :param int bcast:
        1 to enable broadcast Rx, 0 to disable it, -1 no change

    :param int vlanex:
        1 to enable hardware VLAN Tag extraction, 0 to disable it,
        -1 no change

    :param bool sleep_ok:
        *undescribed*

.. _`t4vf_set_rxmode.description`:

Description
-----------

Sets Rx properties of a virtual interface.

.. _`t4vf_alloc_mac_filt`:

t4vf_alloc_mac_filt
===================

.. c:function:: int t4vf_alloc_mac_filt(struct adapter *adapter, unsigned int viid, bool free, unsigned int naddr, const u8 **addr, u16 *idx, u64 *hash, bool sleep_ok)

    allocates exact-match filters for MAC addresses

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the Virtual Interface Identifier

    :param bool free:
        if true any existing filters for this VI id are first removed

    :param unsigned int naddr:
        the number of MAC addresses to allocate filters for (up to 7)

    :param const u8 \*\*addr:
        the MAC address(es)

    :param u16 \*idx:
        where to store the index of each allocated filter

    :param u64 \*hash:
        pointer to hash address filter bitmap

    :param bool sleep_ok:
        call is allowed to sleep

.. _`t4vf_alloc_mac_filt.description`:

Description
-----------

Allocates an exact-match filter for each of the supplied addresses and
sets it to the corresponding address.  If \ ``idx``\  is not \ ``NULL``\  it should
have at least \ ``naddr``\  entries, each of which will be set to the index of
the filter allocated for the corresponding MAC address.  If a filter
could not be allocated for an address its index is set to 0xffff.
If \ ``hash``\  is not \ ``NULL``\  addresses that fail to allocate an exact filter
are hashed and update the hash filter bitmap pointed at by \ ``hash``\ .

Returns a negative error number or the number of filters allocated.

.. _`t4vf_free_mac_filt`:

t4vf_free_mac_filt
==================

.. c:function:: int t4vf_free_mac_filt(struct adapter *adapter, unsigned int viid, unsigned int naddr, const u8 **addr, bool sleep_ok)

    frees exact-match filters of given MAC addresses

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the VI id

    :param unsigned int naddr:
        the number of MAC addresses to allocate filters for (up to 7)

    :param const u8 \*\*addr:
        the MAC address(es)

    :param bool sleep_ok:
        call is allowed to sleep

.. _`t4vf_free_mac_filt.description`:

Description
-----------

Frees the exact-match filter for each of the supplied addresses

Returns a negative error number or the number of filters freed.

.. _`t4vf_change_mac`:

t4vf_change_mac
===============

.. c:function:: int t4vf_change_mac(struct adapter *adapter, unsigned int viid, int idx, const u8 *addr, bool persist)

    modifies the exact-match filter for a MAC address

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the Virtual Interface ID

    :param int idx:
        index of existing filter for old value of MAC address, or -1

    :param const u8 \*addr:
        the new MAC address value

    :param bool persist:
        if idx < 0, the new MAC allocation should be persistent

.. _`t4vf_change_mac.description`:

Description
-----------

Modifies an exact-match filter and sets it to the new MAC address.
Note that in general it is not possible to modify the value of a given
filter so the generic way to modify an address filter is to free the
one being used by the old address value and allocate a new filter for
the new address value.  \ ``idx``\  can be -1 if the address is a new
addition.

Returns a negative error number or the index of the filter with the new
MAC value.

.. _`t4vf_set_addr_hash`:

t4vf_set_addr_hash
==================

.. c:function:: int t4vf_set_addr_hash(struct adapter *adapter, unsigned int viid, bool ucast, u64 vec, bool sleep_ok)

    program the MAC inexact-match hash filter

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int viid:
        the Virtual Interface Identifier

    :param bool ucast:
        whether the hash filter should also match unicast addresses

    :param u64 vec:
        the value to be written to the hash filter

    :param bool sleep_ok:
        call is allowed to sleep

.. _`t4vf_set_addr_hash.description`:

Description
-----------

Sets the 64-bit inexact-match hash filter for a virtual interface.

.. _`t4vf_get_port_stats`:

t4vf_get_port_stats
===================

.. c:function:: int t4vf_get_port_stats(struct adapter *adapter, int pidx, struct t4vf_port_stats *s)

    collect "port" statistics

    :param struct adapter \*adapter:
        the adapter

    :param int pidx:
        the port index

    :param struct t4vf_port_stats \*s:
        the stats structure to fill

.. _`t4vf_get_port_stats.description`:

Description
-----------

Collect statistics for the "port"'s Virtual Interface.

.. _`t4vf_iq_free`:

t4vf_iq_free
============

.. c:function:: int t4vf_iq_free(struct adapter *adapter, unsigned int iqtype, unsigned int iqid, unsigned int fl0id, unsigned int fl1id)

    free an ingress queue and its free lists

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int iqtype:
        the ingress queue type (FW_IQ_TYPE_FL_INT_CAP, etc.)

    :param unsigned int iqid:
        ingress queue ID

    :param unsigned int fl0id:
        FL0 queue ID or 0xffff if no attached FL0

    :param unsigned int fl1id:
        FL1 queue ID or 0xffff if no attached FL1

.. _`t4vf_iq_free.description`:

Description
-----------

Frees an ingress queue and its associated free lists, if any.

.. _`t4vf_eth_eq_free`:

t4vf_eth_eq_free
================

.. c:function:: int t4vf_eth_eq_free(struct adapter *adapter, unsigned int eqid)

    free an Ethernet egress queue

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int eqid:
        egress queue ID

.. _`t4vf_eth_eq_free.description`:

Description
-----------

Frees an Ethernet egress queue.

.. _`t4vf_handle_fw_rpl`:

t4vf_handle_fw_rpl
==================

.. c:function:: int t4vf_handle_fw_rpl(struct adapter *adapter, const __be64 *rpl)

    process a firmware reply message

    :param struct adapter \*adapter:
        the adapter

    :param const __be64 \*rpl:
        start of the firmware message

.. _`t4vf_handle_fw_rpl.description`:

Description
-----------

Processes a firmware message, such as link state change messages.

.. _`t4vf_get_vf_mac_acl`:

t4vf_get_vf_mac_acl
===================

.. c:function:: int t4vf_get_vf_mac_acl(struct adapter *adapter, unsigned int pf, unsigned int *naddr, u8 *addr)

    Get the MAC address to be set to the VI of this VF.

    :param struct adapter \*adapter:
        The adapter

    :param unsigned int pf:
        The pf associated with vf

    :param unsigned int \*naddr:
        the number of ACL MAC addresses returned in addr

    :param u8 \*addr:
        Placeholder for MAC addresses

.. _`t4vf_get_vf_mac_acl.description`:

Description
-----------

Find the MAC address to be set to the VF's VI. The requested MAC address
is from the host OS via callback in the PF driver.

.. This file was automatic generated / don't edit.

