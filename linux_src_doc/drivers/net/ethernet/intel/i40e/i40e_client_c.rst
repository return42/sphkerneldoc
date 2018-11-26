.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_client.c

.. _`i40e_client_get_params`:

i40e_client_get_params
======================

.. c:function:: int i40e_client_get_params(struct i40e_vsi *vsi, struct i40e_params *params)

    Get the params that can change at runtime

    :param vsi:
        the VSI with the message
    :type vsi: struct i40e_vsi \*

    :param params:
        client param struct
    :type params: struct i40e_params \*

.. _`i40e_notify_client_of_vf_msg`:

i40e_notify_client_of_vf_msg
============================

.. c:function:: void i40e_notify_client_of_vf_msg(struct i40e_vsi *vsi, u32 vf_id, u8 *msg, u16 len)

    call the client vf message callback

    :param vsi:
        the VSI with the message
    :type vsi: struct i40e_vsi \*

    :param vf_id:
        the absolute VF id that sent the message
    :type vf_id: u32

    :param msg:
        message buffer
    :type msg: u8 \*

    :param len:
        length of the message
    :type len: u16

.. _`i40e_notify_client_of_vf_msg.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`i40e_notify_client_of_l2_param_changes`:

i40e_notify_client_of_l2_param_changes
======================================

.. c:function:: void i40e_notify_client_of_l2_param_changes(struct i40e_vsi *vsi)

    call the client notify callback

    :param vsi:
        the VSI with l2 param changes
    :type vsi: struct i40e_vsi \*

.. _`i40e_notify_client_of_l2_param_changes.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`i40e_client_release_qvlist`:

i40e_client_release_qvlist
==========================

.. c:function:: void i40e_client_release_qvlist(struct i40e_info *ldev)

    release MSI-X vector mapping for client

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

.. _`i40e_notify_client_of_netdev_close`:

i40e_notify_client_of_netdev_close
==================================

.. c:function:: void i40e_notify_client_of_netdev_close(struct i40e_vsi *vsi, bool reset)

    call the client close callback

    :param vsi:
        the VSI with netdev closed
    :type vsi: struct i40e_vsi \*

    :param reset:
        true when close called due to a reset pending
    :type reset: bool

.. _`i40e_notify_client_of_netdev_close.description`:

Description
-----------

If there is a client to this netdev, call the client with close

.. _`i40e_notify_client_of_vf_reset`:

i40e_notify_client_of_vf_reset
==============================

.. c:function:: void i40e_notify_client_of_vf_reset(struct i40e_pf *pf, u32 vf_id)

    call the client vf reset callback

    :param pf:
        PF device pointer
    :type pf: struct i40e_pf \*

    :param vf_id:
        asolute id of VF being reset
    :type vf_id: u32

.. _`i40e_notify_client_of_vf_reset.description`:

Description
-----------

If there is a client attached to this PF, notify when a VF is reset

.. _`i40e_notify_client_of_vf_enable`:

i40e_notify_client_of_vf_enable
===============================

.. c:function:: void i40e_notify_client_of_vf_enable(struct i40e_pf *pf, u32 num_vfs)

    call the client vf notification callback

    :param pf:
        PF device pointer
    :type pf: struct i40e_pf \*

    :param num_vfs:
        the number of VFs currently enabled, 0 for disable
    :type num_vfs: u32

.. _`i40e_notify_client_of_vf_enable.description`:

Description
-----------

If there is a client attached to this PF, call its VF notification routine

.. _`i40e_vf_client_capable`:

i40e_vf_client_capable
======================

.. c:function:: int i40e_vf_client_capable(struct i40e_pf *pf, u32 vf_id)

    ask the client if it likes the specified VF

    :param pf:
        PF device pointer
    :type pf: struct i40e_pf \*

    :param vf_id:
        the VF in question
    :type vf_id: u32

.. _`i40e_vf_client_capable.description`:

Description
-----------

If there is a client of the specified type attached to this PF, call
its vf_capable routine

.. _`i40e_client_add_instance`:

i40e_client_add_instance
========================

.. c:function:: void i40e_client_add_instance(struct i40e_pf *pf)

    add a client instance struct to the instance list

    :param pf:
        pointer to the board struct
    :type pf: struct i40e_pf \*

.. _`i40e_client_del_instance`:

i40e_client_del_instance
========================

