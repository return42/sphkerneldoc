.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6afe.c

.. _`q6afe_get_port_id`:

q6afe_get_port_id
=================

.. c:function:: int q6afe_get_port_id(int index)

    Get port id from a given port index

    :param index:
        port index
    :type index: int

.. _`q6afe_get_port_id.return`:

Return
------

Will be an negative on error or valid port_id on success

.. _`q6afe_port_stop`:

q6afe_port_stop
===============

.. c:function:: int q6afe_port_stop(struct q6afe_port *port)

    Stop a afe port

    :param port:
        Instance of port to stop
    :type port: struct q6afe_port \*

.. _`q6afe_port_stop.return`:

Return
------

Will be an negative on packet size on success.

.. _`q6afe_slim_port_prepare`:

q6afe_slim_port_prepare
=======================

.. c:function:: void q6afe_slim_port_prepare(struct q6afe_port *port, struct q6afe_slim_cfg *cfg)

    Prepare slim afe port.

    :param port:
        Instance of afe port
    :type port: struct q6afe_port \*

    :param cfg:
        SLIM configuration for the afe port
    :type cfg: struct q6afe_slim_cfg \*

.. _`q6afe_tdm_port_prepare`:

q6afe_tdm_port_prepare
======================

.. c:function:: void q6afe_tdm_port_prepare(struct q6afe_port *port, struct q6afe_tdm_cfg *cfg)

    Prepare tdm afe port.

    :param port:
        Instance of afe port
    :type port: struct q6afe_port \*

    :param cfg:
        TDM configuration for the afe port
    :type cfg: struct q6afe_tdm_cfg \*

.. _`q6afe_hdmi_port_prepare`:

q6afe_hdmi_port_prepare
=======================

.. c:function:: void q6afe_hdmi_port_prepare(struct q6afe_port *port, struct q6afe_hdmi_cfg *cfg)

    Prepare hdmi afe port.

    :param port:
        Instance of afe port
    :type port: struct q6afe_port \*

    :param cfg:
        HDMI configuration for the afe port
    :type cfg: struct q6afe_hdmi_cfg \*

.. _`q6afe_i2s_port_prepare`:

q6afe_i2s_port_prepare
======================

.. c:function:: int q6afe_i2s_port_prepare(struct q6afe_port *port, struct q6afe_i2s_cfg *cfg)

    Prepare i2s afe port.

    :param port:
        Instance of afe port
    :type port: struct q6afe_port \*

    :param cfg:
        I2S configuration for the afe port
    :type cfg: struct q6afe_i2s_cfg \*

.. _`q6afe_i2s_port_prepare.return`:

Return
------

Will be an negative on error and zero on success.

.. _`q6afe_port_start`:

q6afe_port_start
================

.. c:function:: int q6afe_port_start(struct q6afe_port *port)

    Start a afe port

    :param port:
        Instance of port to start
    :type port: struct q6afe_port \*

.. _`q6afe_port_start.return`:

Return
------

Will be an negative on packet size on success.

.. _`q6afe_port_get_from_id`:

q6afe_port_get_from_id
======================

.. c:function:: struct q6afe_port *q6afe_port_get_from_id(struct device *dev, int id)

    Get port instance from a port id

    :param dev:
        Pointer to afe child device.
    :type dev: struct device \*

    :param id:
        port id
    :type id: int

.. _`q6afe_port_get_from_id.return`:

Return
------

Will be an error pointer on error or a valid afe port
on success.

.. _`q6afe_port_put`:

q6afe_port_put
==============

.. c:function:: void q6afe_port_put(struct q6afe_port *port)

    Release port reference

    :param port:
        Instance of port to put
    :type port: struct q6afe_port \*

.. This file was automatic generated / don't edit.

