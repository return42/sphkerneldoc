.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/t4vf_hw.c

.. _`t4vf_record_mbox`:

t4vf_record_mbox
================

.. c:function:: void t4vf_record_mbox(struct adapter *adapter, const __be64 *cmd, int size, int access, int execute)

    record a Firmware Mailbox Command/Reply in the log

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param cmd:
        the Firmware Mailbox Command or Reply
    :type cmd: const __be64 \*

    :param size:
        command length in bytes
    :type size: int

    :param access:
        the time (ms) needed to access the Firmware Mailbox
    :type access: int

    :param execute:
        the time (ms) the command spent being executed
    :type execute: int

.. _`t4vf_wr_mbox_core`:

t4vf_wr_mbox_core
=================

.. c:function:: int t4vf_wr_mbox_core(struct adapter *adapter, const void *cmd, int size, void *rpl, bool sleep_ok)

    send a command to FW through the mailbox

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param cmd:
        the command to write
    :type cmd: const void \*

    :param size:
        command length in bytes
    :type size: int

    :param rpl:
        where to optionally store the reply
    :type rpl: void \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

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

.. _`fwcaps16_to_caps32`:

fwcaps16_to_caps32
==================

.. c:function:: fw_port_cap32_t fwcaps16_to_caps32(fw_port_cap16_t caps16)

    convert 16-bit Port Capabilities to 32-bits

    :param caps16:
        a 16-bit Port Capabilities value
    :type caps16: fw_port_cap16_t

.. _`fwcaps16_to_caps32.description`:

Description
-----------

Returns the equivalent 32-bit Port Capabilities value.

.. _`fwcap_to_speed`:

fwcap_to_speed
==============

.. c:function:: unsigned int fwcap_to_speed(fw_port_cap32_t caps)

    :param caps:
        *undescribed*
    :type caps: fw_port_cap32_t

.. _`fwcap_to_fwspeed`:

fwcap_to_fwspeed
================

.. c:function:: fw_port_cap32_t fwcap_to_fwspeed(fw_port_cap32_t acaps)

    return highest speed in Port Capabilities

    :param acaps:
        advertised Port Capabilities
    :type acaps: fw_port_cap32_t

.. _`fwcap_to_fwspeed.description`:

Description
-----------

Get the highest speed for the port from the advertised Port
Capabilities.  It will be either the highest speed from the list of
speeds or whatever user has set using ethtool.

.. _`t4vf_port_init`:

t4vf_port_init
==============

.. c:function:: int t4vf_port_init(struct adapter *adapter, int pidx)

    initialize port hardware/software state

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param pidx:
        the adapter port index
    :type pidx: int

.. _`t4vf_fw_reset`:

t4vf_fw_reset
=============

.. c:function:: int t4vf_fw_reset(struct adapter *adapter)

    issue a reset to FW

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param nparams:
        the number of parameters
    :type nparams: unsigned int

    :param params:
        the parameter names
    :type params: const u32 \*

    :param vals:
        the parameter values
    :type vals: u32 \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param nparams:
        the number of parameters
    :type nparams: unsigned int

    :param params:
        the parameter names
    :type params: const u32 \*

    :param vals:
        the parameter values
    :type vals: const u32 \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param qid:
        the Queue ID
    :type qid: unsigned int

    :param qtype:
        the Ingress or Egress type for \ ``qid``\ 
    :type qtype: enum t4_bar2_qtype

    :param pbar2_qoffset:
        BAR2 Queue Offset
    :type pbar2_qoffset: u64 \*

    :param pbar2_qid:
        BAR2 Queue ID or 0 for Queue ID inferred SGE Queues
    :type pbar2_qid: unsigned int \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_get_sge_params.description`:

Description
-----------

Retrieves various core SGE parameters in the form of hardware SGE
register values.  The caller is responsible for decoding these as
needed.  The SGE parameters are stored in \ ``adapter->params.sge``\ .

.. _`t4vf_get_vpd_params`:

t4vf_get_vpd_params
===================

.. c:function:: int t4vf_get_vpd_params(struct adapter *adapter)

    retrieve device VPD paremeters

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_get_vpd_params.description`:

Description
-----------

Retrives various device Vital Product Data parameters.  The parameters
are stored in \ ``adapter->params.vpd``\ .

.. _`t4vf_get_dev_params`:

t4vf_get_dev_params
===================

.. c:function:: int t4vf_get_dev_params(struct adapter *adapter)

    retrieve device paremeters

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_get_dev_params.description`:

Description
-----------

Retrives various device parameters.  The parameters are stored in
\ ``adapter->params.dev``\ .

.. _`t4vf_get_rss_glb_config`:

t4vf_get_rss_glb_config
=======================

.. c:function:: int t4vf_get_rss_glb_config(struct adapter *adapter)

    retrieve adapter RSS Global Configuration

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4vf_get_vfres.description`:

Description
-----------

Retrieves configured resource limits and capabilities for a virtual
function.  The results are stored in \ ``adapter->vfres``\ .

.. _`t4vf_read_rss_vi_config`:

t4vf_read_rss_vi_config
=======================

.. c:function:: int t4vf_read_rss_vi_config(struct adapter *adapter, unsigned int viid, union rss_vi_config *config)

    read a VI's RSS configuration

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        Virtual Interface ID
    :type viid: unsigned int

    :param config:
        pointer to host-native VI RSS Configuration buffer
    :type config: union rss_vi_config \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        Virtual Interface ID
    :type viid: unsigned int

    :param config:
        pointer to host-native VI RSS Configuration buffer
    :type config: union rss_vi_config \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        Virtual Interface of RSS Table Slice
    :type viid: unsigned int

    :param start:
        starting entry in the table to write
    :type start: int

    :param n:
        how many table entries to write
    :type n: int

    :param rspq:
        values for the "Response Queue" (Ingress Queue) lookup table
    :type rspq: const u16 \*

    :param nrspq:
        number of values in \ ``rspq``\ 
    :type nrspq: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param port_id:
        physical port associated with the VI
    :type port_id: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the virtual interface identifier
    :type viid: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the Virtual Interface ID
    :type viid: unsigned int

    :param rx_en:
        1=enable Rx, 0=disable Rx
    :type rx_en: bool

    :param tx_en:
        1=enable Tx, 0=disable Tx
    :type tx_en: bool

.. _`t4vf_enable_vi.description`:

Description
-----------

Enables/disables a virtual interface.

.. _`t4vf_enable_pi`:

t4vf_enable_pi
==============

.. c:function:: int t4vf_enable_pi(struct adapter *adapter, struct port_info *pi, bool rx_en, bool tx_en)

    enable/disable a Port's virtual interface

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param pi:
        the Port Information structure
    :type pi: struct port_info \*

    :param rx_en:
        1=enable Rx, 0=disable Rx
    :type rx_en: bool

    :param tx_en:
        1=enable Tx, 0=disable Tx
    :type tx_en: bool

.. _`t4vf_enable_pi.description`:

Description
-----------

Enables/disables a Port's virtual interface.  If the Virtual
Interface enable/disable operation is successful, we notify the
OS-specific code of a potential Link Status change via the OS Contract
API \ :c:func:`t4vf_os_link_changed`\ .

.. _`t4vf_identify_port`:

t4vf_identify_port
==================

.. c:function:: int t4vf_identify_port(struct adapter *adapter, unsigned int viid, unsigned int nblinks)

    identify a VI's port by blinking its LED

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the Virtual Interface ID
    :type viid: unsigned int

    :param nblinks:
        how many times to blink LED at 2.5 Hz
    :type nblinks: unsigned int

.. _`t4vf_identify_port.description`:

Description
-----------

Identifies a VI's port by blinking its LED.

.. _`t4vf_set_rxmode`:

