.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_client.c

.. _`i40e_client_type_to_vsi_type`:

i40e_client_type_to_vsi_type
============================

.. c:function:: enum i40e_vsi_type i40e_client_type_to_vsi_type(enum i40e_client_type type)

    convert client type to vsi type

    :param enum i40e_client_type type:
        *undescribed*

.. _`i40e_client_type_to_vsi_type.description`:

Description
-----------

returns the related vsi type value

.. _`i40e_client_get_params`:

i40e_client_get_params
======================

.. c:function:: int i40e_client_get_params(struct i40e_vsi *vsi, struct i40e_params *params)

    Get the params that can change at runtime

    :param struct i40e_vsi \*vsi:
        the VSI with the message

    :param struct i40e_params \*params:
        *undescribed*

.. _`i40e_notify_client_of_vf_msg`:

i40e_notify_client_of_vf_msg
============================

.. c:function:: void i40e_notify_client_of_vf_msg(struct i40e_vsi *vsi, u32 vf_id, u8 *msg, u16 len)

    call the client vf message callback

    :param struct i40e_vsi \*vsi:
        the VSI with the message

    :param u32 vf_id:
        the absolute VF id that sent the message

    :param u8 \*msg:
        message buffer

    :param u16 len:
        length of the message

.. _`i40e_notify_client_of_vf_msg.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`i40e_notify_client_of_l2_param_changes`:

i40e_notify_client_of_l2_param_changes
======================================

.. c:function:: void i40e_notify_client_of_l2_param_changes(struct i40e_vsi *vsi)

    call the client notify callback

    :param struct i40e_vsi \*vsi:
        the VSI with l2 param changes

.. _`i40e_notify_client_of_l2_param_changes.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`i40e_notify_client_of_netdev_open`:

i40e_notify_client_of_netdev_open
=================================

.. c:function:: void i40e_notify_client_of_netdev_open(struct i40e_vsi *vsi)

    call the client open callback

    :param struct i40e_vsi \*vsi:
        the VSI with netdev opened

.. _`i40e_notify_client_of_netdev_open.description`:

Description
-----------

If there is a client to this netdev, call the client with open

.. _`i40e_client_release_qvlist`:

i40e_client_release_qvlist
==========================

.. c:function:: void i40e_client_release_qvlist(struct i40e_info *ldev)

    :param struct i40e_info \*ldev:
        pointer to L2 context.

.. _`i40e_notify_client_of_netdev_close`:

i40e_notify_client_of_netdev_close
==================================

.. c:function:: void i40e_notify_client_of_netdev_close(struct i40e_vsi *vsi, bool reset)

    call the client close callback

    :param struct i40e_vsi \*vsi:
        the VSI with netdev closed

    :param bool reset:
        true when close called due to a reset pending

.. _`i40e_notify_client_of_netdev_close.description`:

Description
-----------

If there is a client to this netdev, call the client with close

.. _`i40e_notify_client_of_vf_reset`:

i40e_notify_client_of_vf_reset
==============================

.. c:function:: void i40e_notify_client_of_vf_reset(struct i40e_pf *pf, u32 vf_id)

    call the client vf reset callback

    :param struct i40e_pf \*pf:
        PF device pointer

    :param u32 vf_id:
        asolute id of VF being reset

.. _`i40e_notify_client_of_vf_reset.description`:

Description
-----------

If there is a client attached to this PF, notify when a VF is reset

.. _`i40e_notify_client_of_vf_enable`:

i40e_notify_client_of_vf_enable
===============================

.. c:function:: void i40e_notify_client_of_vf_enable(struct i40e_pf *pf, u32 num_vfs)

    call the client vf notification callback

    :param struct i40e_pf \*pf:
        PF device pointer

    :param u32 num_vfs:
        the number of VFs currently enabled, 0 for disable

.. _`i40e_notify_client_of_vf_enable.description`:

Description
-----------

If there is a client attached to this PF, call its VF notification routine

.. _`i40e_vf_client_capable`:

i40e_vf_client_capable
======================

.. c:function:: int i40e_vf_client_capable(struct i40e_pf *pf, u32 vf_id, enum i40e_client_type type)

    ask the client if it likes the specified VF

    :param struct i40e_pf \*pf:
        PF device pointer

    :param u32 vf_id:
        the VF in question

    :param enum i40e_client_type type:
        *undescribed*

.. _`i40e_vf_client_capable.description`:

Description
-----------

If there is a client of the specified type attached to this PF, call
its vf_capable routine

.. _`i40e_client_add_instance`:

i40e_client_add_instance
========================

.. c:function:: struct i40e_client_instance *i40e_client_add_instance(struct i40e_pf *pf, struct i40e_client *client, bool *existing)

    add a client instance struct to the instance list

    :param struct i40e_pf \*pf:
        pointer to the board struct

    :param struct i40e_client \*client:
        pointer to a client struct in the client list.

    :param bool \*existing:
        if there was already an existing instance

