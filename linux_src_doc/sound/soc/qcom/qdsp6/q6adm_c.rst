.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6adm.c

.. _`q6adm_open`:

q6adm_open
==========

.. c:function:: struct q6copp *q6adm_open(struct device *dev, int port_id, int path, int rate, int channel_mode, int topology, int perf_mode, uint16_t bit_width, int app_type, int acdb_id)

    open adm and grab a free copp

    :param struct device \*dev:
        Pointer to adm child device.

    :param int port_id:
        port id

    :param int path:
        playback or capture path.

    :param int rate:
        rate at which copp is required.

    :param int channel_mode:
        channel mode

    :param int topology:
        adm topology id

    :param int perf_mode:
        performace mode.

    :param uint16_t bit_width:
        audio sample bit width

    :param int app_type:
        Application type.

    :param int acdb_id:
        ACDB id

.. _`q6adm_open.return`:

Return
------

Will be an negative on error or a valid copp pointer on success.

.. _`q6adm_get_copp_id`:

q6adm_get_copp_id
=================

.. c:function:: int q6adm_get_copp_id(struct q6copp *copp)

    get copp index

    :param struct q6copp \*copp:
        Pointer to valid copp

.. _`q6adm_get_copp_id.return`:

Return
------

Will be an negative on error or a valid copp index on success.

.. _`q6adm_matrix_map`:

q6adm_matrix_map
================

.. c:function:: int q6adm_matrix_map(struct device *dev, int path, struct route_payload payload_map, int perf_mode)

    Map asm streams and afe ports using payload

    :param struct device \*dev:
        Pointer to adm child device.

    :param int path:
        playback or capture path.

    :param struct route_payload payload_map:
        map between session id and afe ports.

    :param int perf_mode:
        Performace mode.

.. _`q6adm_matrix_map.return`:

Return
------

Will be an negative on error or a zero on success.

.. _`q6adm_close`:

q6adm_close
===========

.. c:function:: int q6adm_close(struct device *dev, struct q6copp *copp)

    Close adm copp

    :param struct device \*dev:
        Pointer to adm child device.

    :param struct q6copp \*copp:
        pointer to previously opened copp

.. _`q6adm_close.return`:

Return
------

Will be an negative on error or a zero on success.

.. This file was automatic generated / don't edit.

