.. -*- coding: utf-8; mode: rst -*-

==================
as10x_cmd_stream.c
==================



.. _xref_as10x_cmd_add_PID_filter:

as10x_cmd_add_PID_filter
========================

.. c:function:: int as10x_cmd_add_PID_filter (struct as10x_bus_adapter_t * adap, struct as10x_ts_filter * filter)

    send add filter command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter

    :param struct as10x_ts_filter * filter:
        TSFilter filter for DVB-T



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_del_PID_filter:

as10x_cmd_del_PID_filter
========================

.. c:function:: int as10x_cmd_del_PID_filter (struct as10x_bus_adapter_t * adap, uint16_t pid_value)

    Send delete filter command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapte

    :param uint16_t pid_value:
        PID to delete



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_start_streaming:

as10x_cmd_start_streaming
=========================

.. c:function:: int as10x_cmd_start_streaming (struct as10x_bus_adapter_t * adap)

    Send start streaming command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter



Description
-----------

Return 0 on success or negative value in case of error.




.. _xref_as10x_cmd_stop_streaming:

as10x_cmd_stop_streaming
========================

.. c:function:: int as10x_cmd_stop_streaming (struct as10x_bus_adapter_t * adap)

    Send stop streaming command to AS10x

    :param struct as10x_bus_adapter_t * adap:
        pointer to AS10x bus adapter



Description
-----------

Return 0 on success or negative value in case of error.


