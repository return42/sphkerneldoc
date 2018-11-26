.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_client.c

.. _`iavf_client_get_params`:

iavf_client_get_params
======================

.. c:function:: void iavf_client_get_params(struct iavf_vsi *vsi, struct i40e_params *params)

    retrieve relevant client parameters

    :param vsi:
        VSI with parameters
    :type vsi: struct iavf_vsi \*

    :param params:
        client param struct
    :type params: struct i40e_params \*

.. _`iavf_notify_client_message`:

iavf_notify_client_message
==========================

.. c:function:: void iavf_notify_client_message(struct iavf_vsi *vsi, u8 *msg, u16 len)

    call the client message receive callback

    :param vsi:
        the VSI associated with this client
    :type vsi: struct iavf_vsi \*

    :param msg:
        message buffer
    :type msg: u8 \*

    :param len:
        length of message
    :type len: u16

.. _`iavf_notify_client_message.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`iavf_notify_client_l2_params`:

iavf_notify_client_l2_params
============================

.. c:function:: void iavf_notify_client_l2_params(struct iavf_vsi *vsi)

    call the client notify callback

    :param vsi:
        the VSI with l2 param changes
    :type vsi: struct iavf_vsi \*

.. _`iavf_notify_client_l2_params.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`iavf_notify_client_open`:

iavf_notify_client_open
=======================

.. c:function:: void iavf_notify_client_open(struct iavf_vsi *vsi)

    call the client open callback

    :param vsi:
        the VSI with netdev opened
    :type vsi: struct iavf_vsi \*

.. _`iavf_notify_client_open.description`:

Description
-----------

If there is a client to this netdev, call the client with open

.. _`iavf_client_release_qvlist`:

iavf_client_release_qvlist
==========================

.. c:function:: int iavf_client_release_qvlist(struct i40e_info *ldev)

    send a message to the PF to release iwarp qv map

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

.. _`iavf_client_release_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`iavf_notify_client_close`:

iavf_notify_client_close
========================

.. c:function:: void iavf_notify_client_close(struct iavf_vsi *vsi, bool reset)

    call the client close callback

    :param vsi:
        the VSI with netdev closed
    :type vsi: struct iavf_vsi \*

    :param reset:
        true when close called due to reset pending
    :type reset: bool

.. _`iavf_notify_client_close.description`:

Description
-----------

If there is a client to this netdev, call the client with close

.. _`iavf_client_add_instance`:

iavf_client_add_instance
========================

.. c:function:: struct i40e_client_instance *iavf_client_add_instance(struct iavf_adapter *adapter)

    add a client instance to the instance list

    :param adapter:
        pointer to the board struct
    :type adapter: struct iavf_adapter \*

.. _`iavf_client_add_instance.description`:

Description
-----------

Returns cinst ptr on success, NULL on failure

.. _`iavf_client_del_instance`:

iavf_client_del_instance
========================

.. c:function:: void iavf_client_del_instance(struct iavf_adapter *adapter)

    removes a client instance from the list

    :param adapter:
        pointer to the board struct
    :type adapter: struct iavf_adapter \*

.. _`iavf_client_subtask`:

iavf_client_subtask
===================

.. c:function:: void iavf_client_subtask(struct iavf_adapter *adapter)

    client maintenance work

    :param adapter:
        board private structure
    :type adapter: struct iavf_adapter \*

.. _`iavf_lan_add_device`:

iavf_lan_add_device
===================

.. c:function:: int iavf_lan_add_device(struct iavf_adapter *adapter)

    add a lan device struct to the list of lan devices

    :param adapter:
        pointer to the board struct
    :type adapter: struct iavf_adapter \*

.. _`iavf_lan_add_device.description`:

Description
-----------

Returns 0 on success or none 0 on error

.. _`iavf_lan_del_device`:

iavf_lan_del_device
===================

.. c:function:: int iavf_lan_del_device(struct iavf_adapter *adapter)

    removes a lan device from the device list

    :param adapter:
        pointer to the board struct
    :type adapter: struct iavf_adapter \*

.. _`iavf_lan_del_device.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`iavf_client_release`:

iavf_client_release
===================

.. c:function:: void iavf_client_release(struct i40e_client *client)

    release client specific resources

    :param client:
        pointer to the registered client
    :type client: struct i40e_client \*

.. _`iavf_client_prepare`:

iavf_client_prepare
===================

.. c:function:: void iavf_client_prepare(struct i40e_client *client)

    prepare client specific resources

    :param client:
        pointer to the registered client
    :type client: struct i40e_client \*

.. _`iavf_client_virtchnl_send`:

iavf_client_virtchnl_send
=========================

.. c:function:: u32 iavf_client_virtchnl_send(struct i40e_info *ldev, struct i40e_client *client, u8 *msg, u16 len)

    send a message to the PF instance

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

    :param client:
        Client pointer.
    :type client: struct i40e_client \*

    :param msg:
        pointer to message buffer
    :type msg: u8 \*

    :param len:
        message length
    :type len: u16

.. _`iavf_client_virtchnl_send.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`iavf_client_setup_qvlist`:

iavf_client_setup_qvlist
========================

.. c:function:: int iavf_client_setup_qvlist(struct i40e_info *ldev, struct i40e_client *client, struct i40e_qvlist_info *qvlist_info)

    send a message to the PF to setup iwarp qv map

    :param ldev:
        pointer to L2 context.
    :type ldev: struct i40e_info \*

    :param client:
        Client pointer.
    :type client: struct i40e_client \*

    :param qvlist_info:
        queue and vector list
    :type qvlist_info: struct i40e_qvlist_info \*

.. _`iavf_client_setup_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`iavf_register_client`:

iavf_register_client
====================

.. c:function:: int iavf_register_client(struct i40e_client *client)

    Register a i40e client driver with the L2 driver

    :param client:
        pointer to the i40e_client struct
    :type client: struct i40e_client \*

.. _`iavf_register_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`iavf_unregister_client`:

iavf_unregister_client
======================

.. c:function:: int iavf_unregister_client(struct i40e_client *client)

    Unregister a i40e client driver with the L2 driver

    :param client:
        pointer to the i40e_client struct
    :type client: struct i40e_client \*

.. _`iavf_unregister_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. This file was automatic generated / don't edit.

