.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_fcoe.c

.. _`i40e_fcoe_sof_is_class2`:

i40e_fcoe_sof_is_class2
=======================

.. c:function:: bool i40e_fcoe_sof_is_class2(u8 sof)

    returns true if this is a FC Class 2 SOF

    :param u8 sof:
        the FCoE start of frame delimiter

.. _`i40e_fcoe_sof_is_class3`:

i40e_fcoe_sof_is_class3
=======================

.. c:function:: bool i40e_fcoe_sof_is_class3(u8 sof)

    returns true if this is a FC Class 3 SOF

    :param u8 sof:
        the FCoE start of frame delimiter

.. _`i40e_fcoe_sof_is_supported`:

i40e_fcoe_sof_is_supported
==========================

.. c:function:: bool i40e_fcoe_sof_is_supported(u8 sof)

    returns true if the FC SOF is supported by HW

    :param u8 sof:
        the input SOF value from the frame

.. _`i40e_fcoe_fc_sof`:

i40e_fcoe_fc_sof
================

.. c:function:: int i40e_fcoe_fc_sof(struct sk_buff *skb, u8 *sof)

    pull the SOF from FCoE header in the frame

    :param struct sk_buff \*skb:
        the frame whose EOF is to be pulled from

    :param u8 \*sof:
        *undescribed*

.. _`i40e_fcoe_eof_is_supported`:

i40e_fcoe_eof_is_supported
==========================

.. c:function:: bool i40e_fcoe_eof_is_supported(u8 eof)

    returns true if the EOF is supported by HW

    :param u8 eof:
        the input EOF value from the frame

.. _`i40e_fcoe_fc_eof`:

i40e_fcoe_fc_eof
================

.. c:function:: int i40e_fcoe_fc_eof(struct sk_buff *skb, u8 *eof)

    pull EOF from FCoE trailer in the frame

    :param struct sk_buff \*skb:
        the frame whose EOF is to be pulled from

    :param u8 \*eof:
        *undescribed*

.. _`i40e_fcoe_ctxt_eof`:

i40e_fcoe_ctxt_eof
==================

.. c:function:: u32 i40e_fcoe_ctxt_eof(u8 eof)

    convert input FC EOF for descriptor programming

    :param u8 eof:
        the input eof value from the frame

.. _`i40e_fcoe_ctxt_eof.description`:

Description
-----------

The FC EOF is converted to the value understood by HW for descriptor
programming. Never call this w/o calling \ :c:func:`i40e_fcoe_eof_is_supported`\ 
first and that already checks for all supported valid eof values.

.. _`i40e_fcoe_xid_is_valid`:

i40e_fcoe_xid_is_valid
======================

.. c:function:: bool i40e_fcoe_xid_is_valid(u16 xid)

    returns true if the exchange id is valid

    :param u16 xid:
        the exchange id

.. _`i40e_fcoe_ddp_unmap`:

i40e_fcoe_ddp_unmap
===================

.. c:function:: void i40e_fcoe_ddp_unmap(struct i40e_pf *pf, struct i40e_fcoe_ddp *ddp)

    unmap the mapped sglist associated

    :param struct i40e_pf \*pf:
        pointer to PF

    :param struct i40e_fcoe_ddp \*ddp:
        sw DDP context

.. _`i40e_fcoe_ddp_unmap.description`:

Description
-----------

Unmap the scatter-gather list associated with the given SW DDP context

.. _`i40e_fcoe_ddp_unmap.return`:

Return
------

data length already ddp-ed in bytes

.. _`i40e_fcoe_ddp_clear`:

i40e_fcoe_ddp_clear
===================

.. c:function:: void i40e_fcoe_ddp_clear(struct i40e_fcoe_ddp *ddp)

    clear the given SW DDP context \ ``ddp``\  - SW DDP context

    :param struct i40e_fcoe_ddp \*ddp:
        *undescribed*

.. _`i40e_fcoe_progid_is_fcoe`:

i40e_fcoe_progid_is_fcoe
========================

.. c:function:: bool i40e_fcoe_progid_is_fcoe(u8 id)

    check if the prog_id is for FCoE

    :param u8 id:
        the prog id for the programming status Rx descriptor write-back

