.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vimc/vimc-core.c

.. _`vimc_ent_node`:

enum vimc_ent_node
==================

.. c:type:: enum vimc_ent_node

    Select the functionality of a node in the topology

.. _`vimc_ent_node.definition`:

Definition
----------

.. code-block:: c

    enum vimc_ent_node {
        VIMC_ENT_NODE_SENSOR,
        VIMC_ENT_NODE_CAPTURE,
        VIMC_ENT_NODE_INPUT,
        VIMC_ENT_NODE_DEBAYER,
        VIMC_ENT_NODE_SCALER
    };

.. _`vimc_ent_node.constants`:

Constants
---------

VIMC_ENT_NODE_SENSOR
    A node of type SENSOR simulates a camera sensor
    generating internal images in bayer format and
    propagating those images through the pipeline

VIMC_ENT_NODE_CAPTURE
    A node of type CAPTURE is a v4l2 video_device
    that exposes the received image from the
    pipeline to the user space

VIMC_ENT_NODE_INPUT
    A node of type INPUT is a v4l2 video_device that
    receives images from the user space and
    propagates them through the pipeline

VIMC_ENT_NODE_DEBAYER
    A node type DEBAYER expects to receive a frame
    in bayer format converts it to RGB

VIMC_ENT_NODE_SCALER
    A node of type SCALER scales the received image
    by a given multiplier

.. _`vimc_ent_node.description`:

Description
-----------

This enum is used in the entity configuration struct to allow the definition
of a custom topology specifying the role of each node on it.

.. This file was automatic generated / don't edit.