.. _`i40e_client_add_instance.description`:

Description
-----------

Returns cdev ptr on success or if already exists, NULL on failure

.. _`i40e_client_del_instance`:

i40e_client_del_instance
========================

.. c:function:: int i40e_client_del_instance(struct i40e_pf *pf, struct i40e_client *client)

    removes a client instance from the list

    :param struct i40e_pf \*pf:
        pointer to the board struct

    :param struct i40e_client \*client:
        *undescribed*

.. _`i40e_client_del_instance.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40e_client_subtask`:

i40e_client_subtask
===================

.. c:function:: void i40e_client_subtask(struct i40e_pf *pf)

    client maintenance work

    :param struct i40e_pf \*pf:
        board private structure

.. _`i40e_lan_add_device`:

i40e_lan_add_device
===================

.. c:function:: int i40e_lan_add_device(struct i40e_pf *pf)

    add a lan device struct to the list of lan devices

    :param struct i40e_pf \*pf:
        pointer to the board struct

.. _`i40e_lan_add_device.description`:

Description
-----------

Returns 0 on success or none 0 on error

.. _`i40e_lan_del_device`:

i40e_lan_del_device
===================

.. c:function:: int i40e_lan_del_device(struct i40e_pf *pf)

    removes a lan device from the device list

    :param struct i40e_pf \*pf:
        pointer to the board struct

.. _`i40e_lan_del_device.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40e_client_release`:

i40e_client_release
===================

.. c:function:: int i40e_client_release(struct i40e_client *client)

    release client specific resources

    :param struct i40e_client \*client:
        pointer to the registered client

.. _`i40e_client_release.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_client_prepare`:

i40e_client_prepare
===================

.. c:function:: int i40e_client_prepare(struct i40e_client *client)

    prepare client specific resources

    :param struct i40e_client \*client:
        pointer to the registered client

.. _`i40e_client_prepare.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_client_virtchnl_send`:

i40e_client_virtchnl_send
=========================

.. c:function:: int i40e_client_virtchnl_send(struct i40e_info *ldev, struct i40e_client *client, u32 vf_id, u8 *msg, u16 len)

    TBD

    :param struct i40e_info \*ldev:
        pointer to L2 context

    :param struct i40e_client \*client:
        Client pointer

    :param u32 vf_id:
        absolute VF identifier

    :param u8 \*msg:
        message buffer

    :param u16 len:
        length of message buffer

.. _`i40e_client_virtchnl_send.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_client_setup_qvlist`:

i40e_client_setup_qvlist
========================

.. c:function:: int i40e_client_setup_qvlist(struct i40e_info *ldev, struct i40e_client *client, struct i40e_qvlist_info *qvlist_info)

    :param struct i40e_info \*ldev:
        pointer to L2 context.

    :param struct i40e_client \*client:
        Client pointer.

    :param struct i40e_qvlist_info \*qvlist_info:
        *undescribed*

.. _`i40e_client_setup_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_client_request_reset`:

i40e_client_request_reset
=========================

.. c:function:: void i40e_client_request_reset(struct i40e_info *ldev, struct i40e_client *client, u32 reset_level)

    :param struct i40e_info \*ldev:
        pointer to L2 context.

    :param struct i40e_client \*client:
        Client pointer.

    :param u32 reset_level:
        *undescribed*

.. _`i40e_client_update_vsi_ctxt`:

i40e_client_update_vsi_ctxt
===========================

.. c:function:: int i40e_client_update_vsi_ctxt(struct i40e_info *ldev, struct i40e_client *client, bool is_vf, u32 vf_id, u32 flag, u32 valid_flag)

    :param struct i40e_info \*ldev:
        pointer to L2 context.

    :param struct i40e_client \*client:
        Client pointer.

    :param bool is_vf:
        if this for the VF

    :param u32 vf_id:
        if is_vf true this carries the vf_id

    :param u32 flag:
        Any device level setting that needs to be done for PE

    :param u32 valid_flag:
        Bits in this match up and enable changing of flag bits

.. _`i40e_client_update_vsi_ctxt.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40e_register_client`:

i40e_register_client
====================

.. c:function:: int i40e_register_client(struct i40e_client *client)

    Register a i40e client driver with the L2 driver

    :param struct i40e_client \*client:
        pointer to the i40e_client struct

.. _`i40e_register_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40e_unregister_client`:

i40e_unregister_client
======================

.. c:function:: int i40e_unregister_client(struct i40e_client *client)

    Unregister a i40e client driver with the L2 driver

    :param struct i40e_client \*client:
        pointer to the i40e_client struct

.. _`i40e_unregister_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. This file was automatic generated / don't edit.