.. _`i40e_fcoe_fc_get_xid`:

i40e_fcoe_fc_get_xid
====================

.. c:function:: u16 i40e_fcoe_fc_get_xid(struct fc_frame_header *fh)

    get xid from the frame header

    :param struct fc_frame_header \*fh:
        the fc frame header

.. _`i40e_fcoe_fc_get_xid.description`:

Description
-----------

In case the incoming frame's exchange is originated from
the initiator, then received frame's exchange id is ANDed
with fc_cpu_mask bits to get the same cpu on which exchange
was originated, otherwise just use the current cpu.

Returns ox_id if exchange originator, rx_id if responder

.. _`i40e_fcoe_fc_frame_header`:

i40e_fcoe_fc_frame_header
=========================

.. c:function:: struct fc_frame_header *i40e_fcoe_fc_frame_header(struct sk_buff *skb)

    get fc frame header from skb

    :param struct sk_buff \*skb:
        packet

.. _`i40e_fcoe_fc_frame_header.description`:

Description
-----------

This checks if there is a VLAN header and returns the data
pointer to the start of the fc_frame_header.

Returns pointer to the fc_frame_header

.. _`i40e_fcoe_ddp_put`:

i40e_fcoe_ddp_put
=================

.. c:function:: int i40e_fcoe_ddp_put(struct net_device *netdev, u16 xid)

    release the DDP context for a given exchange id

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the exchange id that corresponding DDP context will be released

.. _`i40e_fcoe_ddp_put.description`:

Description
-----------

This is the implementation of net_device_ops.ndo_fcoe_ddp_done
and it is expected to be called by ULD, i.e., FCP layer of libfc
to release the corresponding ddp context when the I/O is done.

Returns : data length already ddp-ed in bytes

.. _`i40e_init_pf_fcoe`:

i40e_init_pf_fcoe
=================

.. c:function:: void i40e_init_pf_fcoe(struct i40e_pf *pf)

    sets up the HW for FCoE

    :param struct i40e_pf \*pf:
        pointer to PF

.. _`i40e_get_fcoe_tc_map`:

i40e_get_fcoe_tc_map
====================

.. c:function:: u8 i40e_get_fcoe_tc_map(struct i40e_pf *pf)

    Return TC map for FCoE APP

    :param struct i40e_pf \*pf:
        pointer to PF

.. _`i40e_fcoe_vsi_init`:

i40e_fcoe_vsi_init
==================

.. c:function:: int i40e_fcoe_vsi_init(struct i40e_vsi *vsi, struct i40e_vsi_context *ctxt)

    prepares the VSI context for creating a FCoE VSI

    :param struct i40e_vsi \*vsi:
        pointer to the associated VSI struct

    :param struct i40e_vsi_context \*ctxt:
        pointer to the associated VSI context to be passed to HW

.. _`i40e_fcoe_vsi_init.description`:

Description
-----------

Returns 0 on success or < 0 on error

.. _`i40e_fcoe_enable`:

i40e_fcoe_enable
================

.. c:function:: int i40e_fcoe_enable(struct net_device *netdev)

    this is the implementation of ndo_fcoe_enable, indicating the upper FCoE protocol stack is ready to use FCoE offload features.

    :param struct net_device \*netdev:
        pointer to the netdev that FCoE is created on

.. _`i40e_fcoe_enable.description`:

Description
-----------

Returns 0 on success

in RTNL

.. _`i40e_fcoe_disable`:

i40e_fcoe_disable
=================

.. c:function:: int i40e_fcoe_disable(struct net_device *netdev)

    disables FCoE for upper FCoE protocol stack.

    :param struct net_device \*netdev:
        *undescribed*

.. _`i40e_fcoe_disable.description`:

Description
-----------

Returns 0 on success

.. _`i40e_fcoe_dma_pool_free`:

i40e_fcoe_dma_pool_free
=======================

.. c:function:: void i40e_fcoe_dma_pool_free(struct i40e_fcoe *fcoe, struct device *dev, unsigned int cpu)

    free the per cpu pool for FCoE DDP

    :param struct i40e_fcoe \*fcoe:
        the FCoE sw object

    :param struct device \*dev:
        the device that the pool is associated with

    :param unsigned int cpu:
        the cpu for this pool

