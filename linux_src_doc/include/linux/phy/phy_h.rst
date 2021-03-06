.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/phy/phy.h

.. _`phy_ops`:

struct phy_ops
==============

.. c:type:: struct phy_ops

    set of function pointers for performing phy operations

.. _`phy_ops.definition`:

Definition
----------

.. code-block:: c

    struct phy_ops {
        int (*init)(struct phy *phy);
        int (*exit)(struct phy *phy);
        int (*power_on)(struct phy *phy);
        int (*power_off)(struct phy *phy);
        int (*set_mode)(struct phy *phy, enum phy_mode mode);
        int (*reset)(struct phy *phy);
        int (*calibrate)(struct phy *phy);
        struct module *owner;
    }

.. _`phy_ops.members`:

Members
-------

init
    operation to be performed for initializing phy

exit
    operation to be performed while exiting

power_on
    powering on the phy

power_off
    powering off the phy

set_mode
    set the mode of the phy

reset
    resetting the phy

calibrate
    calibrate the phy

owner
    the module owner containing the ops

.. _`phy_attrs`:

struct phy_attrs
================

.. c:type:: struct phy_attrs

    represents phy attributes

.. _`phy_attrs.definition`:

Definition
----------

.. code-block:: c

    struct phy_attrs {
        u32 bus_width;
        enum phy_mode mode;
    }

.. _`phy_attrs.members`:

Members
-------

bus_width
    Data path width implemented by PHY

mode
    *undescribed*

.. _`phy`:

struct phy
==========

.. c:type:: struct phy

    represents the phy device

.. _`phy.definition`:

Definition
----------

.. code-block:: c

    struct phy {
        struct device dev;
        int id;
        const struct phy_ops *ops;
        struct mutex mutex;
        int init_count;
        int power_count;
        struct phy_attrs attrs;
        struct regulator *pwr;
    }

.. _`phy.members`:

Members
-------

dev
    phy device

id
    id of the phy device

ops
    function pointers for performing phy operations

mutex
    mutex to protect phy_ops

init_count
    used to protect when the PHY is used by multiple consumers

power_count
    used to protect when the PHY is used by multiple consumers

attrs
    used to specify PHY specific attributes

pwr
    power regulator associated with the phy

.. _`phy_provider`:

struct phy_provider
===================

.. c:type:: struct phy_provider

    represents the phy provider

.. _`phy_provider.definition`:

Definition
----------

.. code-block:: c

    struct phy_provider {
        struct device *dev;
        struct device_node *children;
        struct module *owner;
        struct list_head list;
        struct phy * (*of_xlate)(struct device *dev, struct of_phandle_args *args);
    }

.. _`phy_provider.members`:

Members
-------

dev
    phy provider device

children
    can be used to override the default (dev->of_node) child node

owner
    the module owner having of_xlate

list
    to maintain a linked list of PHY providers

of_xlate
    function pointer to obtain phy instance from phy pointer

.. _`phy_lookup`:

struct phy_lookup
=================

.. c:type:: struct phy_lookup

    PHY association in list of phys managed by the phy driver

.. _`phy_lookup.definition`:

Definition
----------

.. code-block:: c

    struct phy_lookup {
        struct list_head node;
        const char *dev_id;
        const char *con_id;
        struct phy *phy;
    }

.. _`phy_lookup.members`:

Members
-------

node
    list node

dev_id
    the device of the association

con_id
    connection ID string on device

phy
    the phy of the association

.. This file was automatic generated / don't edit.

