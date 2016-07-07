.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ntb/ntb_transport.c

.. _`ntb_transport_unregister_client_dev`:

ntb_transport_unregister_client_dev
===================================

.. c:function:: void ntb_transport_unregister_client_dev(char *device_name)

    Unregister NTB client device

    :param char \*device_name:
        Name of NTB client device

.. _`ntb_transport_unregister_client_dev.description`:

Description
-----------

Unregister an NTB client device with the NTB transport layer

.. _`ntb_transport_register_client_dev`:

ntb_transport_register_client_dev
=================================

.. c:function:: int ntb_transport_register_client_dev(char *device_name)

    Register NTB client device

    :param char \*device_name:
        Name of NTB client device

.. _`ntb_transport_register_client_dev.description`:

Description
-----------

Register an NTB client device with the NTB transport layer

.. _`ntb_transport_register_client`:

ntb_transport_register_client
=============================

.. c:function:: int ntb_transport_register_client(struct ntb_transport_client *drv)

    Register NTB client driver

    :param struct ntb_transport_client \*drv:
        NTB client driver to be registered

.. _`ntb_transport_register_client.description`:

Description
-----------

Register an NTB client driver with the NTB transport layer

.. _`ntb_transport_register_client.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`ntb_transport_unregister_client`:

ntb_transport_unregister_client
===============================

.. c:function:: void ntb_transport_unregister_client(struct ntb_transport_client *drv)

    Unregister NTB client driver

    :param struct ntb_transport_client \*drv:
        NTB client driver to be unregistered

.. _`ntb_transport_unregister_client.description`:

Description
-----------

Unregister an NTB client driver with the NTB transport layer

.. _`ntb_transport_unregister_client.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`ntb_transport_create_queue`:

ntb_transport_create_queue
==========================

.. c:function:: struct ntb_transport_qp *ntb_transport_create_queue(void *data, struct device *client_dev, const struct ntb_queue_handlers *handlers)

    Create a new NTB transport layer queue

    :param void \*data:
        *undescribed*

    :param struct device \*client_dev:
        *undescribed*

    :param const struct ntb_queue_handlers \*handlers:
        *undescribed*

.. _`ntb_transport_create_queue.description`:

Description
-----------

Create a new NTB transport layer queue and provide the queue with a callback
routine for both transmit and receive.  The receive callback routine will be
used to pass up data when the transport has received it on the queue.   The
transmit callback routine will be called when the transport has completed the
transmission of the data on the queue and the data is ready to be freed.

.. _`ntb_transport_create_queue.return`:

Return
------

pointer to newly created ntb_queue, NULL on error.

.. _`ntb_transport_free_queue`:

ntb_transport_free_queue
========================

.. c:function:: void ntb_transport_free_queue(struct ntb_transport_qp *qp)

    Frees NTB transport queue

    :param struct ntb_transport_qp \*qp:
        NTB queue to be freed

.. _`ntb_transport_free_queue.description`:

Description
-----------

Frees NTB transport queue

.. _`ntb_transport_rx_remove`:

ntb_transport_rx_remove
=======================

.. c:function:: void *ntb_transport_rx_remove(struct ntb_transport_qp *qp, unsigned int *len)

    Dequeues enqueued rx packet

    :param struct ntb_transport_qp \*qp:
        NTB queue to be freed

    :param unsigned int \*len:
        pointer to variable to write enqueued buffers length

.. _`ntb_transport_rx_remove.description`:

Description
-----------

Dequeues unused buffers from receive queue.  Should only be used during
shutdown of qp.

.. _`ntb_transport_rx_remove.return`:

Return
------

NULL error value on error, or void\* for success.

.. _`ntb_transport_rx_enqueue`:

ntb_transport_rx_enqueue
========================

.. c:function:: int ntb_transport_rx_enqueue(struct ntb_transport_qp *qp, void *cb, void *data, unsigned int len)

    Enqueue a new NTB queue entry

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue the entry is to be enqueued on

    :param void \*cb:
        per buffer pointer for callback function to use

    :param void \*data:
        pointer to data buffer that incoming packets will be copied into

    :param unsigned int len:
        length of the data buffer

.. _`ntb_transport_rx_enqueue.description`:

Description
-----------

Enqueue a new receive buffer onto the transport queue into which a NTB
payload can be received into.

.. _`ntb_transport_rx_enqueue.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`ntb_transport_tx_enqueue`:

ntb_transport_tx_enqueue
========================

.. c:function:: int ntb_transport_tx_enqueue(struct ntb_transport_qp *qp, void *cb, void *data, unsigned int len)

    Enqueue a new NTB queue entry

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue the entry is to be enqueued on

    :param void \*cb:
        per buffer pointer for callback function to use

    :param void \*data:
        pointer to data buffer that will be sent

    :param unsigned int len:
        length of the data buffer

.. _`ntb_transport_tx_enqueue.description`:

Description
-----------

Enqueue a new transmit buffer onto the transport queue from which a NTB
payload will be transmitted.  This assumes that a lock is being held to
serialize access to the qp.

.. _`ntb_transport_tx_enqueue.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`ntb_transport_link_up`:

ntb_transport_link_up
=====================

.. c:function:: void ntb_transport_link_up(struct ntb_transport_qp *qp)

    Notify NTB transport of client readiness to use queue

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue to be enabled

.. _`ntb_transport_link_up.description`:

Description
-----------

Notify NTB transport layer of client readiness to use queue

.. _`ntb_transport_link_down`:

ntb_transport_link_down
=======================

.. c:function:: void ntb_transport_link_down(struct ntb_transport_qp *qp)

    Notify NTB transport to no longer enqueue data

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue to be disabled

.. _`ntb_transport_link_down.description`:

Description
-----------

Notify NTB transport layer of client's desire to no longer receive data on
transport queue specified.  It is the client's responsibility to ensure all
entries on queue are purged or otherwise handled appropriately.

.. _`ntb_transport_link_query`:

ntb_transport_link_query
========================

.. c:function:: bool ntb_transport_link_query(struct ntb_transport_qp *qp)

    Query transport link state

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue to be queried

.. _`ntb_transport_link_query.description`:

Description
-----------

Query connectivity to the remote system of the NTB transport queue

.. _`ntb_transport_link_query.return`:

Return
------

true for link up or false for link down

.. _`ntb_transport_qp_num`:

ntb_transport_qp_num
====================

.. c:function:: unsigned char ntb_transport_qp_num(struct ntb_transport_qp *qp)

    Query the qp number

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue to be queried

.. _`ntb_transport_qp_num.description`:

Description
-----------

Query qp number of the NTB transport queue

.. _`ntb_transport_qp_num.return`:

Return
------

a zero based number specifying the qp number

.. _`ntb_transport_max_size`:

ntb_transport_max_size
======================

.. c:function:: unsigned int ntb_transport_max_size(struct ntb_transport_qp *qp)

    Query the max payload size of a qp

    :param struct ntb_transport_qp \*qp:
        NTB transport layer queue to be queried

.. _`ntb_transport_max_size.description`:

Description
-----------

Query the maximum payload size permissible on the given qp

.. _`ntb_transport_max_size.return`:

Return
------

the max payload size of a qp

.. This file was automatic generated / don't edit.