.. _`i40e_fcoe_dma_pool_create`:

i40e_fcoe_dma_pool_create
=========================

.. c:function:: int i40e_fcoe_dma_pool_create(struct i40e_fcoe *fcoe, struct device *dev, unsigned int cpu)

    per cpu pool for FCoE DDP

    :param struct i40e_fcoe \*fcoe:
        the FCoE sw object

    :param struct device \*dev:
        the device that the pool is associated with

    :param unsigned int cpu:
        the cpu for this pool

.. _`i40e_fcoe_dma_pool_create.description`:

Description
-----------

Returns 0 on successful or non zero on failure

.. _`i40e_fcoe_free_ddp_resources`:

i40e_fcoe_free_ddp_resources
============================

.. c:function:: void i40e_fcoe_free_ddp_resources(struct i40e_vsi *vsi)

    release FCoE DDP resources

    :param struct i40e_vsi \*vsi:
        the vsi FCoE is associated with

.. _`i40e_fcoe_setup_ddp_resources`:

i40e_fcoe_setup_ddp_resources
=============================

.. c:function:: int i40e_fcoe_setup_ddp_resources(struct i40e_vsi *vsi)

    allocate per cpu DDP resources

    :param struct i40e_vsi \*vsi:
        the VSI FCoE is associated with

.. _`i40e_fcoe_setup_ddp_resources.description`:

Description
-----------

Returns 0 on successful or non zero on failure

.. _`i40e_fcoe_handle_status`:

i40e_fcoe_handle_status
=======================

.. c:function:: void i40e_fcoe_handle_status(struct i40e_ring *rx_ring, union i40e_rx_desc *rx_desc, u8 prog_id)

    check the Programming Status for FCoE

    :param struct i40e_ring \*rx_ring:
        the Rx ring for this descriptor

    :param union i40e_rx_desc \*rx_desc:
        the Rx descriptor for Programming Status, not a packet descriptor.

    :param u8 prog_id:
        *undescribed*

.. _`i40e_fcoe_handle_status.description`:

Description
-----------

Check if this is the Rx Programming Status descriptor write-back for FCoE.
This is used to verify if the context/filter programming or invalidation
requested by SW to the HW is successful or not and take actions accordingly.

.. _`i40e_fcoe_handle_offload`:

i40e_fcoe_handle_offload
========================

.. c:function:: int i40e_fcoe_handle_offload(struct i40e_ring *rx_ring, union i40e_rx_desc *rx_desc, struct sk_buff *skb)

    check ddp status and mark it done

    :param struct i40e_ring \*rx_ring:
        *undescribed*

    :param union i40e_rx_desc \*rx_desc:
        advanced rx descriptor

    :param struct sk_buff \*skb:
        the skb holding the received data

.. _`i40e_fcoe_handle_offload.description`:

Description
-----------

This checks ddp status.

Returns : < 0 indicates an error or not a FCOE ddp, 0 indicates
not passing the skb to ULD, > 0 indicates is the length of data
being ddped.

.. _`i40e_fcoe_ddp_setup`:

i40e_fcoe_ddp_setup
===================

.. c:function:: int i40e_fcoe_ddp_setup(struct net_device *netdev, u16 xid, struct scatterlist *sgl, unsigned int sgc, int target_mode)

    called to set up ddp context

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the exchange id requesting ddp

    :param struct scatterlist \*sgl:
        the scatter-gather list for this request

    :param unsigned int sgc:
        the number of scatter-gather items

    :param int target_mode:
        indicates this is a DDP request for target

.. _`i40e_fcoe_ddp_setup.description`:

Description
-----------

Returns : 1 for success and 0 for no DDP on this I/O

.. _`i40e_fcoe_ddp_get`:

i40e_fcoe_ddp_get
=================

.. c:function:: int i40e_fcoe_ddp_get(struct net_device *netdev, u16 xid, struct scatterlist *sgl, unsigned int sgc)

    called to set up ddp context in initiator mode

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the exchange id requesting ddp

    :param struct scatterlist \*sgl:
        the scatter-gather list for this request

    :param unsigned int sgc:
        the number of scatter-gather items

