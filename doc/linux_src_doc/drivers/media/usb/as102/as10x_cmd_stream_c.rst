.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/as102/as10x_cmd_stream.c

.. _`as10x_cmd_add_pid_filter`:

as10x_cmd_add_PID_filter
========================

.. c:function:: int as10x_cmd_add_PID_filter(struct as10x_bus_adapter_t *adap, struct as10x_ts_filter *filter)

    send add filter command to AS10x

    :param struct as10x_bus_adapter_t \*adap:
        pointer to AS10x bus adapter

    :param struct as10x_ts_filter \*filter:
        TSFilter filter for DVB-T

.. _`as10x_cmd_add_pid_filter.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_del_pid_filter`:

as10x_cmd_del_PID_filter
========================

.. c:function:: int as10x_cmd_del_PID_filter(struct as10x_bus_adapter_t *adap, uint16_t pid_value)

    Send delete filter command to AS10x

    :param struct as10x_bus_adapter_t \*adap:
        pointer to AS10x bus adapte

    :param uint16_t pid_value:
        PID to delete

.. _`as10x_cmd_del_pid_filter.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_start_streaming`:

as10x_cmd_start_streaming
=========================

.. c:function:: int as10x_cmd_start_streaming(struct as10x_bus_adapter_t *adap)

    Send start streaming command to AS10x

    :param struct as10x_bus_adapter_t \*adap:
        pointer to AS10x bus adapter

.. _`as10x_cmd_start_streaming.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. _`as10x_cmd_stop_streaming`:

as10x_cmd_stop_streaming
========================

.. c:function:: int as10x_cmd_stop_streaming(struct as10x_bus_adapter_t *adap)

    Send stop streaming command to AS10x

    :param struct as10x_bus_adapter_t \*adap:
        pointer to AS10x bus adapter

.. _`as10x_cmd_stop_streaming.description`:

Description
-----------

Return 0 on success or negative value in case of error.

.. This file was automatic generated / don't edit.

