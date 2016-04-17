.. -*- coding: utf-8; mode: rst -*-

======
core.c
======


.. _`nfc_fw_download_done`:

nfc_fw_download_done
====================

.. c:function:: int nfc_fw_download_done (struct nfc_dev *dev, const char *firmware_name, u32 result)

    inform that a firmware download was completed

    :param struct nfc_dev \*dev:
        The nfc device to which firmware was downloaded

    :param const char \*firmware_name:
        The firmware filename

    :param u32 result:
        The positive value of a standard errno value



.. _`nfc_dev_up`:

nfc_dev_up
==========

.. c:function:: int nfc_dev_up (struct nfc_dev *dev)

    turn on the NFC device

    :param struct nfc_dev \*dev:
        The nfc device to be turned on



.. _`nfc_dev_up.description`:

Description
-----------

The device remains up until the nfc_dev_down function is called.



.. _`nfc_dev_down`:

nfc_dev_down
============

.. c:function:: int nfc_dev_down (struct nfc_dev *dev)

    turn off the NFC device

    :param struct nfc_dev \*dev:
        The nfc device to be turned off



.. _`nfc_start_poll`:

nfc_start_poll
==============

.. c:function:: int nfc_start_poll (struct nfc_dev *dev, u32 im_protocols, u32 tm_protocols)

    start polling for nfc targets

    :param struct nfc_dev \*dev:
        The nfc device that must start polling

    :param u32 im_protocols:

        *undescribed*

    :param u32 tm_protocols:

        *undescribed*



.. _`nfc_start_poll.description`:

Description
-----------

The device remains polling for targets until a target is found or
the nfc_stop_poll function is called.



.. _`nfc_stop_poll`:

nfc_stop_poll
=============

.. c:function:: int nfc_stop_poll (struct nfc_dev *dev)

    stop polling for nfc targets

    :param struct nfc_dev \*dev:
        The nfc device that must stop polling



.. _`nfc_activate_target`:

nfc_activate_target
===================

.. c:function:: int nfc_activate_target (struct nfc_dev *dev, u32 target_idx, u32 protocol)

    prepare the target for data exchange

    :param struct nfc_dev \*dev:
        The nfc device that found the target

    :param u32 target_idx:
        index of the target that must be activated

    :param u32 protocol:
        nfc protocol that will be used for data exchange



.. _`nfc_deactivate_target`:

nfc_deactivate_target
=====================

.. c:function:: int nfc_deactivate_target (struct nfc_dev *dev, u32 target_idx, u8 mode)

    deactivate a nfc target

    :param struct nfc_dev \*dev:
        The nfc device that found the target

    :param u32 target_idx:
        index of the target that must be deactivated

    :param u8 mode:

        *undescribed*



.. _`nfc_data_exchange`:

nfc_data_exchange
=================

.. c:function:: int nfc_data_exchange (struct nfc_dev *dev, u32 target_idx, struct sk_buff *skb, data_exchange_cb_t cb, void *cb_context)

    transceive data

    :param struct nfc_dev \*dev:
        The nfc device that found the target

    :param u32 target_idx:
        index of the target

    :param struct sk_buff \*skb:
        data to be sent

    :param data_exchange_cb_t cb:
        callback called when the response is received

    :param void \*cb_context:
        parameter for the callback function



.. _`nfc_data_exchange.description`:

Description
-----------

The user must wait for the callback before calling this function again.



.. _`nfc_alloc_send_skb`:

nfc_alloc_send_skb
==================

.. c:function:: struct sk_buff *nfc_alloc_send_skb (struct nfc_dev *dev, struct sock *sk, unsigned int flags, unsigned int size, unsigned int *err)

    allocate a skb for data exchange responses

    :param struct nfc_dev \*dev:

        *undescribed*

    :param struct sock \*sk:

        *undescribed*

    :param unsigned int flags:

        *undescribed*

    :param unsigned int size:
        size to allocate

    :param unsigned int \*err:

        *undescribed*



.. _`nfc_alloc_recv_skb`:

nfc_alloc_recv_skb
==================

.. c:function:: struct sk_buff *nfc_alloc_recv_skb (unsigned int size, gfp_t gfp)

    allocate a skb for data exchange responses

    :param unsigned int size:
        size to allocate

    :param gfp_t gfp:
        gfp flags



.. _`nfc_targets_found`:

nfc_targets_found
=================

.. c:function:: int nfc_targets_found (struct nfc_dev *dev, struct nfc_target *targets, int n_targets)

    inform that targets were found

    :param struct nfc_dev \*dev:
        The nfc device that found the targets

    :param struct nfc_target \*targets:
        array of nfc targets found

    :param int n_targets:

        *undescribed*



.. _`nfc_targets_found.description`:

Description
-----------

The device driver must call this function when one or many nfc targets
are found. After calling this function, the device driver must stop
polling for targets.



.. _`nfc_targets_found.note`:

NOTE
----

This function can be called with targets=NULL and n_targets=0 to
notify a driver error, meaning that the polling operation cannot complete.



.. _`nfc_targets_found.important`:

IMPORTANT
---------

this function must not be called from an atomic context.
In addition, it must also not be called from a context that would prevent
the NFC Core to call other nfc ops entry point concurrently.



.. _`nfc_target_lost`:

nfc_target_lost
===============

.. c:function:: int nfc_target_lost (struct nfc_dev *dev, u32 target_idx)

    inform that an activated target went out of field

    :param struct nfc_dev \*dev:
        The nfc device that had the activated target in field

    :param u32 target_idx:
        the nfc index of the target



.. _`nfc_target_lost.description`:

Description
-----------

The device driver must call this function when the activated target
goes out of the field.



.. _`nfc_target_lost.important`:

IMPORTANT
---------

this function must not be called from an atomic context.
In addition, it must also not be called from a context that would prevent
the NFC Core to call other nfc ops entry point concurrently.



.. _`nfc_allocate_device`:

nfc_allocate_device
===================

.. c:function:: struct nfc_dev *nfc_allocate_device (struct nfc_ops *ops, u32 supported_protocols, int tx_headroom, int tx_tailroom)

    allocate a new nfc device

    :param struct nfc_ops \*ops:
        device operations

    :param u32 supported_protocols:
        NFC protocols supported by the device

    :param int tx_headroom:

        *undescribed*

    :param int tx_tailroom:

        *undescribed*



.. _`nfc_register_device`:

nfc_register_device
===================

.. c:function:: int nfc_register_device (struct nfc_dev *dev)

    register a nfc device in the nfc subsystem

    :param struct nfc_dev \*dev:
        The nfc device to register



.. _`nfc_unregister_device`:

nfc_unregister_device
=====================

.. c:function:: void nfc_unregister_device (struct nfc_dev *dev)

    unregister a nfc device in the nfc subsystem

    :param struct nfc_dev \*dev:
        The nfc device to unregister

