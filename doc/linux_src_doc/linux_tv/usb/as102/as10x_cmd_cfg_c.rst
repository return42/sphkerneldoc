.. -*- coding: utf-8; mode: rst -*-

===============
as10x_cmd_cfg.c
===============



.. _xref_as10x_cmd_get_context:

as10x_cmd_get_context
=====================

.. c:function:: int as10x_cmd_get_context (struct as10x_bus_adapter_t * adap, uint16_t tag, uint32_t * pvalue)

    Send get context command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param uint16_t tag:
        context tag

    :param uint32_t * pvalue:
        pointer where to store context value read



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_set_context:

as10x_cmd_set_context
=====================

.. c:function:: int as10x_cmd_set_context (struct as10x_bus_adapter_t * adap, uint16_t tag, uint32_t value)

    send set context command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param uint16_t tag:
        context tag

    :param uint32_t value:
        value to set in context



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_eLNA_change_mode:

as10x_cmd_eLNA_change_mode
==========================

.. c:function:: int as10x_cmd_eLNA_change_mode (struct as10x_bus_adapter_t * adap, uint8_t mode)

    send eLNA change mode command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param uint8_t mode:
        mode selected:
        	        - ON    : 0x0 => eLNA always ON
        	        - OFF   : 0x1 => eLNA always OFF
        	        - AUTO  : 0x2 => eLNA follow hysteresis parameters
        				 to be ON or OFF



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_context_rsp_parse:

as10x_context_rsp_parse
=======================

.. c:function:: int as10x_context_rsp_parse (struct as10x_cmd_t * prsp, uint16_t proc_id)

    Parse context command response

    :param struct as10x_cmd_t * prsp:
        pointer to AS10x command response buffer

    :param uint16_t proc_id:
        id of the command



Description
-----------

Since the contex command response does not follow the common
response, a specific parse function is required.
Return 0 on success or negative value in case of error.


