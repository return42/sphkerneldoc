.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb3/cxgb3_offload.c

.. _`cxgb3_register_client`:

cxgb3_register_client
=====================

.. c:function:: void cxgb3_register_client(struct cxgb3_client *client)

    register an offload client

    :param struct cxgb3_client \*client:
        the client

.. _`cxgb3_register_client.description`:

Description
-----------

Add the client to the client list,
and call backs the client for each activated offload device

.. _`cxgb3_unregister_client`:

cxgb3_unregister_client
=======================

.. c:function:: void cxgb3_unregister_client(struct cxgb3_client *client)

    unregister an offload client

    :param struct cxgb3_client \*client:
        the client

.. _`cxgb3_unregister_client.description`:

Description
-----------

Remove the client to the client list,
and call backs the client for each activated offload device.

.. _`cxgb3_add_clients`:

cxgb3_add_clients
=================

.. c:function:: void cxgb3_add_clients(struct t3cdev *tdev)

    activate registered clients for an offload device

    :param struct t3cdev \*tdev:
        the offload device

.. _`cxgb3_add_clients.description`:

Description
-----------

Call backs all registered clients once a offload device is activated

.. _`cxgb3_remove_clients`:

cxgb3_remove_clients
====================

.. c:function:: void cxgb3_remove_clients(struct t3cdev *tdev)

    deactivates registered clients for an offload device

    :param struct t3cdev \*tdev:
        the offload device

.. _`cxgb3_remove_clients.description`:

Description
-----------

Call backs all registered clients once a offload device is deactivated

.. This file was automatic generated / don't edit.

