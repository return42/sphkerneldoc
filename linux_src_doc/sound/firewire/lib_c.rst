.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/lib.c

.. _`snd_fw_transaction`:

snd_fw_transaction
==================

.. c:function:: int snd_fw_transaction(struct fw_unit *unit, int tcode, u64 offset, void *buffer, size_t length, unsigned int flags)

    send a request and wait for its completion

    :param struct fw_unit \*unit:
        the driver's unit on the target device

    :param int tcode:
        the transaction code

    :param u64 offset:
        the address in the target's address space

    :param void \*buffer:
        input/output data

    :param size_t length:
        length of \ ``buffer``\ 

    :param unsigned int flags:
        use \ ``FW_FIXED_GENERATION``\  and add the generation value to attempt the
        request only in that generation; use \ ``FW_QUIET``\  to suppress error
        messages

.. _`snd_fw_transaction.description`:

Description
-----------

Submits an asynchronous request to the target device, and waits for the
response.  The node ID and the current generation are derived from \ ``unit``\ .
On a bus reset or an error, the transaction is retried a few times.
Returns zero on success, or a negative error code.

.. _`snd_fw_schedule_registration`:

snd_fw_schedule_registration
============================

.. c:function:: void snd_fw_schedule_registration(struct fw_unit *unit, struct delayed_work *dwork)

    schedule work for sound card registration

    :param struct fw_unit \*unit:
        an instance for unit on IEEE 1394 bus

    :param struct delayed_work \*dwork:
        delayed work with callback function

.. _`snd_fw_schedule_registration.description`:

Description
-----------

This function is not designed for general purposes. When new unit is
connected to IEEE 1394 bus, the bus is under bus-reset state because of
topological change. In this state, units tend to fail both of asynchronous
and isochronous communication. To avoid this problem, this function is used
to postpone sound card registration after the state. The callers must
set up instance of delayed work in advance.

.. This file was automatic generated / don't edit.

