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

.. _`v4l2_fwnode_endpoint_parse`:

v4l2_fwnode_endpoint_parse
==========================

.. c:function:: int v4l2_fwnode_endpoint_parse(struct fwnode_handle *fwnode, struct v4l2_fwnode_endpoint *vep)

    parse all fwnode node properties

    :param struct fwnode_handle \*fwnode:
        pointer to the endpoint's fwnode handle

    :param struct v4l2_fwnode_endpoint \*vep:
        pointer to the V4L2 fwnode data structure

.. _`v4l2_fwnode_endpoint_parse.description`:

Description
-----------

All properties are optional. If none are found, we don't set any flags. This
means the port has a static configuration and no properties have to be
specified explicitly. If any properties that identify the bus as parallel
are found and slave-mode isn't set, we set V4L2_MBUS_MASTER. Similarly, if
we recognise the bus as serial CSI-2 and clock-noncontinuous isn't set, we
set the V4L2_MBUS_CSI2_CONTINUOUS_CLOCK flag. The caller should hold a
reference to \ ``fwnode``\ .

.. _`v4l2_fwnode_endpoint_parse.note`:

NOTE
----

This function does not parse properties the size of which is variable
without a low fixed limit. Please use \ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\  in
new drivers instead.

.. _`v4l2_fwnode_endpoint_parse.return`:

Return
------

0 on success or a negative error code on failure.

.. _`v4l2_fwnode_endpoint_free`:

v4l2_fwnode_endpoint_free
=========================

.. c:function:: void v4l2_fwnode_endpoint_free(struct v4l2_fwnode_endpoint *vep)

    free the V4L2 fwnode acquired by \ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\ 

    :param struct v4l2_fwnode_endpoint \*vep:
        the V4L2 fwnode the resources of which are to be released

.. _`v4l2_fwnode_endpoint_free.description`:

Description
-----------

It is safe to call this function with NULL argument or on a V4L2 fwnode the
parsing of which failed.

.. _`v4l2_fwnode_endpoint_alloc_parse`:

v4l2_fwnode_endpoint_alloc_parse
================================

.. c:function:: struct v4l2_fwnode_endpoint *v4l2_fwnode_endpoint_alloc_parse(struct fwnode_handle *fwnode)

    parse all fwnode node properties

    :param struct fwnode_handle \*fwnode:
        pointer to the endpoint's fwnode handle

.. _`v4l2_fwnode_endpoint_alloc_parse.description`:

Description
-----------

All properties are optional. If none are found, we don't set any flags. This
means the port has a static configuration and no properties have to be
specified explicitly. If any properties that identify the bus as parallel
are found and slave-mode isn't set, we set V4L2_MBUS_MASTER. Similarly, if
we recognise the bus as serial CSI-2 and clock-noncontinuous isn't set, we
set the V4L2_MBUS_CSI2_CONTINUOUS_CLOCK flag. The caller should hold a
reference to \ ``fwnode``\ .

\ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\  has two important differences to
\ :c:func:`v4l2_fwnode_endpoint_parse`\ :

1. It also parses variable size data.

2. The memory it has allocated to store the variable size data must be freed
   using \ :c:func:`v4l2_fwnode_endpoint_free`\  when no longer needed.

.. _`v4l2_fwnode_endpoint_alloc_parse.return`:

Return
------

Pointer to v4l2_fwnode_endpoint if successful, on an error pointer
on error.

.. _`v4l2_fwnode_parse_link`:

v4l2_fwnode_parse_link
======================

.. c:function:: int v4l2_fwnode_parse_link(struct fwnode_handle *fwnode, struct v4l2_fwnode_link *link)

    parse a link between two endpoints

    :param struct fwnode_handle \*fwnode:
        pointer to the endpoint's fwnode at the local end of the link

    :param struct v4l2_fwnode_link \*link:
        pointer to the V4L2 fwnode link data structure

.. _`v4l2_fwnode_parse_link.description`:

Description
-----------