t4vf_set_rxmode
===============

.. c:function:: int t4vf_set_rxmode(struct adapter *adapter, unsigned int viid, int mtu, int promisc, int all_multi, int bcast, int vlanex, bool sleep_ok)

    set Rx properties of a virtual interface

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the VI id
    :type viid: unsigned int

    :param mtu:
        the new MTU or -1 for no change
    :type mtu: int

    :param promisc:
        1 to enable promiscuous mode, 0 to disable it, -1 no change
    :type promisc: int

    :param all_multi:
        1 to enable all-multi mode, 0 to disable it, -1 no change
    :type all_multi: int

    :param bcast:
        1 to enable broadcast Rx, 0 to disable it, -1 no change
    :type bcast: int

    :param vlanex:
        1 to enable hardware VLAN Tag extraction, 0 to disable it,
        -1 no change
    :type vlanex: int

    :param sleep_ok:
        *undescribed*
    :type sleep_ok: bool

.. _`t4vf_set_rxmode.description`:

Description
-----------

Sets Rx properties of a virtual interface.

.. _`t4vf_alloc_mac_filt`:

t4vf_alloc_mac_filt
===================

.. c:function:: int t4vf_alloc_mac_filt(struct adapter *adapter, unsigned int viid, bool free, unsigned int naddr, const u8 **addr, u16 *idx, u64 *hash, bool sleep_ok)

    allocates exact-match filters for MAC addresses

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the Virtual Interface Identifier
    :type viid: unsigned int

    :param free:
        if true any existing filters for this VI id are first removed
    :type free: bool

    :param naddr:
        the number of MAC addresses to allocate filters for (up to 7)
    :type naddr: unsigned int

    :param addr:
        the MAC address(es)
    :type addr: const u8 \*\*

    :param idx:
        where to store the index of each allocated filter
    :type idx: u16 \*

    :param hash:
        pointer to hash address filter bitmap
    :type hash: u64 \*

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the VI id
    :type viid: unsigned int

    :param naddr:
        the number of MAC addresses to allocate filters for (up to 7)
    :type naddr: unsigned int

    :param addr:
        the MAC address(es)
    :type addr: const u8 \*\*

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the Virtual Interface ID
    :type viid: unsigned int

    :param idx:
        index of existing filter for old value of MAC address, or -1
    :type idx: int

    :param addr:
        the new MAC address value
    :type addr: const u8 \*

    :param persist:
        if idx < 0, the new MAC allocation should be persistent
    :type persist: bool

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param viid:
        the Virtual Interface Identifier
    :type viid: unsigned int

    :param ucast:
        whether the hash filter should also match unicast addresses
    :type ucast: bool

    :param vec:
        the value to be written to the hash filter
    :type vec: u64

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

.. _`t4vf_set_addr_hash.description`:

Description
-----------

Sets the 64-bit inexact-match hash filter for a virtual interface.

.. _`t4vf_get_port_stats`:

t4vf_get_port_stats
===================

.. c:function:: int t4vf_get_port_stats(struct adapter *adapter, int pidx, struct t4vf_port_stats *s)

    collect "port" statistics

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

    :param s:
        the stats structure to fill
    :type s: struct t4vf_port_stats \*

.. _`t4vf_get_port_stats.description`:

Description
-----------

Collect statistics for the "port"'s Virtual Interface.

.. _`t4vf_iq_free`:

t4vf_iq_free
============

.. c:function:: int t4vf_iq_free(struct adapter *adapter, unsigned int iqtype, unsigned int iqid, unsigned int fl0id, unsigned int fl1id)

    free an ingress queue and its free lists

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param iqtype:
        the ingress queue type (FW_IQ_TYPE_FL_INT_CAP, etc.)
    :type iqtype: unsigned int

    :param iqid:
        ingress queue ID
    :type iqid: unsigned int

    :param fl0id:
        FL0 queue ID or 0xffff if no attached FL0
    :type fl0id: unsigned int

    :param fl1id:
        FL1 queue ID or 0xffff if no attached FL1
    :type fl1id: unsigned int