.. c:function:: void i40e_client_del_instance(struct i40e_pf *pf)

    removes a client instance from the list

    :param pf:
        pointer to the board struct
    :type pf: struct i40e_pf \*

.. _`i40e_client_subtask`:

i40e_client_subtask
===================

.. c:function:: void i40e_client_subtask(struct i40e_pf *pf)

    client maintenance work

    :param pf:
        board private structure
    :type pf: struct i40e_pf \*

.. _`i40e_lan_add_device`:

i40e_lan_add_device
===================

.. c:function:: int i40e_lan_add_device(struct i40e_pf *pf)

    add a lan device struct to the list of lan devices

    :param pf:
        pointer to the board struct
    :type pf: struct i40e_pf \*

.. _`i40e_lan_add_device.description`:

Description
-----------

Returns 0 on success or none 0 on error

.. _`i40e_lan_del_device`:

i40e_lan_del_device
===================

.. c:function:: int i40e_lan_del_device(struct i40e_pf *pf)

    removes a lan device from the device list

    :param pf:
        pointer to the board struct
    :type pf: struct i40e_pf \*

.. _`i40e_lan_del_device.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40e_client_release`:

i40e_client_release
===================

.. c:function:: void i40e_client_release(struct i40e_client *client)

    release client specific resources

    :param client:
        pointer to the registered client
    :type client: struct i40e_client \*

.. _`i40e_client_prepare`:

i40e_client_prepare
===================

.. c:function:: void i40e_client_prepare(struct i40e_client *client)

    prepare client specific resources

    :param client:
        pointer to the registered client
    :type client: struct i40e_client \*

.. _`i40e_client_virtchnl_send`:

i40e_client_virtchnl_send
=========================

.. c:function:: int i40e_client_virtchnl_send(struct i40e_info *ldev, struct i40e_client *client, u32 vf_id, u8 *msg, u16 len)

    TBD

    :param ldev:
        pointer to L2 context
    :type ldev: struct i40e_info \*

    :param client:
        Client pointer
    :type client: struct i40e_client \*

    :param vf_id:
        absolute VF identifier
    :type vf_id: u32

    :param msg:
        message buffer
    :type msg: u8 \*

    :param len:
        length of message buffer
    :type len: u16

.. _`i40e_client_virtchnl_send.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_client_setup_qvlist`:

i40e_client_setup_qvlist
========================

.. c:function:: int i40e_client_setup_qvlist(struct i40e_info *ldev, struct i40e_client *client, struct i40e_qvlist_info *qvlist_info)

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

    :param client:
        Client pointer.
    :type client: struct i40e_client \*

    :param qvlist_info:
        queue and vector list
    :type qvlist_info: struct i40e_qvlist_info \*

.. _`i40e_client_setup_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_client_request_reset`:

i40e_client_request_reset
=========================

.. c:function:: void i40e_client_request_reset(struct i40e_info *ldev, struct i40e_client *client, u32 reset_level)

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

    :param client:
        Client pointer.
    :type client: struct i40e_client \*

    :param reset_level:
        reset level
    :type reset_level: u32

.. _`i40e_client_update_vsi_ctxt`:

i40e_client_update_vsi_ctxt
===========================

.. c:function:: int i40e_client_update_vsi_ctxt(struct i40e_info *ldev, struct i40e_client *client, bool is_vf, u32 vf_id, u32 flag, u32 valid_flag)

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

    :param client:
        Client pointer.
    :type client: struct i40e_client \*

    :param is_vf:
        if this for the VF
    :type is_vf: bool

    :param vf_id:
        if is_vf true this carries the vf_id
    :type vf_id: u32

    :param flag:
        Any device level setting that needs to be done for PE
    :type flag: u32

    :param valid_flag:
        Bits in this match up and enable changing of flag bits
    :type valid_flag: u32

.. _`i40e_client_update_vsi_ctxt.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_register_client`:

i40e_register_client
====================

.. c:function:: int i40e_register_client(struct i40e_client *client)

    Register a i40e client driver with the L2 driver

    :param client:
        pointer to the i40e_client struct
    :type client: struct i40e_client \*

.. _`i40e_register_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40e_unregister_client`:

i40e_unregister_client
======================

.. c:function:: int i40e_unregister_client(struct i40e_client *client)

    Unregister a i40e client driver with the L2 driver

    :param client:
        pointer to the i40e_client struct
    :type client: struct i40e_client \*

.. _`i40e_unregister_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. This file was automatic generated / don't edit.

