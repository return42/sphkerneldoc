.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ccp/ccp-dev.c

.. _`ccp_add_device`:

ccp_add_device
==============

.. c:function:: void ccp_add_device(struct ccp_device *ccp)

    add a CCP device to the list

    :param struct ccp_device \*ccp:
        ccp_device struct pointer

.. _`ccp_add_device.description`:

Description
-----------

Put this CCP on the unit list, which makes it available
for use.

Returns zero if a CCP device is present, -ENODEV otherwise.

.. _`ccp_del_device`:

ccp_del_device
==============

.. c:function:: void ccp_del_device(struct ccp_device *ccp)

    remove a CCP device from the list

    :param struct ccp_device \*ccp:
        ccp_device struct pointer

.. _`ccp_del_device.description`:

Description
-----------

Remove this unit from the list of devices. If the next device
up for use is this one, adjust the pointer. If this is the last
device, NULL the pointer.

.. _`ccp_present`:

ccp_present
===========

.. c:function:: int ccp_present( void)

    check if a CCP device is present

    :param  void:
        no arguments

.. _`ccp_present.description`:

Description
-----------

Returns zero if a CCP device is present, -ENODEV otherwise.

.. _`ccp_version`:

ccp_version
===========

.. c:function:: unsigned int ccp_version( void)

    get the version of the CCP device

    :param  void:
        no arguments

.. _`ccp_version.description`:

Description
-----------

Returns the version from the first unit on the list;
otherwise a zero if no CCP device is present

.. _`ccp_enqueue_cmd`:

ccp_enqueue_cmd
===============

.. c:function:: int ccp_enqueue_cmd(struct ccp_cmd *cmd)

    queue an operation for processing by the CCP

    :param struct ccp_cmd \*cmd:
        ccp_cmd struct to be processed

.. _`ccp_enqueue_cmd.description`:

Description
-----------

Queue a cmd to be processed by the CCP. If queueing the cmd
would exceed the defined length of the cmd queue the cmd will
only be queued if the CCP_CMD_MAY_BACKLOG flag is set and will
result in a return code of -EBUSY.

The callback routine specified in the ccp_cmd struct will be
called to notify the caller of completion (if the cmd was not
backlogged) or advancement out of the backlog. If the cmd has
advanced out of the backlog the "err" value of the callback
will be -EINPROGRESS. Any other "err" value during callback is
the result of the operation.

.. _`ccp_enqueue_cmd.the-cmd-has-been-successfully-queued-if`:

The cmd has been successfully queued if
---------------------------------------

the return code is -EINPROGRESS or
the return code is -EBUSY and CCP_CMD_MAY_BACKLOG flag is set

.. _`ccp_cmd_queue_thread`:

ccp_cmd_queue_thread
====================

.. c:function:: int ccp_cmd_queue_thread(void *data)

    create a kernel thread to manage a CCP queue

    :param void \*data:
        thread-specific data

.. _`ccp_alloc_struct`:

ccp_alloc_struct
================

.. c:function:: struct ccp_device *ccp_alloc_struct(struct device *dev)

    allocate and initialize the ccp_device struct

    :param struct device \*dev:
        device struct of the CCP

.. This file was automatic generated / don't edit.