.. _`t4vf_iq_free.description`:

Description
-----------

Frees an ingress queue and its associated free lists, if any.

.. _`t4vf_eth_eq_free`:

t4vf_eth_eq_free
================

.. c:function:: int t4vf_eth_eq_free(struct adapter *adapter, unsigned int eqid)

    free an Ethernet egress queue

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param eqid:
        egress queue ID
    :type eqid: unsigned int

.. _`t4vf_eth_eq_free.description`:

Description
-----------

Frees an Ethernet egress queue.

.. _`t4vf_link_down_rc_str`:

t4vf_link_down_rc_str
=====================

.. c:function:: const char *t4vf_link_down_rc_str(unsigned char link_down_rc)

    return a string for a Link Down Reason Code

    :param link_down_rc:
        Link Down Reason Code
    :type link_down_rc: unsigned char

.. _`t4vf_link_down_rc_str.description`:

Description
-----------

Returns a string representation of the Link Down Reason Code.

.. _`t4vf_handle_get_port_info`:

t4vf_handle_get_port_info
=========================

.. c:function:: void t4vf_handle_get_port_info(struct port_info *pi, const struct fw_port_cmd *cmd)

    process a FW reply message

    :param pi:
        the port info
    :type pi: struct port_info \*

    :param cmd:
        *undescribed*
    :type cmd: const struct fw_port_cmd \*

.. _`t4vf_handle_get_port_info.description`:

Description
-----------

Processes a GET_PORT_INFO FW reply message.

.. _`t4vf_update_port_info`:

t4vf_update_port_info
=====================

.. c:function:: int t4vf_update_port_info(struct port_info *pi)

    retrieve and update port information if changed

    :param pi:
        the port_info
    :type pi: struct port_info \*

.. _`t4vf_update_port_info.description`:

Description
-----------

We issue a Get Port Information Command to the Firmware and, if
successful, we check to see if anything is different from what we
last recorded and update things accordingly.

.. _`t4vf_handle_fw_rpl`:

t4vf_handle_fw_rpl
==================

.. c:function:: int t4vf_handle_fw_rpl(struct adapter *adapter, const __be64 *rpl)

    process a firmware reply message

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param rpl:
        start of the firmware message
    :type rpl: const __be64 \*

.. _`t4vf_handle_fw_rpl.description`:

Description
-----------

Processes a firmware message, such as link state change messages.

.. _`t4vf_get_vf_mac_acl`:

t4vf_get_vf_mac_acl
===================

.. c:function:: int t4vf_get_vf_mac_acl(struct adapter *adapter, unsigned int pf, unsigned int *naddr, u8 *addr)

    Get the MAC address to be set to the VI of this VF.

    :param adapter:
        The adapter
    :type adapter: struct adapter \*

    :param pf:
        The pf associated with vf
    :type pf: unsigned int

    :param naddr:
        the number of ACL MAC addresses returned in addr
    :type naddr: unsigned int \*

    :param addr:
        Placeholder for MAC addresses
    :type addr: u8 \*

.. _`t4vf_get_vf_mac_acl.description`:

Description
-----------

Find the MAC address to be set to the VF's VI. The requested MAC address
is from the host OS via callback in the PF driver.

.. _`t4vf_get_vf_vlan_acl`:

t4vf_get_vf_vlan_acl
====================

.. c:function:: int t4vf_get_vf_vlan_acl(struct adapter *adapter)

    Get the VLAN ID to be set to the VI of this VF.

    :param adapter:
        The adapter
    :type adapter: struct adapter \*

.. _`t4vf_get_vf_vlan_acl.description`:

Description
-----------

Find the VLAN ID to be set to the VF's VI. The requested VLAN ID
is from the host OS via callback in the PF driver.

.. This file was automatic generated / don't edit.

