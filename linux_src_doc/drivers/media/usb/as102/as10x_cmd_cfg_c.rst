.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/as102/as10x_cmd_cfg.c

.. _`as10x_cmd_get_context`:

as10x_cmd_get_context
=====================

.. c:function:: int as10x_cmd_get_context(struct as10x_bus_adapter_t *adap, uint16_t tag, uint32_t *pvalue)

    Send get context command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param tag:
        context tag
    :type tag: uint16_t

    :param pvalue:
        pointer where to store context value read
    :type pvalue: uint32_t \*

.. _`as10x_cmd_get_context.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_set_context`:

as10x_cmd_set_context
=====================

.. c:function:: int as10x_cmd_set_context(struct as10x_bus_adapter_t *adap, uint16_t tag, uint32_t value)

    send set context command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param tag:
        context tag
    :type tag: uint16_t

    :param value:
        value to set in context
    :type value: uint32_t

.. _`as10x_cmd_set_context.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_elna_change_mode`:

as10x_cmd_eLNA_change_mode
==========================

.. c:function:: int as10x_cmd_eLNA_change_mode(struct as10x_bus_adapter_t *adap, uint8_t mode)

    send eLNA change mode command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param mode:
        mode selected:
        - ON    : 0x0 => eLNA always ON
        - OFF   : 0x1 => eLNA always OFF
        - AUTO  : 0x2 => eLNA follow hysteresis parameters
        to be ON or OFF
    :type mode: uint8_t

.. _`as10x_cmd_elna_change_mode.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_context_rsp_parse`:

as10x_context_rsp_parse
=======================

.. c:function:: int as10x_context_rsp_parse(struct as10x_cmd_t *prsp, uint16_t proc_id)

    Parse context command response

    :param prsp:
        pointer to AS10x command response buffer
    :type prsp: struct as10x_cmd_t \*

    :param proc_id:
        id of the command
    :type proc_id: uint16_t

.. _`as10x_context_rsp_parse.description`:

Description
-----------

Since the contex command response does not follow the common
response, a specific parse function is required.
Return 0 on success or negative value in case of error.

.. This file was automatic generated / don't edit.

