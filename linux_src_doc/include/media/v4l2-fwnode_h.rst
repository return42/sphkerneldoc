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
        unsigned char clock_inv:1;
        unsigned char strobe:1;
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
    union with bus configuration data structure

bus.parallel
    embedded \ :c:type:`struct v4l2_fwnode_bus_parallel <v4l2_fwnode_bus_parallel>`\ .
    Used if the bus is parallel.

bus.mipi_csi1
    embedded \ :c:type:`struct v4l2_fwnode_bus_mipi_csi1 <v4l2_fwnode_bus_mipi_csi1>`\ .
    Used if the bus is MIPI Alliance's Camera Serial
    Interface version 1 (MIPI CSI1) or Standard
    Mobile Imaging Architecture's Compact Camera Port 2
    (SMIA CCP2).

bus.mipi_csi2
    embedded \ :c:type:`struct v4l2_fwnode_bus_mipi_csi2 <v4l2_fwnode_bus_mipi_csi2>`\ .
    Used if the bus is MIPI Alliance's Camera Serial
    Interface version 2 (MIPI CSI2).

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

    :param fwnode:
        pointer to the endpoint's fwnode handle
    :type fwnode: struct fwnode_handle \*

    :param vep:
        pointer to the V4L2 fwnode data structure
    :type vep: struct v4l2_fwnode_endpoint \*

.. _`v4l2_fwnode_endpoint_parse.description`:

Description
-----------

This function parses the V4L2 fwnode endpoint specific parameters from the
firmware. The caller is responsible for assigning \ ``vep.bus_type``\  to a valid
media bus type. The caller may also set the default configuration for the
endpoint --- a configuration that shall be in line with the DT binding
documentation. Should a device support multiple bus types, the caller may
call this function once the correct type is found --- with a default
configuration valid for that type.

As a compatibility means guessing the bus type is also supported by setting
\ ``vep.bus_type``\  to V4L2_MBUS_UNKNOWN. The caller may not provide a default
configuration in this case as the defaults are specific to a given bus type.
This functionality is deprecated and should not be used in new drivers and it
is only supported for CSI-2 D-PHY, parallel and Bt.656 busses.

The function does not change the V4L2 fwnode endpoint state if it fails.

.. _`v4l2_fwnode_endpoint_parse.note`:

NOTE
----

This function does not parse properties the size of which is variable
without a low fixed limit. Please use \ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\  in
new drivers instead.

.. _`v4l2_fwnode_endpoint_parse.return`:

Return
------

\ ``0``\  on success or a negative error code on failure:
        \ ``-ENOMEM``\  on memory allocation failure
        \ ``-EINVAL``\  on parsing failure
        \ ``-ENXIO``\  on mismatching bus types

.. _`v4l2_fwnode_endpoint_free`:

v4l2_fwnode_endpoint_free
=========================

.. c:function:: void v4l2_fwnode_endpoint_free(struct v4l2_fwnode_endpoint *vep)

    free the V4L2 fwnode acquired by \ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\ 

    :param vep:
        the V4L2 fwnode the resources of which are to be released
    :type vep: struct v4l2_fwnode_endpoint \*

.. _`v4l2_fwnode_endpoint_free.description`:

Description
-----------

It is safe to call this function with NULL argument or on a V4L2 fwnode the
parsing of which failed.

.. _`v4l2_fwnode_endpoint_alloc_parse`:

v4l2_fwnode_endpoint_alloc_parse
================================

.. c:function:: int v4l2_fwnode_endpoint_alloc_parse(struct fwnode_handle *fwnode, struct v4l2_fwnode_endpoint *vep)

    parse all fwnode node properties

    :param fwnode:
        pointer to the endpoint's fwnode handle
    :type fwnode: struct fwnode_handle \*

    :param vep:
        pointer to the V4L2 fwnode data structure
    :type vep: struct v4l2_fwnode_endpoint \*

.. _`v4l2_fwnode_endpoint_alloc_parse.description`:

Description
-----------

This function parses the V4L2 fwnode endpoint specific parameters from the
firmware. The caller is responsible for assigning \ ``vep.bus_type``\  to a valid
media bus type. The caller may also set the default configuration for the
endpoint --- a configuration that shall be in line with the DT binding
documentation. Should a device support multiple bus types, the caller may
call this function once the correct type is found --- with a default
configuration valid for that type.

