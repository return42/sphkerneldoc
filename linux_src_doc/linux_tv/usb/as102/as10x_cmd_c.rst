.. -*- coding: utf-8; mode: rst -*-

===========
as10x_cmd.c
===========



.. _xref_as10x_cmd_turn_on:

as10x_cmd_turn_on
=================

.. c:function:: int as10x_cmd_turn_on (struct as10x_bus_adapter_t * adap)

    send turn on command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter



Description
-----------

Return 0 when no error, < 0 in case of error.




.. _xref_as10x_cmd_turn_off:

as10x_cmd_turn_off
==================

.. c:function:: int as10x_cmd_turn_off (struct as10x_bus_adapter_t * adap)

    send turn off command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_set_tune:

as10x_cmd_set_tune
==================

.. c:function:: int as10x_cmd_set_tune (struct as10x_bus_adapter_t * adap, struct as10x_tune_args * ptune)

    send set tune command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param struct as10x_tune_args * ptune:
        tune parameters



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_get_tune_status:

as10x_cmd_get_tune_status
=========================

.. c:function:: int as10x_cmd_get_tune_status (struct as10x_bus_adapter_t * adap, struct as10x_tune_status * pstatus)

    send get tune status command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param struct as10x_tune_status * pstatus:
        pointer to updated status structure of the current tune



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_get_tps:

as10x_cmd_get_tps
=================

.. c:function:: int as10x_cmd_get_tps (struct as10x_bus_adapter_t * adap, struct as10x_tps * ptps)

    send get TPS command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x handle

    :param struct as10x_tps * ptps:
        pointer to TPS parameters structure



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_get_demod_stats:

as10x_cmd_get_demod_stats
=========================

.. c:function:: int as10x_cmd_get_demod_stats (struct as10x_bus_adapter_t * adap, struct as10x_demod_stats * pdemod_stats)

    send get demod stats command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param struct as10x_demod_stats * pdemod_stats:
        pointer to demod stats parameters structure



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_get_impulse_resp:

as10x_cmd_get_impulse_resp
==========================

.. c:function:: int as10x_cmd_get_impulse_resp (struct as10x_bus_adapter_t * adap, uint8_t * is_ready)

    send get impulse response command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param uint8_t * is_ready:
        pointer to value indicating when impulse
        	      response data is ready



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_build:

as10x_cmd_build
===============

.. c:function:: void as10x_cmd_build (struct as10x_cmd_t * pcmd, uint16_t xid, uint16_t cmd_len)

    build AS10x command header

    :param struct as10x_cmd_t * pcmd:
        pointer to AS10x command buffer

    :param uint16_t xid:
        sequence id of the command

    :param uint16_t cmd_len:
        length of the command




.. _xref_as10x_rsp_parse:

as10x_rsp_parse
===============

.. c:function:: int as10x_rsp_parse (struct as10x_cmd_t * prsp, uint16_t proc_id)

    Parse command response

    :param struct as10x_cmd_t * prsp:
        pointer to AS10x command buffer

    :param uint16_t proc_id:
        id of the command



Description
-----------

Return 0 on success or negative value in case of error.