Fill the link structure with the local and remote nodes and port numbers.
The local_node and remote_node fields are set to point to the local and
remote port's parent nodes respectively (the port parent node being the
parent node of the port node if that node isn't a 'ports' node, or the
grand-parent node of the port node otherwise).

A reference is taken to both the local and remote nodes, the caller must use
\ :c:func:`v4l2_fwnode_put_link`\  to drop the references when done with the
link.

.. _`v4l2_fwnode_parse_link.return`:

Return
------

0 on success, or -ENOLINK if the remote endpoint fwnode can't be
found.

.. _`v4l2_fwnode_put_link`:

v4l2_fwnode_put_link
====================

.. c:function:: void v4l2_fwnode_put_link(struct v4l2_fwnode_link *link)

    drop references to nodes in a link

    :param struct v4l2_fwnode_link \*link:
        pointer to the V4L2 fwnode link data structure

.. _`v4l2_fwnode_put_link.description`:

Description
-----------

Drop references to the local and remote nodes in the link. This function
must be called on every link parsed with \ :c:func:`v4l2_fwnode_parse_link`\ .

.. _`parse_endpoint_func`:

parse_endpoint_func
===================

.. c:function:: int parse_endpoint_func(struct device *dev, struct v4l2_fwnode_endpoint *vep, struct v4l2_async_subdev *asd)

    Driver's callback function to be called on each V4L2 fwnode endpoint.

    :param struct device \*dev:
        pointer to \ :c:type:`struct device <device>`\ 

    :param struct v4l2_fwnode_endpoint \*vep:
        pointer to \ :c:type:`struct v4l2_fwnode_endpoint <v4l2_fwnode_endpoint>`\ 

    :param struct v4l2_async_subdev \*asd:
        pointer to \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\ 

.. _`parse_endpoint_func.return`:

Return
------

* \ ``0``\  on success
* \ ``-ENOTCONN``\  if the endpoint is to be skipped but this
  should not be considered as an error
* \ ``-EINVAL``\  if the endpoint configuration is invalid

.. _`v4l2_async_notifier_parse_fwnode_endpoints`:

v4l2_async_notifier_parse_fwnode_endpoints
==========================================

.. c:function:: int v4l2_async_notifier_parse_fwnode_endpoints(struct device *dev, struct v4l2_async_notifier *notifier, size_t asd_struct_size, parse_endpoint_func parse_endpoint)

    Parse V4L2 fwnode endpoints in a device node

    :param struct device \*dev:
        the device the endpoints of which are to be parsed

    :param struct v4l2_async_notifier \*notifier:
        notifier for \ ``dev``\ 

    :param size_t asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\  shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.

    :param parse_endpoint_func parse_endpoint:
        Driver's callback function called on each V4L2 fwnode
        endpoint. Optional.

.. _`v4l2_async_notifier_parse_fwnode_endpoints.description`:

Description
-----------

Parse the fwnode endpoints of the \ ``dev``\  device and populate the async sub-
devices array of the notifier. The \ ``parse_endpoint``\  callback function is
called for each endpoint with the corresponding async sub-device pointer to
let the caller initialize the driver-specific part of the async sub-device
structure.

The notifier memory shall be zeroed before this function is called on the
notifier.

This function may not be called on a registered notifier and may be called on
a notifier only once.

Do not change the notifier's subdevs array, take references to the subdevs
array itself or change the notifier's num_subdevs field. This is because this
function allocates and reallocates the subdevs array based on parsing
endpoints.

The \ :c:type:`struct v4l2_fwnode_endpoint <v4l2_fwnode_endpoint>`\  passed to the callback function
\ ``parse_endpoint``\  is released once the function is finished. If there is a need
to retain that configuration, the user needs to allocate memory for it.

Any notifier populated using this function must be released with a call to
\ :c:func:`v4l2_async_notifier_cleanup`\  after it has been unregistered and the async
sub-devices are no longer in use, even if the function returned an error.

.. _`v4l2_async_notifier_parse_fwnode_endpoints.return`:

Return
------

