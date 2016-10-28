.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-vipp.c

.. _`xvip_graph_entity`:

struct xvip_graph_entity
========================

.. c:type:: struct xvip_graph_entity

    Entity in the video graph

.. _`xvip_graph_entity.definition`:

Definition
----------

.. code-block:: c

    struct xvip_graph_entity {
        struct list_head list;
        struct device_node *node;
        struct media_entity *entity;
        struct v4l2_async_subdev asd;
        struct v4l2_subdev *subdev;
    }

.. _`xvip_graph_entity.members`:

Members
-------

list
    list entry in a graph entities list

node
    the entity's DT node

entity
    media entity, from the corresponding V4L2 subdev

asd
    subdev asynchronous registration information

subdev
    V4L2 subdev

.. This file was automatic generated / don't edit.

