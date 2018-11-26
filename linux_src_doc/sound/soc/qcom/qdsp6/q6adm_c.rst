.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6adm.c

.. _`q6adm_open`:

q6adm_open
==========

.. c:function:: struct q6copp *q6adm_open(struct device *dev, int port_id, int path, int rate, int channel_mode, int topology, int perf_mode, uint16_t bit_width, int app_type, int acdb_id)

    open adm and grab a free copp

    :param dev:
        Pointer to adm child device.
    :type dev: struct device \*

    :param port_id:
        port id
    :type port_id: int

    :param path:
        playback or capture path.
    :type path: int

    :param rate:
        rate at which copp is required.
    :type rate: int

    :param channel_mode:
        channel mode
    :type channel_mode: int

    :param topology:
        adm topology id
    :type topology: int

    :param perf_mode:
        performace mode.
    :type perf_mode: int

    :param bit_width:
        audio sample bit width
    :type bit_width: uint16_t

    :param app_type:
        Application type.
    :type app_type: int

    :param acdb_id:
        ACDB id
    :type acdb_id: int

.. _`q6adm_open.return`:

Return
------

Will be an negative on error or a valid copp pointer on success.

.. _`q6adm_get_copp_id`:

q6adm_get_copp_id
=================

.. c:function:: int q6adm_get_copp_id(struct q6copp *copp)

    get copp index

    :param copp:
        Pointer to valid copp
    :type copp: struct q6copp \*

.. _`q6adm_get_copp_id.return`:

Return
------

Will be an negative on error or a valid copp index on success.

.. _`q6adm_matrix_map`:

q6adm_matrix_map
================

.. c:function:: int q6adm_matrix_map(struct device *dev, int path, struct route_payload payload_map, int perf_mode)

    Map asm streams and afe ports using payload

    :param dev:
        Pointer to adm child device.
    :type dev: struct device \*

    :param path:
        playback or capture path.
    :type path: int

    :param payload_map:
        map between session id and afe ports.
    :type payload_map: struct route_payload

    :param perf_mode:
        Performace mode.
    :type perf_mode: int

.. _`q6adm_matrix_map.return`:

Return
------

Will be an negative on error or a zero on success.

.. _`q6adm_close`:

q6adm_close
===========

.. c:function:: int q6adm_close(struct device *dev, struct q6copp *copp)

    Close adm copp

    :param dev:
        Pointer to adm child device.
    :type dev: struct device \*

    :param copp:
        pointer to previously opened copp
    :type copp: struct q6copp \*

.. _`q6adm_close.return`:

Return
------

Will be an negative on error or a zero on success.

.. This file was automatic generated / don't edit.

