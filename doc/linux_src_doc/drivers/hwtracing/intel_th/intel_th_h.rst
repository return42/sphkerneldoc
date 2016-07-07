.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/intel_th/intel_th.h

.. _`intel_th_output`:

struct intel_th_output
======================

.. c:type:: struct intel_th_output

    descriptor INTEL_TH_OUTPUT type devices

.. _`intel_th_output.definition`:

Definition
----------

.. code-block:: c

    struct intel_th_output {
        int port;
        unsigned int type;
        unsigned int scratchpad;
        bool multiblock;
        bool active;
    }

.. _`intel_th_output.members`:

Members
-------

port
    output port number, assigned by the switch

type
    GTH_{MSU,CTP,PTI}

scratchpad
    scratchpad bits to flag when this output is enabled

multiblock
    true for multiblock output configuration

active
    true when this output is enabled

.. _`intel_th_output.description`:

Description
-----------

Output port descriptor, used by switch driver to tell which output
port this output device corresponds to. Filled in at output device's
probe time by switch::\ :c:func:`assign`\ . Passed from output device driver to
switch related code to enable/disable its port.

.. _`intel_th_device`:

struct intel_th_device
======================

.. c:type:: struct intel_th_device

    device on the intel_th bus

.. _`intel_th_device.definition`:

Definition
----------

.. code-block:: c

    struct intel_th_device {
        struct device dev;
        struct resource *resource;
        unsigned int num_resources;
        unsigned int type;
        int id;
        struct intel_th_output output;
        char name[];
    }

.. _`intel_th_device.members`:

Members
-------

dev
    device

resource
    array of resources available to this device

num_resources
    number of resources in \ ``resource``\  array

type
    INTEL_TH_{SOURCE,OUTPUT,SWITCH}

id
    device instance or -1

output
    output descriptor for INTEL_TH_OUTPUT devices

name
    device name to match the driver

.. _`intel_th_device_get_resource`:

intel_th_device_get_resource
============================

.. c:function:: struct resource *intel_th_device_get_resource(struct intel_th_device *thdev, unsigned int type, unsigned int num)

    obtain \ ``num``\ 'th resource of type \ ``type``\ 

    :param struct intel_th_device \*thdev:
        the device to search the resource for

    :param unsigned int type:
        resource type

    :param unsigned int num:
        number of the resource

.. _`intel_th_output_assigned`:

intel_th_output_assigned
========================

.. c:function:: bool intel_th_output_assigned(struct intel_th_device *thdev)

    if an output device is assigned to a switch port

    :param struct intel_th_device \*thdev:
        the output device

.. _`intel_th_output_assigned.return`:

Return
------

true if the device is INTEL_TH_OUTPUT \*and\* is assigned a port

.. _`intel_th_driver`:

struct intel_th_driver
======================

.. c:type:: struct intel_th_driver

    driver for an intel_th_device device

.. _`intel_th_driver.definition`:

Definition
----------

.. code-block:: c

    struct intel_th_driver {
        struct device_driver driver;
        int (* probe) (struct intel_th_device *thdev);
        void (* remove) (struct intel_th_device *thdev);
        int (* assign) (struct intel_th_device *thdev,struct intel_th_device *othdev);
        void (* unassign) (struct intel_th_device *thdev,struct intel_th_device *othdev);
        void (* enable) (struct intel_th_device *thdev,struct intel_th_output *output);
        void (* disable) (struct intel_th_device *thdev,struct intel_th_output *output);
        void (* irq) (struct intel_th_device *thdev);
        int (* activate) (struct intel_th_device *thdev);
        void (* deactivate) (struct intel_th_device *thdev);
        const struct file_operations *fops;
        struct attribute_group *attr_group;
        int (* set_output) (struct intel_th_device *thdev,unsigned int master);
    }

.. _`intel_th_driver.members`:

Members
-------

driver
    generic driver

probe
    probe method

remove
    remove method

assign
    match a given output type device against available outputs

unassign
    deassociate an output type device from an output port

enable
    enable tracing for a given output device

disable
    disable tracing for a given output device

irq
    *undescribed*

activate
    *undescribed*

deactivate
    *undescribed*

fops
    file operations for device nodes

attr_group
    attributes provided by the driver

set_output
    *undescribed*

.. _`intel_th_driver.description`:

Description
-----------

Callbacks \ ``probe``\  and \ ``remove``\  are required for all device types.
Switch device driver needs to fill in \ ``assign``\ , \ ``enable``\  and \ ``disable``\ 
callbacks.

.. _`intel_th`:

struct intel_th
===============

.. c:type:: struct intel_th

    Intel TH controller

.. _`intel_th.definition`:

Definition
----------

.. code-block:: c

    struct intel_th {
        struct device *dev;
        struct intel_th_device  *thdev[TH_SUBDEVICE_MAX];
        struct intel_th_device *hub;
        int id;
        int major;
        #ifdef CONFIG_INTEL_TH_DEBUG
        struct dentry *dbg;
        #endif
    }

.. _`intel_th.members`:

Members
-------

dev
    driver core's device

thdev
    subdevices

hub
    "switch" subdevice (GTH)

id
    this Intel TH controller's device ID in the system

major
    device node major for output devices

dbg
    *undescribed*

.. This file was automatic generated / don't edit.

