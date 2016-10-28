.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_of.c

.. _`drm_crtc_port_mask`:

drm_crtc_port_mask
==================

.. c:function:: uint32_t drm_crtc_port_mask(struct drm_device *dev, struct device_node *port)

    find the mask of a registered CRTC by port OF node

    :param struct drm_device \*dev:
        DRM device

    :param struct device_node \*port:
        port OF node

.. _`drm_crtc_port_mask.description`:

Description
-----------

Given a port OF node, return the possible mask of the corresponding
CRTC within a device's list of CRTCs.  Returns zero if not found.

.. _`drm_of_find_possible_crtcs`:

drm_of_find_possible_crtcs
==========================

.. c:function:: uint32_t drm_of_find_possible_crtcs(struct drm_device *dev, struct device_node *port)

    find the possible CRTCs for an encoder port

    :param struct drm_device \*dev:
        DRM device

    :param struct device_node \*port:
        encoder port to scan for endpoints

.. _`drm_of_find_possible_crtcs.description`:

Description
-----------

Scan all endpoints attached to a port, locate their attached CRTCs,
and generate the DRM mask of CRTCs which may be attached to this
encoder.

See Documentation/devicetree/bindings/graph.txt for the bindings.

.. _`drm_of_component_probe`:

drm_of_component_probe
======================

.. c:function:: int drm_of_component_probe(struct device *dev, int (*compare_of)(struct device *, void *), const struct component_master_ops *m_ops)

    Generic probe function for a component based master

    :param struct device \*dev:
        master device containing the OF node

    :param int (\*compare_of)(struct device \*, void \*):
        compare function used for matching components

    :param const struct component_master_ops \*m_ops:
        *undescribed*

.. _`drm_of_component_probe.description`:

Description
-----------

Parse the platform device OF node and bind all the components associated
with the master. Interface ports are added before the encoders in order to
satisfy their .bind requirements
See Documentation/devicetree/bindings/graph.txt for the bindings.

Returns zero if successful, or one of the standard error codes if it fails.

.. This file was automatic generated / don't edit.

