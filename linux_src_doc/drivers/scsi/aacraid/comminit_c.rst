.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/comminit.c

.. _`aac_send_shutdown`:

aac_send_shutdown
=================

.. c:function:: int aac_send_shutdown(struct aac_dev *dev)

    shutdown an adapter

    :param dev:
        Adapter to shutdown
    :type dev: struct aac_dev \*

.. _`aac_send_shutdown.description`:

Description
-----------

This routine will send a VM_CloseAll (shutdown) request to the adapter.

.. _`aac_comm_init`:

aac_comm_init
=============

.. c:function:: int aac_comm_init(struct aac_dev *dev)

    Initialise FSA data structures

    :param dev:
        Adapter to initialise
    :type dev: struct aac_dev \*

.. _`aac_comm_init.description`:

Description
-----------

Initializes the data structures that are required for the FSA commuication
interface to operate.
Returns
1 - if we were able to init the commuication interface.
0 - If there were errors initing. This is a fatal error.

.. This file was automatic generated / don't edit.

