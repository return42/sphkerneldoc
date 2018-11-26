.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/as102/as10x_cmd_stream.c

.. _`as10x_cmd_add_pid_filter`:

as10x_cmd_add_PID_filter
========================

.. c:function:: int as10x_cmd_add_PID_filter(struct as10x_bus_adapter_t *adap, struct as10x_ts_filter *filter)

    send add filter command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

    :param filter:
        TSFilter filter for DVB-T
    :type filter: struct as10x_ts_filter \*

.. _`as10x_cmd_add_pid_filter.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_del_pid_filter`:

as10x_cmd_del_PID_filter
========================

.. c:function:: int as10x_cmd_del_PID_filter(struct as10x_bus_adapter_t *adap, uint16_t pid_value)

    Send delete filter command to AS10x

    :param adap:
        pointer to AS10x bus adapte
    :type adap: struct as10x_bus_adapter_t \*

    :param pid_value:
        PID to delete
    :type pid_value: uint16_t

.. _`as10x_cmd_del_pid_filter.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_start_streaming`:

as10x_cmd_start_streaming
=========================

.. c:function:: int as10x_cmd_start_streaming(struct as10x_bus_adapter_t *adap)

    Send start streaming command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

.. _`as10x_cmd_start_streaming.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_stop_streaming`:

as10x_cmd_stop_streaming
========================

.. c:function:: int as10x_cmd_stop_streaming(struct as10x_bus_adapter_t *adap)

    Send stop streaming command to AS10x

    :param adap:
        pointer to AS10x bus adapter
    :type adap: struct as10x_bus_adapter_t \*

.. _`as10x_cmd_stop_streaming.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. This file was automatic generated / don't edit.

