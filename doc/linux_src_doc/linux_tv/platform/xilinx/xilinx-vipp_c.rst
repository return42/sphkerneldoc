.. -*- coding: utf-8; mode: rst -*-

=============
xilinx-vipp.c
=============



.. _xref_struct_xvip_graph_entity:

struct xvip_graph_entity
========================

.. c:type:: struct xvip_graph_entity

    Entity in the video graph



Definition
----------

.. code-block:: c

  struct xvip_graph_entity {
    struct list_head list;
    struct device_node * node;
    struct media_entity * entity;
    struct v4l2_async_subdev asd;
    struct v4l2_subdev * subdev;
  };



Members
-------

:``struct list_head list``:
    list entry in a graph entities list

:``struct device_node * node``:
    the entity's DT node

:``struct media_entity * entity``:
    media entity, from the corresponding V4L2 subdev

:``struct v4l2_async_subdev asd``:
    subdev asynchronous registration information

:``struct v4l2_subdev * subdev``:
    V4L2 subdev



