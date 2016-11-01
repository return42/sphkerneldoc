.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/epapr_hcalls.h

.. _`ev_int_set_config`:

ev_int_set_config
=================

.. c:function:: unsigned int ev_int_set_config(unsigned int interrupt, uint32_t config, unsigned int priority, uint32_t destination)

    configure the specified interrupt

    :param unsigned int interrupt:
        the interrupt number

    :param uint32_t config:
        configuration for this interrupt

    :param unsigned int priority:
        interrupt priority

    :param uint32_t destination:
        destination CPU number

.. _`ev_int_set_config.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`ev_int_get_config`:

ev_int_get_config
=================

.. c:function:: unsigned int ev_int_get_config(unsigned int interrupt, uint32_t *config, unsigned int *priority, uint32_t *destination)

    return the config of the specified interrupt

    :param unsigned int interrupt:
        the interrupt number

    :param uint32_t \*config:
        returned configuration for this interrupt

    :param unsigned int \*priority:
        returned interrupt priority

    :param uint32_t \*destination:
        returned destination CPU number

.. _`ev_int_get_config.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`ev_int_set_mask`:

ev_int_set_mask
===============

.. c:function:: unsigned int ev_int_set_mask(unsigned int interrupt, unsigned int mask)

    sets the mask for the specified interrupt source

    :param unsigned int interrupt:
        the interrupt number

    :param unsigned int mask:
        0=enable interrupts, 1=disable interrupts

.. _`ev_int_set_mask.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`ev_int_get_mask`:

ev_int_get_mask
===============

.. c:function:: unsigned int ev_int_get_mask(unsigned int interrupt, unsigned int *mask)

    returns the mask for the specified interrupt source

    :param unsigned int interrupt:
        the interrupt number

    :param unsigned int \*mask:
        returned mask for this interrupt (0=enabled, 1=disabled)

.. _`ev_int_get_mask.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`ev_int_eoi`:

ev_int_eoi
==========

.. c:function:: unsigned int ev_int_eoi(unsigned int interrupt)

    signal the end of interrupt processing

    :param unsigned int interrupt:
        the interrupt number

.. _`ev_int_eoi.description`:

Description
-----------

This function signals the end of processing for the the specified
interrupt, which must be the interrupt currently in service. By
definition, this is also the highest-priority interrupt.

Returns 0 for success, or an error code.

.. _`ev_byte_channel_send`:

ev_byte_channel_send
====================

.. c:function:: unsigned int ev_byte_channel_send(unsigned int handle, unsigned int *count, const char buffer[EV_BYTE_CHANNEL_MAX_BYTES])

    send characters to a byte stream

    :param unsigned int handle:
        byte stream handle

    :param unsigned int \*count:
        (input) num of chars to send, (output) num chars sent

    :param const char buffer:
        pointer to a 16-byte buffer

.. _`ev_byte_channel_send.description`:

Description
-----------

@buffer must be at least 16 bytes long, because all 16 bytes will be
read from memory into registers, even if count < 16.

Returns 0 for success, or an error code.

.. _`ev_byte_channel_receive`:

ev_byte_channel_receive
=======================

.. c:function:: unsigned int ev_byte_channel_receive(unsigned int handle, unsigned int *count, char buffer[EV_BYTE_CHANNEL_MAX_BYTES])

    fetch characters from a byte channel

    :param unsigned int handle:
        byte channel handle

    :param unsigned int \*count:
        (input) max num of chars to receive, (output) num chars received

    :param char buffer:
        pointer to a 16-byte buffer

.. _`ev_byte_channel_receive.description`:

Description
-----------

The size of \ ``buffer``\  must be at least 16 bytes, even if you request fewer
than 16 characters, because we always write 16 bytes to \ ``buffer``\ .  This is
for performance reasons.

Returns 0 for success, or an error code.

.. _`ev_byte_channel_poll`:

ev_byte_channel_poll
====================

.. c:function:: unsigned int ev_byte_channel_poll(unsigned int handle, unsigned int *rx_count, unsigned int *tx_count)

    returns the status of the byte channel buffers

    :param unsigned int handle:
        byte channel handle

    :param unsigned int \*rx_count:
        returned count of bytes in receive queue

    :param unsigned int \*tx_count:
        returned count of free space in transmit queue

.. _`ev_byte_channel_poll.description`:

Description
-----------

This function reports the amount of data in the receive queue (i.e. the
number of bytes you can read), and the amount of free space in the transmit
queue (i.e. the number of bytes you can write).

Returns 0 for success, or an error code.

.. _`ev_int_iack`:

ev_int_iack
===========

.. c:function:: unsigned int ev_int_iack(unsigned int handle, unsigned int *vector)

    acknowledge an interrupt

    :param unsigned int handle:
        handle to the target interrupt controller

    :param unsigned int \*vector:
        returned interrupt vector

.. _`ev_int_iack.description`:

Description
-----------

If handle is zero, the function returns the next interrupt source
number to be handled irrespective of the hierarchy or cascading
of interrupt controllers. If non-zero, specifies a handle to the
interrupt controller that is the target of the acknowledge.

Returns 0 for success, or an error code.

.. _`ev_doorbell_send`:

ev_doorbell_send
================

.. c:function:: unsigned int ev_doorbell_send(unsigned int handle)

    send a doorbell to another partition

    :param unsigned int handle:
        doorbell send handle

.. _`ev_doorbell_send.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`ev_idle`:

ev_idle
=======

.. c:function:: unsigned int ev_idle( void)

    - wait for next interrupt on this core

    :param  void:
        no arguments

.. _`ev_idle.description`:

Description
-----------

Returns 0 for success, or an error code.

.. This file was automatic generated / don't edit.

