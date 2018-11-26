.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/nfc/core.c

.. _`nfc_fw_download_done`:

nfc_fw_download_done
====================

.. c:function:: int nfc_fw_download_done(struct nfc_dev *dev, const char *firmware_name, u32 result)

    inform that a firmware download was completed

    :param dev:
        The nfc device to which firmware was downloaded
    :type dev: struct nfc_dev \*

    :param firmware_name:
        The firmware filename
    :type firmware_name: const char \*

    :param result:
        The positive value of a standard errno value
    :type result: u32

.. _`nfc_dev_up`:

nfc_dev_up
==========

.. c:function:: int nfc_dev_up(struct nfc_dev *dev)

    turn on the NFC device

    :param dev:
        The nfc device to be turned on
    :type dev: struct nfc_dev \*

.. _`nfc_dev_up.description`:

Description
-----------

The device remains up until the nfc_dev_down function is called.

.. _`nfc_dev_down`:

nfc_dev_down
============

.. c:function:: int nfc_dev_down(struct nfc_dev *dev)

    turn off the NFC device

    :param dev:
        The nfc device to be turned off
    :type dev: struct nfc_dev \*

.. _`nfc_start_poll`:

nfc_start_poll
==============

.. c:function:: int nfc_start_poll(struct nfc_dev *dev, u32 im_protocols, u32 tm_protocols)

    start polling for nfc targets

    :param dev:
        The nfc device that must start polling
    :type dev: struct nfc_dev \*

    :param im_protocols:
        *undescribed*
    :type im_protocols: u32

    :param tm_protocols:
        *undescribed*
    :type tm_protocols: u32

.. _`nfc_start_poll.description`:

Description
-----------

The device remains polling for targets until a target is found or
the nfc_stop_poll function is called.

.. _`nfc_stop_poll`:

nfc_stop_poll
=============

.. c:function:: int nfc_stop_poll(struct nfc_dev *dev)

    stop polling for nfc targets

    :param dev:
        The nfc device that must stop polling
    :type dev: struct nfc_dev \*

.. _`nfc_activate_target`:

nfc_activate_target
===================

.. c:function:: int nfc_activate_target(struct nfc_dev *dev, u32 target_idx, u32 protocol)

    prepare the target for data exchange

    :param dev:
        The nfc device that found the target
    :type dev: struct nfc_dev \*

    :param target_idx:
        index of the target that must be activated
    :type target_idx: u32

    :param protocol:
        nfc protocol that will be used for data exchange
    :type protocol: u32

.. _`nfc_deactivate_target`:

nfc_deactivate_target
=====================

.. c:function:: int nfc_deactivate_target(struct nfc_dev *dev, u32 target_idx, u8 mode)

    deactivate a nfc target

    :param dev:
        The nfc device that found the target
    :type dev: struct nfc_dev \*

    :param target_idx:
        index of the target that must be deactivated
    :type target_idx: u32

    :param mode:
        *undescribed*
    :type mode: u8

.. _`nfc_data_exchange`:

nfc_data_exchange
=================

.. c:function:: int nfc_data_exchange(struct nfc_dev *dev, u32 target_idx, struct sk_buff *skb, data_exchange_cb_t cb, void *cb_context)

    transceive data

    :param dev:
        The nfc device that found the target
    :type dev: struct nfc_dev \*

    :param target_idx:
        index of the target
    :type target_idx: u32

    :param skb:
        data to be sent
    :type skb: struct sk_buff \*

    :param cb:
        callback called when the response is received
    :type cb: data_exchange_cb_t

    :param cb_context:
        parameter for the callback function
    :type cb_context: void \*

.. _`nfc_data_exchange.description`:

Description
-----------

The user must wait for the callback before calling this function again.

.. _`nfc_alloc_send_skb`:

nfc_alloc_send_skb
==================

.. c:function:: struct sk_buff *nfc_alloc_send_skb(struct nfc_dev *dev, struct sock *sk, unsigned int flags, unsigned int size, unsigned int *err)

    allocate a skb for data exchange responses

    :param dev:
        *undescribed*
    :type dev: struct nfc_dev \*

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param flags:
        *undescribed*
    :type flags: unsigned int

    :param size:
        size to allocate
    :type size: unsigned int

    :param err:
        *undescribed*
    :type err: unsigned int \*

.. _`nfc_alloc_recv_skb`:

nfc_alloc_recv_skb
==================

.. c:function:: struct sk_buff *nfc_alloc_recv_skb(unsigned int size, gfp_t gfp)

    allocate a skb for data exchange responses

    :param size:
        size to allocate
    :type size: unsigned int

    :param gfp:
        gfp flags
    :type gfp: gfp_t

.. _`nfc_targets_found`:

nfc_targets_found
=================

.. c:function:: int nfc_targets_found(struct nfc_dev *dev, struct nfc_target *targets, int n_targets)

    inform that targets were found

    :param dev:
        The nfc device that found the targets
    :type dev: struct nfc_dev \*

    :param targets:
        array of nfc targets found
    :type targets: struct nfc_target \*

    :param n_targets:
        *undescribed*
    :type n_targets: int

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

.. c:function:: int nfc_target_lost(struct nfc_dev *dev, u32 target_idx)

    inform that an activated target went out of field

    :param dev:
        The nfc device that had the activated target in field
    :type dev: struct nfc_dev \*

    :param target_idx:
        the nfc index of the target
    :type target_idx: u32

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

.. c:function:: struct nfc_dev *nfc_allocate_device(struct nfc_ops *ops, u32 supported_protocols, int tx_headroom, int tx_tailroom)

    allocate a new nfc device

    :param ops:
        device operations
    :type ops: struct nfc_ops \*

    :param supported_protocols:
        NFC protocols supported by the device
    :type supported_protocols: u32

    :param tx_headroom:
        *undescribed*
    :type tx_headroom: int

    :param tx_tailroom:
        *undescribed*
    :type tx_tailroom: int

.. _`nfc_register_device`:

nfc_register_device
===================

.. c:function:: int nfc_register_device(struct nfc_dev *dev)

    register a nfc device in the nfc subsystem

    :param dev:
        The nfc device to register
    :type dev: struct nfc_dev \*

.. _`nfc_unregister_device`:

nfc_unregister_device
=====================

.. c:function:: void nfc_unregister_device(struct nfc_dev *dev)

    unregister a nfc device in the nfc subsystem

    :param dev:
        The nfc device to unregister
    :type dev: struct nfc_dev \*

.. This file was automatic generated / don't edit.