.. _`i40e_fcoe_ddp_get.description`:

Description
-----------

This is the implementation of net_device_ops.ndo_fcoe_ddp_setup
and is expected to be called from ULD, e.g., FCP layer of libfc
to set up ddp for the corresponding xid of the given sglist for
the corresponding I/O.

Returns : 1 for success and 0 for no ddp

.. _`i40e_fcoe_ddp_target`:

i40e_fcoe_ddp_target
====================

.. c:function:: int i40e_fcoe_ddp_target(struct net_device *netdev, u16 xid, struct scatterlist *sgl, unsigned int sgc)

    called to set up ddp context in target mode

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the exchange id requesting ddp

    :param struct scatterlist \*sgl:
        the scatter-gather list for this request

    :param unsigned int sgc:
        the number of scatter-gather items

.. _`i40e_fcoe_ddp_target.description`:

Description
-----------

This is the implementation of net_device_ops.ndo_fcoe_ddp_target
and is expected to be called from ULD, e.g., FCP layer of libfc
to set up ddp for the corresponding xid of the given sglist for
the corresponding I/O. The DDP in target mode is a write I/O request
from the initiator.

Returns : 1 for success and 0 for no ddp

.. _`i40e_fcoe_program_ddp`:

i40e_fcoe_program_ddp
=====================

.. c:function:: void i40e_fcoe_program_ddp(struct i40e_ring *tx_ring, struct sk_buff *skb, struct i40e_fcoe_ddp *ddp, u8 sof)

    programs the HW DDP related descriptors

    :param struct i40e_ring \*tx_ring:
        transmit ring for this packet

    :param struct sk_buff \*skb:
        the packet to be sent out

    :param struct i40e_fcoe_ddp \*ddp:
        *undescribed*

    :param u8 sof:
        the SOF to indicate class of service

.. _`i40e_fcoe_program_ddp.description`:

Description
-----------

Determine if it is READ/WRITE command, and finds out if there is
a matching SW DDP context for this command. DDP is applicable
only in case of READ if initiator or WRITE in case of
responder (via checking XFER_RDY).

.. _`i40e_fcoe_program_ddp.note`:

Note
----

caller checks sof and ddp sw context

Returns : none

.. _`i40e_fcoe_invalidate_ddp`:

i40e_fcoe_invalidate_ddp
========================

.. c:function:: void i40e_fcoe_invalidate_ddp(struct i40e_ring *tx_ring, struct sk_buff *skb, struct i40e_fcoe_ddp *ddp)

    invalidates DDP in case of abort

    :param struct i40e_ring \*tx_ring:
        transmit ring for this packet

    :param struct sk_buff \*skb:
        the packet associated w/ this DDP invalidation, i.e., ABTS

    :param struct i40e_fcoe_ddp \*ddp:
        the SW DDP context for this DDP

.. _`i40e_fcoe_invalidate_ddp.description`:

Description
-----------

Programs the Tx context descriptor to do DDP invalidation.

.. _`i40e_fcoe_handle_ddp`:

i40e_fcoe_handle_ddp
====================

.. c:function:: void i40e_fcoe_handle_ddp(struct i40e_ring *tx_ring, struct sk_buff *skb, u8 sof)

    check we should setup or invalidate DDP

    :param struct i40e_ring \*tx_ring:
        transmit ring for this packet

    :param struct sk_buff \*skb:
        the packet to be sent out

    :param u8 sof:
        the SOF to indicate class of service

.. _`i40e_fcoe_handle_ddp.description`:

Description
-----------

Determine if it is ABTS/READ/XFER_RDY, and finds out if there is
a matching SW DDP context for this command. DDP is applicable
only in case of READ if initiator or WRITE in case of
responder (via checking XFER_RDY). In case this is an ABTS, send
just invalidate the context.

.. _`i40e_fcoe_tso`:

i40e_fcoe_tso
=============

