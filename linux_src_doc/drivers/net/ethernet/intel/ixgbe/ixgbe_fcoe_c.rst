.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_fcoe.c

.. _`ixgbe_fcoe_clear_ddp`:

ixgbe_fcoe_clear_ddp
====================

.. c:function:: void ixgbe_fcoe_clear_ddp(struct ixgbe_fcoe_ddp *ddp)

    clear the given ddp context

    :param struct ixgbe_fcoe_ddp \*ddp:
        ptr to the ixgbe_fcoe_ddp

.. _`ixgbe_fcoe_clear_ddp.description`:

Description
-----------

Returns : none

.. _`ixgbe_fcoe_ddp_put`:

ixgbe_fcoe_ddp_put
==================

.. c:function:: int ixgbe_fcoe_ddp_put(struct net_device *netdev, u16 xid)

    free the ddp context for a given xid

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the xid that corresponding ddp will be freed

.. _`ixgbe_fcoe_ddp_put.description`:

Description
-----------

This is the implementation of net_device_ops.ndo_fcoe_ddp_done
and it is expected to be called by ULD, i.e., FCP layer of libfc
to release the corresponding ddp context when the I/O is done.

Returns : data length already ddp-ed in bytes

.. _`ixgbe_fcoe_ddp_setup`:

ixgbe_fcoe_ddp_setup
====================

.. c:function:: int ixgbe_fcoe_ddp_setup(struct net_device *netdev, u16 xid, struct scatterlist *sgl, unsigned int sgc, int target_mode)

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
        *undescribed*

.. _`ixgbe_fcoe_ddp_setup.description`:

Description
-----------

Returns : 1 for success and 0 for no ddp

.. _`ixgbe_fcoe_ddp_get`:

ixgbe_fcoe_ddp_get
==================

.. c:function:: int ixgbe_fcoe_ddp_get(struct net_device *netdev, u16 xid, struct scatterlist *sgl, unsigned int sgc)

    called to set up ddp context in initiator mode

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the exchange id requesting ddp

    :param struct scatterlist \*sgl:
        the scatter-gather list for this request

    :param unsigned int sgc:
        the number of scatter-gather items

.. _`ixgbe_fcoe_ddp_get.description`:

Description
-----------

This is the implementation of net_device_ops.ndo_fcoe_ddp_setup
and is expected to be called from ULD, e.g., FCP layer of libfc
to set up ddp for the corresponding xid of the given sglist for
the corresponding I/O.

Returns : 1 for success and 0 for no ddp

.. _`ixgbe_fcoe_ddp_target`:

ixgbe_fcoe_ddp_target
=====================

.. c:function:: int ixgbe_fcoe_ddp_target(struct net_device *netdev, u16 xid, struct scatterlist *sgl, unsigned int sgc)

    called to set up ddp context in target mode

    :param struct net_device \*netdev:
        the corresponding net_device

    :param u16 xid:
        the exchange id requesting ddp

    :param struct scatterlist \*sgl:
        the scatter-gather list for this request

    :param unsigned int sgc:
        the number of scatter-gather items

.. _`ixgbe_fcoe_ddp_target.description`:

Description
-----------

This is the implementation of net_device_ops.ndo_fcoe_ddp_target
and is expected to be called from ULD, e.g., FCP layer of libfc
to set up ddp for the corresponding xid of the given sglist for
the corresponding I/O. The DDP in target mode is a write I/O request
from the initiator.

Returns : 1 for success and 0 for no ddp

.. _`ixgbe_fcoe_ddp`:

ixgbe_fcoe_ddp
==============

