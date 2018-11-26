.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/dln2.h

.. _`dln2_event_cb_t`:

dln2_event_cb_t
===============

.. c:function:: void dln2_event_cb_t(struct platform_device *pdev, u16 echo, const void *data, int len)

    event callback function signature

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param echo:
        *undescribed*
    :type echo: u16

    :param data:
        *undescribed*
    :type data: const void \*

    :param len:
        *undescribed*
    :type len: int

.. _`dln2_event_cb_t.description`:

Description
-----------

\ ``pdev``\  - the sub-device that registered this callback
\ ``echo``\  - the echo header field received in the message
\ ``data``\  - the data payload
\ ``len``\   - the data payload length

The callback function is called in interrupt context and the data payload is
only valid during the call. If the user needs later access of the data, it
must copy it.

.. _`dln2_register_event_cb`:

dln2_register_event_cb
======================

.. c:function:: int dln2_register_event_cb(struct platform_device *pdev, u16 event, dln2_event_cb_t event_cb)

    register a callback function for an event

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param event:
        *undescribed*
    :type event: u16

    :param event_cb:
        *undescribed*
    :type event_cb: dln2_event_cb_t

.. _`dln2_register_event_cb.description`:

Description
-----------

\ ``pdev``\  - the sub-device that registers the callback
\ ``event``\  - the event for which to register a callback
\ ``event_cb``\  - the callback function

\ ``return``\  0 in case of success, negative value in case of error

.. _`dln2_unregister_event_cb`:

dln2_unregister_event_cb
========================

.. c:function:: void dln2_unregister_event_cb(struct platform_device *pdev, u16 event)

    unregister the callback function for an event

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param event:
        *undescribed*
    :type event: u16

.. _`dln2_unregister_event_cb.description`:

Description
-----------

\ ``pdev``\  - the sub-device that registered the callback
\ ``event``\  - the event for which to register a callback

.. _`dln2_transfer`:

dln2_transfer
=============

.. c:function:: int dln2_transfer(struct platform_device *pdev, u16 cmd, const void *obuf, unsigned obuf_len, void *ibuf, unsigned *ibuf_len)

    issue a DLN2 command and wait for a response and the associated data

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param cmd:
        *undescribed*
    :type cmd: u16

    :param obuf:
        *undescribed*
    :type obuf: const void \*

    :param obuf_len:
        *undescribed*
    :type obuf_len: unsigned

    :param ibuf:
        *undescribed*
    :type ibuf: void \*

    :param ibuf_len:
        *undescribed*
    :type ibuf_len: unsigned \*

.. _`dln2_transfer.description`:

Description
-----------

\ ``pdev``\  - the sub-device which is issuing this transfer
\ ``cmd``\  - the command to be sent to the device
\ ``obuf``\  - the buffer to be sent to the device; it can be NULL if the user
doesn't need to transmit data with this command
\ ``obuf_len``\  - the size of the buffer to be sent to the device
\ ``ibuf``\  - any data associated with the response will be copied here; it can be
NULL if the user doesn't need the response data
\ ``ibuf_len``\  - must be initialized to the input buffer size; it will be modified
to indicate the actual data transferred;

\ ``return``\  0 for success, negative value for errors

.. _`dln2_transfer_rx`:

dln2_transfer_rx
================

.. c:function:: int dln2_transfer_rx(struct platform_device *pdev, u16 cmd, void *ibuf, unsigned *ibuf_len)

    variant of \ ``dln2_transfer``\ () where TX buffer is not needed

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param cmd:
        *undescribed*
    :type cmd: u16

    :param ibuf:
        *undescribed*
    :type ibuf: void \*

    :param ibuf_len:
        *undescribed*
    :type ibuf_len: unsigned \*

.. _`dln2_transfer_rx.description`:

Description
-----------

\ ``pdev``\  - the sub-device which is issuing this transfer
\ ``cmd``\  - the command to be sent to the device
\ ``ibuf``\  - any data associated with the response will be copied here; it can be
NULL if the user doesn't need the response data
\ ``ibuf_len``\  - must be initialized to the input buffer size; it will be modified
to indicate the actual data transferred;

\ ``return``\  0 for success, negative value for errors

.. _`dln2_transfer_tx`:

dln2_transfer_tx
================

.. c:function:: int dln2_transfer_tx(struct platform_device *pdev, u16 cmd, const void *obuf, unsigned obuf_len)

    variant of \ ``dln2_transfer``\ () where RX buffer is not needed

    :param pdev:
        *undescribed*
    :type pdev: struct platform_device \*

    :param cmd:
        *undescribed*
    :type cmd: u16

    :param obuf:
        *undescribed*
    :type obuf: const void \*

    :param obuf_len:
        *undescribed*
    :type obuf_len: unsigned

.. _`dln2_transfer_tx.description`:

Description
-----------

\ ``pdev``\  - the sub-device which is issuing this transfer
\ ``cmd``\  - the command to be sent to the device
\ ``obuf``\  - the buffer to be sent to the device; it can be NULL if the
user doesn't need to transmit data with this command
\ ``obuf_len``\  - the size of the buffer to be sent to the device

\ ``return``\  0 for success, negative value for errors

.. This file was automatic generated / don't edit.

