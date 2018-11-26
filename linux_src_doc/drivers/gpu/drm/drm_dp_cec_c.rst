.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dp_cec.c

.. _`dp-cec-helpers`:

dp cec helpers
==============

These functions take care of supporting the CEC-Tunneling-over-AUX
feature of DisplayPort-to-HDMI adapters.

.. _`drm_dp_cec_irq`:

drm_dp_cec_irq
==============

.. c:function:: void drm_dp_cec_irq(struct drm_dp_aux *aux)

    handle CEC interrupt, if any

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. _`drm_dp_cec_irq.description`:

Description
-----------

Should be called when handling an IRQ_HPD request. If CEC-tunneling-over-AUX
is present, then it will check for a CEC_IRQ and handle it accordingly.

.. _`drm_dp_cec_register_connector`:

drm_dp_cec_register_connector
=============================

.. c:function:: void drm_dp_cec_register_connector(struct drm_dp_aux *aux, const char *name, struct device *parent)

    register a new connector

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

    :param name:
        name of the CEC device
    :type name: const char \*

    :param parent:
        parent device
    :type parent: struct device \*

.. _`drm_dp_cec_register_connector.description`:

Description
-----------

A new connector was registered with associated CEC adapter name and
CEC adapter parent device. After registering the name and parent
\ :c:func:`drm_dp_cec_set_edid`\  is called to check if the connector supports
CEC and to register a CEC adapter if that is the case.

.. _`drm_dp_cec_unregister_connector`:

drm_dp_cec_unregister_connector
===============================

.. c:function:: void drm_dp_cec_unregister_connector(struct drm_dp_aux *aux)

    unregister the CEC adapter, if any

    :param aux:
        DisplayPort AUX channel
    :type aux: struct drm_dp_aux \*

.. This file was automatic generated / don't edit.

