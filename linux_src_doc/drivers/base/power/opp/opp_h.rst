.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/opp/opp.h

.. _`dev_pm_opp`:

struct dev_pm_opp
=================

.. c:type:: struct dev_pm_opp

    Generic OPP description structure

.. _`dev_pm_opp.definition`:

Definition
----------

.. code-block:: c

    struct dev_pm_opp {
        struct list_head node;
        struct kref kref;
        bool available;
        bool dynamic;
        bool turbo;
        bool suspend;
        unsigned long rate;
        struct dev_pm_opp_supply *supplies;
        unsigned long clock_latency_ns;
        struct opp_table *opp_table;
        struct device_node *np;
    #ifdef CONFIG_DEBUG_FS
        struct dentry *dentry;
    #endif
    }

.. _`dev_pm_opp.members`:

Members
-------

node
    opp table node. The nodes are maintained throughout the lifetime
    of boot. It is expected only an optimal set of OPPs are
    added to the library by the SoC framework.
    IMPORTANT: the opp nodes should be maintained in increasing
    order.

kref
    for reference count of the OPP.

available
    true/false - marks if this OPP as available or not

dynamic
    not-created from static DT entries.

turbo
    true if turbo (boost) OPP

suspend
    true if suspend OPP

rate
    Frequency in hertz

supplies
    Power supplies voltage/current values

clock_latency_ns
    Latency (in nanoseconds) of switching to this OPP's
    frequency from any other OPP's frequency.

opp_table
    points back to the opp_table struct this opp belongs to

np
    OPP's device node.

dentry
    debugfs dentry pointer (per opp)

.. _`dev_pm_opp.description`:

Description
-----------

This structure stores the OPP information for a given device.

.. _`opp_device`:

struct opp_device
=================

.. c:type:: struct opp_device

    devices managed by 'struct opp_table'

.. _`opp_device.definition`:

Definition
----------

.. code-block:: c

    struct opp_device {
        struct list_head node;
        const struct device *dev;
    #ifdef CONFIG_DEBUG_FS
        struct dentry *dentry;
    #endif
    }

.. _`opp_device.members`:

Members
-------

node
    list node

dev
    device to which the struct object belongs

dentry
    debugfs dentry pointer (per device)

.. _`opp_device.description`:

Description
-----------

This is an internal data structure maintaining the devices that are managed
by 'struct opp_table'.

.. _`opp_table`:

struct opp_table
================

.. c:type:: struct opp_table

    Device opp structure

.. _`opp_table.definition`:

Definition
----------

.. code-block:: c

    struct opp_table {
        struct list_head node;
        struct blocking_notifier_head head;
        struct list_head dev_list;
        struct list_head opp_list;
        struct kref kref;
        struct mutex lock;
        struct device_node *np;
        unsigned long clock_latency_ns_max;
        unsigned int voltage_tolerance_v1;
        enum opp_table_access shared_opp;
        struct dev_pm_opp *suspend_opp;
        unsigned int *supported_hw;
        unsigned int supported_hw_count;
        const char *prop_name;
        struct clk *clk;
        struct regulator **regulators;
        unsigned int regulator_count;
        int (*set_opp)(struct dev_pm_set_opp_data *data);
        struct dev_pm_set_opp_data *set_opp_data;
    #ifdef CONFIG_DEBUG_FS
        struct dentry *dentry;
        char dentry_name[NAME_MAX];
    #endif
    }

.. _`opp_table.members`:

Members
-------

node
    table node - contains the devices with OPPs that
    have been registered. Nodes once added are not modified in this
    table.

head
    notifier head to notify the OPP availability changes.

dev_list
    list of devices that share these OPPs

opp_list
    table of opps

kref
    for reference count of the table.

lock
    mutex protecting the opp_list.

np
    struct device_node pointer for opp's DT node.

clock_latency_ns_max
    Max clock latency in nanoseconds.

voltage_tolerance_v1
    In percentage, for v1 bindings only.

shared_opp
    OPP is shared between multiple devices.

suspend_opp
    Pointer to OPP to be used during device suspend.

supported_hw
    Array of version number to support.

supported_hw_count
    Number of elements in supported_hw array.

prop_name
    A name to postfix to many DT properties, while parsing them.

clk
    Device's clock handle

regulators
    Supply regulators

regulator_count
    Number of power supply regulators

set_opp
    Platform specific set_opp callback

set_opp_data
    Data to be passed to set_opp callback

dentry
    debugfs dentry pointer of the real device directory (not links).

dentry_name
    Name of the real dentry.

.. _`opp_table.description`:

Description
-----------

This is an internal data structure maintaining the link to opps attached to
a device. This structure is not meant to be shared to users as it is
meant for book keeping and private to OPP library.

.. This file was automatic generated / don't edit.

