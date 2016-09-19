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
    }

.. _`phy_attrs.members`:

Members
-------

bus_width
    Data path width implemented by PHY

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
    *undescribed*

pwr
    *undescribed*

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
        struct phy * (*of_xlate)(struct device *dev,struct of_phandle_args *args);
    }

.. _`phy_provider.members`:

Members
-------

dev
    phy provider device

children
    *undescribed*

owner
    the module owner having of_xlate

list
    to maintain a linked list of PHY providers

of_xlate
    function pointer to obtain phy instance from phy pointer

.. This file was automatic generated / don't edit.