.. c:function:: int i40e_fcoe_tso(struct i40e_ring *tx_ring, struct sk_buff *skb, u32 tx_flags, u8 *hdr_len, u8 sof)

    set up FCoE TSO

    :param struct i40e_ring \*tx_ring:
        ring to send buffer on

    :param struct sk_buff \*skb:
        send buffer

    :param u32 tx_flags:
        collected send information

    :param u8 \*hdr_len:
        the tso header length

    :param u8 sof:
        the SOF to indicate class of service

.. _`i40e_fcoe_tso.description`:

Description
-----------

Note must already have sof checked to be either class 2 or class 3 before
calling this function.

Returns 1 to indicate sequence segmentation offload is properly setup
or returns 0 to indicate no tso is needed, otherwise returns error
code to drop the frame.

.. _`i40e_fcoe_tx_map`:

i40e_fcoe_tx_map
================

.. c:function:: void i40e_fcoe_tx_map(struct i40e_ring *tx_ring, struct sk_buff *skb, struct i40e_tx_buffer *first, u32 tx_flags, u8 hdr_len, u8 eof)

    build the tx descriptor

    :param struct i40e_ring \*tx_ring:
        ring to send buffer on

    :param struct sk_buff \*skb:
        send buffer

    :param struct i40e_tx_buffer \*first:
        first buffer info buffer to use

    :param u32 tx_flags:
        collected send information

    :param u8 hdr_len:
        ptr to the size of the packet header

    :param u8 eof:
        the frame eof value

.. _`i40e_fcoe_tx_map.description`:

Description
-----------

Note, for FCoE, sof and eof are already checked

.. _`i40e_fcoe_set_skb_header`:

i40e_fcoe_set_skb_header
========================

.. c:function:: int i40e_fcoe_set_skb_header(struct sk_buff *skb)

    adjust skb header point for FIP/FCoE/FC

    :param struct sk_buff \*skb:
        the skb to be adjusted

.. _`i40e_fcoe_set_skb_header.description`:

Description
-----------

Returns true if this skb is a FCoE/FIP or VLAN carried FCoE/FIP and then
adjusts the skb header pointers correspondingly. Otherwise, returns false.

.. _`i40e_fcoe_xmit_frame`:

i40e_fcoe_xmit_frame
====================

.. c:function:: netdev_tx_t i40e_fcoe_xmit_frame(struct sk_buff *skb, struct net_device *netdev)

    transmit buffer

    :param struct sk_buff \*skb:
        send buffer

    :param struct net_device \*netdev:
        the fcoe netdev

.. _`i40e_fcoe_xmit_frame.description`:

Description
-----------

Returns 0 if sent, else an error code

.. _`i40e_fcoe_change_mtu`:

i40e_fcoe_change_mtu
====================

.. c:function:: int i40e_fcoe_change_mtu(struct net_device *netdev, int new_mtu)

    NDO callback to change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`i40e_fcoe_change_mtu.description`:

Description
-----------

Returns error as operation not permitted

.. _`i40e_fcoe_set_features`:

i40e_fcoe_set_features
======================

.. c:function:: int i40e_fcoe_set_features(struct net_device *netdev, netdev_features_t features)

    set the netdev feature flags

    :param struct net_device \*netdev:
        ptr to the netdev being adjusted

    :param netdev_features_t features:
        the feature set that the stack is suggesting

.. _`i40e_fcoe_config_netdev`:

i40e_fcoe_config_netdev
=======================

.. c:function:: void i40e_fcoe_config_netdev(struct net_device *netdev, struct i40e_vsi *vsi)

    prepares the VSI context for creating a FCoE VSI

    :param struct net_device \*netdev:
        *undescribed*

    :param struct i40e_vsi \*vsi:
        pointer to the associated VSI struct

.. _`i40e_fcoe_config_netdev.description`:

Description
-----------

Returns 0 on success or < 0 on error

.. _`i40e_fcoe_vsi_setup`:

i40e_fcoe_vsi_setup
===================

.. c:function:: void i40e_fcoe_vsi_setup(struct i40e_pf *pf)

    allocate and set up FCoE VSI

    :param struct i40e_pf \*pf:
        the PF that VSI is associated with

.. This file was automatic generated / don't edit.

