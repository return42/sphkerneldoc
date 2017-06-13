.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40evf/i40evf_client.c

.. _`i40evf_notify_client_message`:

i40evf_notify_client_message
============================

.. c:function:: void i40evf_notify_client_message(struct i40e_vsi *vsi, u8 *msg, u16 len)

    call the client message receive callback

    :param struct i40e_vsi \*vsi:
        the VSI associated with this client

    :param u8 \*msg:
        message buffer

    :param u16 len:
        length of message

.. _`i40evf_notify_client_message.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`i40evf_notify_client_l2_params`:

i40evf_notify_client_l2_params
==============================

.. c:function:: void i40evf_notify_client_l2_params(struct i40e_vsi *vsi)

    call the client notify callback

    :param struct i40e_vsi \*vsi:
        the VSI with l2 param changes

.. _`i40evf_notify_client_l2_params.description`:

Description
-----------

If there is a client to this VSI, call the client

.. _`i40evf_notify_client_open`:

i40evf_notify_client_open
=========================

.. c:function:: void i40evf_notify_client_open(struct i40e_vsi *vsi)

    call the client open callback

    :param struct i40e_vsi \*vsi:
        the VSI with netdev opened

.. _`i40evf_notify_client_open.description`:

Description
-----------

If there is a client to this netdev, call the client with open

.. _`i40evf_client_release_qvlist`:

i40evf_client_release_qvlist
============================

.. c:function:: int i40evf_client_release_qvlist(struct i40e_info *ldev)

    send a message to the PF to release iwarp qv map

    :param struct i40e_info \*ldev:
        pointer to L2 context.

.. _`i40evf_client_release_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40evf_notify_client_close`:

i40evf_notify_client_close
==========================

.. c:function:: void i40evf_notify_client_close(struct i40e_vsi *vsi, bool reset)

    call the client close callback

    :param struct i40e_vsi \*vsi:
        the VSI with netdev closed

    :param bool reset:
        true when close called due to reset pending

.. _`i40evf_notify_client_close.description`:

Description
-----------

If there is a client to this netdev, call the client with close

.. _`i40evf_client_add_instance`:

i40evf_client_add_instance
==========================

.. c:function:: struct i40e_client_instance *i40evf_client_add_instance(struct i40evf_adapter *adapter)

    add a client instance to the instance list

    :param struct i40evf_adapter \*adapter:
        pointer to the board struct

.. _`i40evf_client_add_instance.description`:

Description
-----------

Returns cinst ptr on success, NULL on failure

.. _`i40evf_client_del_instance`:

i40evf_client_del_instance
==========================

.. c:function:: void i40evf_client_del_instance(struct i40evf_adapter *adapter)

    removes a client instance from the list

    :param struct i40evf_adapter \*adapter:
        pointer to the board struct

.. _`i40evf_client_subtask`:

i40evf_client_subtask
=====================

.. c:function:: void i40evf_client_subtask(struct i40evf_adapter *adapter)

    client maintenance work

    :param struct i40evf_adapter \*adapter:
        board private structure

.. _`i40evf_lan_add_device`:

i40evf_lan_add_device
=====================

.. c:function:: int i40evf_lan_add_device(struct i40evf_adapter *adapter)

    add a lan device struct to the list of lan devices

    :param struct i40evf_adapter \*adapter:
        pointer to the board struct

.. _`i40evf_lan_add_device.description`:

Description
-----------

Returns 0 on success or none 0 on error

.. _`i40evf_lan_del_device`:

i40evf_lan_del_device
=====================

.. c:function:: int i40evf_lan_del_device(struct i40evf_adapter *adapter)

    removes a lan device from the device list

    :param struct i40evf_adapter \*adapter:
        pointer to the board struct

.. _`i40evf_lan_del_device.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40evf_client_release`:

i40evf_client_release
=====================

.. c:function:: void i40evf_client_release(struct i40e_client *client)

    release client specific resources

    :param struct i40e_client \*client:
        pointer to the registered client

.. _`i40evf_client_prepare`:

i40evf_client_prepare
=====================

.. c:function:: void i40evf_client_prepare(struct i40e_client *client)

    prepare client specific resources

    :param struct i40e_client \*client:
        pointer to the registered client

.. _`i40evf_client_virtchnl_send`:

i40evf_client_virtchnl_send
===========================

.. c:function:: u32 i40evf_client_virtchnl_send(struct i40e_info *ldev, struct i40e_client *client, u8 *msg, u16 len)

    send a message to the PF instance

    :param struct i40e_info \*ldev:
        pointer to L2 context.

    :param struct i40e_client \*client:
        Client pointer.

    :param u8 \*msg:
        pointer to message buffer

    :param u16 len:
        message length

.. _`i40evf_client_virtchnl_send.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40evf_client_setup_qvlist`:

i40evf_client_setup_qvlist
==========================

.. c:function:: int i40evf_client_setup_qvlist(struct i40e_info *ldev, struct i40e_client *client, struct i40e_qvlist_info *qvlist_info)

    send a message to the PF to setup iwarp qv map

    :param struct i40e_info \*ldev:
        pointer to L2 context.

    :param struct i40e_client \*client:
        Client pointer.

    :param struct i40e_qvlist_info \*qvlist_info:
        *undescribed*

.. _`i40evf_client_setup_qvlist.description`:

Description
-----------

Return 0 on success or < 0 on error

.. _`i40evf_register_client`:

i40evf_register_client
======================

.. c:function:: int i40evf_register_client(struct i40e_client *client)

    Register a i40e client driver with the L2 driver

    :param struct i40e_client \*client:
        pointer to the i40e_client struct

.. _`i40evf_register_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. _`i40evf_unregister_client`:

i40evf_unregister_client
========================

.. c:function:: int i40evf_unregister_client(struct i40e_client *client)

    Unregister a i40e client driver with the L2 driver

    :param struct i40e_client \*client:
        pointer to the i40e_client struct

.. _`i40evf_unregister_client.description`:

Description
-----------

Returns 0 on success or non-0 on error

.. This file was automatic generated / don't edit.