As a compatibility means guessing the bus type is also supported by setting
\ ``vep.bus_type``\  to V4L2_MBUS_UNKNOWN. The caller may not provide a default
configuration in this case as the defaults are specific to a given bus type.
This functionality is deprecated and should not be used in new drivers and it
is only supported for CSI-2 D-PHY, parallel and Bt.656 busses.

The function does not change the V4L2 fwnode endpoint state if it fails.

\ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\  has two important differences to
\ :c:func:`v4l2_fwnode_endpoint_parse`\ :

1. It also parses variable size data.

2. The memory it has allocated to store the variable size data must be freed
   using \ :c:func:`v4l2_fwnode_endpoint_free`\  when no longer needed.

.. _`v4l2_fwnode_endpoint_alloc_parse.return`:

Return
------

\ ``0``\  on success or a negative error code on failure:
        \ ``-ENOMEM``\  on memory allocation failure
        \ ``-EINVAL``\  on parsing failure
        \ ``-ENXIO``\  on mismatching bus types

.. _`v4l2_fwnode_parse_link`:

v4l2_fwnode_parse_link
======================

.. c:function:: int v4l2_fwnode_parse_link(struct fwnode_handle *fwnode, struct v4l2_fwnode_link *link)

    parse a link between two endpoints

    :param fwnode:
        pointer to the endpoint's fwnode at the local end of the link
    :type fwnode: struct fwnode_handle \*

    :param link:
        pointer to the V4L2 fwnode link data structure
    :type link: struct v4l2_fwnode_link \*

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

    :param link:
        pointer to the V4L2 fwnode link data structure
    :type link: struct v4l2_fwnode_link \*

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

    :param dev:
        pointer to \ :c:type:`struct device <device>`\ 
    :type dev: struct device \*

    :param vep:
        pointer to \ :c:type:`struct v4l2_fwnode_endpoint <v4l2_fwnode_endpoint>`\ 
    :type vep: struct v4l2_fwnode_endpoint \*

    :param asd:
        pointer to \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\ 
    :type asd: struct v4l2_async_subdev \*

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

    :param dev:
        the device the endpoints of which are to be parsed
    :type dev: struct device \*

    :param notifier:
        notifier for \ ``dev``\ 
    :type notifier: struct v4l2_async_notifier \*

    :param asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct struct <struct>`\ 
        v4l2_async_subdev shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.
    :type asd_struct_size: size_t

    :param parse_endpoint:
        Driver's callback function called on each V4L2 fwnode
        endpoint. Optional.
    :type parse_endpoint: parse_endpoint_func

.. _`v4l2_async_notifier_parse_fwnode_endpoints.description`:

Description
-----------

Parse the fwnode endpoints of the \ ``dev``\  device and populate the async sub-
devices list in the notifier. The \ ``parse_endpoint``\  callback function is
called for each endpoint with the corresponding async sub-device pointer to
let the caller initialize the driver-specific part of the async sub-device
structure.

The notifier memory shall be zeroed before this function is called on the
notifier.

This function may not be called on a registered notifier and may be called on
a notifier only once.

The \ :c:type:`struct v4l2_fwnode_endpoint <v4l2_fwnode_endpoint>`\  passed to the callback function
\ ``parse_endpoint``\  is released once the function is finished. If there is a need
to retain that configuration, the user needs to allocate memory for it.

Any notifier populated using this function must be released with a call to
\ :c:func:`v4l2_async_notifier_cleanup`\  after it has been unregistered and the async
sub-devices are no longer in use, even if the function returned an error.

.. _`v4l2_async_notifier_parse_fwnode_endpoints.return`:

Return
------

\ ``0``\  on success, including when no async sub-devices are found
        \ ``-ENOMEM``\  if memory allocation failed
        \ ``-EINVAL``\  if graph or endpoint parsing failed
        Other error codes as returned by \ ``parse_endpoint``\ 

.. _`v4l2_async_notifier_parse_fwnode_endpoints_by_port`:

v4l2_async_notifier_parse_fwnode_endpoints_by_port
==================================================

.. c:function:: int v4l2_async_notifier_parse_fwnode_endpoints_by_port(struct device *dev, struct v4l2_async_notifier *notifier, size_t asd_struct_size, unsigned int port, parse_endpoint_func parse_endpoint)

    Parse V4L2 fwnode endpoints of a port in a device node

    :param dev:
        the device the endpoints of which are to be parsed
    :type dev: struct device \*

    :param notifier:
        notifier for \ ``dev``\ 
    :type notifier: struct v4l2_async_notifier \*

    :param asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct struct <struct>`\ 
        v4l2_async_subdev shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.
    :type asd_struct_size: size_t

    :param port:
        port number where endpoints are to be parsed
    :type port: unsigned int

    :param parse_endpoint:
        Driver's callback function called on each V4L2 fwnode
        endpoint. Optional.
    :type parse_endpoint: parse_endpoint_func

