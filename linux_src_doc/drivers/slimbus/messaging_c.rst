.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/slimbus/messaging.c

.. _`slim_msg_response`:

slim_msg_response
=================

.. c:function:: void slim_msg_response(struct slim_controller *ctrl, u8 *reply, u8 tid, u8 len)

    Deliver Message response received from a device to the framework.

    :param ctrl:
        Controller handle
    :type ctrl: struct slim_controller \*

    :param reply:
        Reply received from the device
    :type reply: u8 \*

    :param tid:
        Transaction ID received with which framework can associate reply.
    :type tid: u8

    :param len:
        Length of the reply
    :type len: u8

.. _`slim_msg_response.description`:

Description
-----------

Called by controller to inform framework about the response received.
This helps in making the API asynchronous, and controller-driver doesn't need
to manage 1 more table other than the one managed by framework mapping TID
with buffers

.. _`slim_alloc_txn_tid`:

slim_alloc_txn_tid
==================

.. c:function:: int slim_alloc_txn_tid(struct slim_controller *ctrl, struct slim_msg_txn *txn)

    Allocate a tid to txn

    :param ctrl:
        Controller handle
    :type ctrl: struct slim_controller \*

    :param txn:
        transaction to be allocated with tid.
    :type txn: struct slim_msg_txn \*

.. _`slim_alloc_txn_tid.return`:

Return
------

zero on success with valid txn->tid and error code on failures.

.. _`slim_free_txn_tid`:

slim_free_txn_tid
=================

.. c:function:: void slim_free_txn_tid(struct slim_controller *ctrl, struct slim_msg_txn *txn)

    Freee tid of txn

    :param ctrl:
        Controller handle
    :type ctrl: struct slim_controller \*

    :param txn:
        transaction whose tid should be freed
    :type txn: struct slim_msg_txn \*

.. _`slim_do_transfer`:

slim_do_transfer
================

.. c:function:: int slim_do_transfer(struct slim_controller *ctrl, struct slim_msg_txn *txn)

    Process a SLIMbus-messaging transaction

    :param ctrl:
        Controller handle
    :type ctrl: struct slim_controller \*

    :param txn:
        Transaction to be sent over SLIMbus
    :type txn: struct slim_msg_txn \*

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

    :param sbdev:
        slim device to which this msg has to be transfered
    :type sbdev: struct slim_device \*

    :param msg:
        value info message pointer
    :type msg: struct slim_val_inf \*

    :param mc:
        message code of the message
    :type mc: u8

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

    :param sdev:
        client handle.
    :type sdev: struct slim_device \*

    :param addr:
        address of value element to read.
    :type addr: u32

    :param count:
        number of bytes to read. Maximum bytes allowed are 16.
    :type count: size_t

    :param val:
        will return what the value element value was
    :type val: u8 \*

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

    :param sdev:
        client handle.
    :type sdev: struct slim_device \*

    :param addr:
        address in the value element to read.
    :type addr: u32

.. _`slim_readb.return`:

Return
------

byte value of value element.

.. _`slim_write`:

slim_write
==========

.. c:function:: int slim_write(struct slim_device *sdev, u32 addr, size_t count, u8 *val)

    Write SLIMbus value element

    :param sdev:
        client handle.
    :type sdev: struct slim_device \*

    :param addr:
        address in the value element to write.
    :type addr: u32

    :param count:
        number of bytes to write. Maximum bytes allowed are 16.
    :type count: size_t

    :param val:
        value to write to value element
    :type val: u8 \*

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

    :param sdev:
        client handle.
    :type sdev: struct slim_device \*

    :param addr:
        address of value element to write.
    :type addr: u32

    :param value:
        value to write to value element
    :type value: u8

.. _`slim_writeb.return`:

Return
------

-EINVAL for Invalid parameters, -ETIMEDOUT If transmission of
this message timed out (e.g. due to bus lines not being clocked
or driven by controller)

.. This file was automatic generated / don't edit.

