.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/coresight.h

.. _`coresight_dev_subtype`:

struct coresight_dev_subtype
============================

.. c:type:: struct coresight_dev_subtype

    further characterisation of a type

.. _`coresight_dev_subtype.definition`:

Definition
----------

.. code-block:: c

    struct coresight_dev_subtype {
        enum coresight_dev_subtype_sink sink_subtype;
        enum coresight_dev_subtype_link link_subtype;
        enum coresight_dev_subtype_source source_subtype;
    }

.. _`coresight_dev_subtype.members`:

Members
-------

sink_subtype
    type of sink this component is, as defined

link_subtype
    type of link this component is, as defined

source_subtype
    type of source this component is, as defined

.. _`coresight_platform_data`:

struct coresight_platform_data
==============================

.. c:type:: struct coresight_platform_data

    data harvested from the DT specification

.. _`coresight_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct coresight_platform_data {
        int cpu;
        const char *name;
        int nr_inport;
        int *outports;
        const char **child_names;
        int *child_ports;
        int nr_outport;
        struct clk *clk;
    }

.. _`coresight_platform_data.members`:

Members
-------

cpu
    the CPU a source belongs to. Only applicable for ETM/PTMs.

name
    name of the component as shown under sysfs.

nr_inport
    number of input ports for this component.

outports
    list of remote endpoint port number.

child_names
    name of all child components connected to this device.

child_ports
    child component port number the current component is

nr_outport
    number of output ports for this component.

clk
    The clock this component is associated to.

.. _`coresight_desc`:

struct coresight_desc
=====================

.. c:type:: struct coresight_desc

    description of a component required from drivers

.. _`coresight_desc.definition`:

Definition
----------

.. code-block:: c

    struct coresight_desc {
        enum coresight_dev_type type;
        struct coresight_dev_subtype subtype;
        const struct coresight_ops *ops;
        struct coresight_platform_data *pdata;
        struct device *dev;
        const struct attribute_group **groups;
    }

.. _`coresight_desc.members`:

Members
-------

type
    as defined by \ ``coresight_dev_type``\ .

subtype
    as defined by \ ``coresight_dev_subtype``\ .

ops
    generic operations for this component, as defined

pdata
    platform data collected from DT.

dev
    The device entity associated to this component.

groups
    operations specific to this component. These will end up

.. _`coresight_connection`:

struct coresight_connection
===========================

.. c:type:: struct coresight_connection

    representation of a single connection

.. _`coresight_connection.definition`:

Definition
----------

.. code-block:: c

    struct coresight_connection {
        int outport;
        const char *child_name;
        int child_port;
        struct coresight_device *child_dev;
    }

.. _`coresight_connection.members`:

Members
-------

outport
    a connection's output port number.

child_name
    *undescribed*

child_port
    remote component's port number \ ``output``\  is connected to.

child_dev
    a \ ``coresight_device``\  representation of the component

.. _`coresight_device`:

struct coresight_device
=======================

.. c:type:: struct coresight_device

    representation of a device as used by the framework

.. _`coresight_device.definition`:

Definition
----------

.. code-block:: c

    struct coresight_device {
        struct coresight_connection *conns;
        int nr_inport;
        int nr_outport;
        enum coresight_dev_type type;
        struct coresight_dev_subtype subtype;
        const struct coresight_ops *ops;
        struct device dev;
        atomic_t *refcnt;
        bool orphan;
        bool enable;
        bool activated;
    }

.. _`coresight_device.members`:

Members
-------

conns
    array of coresight_connections associated to this component.

nr_inport
    number of input port associated to this component.

nr_outport
    number of output port associated to this component.

type
    as defined by \ ``coresight_dev_type``\ .

subtype
    as defined by \ ``coresight_dev_subtype``\ .

ops
    generic operations for this component, as defined

dev
    The device entity associated to this component.

refcnt
    keep track of what is in use.

orphan
    true if the component has connections that haven't been linked.

enable
    'true' if component is currently part of an active path.

activated
    'true' only if a \_sink\_ has been activated.  A sink can be

.. _`coresight_ops_sink`:

struct coresight_ops_sink
=========================

.. c:type:: struct coresight_ops_sink

    basic operations for a sink Operations available for sinks

.. _`coresight_ops_sink.definition`:

Definition
----------

.. code-block:: c

    struct coresight_ops_sink {
        int (*enable)(struct coresight_device *csdev, u32 mode);
        void (*disable)(struct coresight_device *csdev);
        void *(*alloc_buffer)(struct coresight_device *csdev, int cpu, void **pages, int nr_pages, bool overwrite);
        void (*free_buffer)(void *config);
        int (*set_buffer)(struct coresight_device *csdev,struct perf_output_handle *handle, void *sink_config);
        unsigned long (*reset_buffer)(struct coresight_device *csdev,struct perf_output_handle *handle, void *sink_config);
        void (*update_buffer)(struct coresight_device *csdev,struct perf_output_handle *handle, void *sink_config);
    }

.. _`coresight_ops_sink.members`:

Members
-------

enable
    enables the sink.

disable
    disables the sink.

alloc_buffer
    initialises perf's ring buffer for trace collection.

free_buffer
    release memory allocated in \ ``get_config``\ .

set_buffer
    initialises buffer mechanic before a trace session.

reset_buffer
    finalises buffer mechanic after a trace session.

update_buffer
    update buffer pointers after a trace session.

.. _`coresight_ops_link`:

struct coresight_ops_link
=========================

.. c:type:: struct coresight_ops_link

    basic operations for a link Operations available for links.

.. _`coresight_ops_link.definition`:

Definition
----------

.. code-block:: c

    struct coresight_ops_link {
        int (*enable)(struct coresight_device *csdev, int iport, int oport);
        void (*disable)(struct coresight_device *csdev, int iport, int oport);
    }

.. _`coresight_ops_link.members`:

Members
-------

enable
    enables flow between iport and oport.

disable
    disables flow between iport and oport.

.. _`coresight_ops_source`:

struct coresight_ops_source
===========================

.. c:type:: struct coresight_ops_source

    basic operations for a source Operations available for sources.

.. _`coresight_ops_source.definition`:

Definition
----------

.. code-block:: c

    struct coresight_ops_source {
        int (*cpu_id)(struct coresight_device *csdev);
        int (*trace_id)(struct coresight_device *csdev);
        int (*enable)(struct coresight_device *csdev, struct perf_event *event, u32 mode);
        void (*disable)(struct coresight_device *csdev, struct perf_event *event);
    }

.. _`coresight_ops_source.members`:

Members
-------

cpu_id
    returns the value of the CPU number this component
    is associated to.

trace_id
    returns the value of the component's trace ID as known
    to the HW.

enable
    enables tracing for a source.

disable
    disables tracing for a source.

.. This file was automatic generated / don't edit.

