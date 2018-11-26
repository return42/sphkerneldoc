.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/as102/as10x_cmd.c

.. _`as10x_cmd_turn_on`:

as10x_cmd_turn_on
=================

.. c:function:: int as10x_cmd_turn_on(struct as10x_bus_adapter_t *adap)

    send turn on command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

.. _`as10x_cmd_turn_on.description`:

Description
-----------

Return 0 when no error, < 0 in case of error.

.. _`as10x_cmd_turn_off`:

as10x_cmd_turn_off
==================

.. c:function:: int as10x_cmd_turn_off(struct as10x_bus_adapter_t *adap)

    send turn off command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

.. _`as10x_cmd_turn_off.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_set_tune`:

as10x_cmd_set_tune
==================

.. c:function:: int as10x_cmd_set_tune(struct as10x_bus_adapter_t *adap, struct as10x_tune_args *ptune)

    send set tune command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param ptune:
        tune parameters
    :type ptune: struct as10x_tune_args \*

.. _`as10x_cmd_set_tune.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_get_tune_status`:

as10x_cmd_get_tune_status
=========================

.. c:function:: int as10x_cmd_get_tune_status(struct as10x_bus_adapter_t *adap, struct as10x_tune_status *pstatus)

    send get tune status command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param pstatus:
        pointer to updated status structure of the current tune
    :type pstatus: struct as10x_tune_status \*

.. _`as10x_cmd_get_tune_status.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_get_tps`:

as10x_cmd_get_tps
=================

.. c:function:: int as10x_cmd_get_tps(struct as10x_bus_adapter_t *adap, struct as10x_tps *ptps)

    send get TPS command to AS10x

    :param adap:
        pointer to AS10x handle
    :type adap: struct as10x_bus_adapter_t \*

    :param ptps:
        pointer to TPS parameters structure
    :type ptps: struct as10x_tps \*

.. _`as10x_cmd_get_tps.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_get_demod_stats`:

as10x_cmd_get_demod_stats
=========================

.. c:function:: int as10x_cmd_get_demod_stats(struct as10x_bus_adapter_t *adap, struct as10x_demod_stats *pdemod_stats)

    send get demod stats command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param pdemod_stats:
        pointer to demod stats parameters structure
    :type pdemod_stats: struct as10x_demod_stats \*

.. _`as10x_cmd_get_demod_stats.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_get_impulse_resp`:

as10x_cmd_get_impulse_resp
==========================

.. c:function:: int as10x_cmd_get_impulse_resp(struct as10x_bus_adapter_t *adap, uint8_t *is_ready)

    send get impulse response command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param is_ready:
        pointer to value indicating when impulse
        response data is ready
    :type is_ready: uint8_t \*

.. _`as10x_cmd_get_impulse_resp.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_build`:

as10x_cmd_build
===============

.. c:function:: void as10x_cmd_build(struct as10x_cmd_t *pcmd, uint16_t xid, uint16_t cmd_len)

    build AS10x command header

    :param pcmd:
        pointer to AS10x command buffer
    :type pcmd: struct as10x_cmd_t \*

    :param xid:
        sequence id of the command
    :type xid: uint16_t

    :param cmd_len:
        length of the command
    :type cmd_len: uint16_t

.. _`as10x_rsp_parse`:

as10x_rsp_parse
===============

.. c:function:: int as10x_rsp_parse(struct as10x_cmd_t *prsp, uint16_t proc_id)

    Parse command response

    :param prsp:
        pointer to AS10x command buffer
    :type prsp: struct as10x_cmd_t \*

    :param proc_id:
        id of the command
    :type proc_id: uint16_t

.. _`as10x_rsp_parse.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. This file was automatic generated / don't edit.

