.. -*- coding: utf-8; mode: rst -*-

=========
v4l2-of.h
=========


.. _`v4l2_of_bus_mipi_csi2`:

struct v4l2_of_bus_mipi_csi2
============================

.. c:type:: v4l2_of_bus_mipi_csi2

    MIPI CSI-2 bus data structure


.. _`v4l2_of_bus_mipi_csi2.definition`:

Definition
----------

.. code-block:: c

  struct v4l2_of_bus_mipi_csi2 {
    unsigned int flags;
    unsigned char data_lanes[4];
    unsigned char clock_lane;
    unsigned short num_data_lanes;
    bool lane_polarities[5];
  };


.. _`v4l2_of_bus_mipi_csi2.members`:

Members
-------

:``flags``:
    media bus (V4L2_MBUS\_\*) flags

:``data_lanes[4]``:
    an array of physical data lane indexes

:``clock_lane``:
    physical lane index of the clock lane

:``num_data_lanes``:
    number of data lanes

:``lane_polarities[5]``:
    polarity of the lanes. The order is the same of
    the physical lanes.




.. _`v4l2_of_bus_parallel`:

struct v4l2_of_bus_parallel
===========================

.. c:type:: v4l2_of_bus_parallel

    parallel data bus data structure


.. _`v4l2_of_bus_parallel.definition`:

Definition
----------

.. code-block:: c

  struct v4l2_of_bus_parallel {
    unsigned int flags;
    unsigned char bus_width;
    unsigned char data_shift;
  };


.. _`v4l2_of_bus_parallel.members`:

Members
-------

:``flags``:
    media bus (V4L2_MBUS\_\*) flags

:``bus_width``:
    bus width in bits

:``data_shift``:
    data shift in bits




.. _`v4l2_of_endpoint`:

struct v4l2_of_endpoint
=======================

.. c:type:: v4l2_of_endpoint

    the endpoint data structure


.. _`v4l2_of_endpoint.definition`:

Definition
----------

.. code-block:: c

  struct v4l2_of_endpoint {
    struct of_endpoint base;
    enum v4l2_mbus_type bus_type;
    union bus;
    u64 * link_frequencies;
    unsigned int nr_of_link_frequencies;
  };


.. _`v4l2_of_endpoint.members`:

Members
-------

:``base``:
    struct of_endpoint containing port, id, and local of_node

:``bus_type``:
    bus type

:``bus``:
    bus configuration data structure

:``link_frequencies``:
    array of supported link frequencies

:``nr_of_link_frequencies``:
    number of elements in link_frequenccies array




.. _`v4l2_of_link`:

struct v4l2_of_link
===================

.. c:type:: v4l2_of_link

    a link between two endpoints


.. _`v4l2_of_link.definition`:

Definition
----------

.. code-block:: c

  struct v4l2_of_link {
    struct device_node * local_node;
    unsigned int local_port;
    struct device_node * remote_node;
    unsigned int remote_port;
  };


.. _`v4l2_of_link.members`:

Members
-------

:``local_node``:
    pointer to device_node of this endpoint

:``local_port``:
    identifier of the port this endpoint belongs to

:``remote_node``:
    pointer to device_node of the remote endpoint

:``remote_port``:
    identifier of the port the remote endpoint belongs to