.. _`v4l2_async_notifier_parse_fwnode_endpoints_by_port.description`:

Description
-----------

This function is just like \ :c:func:`v4l2_async_notifier_parse_fwnode_endpoints`\  with
the exception that it only parses endpoints in a given port. This is useful
on devices that have both sinks and sources: the async sub-devices connected
to sources have already been configured by another driver (on capture
devices). In this case the driver must know which ports to parse.

Parse the fwnode endpoints of the \ ``dev``\  device on a given \ ``port``\  and populate
the async sub-devices list of the notifier. The \ ``parse_endpoint``\  callback
function is called for each endpoint with the corresponding async sub-device
pointer to let the caller initialize the driver-specific part of the async
sub-device structure.

The notifier memory shall be zeroed before this function is called on the
notifier the first time.

This function may not be called on a registered notifier and may be called on
a notifier only once per port.

The \ :c:type:`struct v4l2_fwnode_endpoint <v4l2_fwnode_endpoint>`\  passed to the callback function
\ ``parse_endpoint``\  is released once the function is finished. If there is a need
to retain that configuration, the user needs to allocate memory for it.

Any notifier populated using this function must be released with a call to
\ :c:func:`v4l2_async_notifier_cleanup`\  after it has been unregistered and the async
sub-devices are no longer in use, even if the function returned an error.

.. _`v4l2_async_notifier_parse_fwnode_endpoints_by_port.return`:

Return
------

\ ``0``\  on success, including when no async sub-devices are found
        \ ``-ENOMEM``\  if memory allocation failed
        \ ``-EINVAL``\  if graph or endpoint parsing failed
        Other error codes as returned by \ ``parse_endpoint``\ 

.. _`v4l2_async_notifier_parse_fwnode_sensor_common`:

v4l2_async_notifier_parse_fwnode_sensor_common
==============================================

.. c:function:: int v4l2_async_notifier_parse_fwnode_sensor_common(struct device *dev, struct v4l2_async_notifier *notifier)

    parse common references on sensors for async sub-devices

    :param dev:
        the device node the properties of which are parsed for references
    :type dev: struct device \*

    :param notifier:
        the async notifier where the async subdevs will be added
    :type notifier: struct v4l2_async_notifier \*

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

.. _`v4l2_async_register_fwnode_subdev`:

v4l2_async_register_fwnode_subdev
=================================

.. c:function:: int v4l2_async_register_fwnode_subdev(struct v4l2_subdev *sd, size_t asd_struct_size, unsigned int *ports, unsigned int num_ports, parse_endpoint_func parse_endpoint)

    registers a sub-device to the asynchronous sub-device framework and parses fwnode endpoints

    :param sd:
        pointer to struct \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct struct <struct>`\ 
        v4l2_async_subdev shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.
    :type asd_struct_size: size_t

    :param ports:
        array of port id's to parse for fwnode endpoints. If NULL, will
        parse all ports owned by the sub-device.
    :type ports: unsigned int \*

    :param num_ports:
        number of ports in \ ``ports``\  array. Ignored if \ ``ports``\  is NULL.
    :type num_ports: unsigned int

    :param parse_endpoint:
        Driver's callback function called on each V4L2 fwnode
        endpoint. Optional.
    :type parse_endpoint: parse_endpoint_func

.. _`v4l2_async_register_fwnode_subdev.description`:

Description
-----------

This function is just like \ :c:func:`v4l2_async_register_subdev`\  with the
exception that calling it will also allocate a notifier for the
sub-device, parse the sub-device's firmware node endpoints using
\ :c:func:`v4l2_async_notifier_parse_fwnode_endpoints`\  or
\ :c:func:`v4l2_async_notifier_parse_fwnode_endpoints_by_port`\ , and
registers the sub-device notifier. The sub-device is similarly
unregistered by calling \ :c:func:`v4l2_async_unregister_subdev`\ .

While registered, the subdev module is marked as in-use.

An error is returned if the module is no longer loaded on any attempts
to register it.

.. This file was automatic generated / don't edit.

