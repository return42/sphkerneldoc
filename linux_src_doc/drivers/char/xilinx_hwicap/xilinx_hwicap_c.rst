.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/xilinx_hwicap/xilinx_hwicap.c

.. _`hwicap_command_desync`:

hwicap_command_desync
=====================

.. c:function:: int hwicap_command_desync(struct hwicap_drvdata *drvdata)

    Send a DESYNC command to the ICAP port.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

.. _`hwicap_command_desync.return`:

Return
------

'0' on success and failure value on error

This command desynchronizes the ICAP After this command, a
bitstream containing a NULL packet, followed by a SYNCH packet is
required before the ICAP will recognize commands.

.. _`hwicap_get_configuration_register`:

hwicap_get_configuration_register
=================================

.. c:function:: int hwicap_get_configuration_register(struct hwicap_drvdata *drvdata, u32 reg, u32 *reg_data)

    Query a configuration register.

    :param drvdata:
        a pointer to the drvdata.
    :type drvdata: struct hwicap_drvdata \*

    :param reg:
        a constant which represents the configuration
        register value to be returned.
    :type reg: u32

    :param reg_data:
        returns the value of the register.
    :type reg_data: u32 \*

.. _`hwicap_get_configuration_register.examples`:

Examples
--------

XHI_IDCODE, XHI_FLR.

.. _`hwicap_get_configuration_register.return`:

Return
------

'0' on success and failure value on error

Sends a query packet to the ICAP and then receives the response.
The icap is left in Synched state.

.. This file was automatic generated / don't edit.

