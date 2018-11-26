.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/fcp.c

.. _`fcp_avc_transaction`:

fcp_avc_transaction
===================

.. c:function:: int fcp_avc_transaction(struct fw_unit *unit, const void *command, unsigned int command_size, void *response, unsigned int response_size, unsigned int response_match_bytes)

    send an AV/C command and wait for its response

    :param unit:
        a unit on the target device
    :type unit: struct fw_unit \*

    :param command:
        a buffer containing the command frame; must be DMA-able
    :type command: const void \*

    :param command_size:
        the size of \ ``command``\ 
    :type command_size: unsigned int

    :param response:
        a buffer for the response frame
    :type response: void \*

    :param response_size:
        the maximum size of \ ``response``\ 
    :type response_size: unsigned int

    :param response_match_bytes:
        a bitmap specifying the bytes used to detect the
        correct response frame
    :type response_match_bytes: unsigned int

.. _`fcp_avc_transaction.description`:

Description
-----------

This function sends a FCP command frame to the target and waits for the
corresponding response frame to be returned.

Because it is possible for multiple FCP transactions to be active at the
same time, the correct response frame is detected by the value of certain
bytes.  These bytes must be set in \ ``response``\  before calling this function,
and the corresponding bits must be set in \ ``response_match_bytes``\ .

\ ``command``\  and \ ``response``\  can point to the same buffer.

Returns the actual size of the response frame, or a negative error code.

.. _`fcp_bus_reset`:

fcp_bus_reset
=============

.. c:function:: void fcp_bus_reset(struct fw_unit *unit)

    inform the target handler about a bus reset

    :param unit:
        the unit that might be used by \ :c:func:`fcp_avc_transaction`\ 
    :type unit: struct fw_unit \*

.. _`fcp_bus_reset.description`:

Description
-----------

This function must be called from the driver's .update handler to inform
the FCP transaction handler that a bus reset has happened.  Any pending FCP
transactions are retried.

.. This file was automatic generated / don't edit.

