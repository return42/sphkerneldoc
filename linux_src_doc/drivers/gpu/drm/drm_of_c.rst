.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_of.c

.. _`overview`:

overview
========

A set of helper functions to aid DRM drivers in parsing standard DT
properties.

.. _`drm_of_crtc_port_mask`:

drm_of_crtc_port_mask
=====================

.. c:function:: uint32_t drm_of_crtc_port_mask(struct drm_device *dev, struct device_node *port)

    find the mask of a registered CRTC by port OF node

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param port:
        port OF node
    :type port: struct device_node \*

.. _`drm_of_crtc_port_mask.description`:

Description
-----------

Given a port OF node, return the possible mask of the corresponding
CRTC within a device's list of CRTCs.  Returns zero if not found.

.. _`drm_of_find_possible_crtcs`:

drm_of_find_possible_crtcs
==========================

.. c:function:: uint32_t drm_of_find_possible_crtcs(struct drm_device *dev, struct device_node *port)

    find the possible CRTCs for an encoder port

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param port:
        encoder port to scan for endpoints
    :type port: struct device_node \*

.. _`drm_of_find_possible_crtcs.description`:

Description
-----------

Scan all endpoints attached to a port, locate their attached CRTCs,
and generate the DRM mask of CRTCs which may be attached to this
encoder.

See Documentation/devicetree/bindings/graph.txt for the bindings.

.. _`drm_of_component_match_add`:

drm_of_component_match_add
==========================

.. c:function:: void drm_of_component_match_add(struct device *master, struct component_match **matchptr, int (*compare)(struct device *, void *), struct device_node *node)

    Add a component helper OF node match rule

    :param master:
        master device
    :type master: struct device \*

    :param matchptr:
        component match pointer
    :type matchptr: struct component_match \*\*

    :param int (\*compare)(struct device \*, void \*):
        compare function used for matching component

    :param node:
        of_node
    :type node: struct device_node \*

.. _`drm_of_component_probe`:

drm_of_component_probe
======================

.. c:function:: int drm_of_component_probe(struct device *dev, int (*compare_of)(struct device *, void *), const struct component_master_ops *m_ops)

    Generic probe function for a component based master

    :param dev:
        master device containing the OF node
    :type dev: struct device \*

    :param int (\*compare_of)(struct device \*, void \*):
        compare function used for matching components

    :param m_ops:
        component master ops to be used
    :type m_ops: const struct component_master_ops \*

.. _`drm_of_component_probe.description`:

Description
-----------

Parse the platform device OF node and bind all the components associated
with the master. Interface ports are added before the encoders in order to
satisfy their .bind requirements
See Documentation/devicetree/bindings/graph.txt for the bindings.

Returns zero if successful, or one of the standard error codes if it fails.

.. This file was automatic generated / don't edit.

