.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/slimbus/messaging.c

.. _`slim_msg_response`:

slim_msg_response
=================

.. c:function:: void slim_msg_response(struct slim_controller *ctrl, u8 *reply, u8 tid, u8 len)

    Deliver Message response received from a device to the framework.

    :param struct slim_controller \*ctrl:
        Controller handle

    :param u8 \*reply:
        Reply received from the device

    :param u8 tid:
        Transaction ID received with which framework can associate reply.

    :param u8 len:
        Length of the reply

.. _`slim_msg_response.description`:

Description
-----------

Called by controller to inform framework about the response received.
This helps in making the API asynchronous, and controller-driver doesn't need
to manage 1 more table other than the one managed by framework mapping TID
with buffers

.. _`slim_do_transfer`:

slim_do_transfer
================

.. c:function:: int slim_do_transfer(struct slim_controller *ctrl, struct slim_msg_txn *txn)

    Process a SLIMbus-messaging transaction

    :param struct slim_controller \*ctrl:
        Controller handle

    :param struct slim_msg_txn \*txn:
        Transaction to be sent over SLIMbus

.. _`slim_do_transfer.description`:

Description
-----------

Called by controller to transmit messaging transactions not dealing with
Interface/Value elements. (e.g. transmittting a message to assign logical
address to a slave device

.. _`slim_do_transfer.return`:

Return
------

-ETIMEDOUT: If transmission of this message timed out
     (e.g. due to bus lines not being clocked or driven by controller)

.. _`slim_xfer_msg`:

slim_xfer_msg
=============

.. c:function:: int slim_xfer_msg(struct slim_device *sbdev, struct slim_val_inf *msg, u8 mc)

    Transfer a value info message on slim device

    :param struct slim_device \*sbdev:
        slim device to which this msg has to be transfered

    :param struct slim_val_inf \*msg:
        value info message pointer

    :param u8 mc:
        message code of the message

.. _`slim_xfer_msg.description`:

Description
-----------

Called by drivers which want to transfer a vlaue or info elements.

.. _`slim_xfer_msg.return`:

Return
------

-ETIMEDOUT: If transmission of this message timed out

.. _`slim_read`:

slim_read
=========

.. c:function:: int slim_read(struct slim_device *sdev, u32 addr, size_t count, u8 *val)

    Read SLIMbus value element

    :param struct slim_device \*sdev:
        client handle.

    :param u32 addr:
        address of value element to read.

    :param size_t count:
        number of bytes to read. Maximum bytes allowed are 16.

    :param u8 \*val:
        will return what the value element value was

.. _`slim_read.return`:

Return
------

-EINVAL for Invalid parameters, -ETIMEDOUT If transmission of
this message timed out (e.g. due to bus lines not being clocked
or driven by controller)

.. _`slim_readb`:

slim_readb
==========

.. c:function:: int slim_readb(struct slim_device *sdev, u32 addr)

    Read byte from SLIMbus value element

    :param struct slim_device \*sdev:
        client handle.

    :param u32 addr:
        address in the value element to read.

.. _`slim_readb.return`:

Return
------

byte value of value element.

.. _`slim_write`:

slim_write
==========

.. c:function:: int slim_write(struct slim_device *sdev, u32 addr, size_t count, u8 *val)

    Write SLIMbus value element

    :param struct slim_device \*sdev:
        client handle.

    :param u32 addr:
        address in the value element to write.

    :param size_t count:
        number of bytes to write. Maximum bytes allowed are 16.

    :param u8 \*val:
        value to write to value element

.. _`slim_write.return`:

Return
------

-EINVAL for Invalid parameters, -ETIMEDOUT If transmission of
this message timed out (e.g. due to bus lines not being clocked
or driven by controller)

.. _`slim_writeb`:

slim_writeb
===========

.. c:function:: int slim_writeb(struct slim_device *sdev, u32 addr, u8 value)

    Write byte to SLIMbus value element

    :param struct slim_device \*sdev:
        client handle.

    :param u32 addr:
        address of value element to write.

    :param u8 value:
        value to write to value element

.. _`slim_writeb.return`:

Return
------

-EINVAL for Invalid parameters, -ETIMEDOUT If transmission of
this message timed out (e.g. due to bus lines not being clocked
or driven by controller)

.. This file was automatic generated / don't edit.

