.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-fwnode.h

.. _`v4l2_fwnode_bus_mipi_csi2`:

struct v4l2_fwnode_bus_mipi_csi2
================================

.. c:type:: struct v4l2_fwnode_bus_mipi_csi2

    MIPI CSI-2 bus data structure

.. _`v4l2_fwnode_bus_mipi_csi2.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_fwnode_bus_mipi_csi2 {
        unsigned int flags;
        unsigned char data_lanes[V4L2_FWNODE_CSI2_MAX_DATA_LANES];
        unsigned char clock_lane;
        unsigned short num_data_lanes;
        bool lane_polarities[1 + V4L2_FWNODE_CSI2_MAX_DATA_LANES];
    }

.. _`v4l2_fwnode_bus_mipi_csi2.members`:

Members
-------

flags
    media bus (V4L2_MBUS_*) flags

data_lanes
    an array of physical data lane indexes

clock_lane
    physical lane index of the clock lane

num_data_lanes
    number of data lanes

lane_polarities
    polarity of the lanes. The order is the same of
    the physical lanes.

.. _`v4l2_fwnode_bus_parallel`:

struct v4l2_fwnode_bus_parallel
===============================

.. c:type:: struct v4l2_fwnode_bus_parallel

    parallel data bus data structure

.. _`v4l2_fwnode_bus_parallel.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_fwnode_bus_parallel {
        unsigned int flags;
        unsigned char bus_width;
        unsigned char data_shift;
    }

.. _`v4l2_fwnode_bus_parallel.members`:

Members
-------

flags
    media bus (V4L2_MBUS_*) flags

bus_width
    bus width in bits

data_shift
    data shift in bits

.. _`v4l2_fwnode_bus_mipi_csi1`:

struct v4l2_fwnode_bus_mipi_csi1
================================

.. c:type:: struct v4l2_fwnode_bus_mipi_csi1

    CSI-1/CCP2 data bus structure

.. _`v4l2_fwnode_bus_mipi_csi1.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_fwnode_bus_mipi_csi1 {
        bool clock_inv;
        bool strobe;
        bool lane_polarity[2];
        unsigned char data_lane;
        unsigned char clock_lane;
    }

.. _`v4l2_fwnode_bus_mipi_csi1.members`:

Members
-------

clock_inv
    polarity of clock/strobe signal
    false - not inverted, true - inverted

strobe
    false - data/clock, true - data/strobe

lane_polarity
    the polarities of the clock (index 0) and data lanes
    index (1)

data_lane
    the number of the data lane

clock_lane
    the number of the clock lane

.. _`v4l2_fwnode_endpoint`:

struct v4l2_fwnode_endpoint
===========================

.. c:type:: struct v4l2_fwnode_endpoint

    the endpoint data structure

.. _`v4l2_fwnode_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_fwnode_endpoint {
        struct fwnode_endpoint base;
        enum v4l2_mbus_type bus_type;
        union {
            struct v4l2_fwnode_bus_parallel parallel;
            struct v4l2_fwnode_bus_mipi_csi1 mipi_csi1;
            struct v4l2_fwnode_bus_mipi_csi2 mipi_csi2;
        } bus;
        u64 *link_frequencies;
        unsigned int nr_of_link_frequencies;
    }

.. _`v4l2_fwnode_endpoint.members`:

Members
-------

base
    fwnode endpoint of the v4l2_fwnode

bus_type
    bus type

bus
    bus configuration data structure

parallel
    *undescribed*

mipi_csi1
    *undescribed*

mipi_csi2
    *undescribed*

link_frequencies
    array of supported link frequencies

nr_of_link_frequencies
    number of elements in link_frequenccies array

.. _`v4l2_fwnode_link`:

struct v4l2_fwnode_link
=======================

.. c:type:: struct v4l2_fwnode_link

    a link between two endpoints

.. _`v4l2_fwnode_link.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_fwnode_link {
        struct fwnode_handle *local_node;
        unsigned int local_port;
        struct fwnode_handle *remote_node;
        unsigned int remote_port;
    }

.. _`v4l2_fwnode_link.members`:

Members
-------

local_node
    pointer to device_node of this endpoint

local_port
    identifier of the port this endpoint belongs to

remote_node
    pointer to device_node of the remote endpoint

remote_port
    identifier of the port the remote endpoint belongs to

.. This file was automatic generated / don't edit.