%0 on success, including when no async sub-devices are found
        \ ``-ENOMEM``\  if memory allocation failed
        \ ``-EINVAL``\  if graph or endpoint parsing failed
        Other error codes as returned by \ ``parse_endpoint``\ 

.. _`v4l2_async_notifier_parse_fwnode_endpoints_by_port`:

v4l2_async_notifier_parse_fwnode_endpoints_by_port
==================================================

.. c:function:: int v4l2_async_notifier_parse_fwnode_endpoints_by_port(struct device *dev, struct v4l2_async_notifier *notifier, size_t asd_struct_size, unsigned int port, parse_endpoint_func parse_endpoint)

    Parse V4L2 fwnode endpoints of a port in a device node

    :param struct device \*dev:
        the device the endpoints of which are to be parsed

    :param struct v4l2_async_notifier \*notifier:
        notifier for \ ``dev``\ 

    :param size_t asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\  shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.

    :param unsigned int port:
        port number where endpoints are to be parsed

    :param parse_endpoint_func parse_endpoint:
        Driver's callback function called on each V4L2 fwnode
        endpoint. Optional.

.. _`v4l2_async_notifier_parse_fwnode_endpoints_by_port.description`:

Description
-----------

This function is just like \ :c:func:`v4l2_async_notifier_parse_fwnode_endpoints`\  with
the exception that it only parses endpoints in a given port. This is useful
on devices that have both sinks and sources: the async sub-devices connected
to sources have already been configured by another driver (on capture
devices). In this case the driver must know which ports to parse.

Parse the fwnode endpoints of the \ ``dev``\  device on a given \ ``port``\  and populate
the async sub-devices array of the notifier. The \ ``parse_endpoint``\  callback
function is called for each endpoint with the corresponding async sub-device
pointer to let the caller initialize the driver-specific part of the async
sub-device structure.

The notifier memory shall be zeroed before this function is called on the
notifier the first time.

This function may not be called on a registered notifier and may be called on
a notifier only once per port.

Do not change the notifier's subdevs array, take references to the subdevs
array itself or change the notifier's num_subdevs field. This is because this
function allocates and reallocates the subdevs array based on parsing
endpoints.

The \ :c:type:`struct v4l2_fwnode_endpoint <v4l2_fwnode_endpoint>`\  passed to the callback function
\ ``parse_endpoint``\  is released once the function is finished. If there is a need
to retain that configuration, the user needs to allocate memory for it.

Any notifier populated using this function must be released with a call to
\ :c:func:`v4l2_async_notifier_cleanup`\  after it has been unregistered and the async
sub-devices are no longer in use, even if the function returned an error.

.. _`v4l2_async_notifier_parse_fwnode_endpoints_by_port.return`:

Return
------

%0 on success, including when no async sub-devices are found
        \ ``-ENOMEM``\  if memory allocation failed
        \ ``-EINVAL``\  if graph or endpoint parsing failed
        Other error codes as returned by \ ``parse_endpoint``\ 

.. _`v4l2_async_notifier_parse_fwnode_sensor_common`:

v4l2_async_notifier_parse_fwnode_sensor_common
==============================================

.. c:function:: int v4l2_async_notifier_parse_fwnode_sensor_common(struct device *dev, struct v4l2_async_notifier *notifier)

    parse common references on sensors for async sub-devices

    :param struct device \*dev:
        the device node the properties of which are parsed for references

    :param struct v4l2_async_notifier \*notifier:
        the async notifier where the async subdevs will be added

.. _`v4l2_async_notifier_parse_fwnode_sensor_common.description`:

Description
-----------

Parse common sensor properties for remote devices related to the
sensor and set up async sub-devices for them.

Any notifier populated using this function must be released with a call to
\ :c:func:`v4l2_async_notifier_release`\  after it has been unregistered and the async
sub-devices are no longer in use, even in the case the function returned an
error.

.. _`v4l2_async_notifier_parse_fwnode_sensor_common.return`:

Return
------

0 on success
        -ENOMEM if memory allocation failed
        -EINVAL if property parsing failed

.. This file was automatic generated / don't edit.