.. c:function:: int ixgbe_fcoe_ddp(struct ixgbe_adapter *adapter, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    check ddp status and mark it done

    :param struct ixgbe_adapter \*adapter:
        ixgbe adapter

    :param union ixgbe_adv_rx_desc \*rx_desc:
        advanced rx descriptor

    :param struct sk_buff \*skb:
        the skb holding the received data

.. _`ixgbe_fcoe_ddp.description`:

Description
-----------

This checks ddp status.

Returns : < 0 indicates an error or not a FCiE ddp, 0 indicates
not passing the skb to ULD, > 0 indicates is the length of data
being ddped.

.. _`ixgbe_fso`:

ixgbe_fso
=========

.. c:function:: int ixgbe_fso(struct ixgbe_ring *tx_ring, struct ixgbe_tx_buffer *first, u8 *hdr_len)

    ixgbe FCoE Sequence Offload (FSO)

    :param struct ixgbe_ring \*tx_ring:
        tx desc ring

    :param struct ixgbe_tx_buffer \*first:
        first tx_buffer structure containing skb, tx_flags, and protocol

    :param u8 \*hdr_len:
        hdr_len to be returned

.. _`ixgbe_fso.description`:

Description
-----------

This sets up large send offload for FCoE

Returns : 0 indicates success, < 0 for error

.. _`ixgbe_configure_fcoe`:

ixgbe_configure_fcoe
====================

.. c:function:: void ixgbe_configure_fcoe(struct ixgbe_adapter *adapter)

    configures registers for fcoe at start

    :param struct ixgbe_adapter \*adapter:
        ptr to ixgbe adapter

.. _`ixgbe_configure_fcoe.description`:

Description
-----------

This sets up FCoE related registers

Returns : none

.. _`ixgbe_free_fcoe_ddp_resources`:

ixgbe_free_fcoe_ddp_resources
=============================

.. c:function:: void ixgbe_free_fcoe_ddp_resources(struct ixgbe_adapter *adapter)

    release all fcoe ddp context resources

    :param struct ixgbe_adapter \*adapter:
        ixgbe adapter

.. _`ixgbe_free_fcoe_ddp_resources.description`:

Description
-----------

Cleans up outstanding ddp context resources

Returns : none

.. _`ixgbe_setup_fcoe_ddp_resources`:

ixgbe_setup_fcoe_ddp_resources
==============================

.. c:function:: int ixgbe_setup_fcoe_ddp_resources(struct ixgbe_adapter *adapter)

    setup all fcoe ddp context resources

    :param struct ixgbe_adapter \*adapter:
        ixgbe adapter

.. _`ixgbe_setup_fcoe_ddp_resources.description`:

Description
-----------

Sets up ddp context resouces

Returns : 0 indicates success or -EINVAL on failure

.. _`ixgbe_fcoe_enable`:

ixgbe_fcoe_enable
=================

.. c:function:: int ixgbe_fcoe_enable(struct net_device *netdev)

    turn on FCoE offload feature

    :param struct net_device \*netdev:
        the corresponding netdev

.. _`ixgbe_fcoe_enable.description`:

Description
-----------

Turns on FCoE offload feature in 82599.

Returns : 0 indicates success or -EINVAL on failure

.. _`ixgbe_fcoe_disable`:

ixgbe_fcoe_disable
==================

.. c:function:: int ixgbe_fcoe_disable(struct net_device *netdev)

    turn off FCoE offload feature

    :param struct net_device \*netdev:
        the corresponding netdev

.. _`ixgbe_fcoe_disable.description`:

Description
-----------

Turns off FCoE offload feature in 82599.

Returns : 0 indicates success or -EINVAL on failure

.. _`ixgbe_fcoe_get_wwn`:

ixgbe_fcoe_get_wwn
==================

.. c:function:: int ixgbe_fcoe_get_wwn(struct net_device *netdev, u64 *wwn, int type)

    get world wide name for the node or the port

    :param struct net_device \*netdev:
        ixgbe adapter

    :param u64 \*wwn:
        the world wide name

    :param int type:
        the type of world wide name

.. _`ixgbe_fcoe_get_wwn.description`:

Description
-----------

Returns the node or port world wide name if both the prefix and the san
mac address are valid, then the wwn is formed based on the NAA-2 for
IEEE Extended name identifier (ref. to T10 FC-LS Spec., Sec. 15.3).

Returns : 0 on success

.. _`ixgbe_fcoe_get_hbainfo`:

ixgbe_fcoe_get_hbainfo
======================

.. c:function:: int ixgbe_fcoe_get_hbainfo(struct net_device *netdev, struct netdev_fcoe_hbainfo *info)

    get FCoE HBA information

    :param struct net_device \*netdev:
        ixgbe adapter

    :param struct netdev_fcoe_hbainfo \*info:
        HBA information

.. _`ixgbe_fcoe_get_hbainfo.description`:

Description
-----------

Returns ixgbe HBA information

Returns : 0 on success

.. _`ixgbe_fcoe_get_tc`:

ixgbe_fcoe_get_tc
=================

.. c:function:: u8 ixgbe_fcoe_get_tc(struct ixgbe_adapter *adapter)

    get the current TC that fcoe is mapped to \ ``adapter``\  - pointer to the device adapter structure

    :param struct ixgbe_adapter \*adapter:
        *undescribed*

.. _`ixgbe_fcoe_get_tc.description`:

Description
-----------

Return : TC that FCoE is mapped to

.. This file was automatic generated / don't edit.

