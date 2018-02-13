.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sfp.h

.. _`sfp_eeprom_id`:

struct sfp_eeprom_id
====================

.. c:type:: struct sfp_eeprom_id

    raw SFP module identification information

.. _`sfp_eeprom_id.definition`:

Definition
----------

.. code-block:: c

    struct sfp_eeprom_id {
        struct sfp_eeprom_base base;
        struct sfp_eeprom_ext ext;
    }

.. _`sfp_eeprom_id.members`:

Members
-------

base
    base SFP module identification structure

ext
    extended SFP module identification structure

.. _`sfp_eeprom_id.description`:

Description
-----------

See the SFF-8472 specification and related documents for the definition
of these structure members. This can be obtained from
ftp://ftp.seagate.com/sff

.. _`sfp_upstream_ops`:

struct sfp_upstream_ops
=======================

.. c:type:: struct sfp_upstream_ops

    upstream operations structure

.. _`sfp_upstream_ops.definition`:

Definition
----------

.. code-block:: c

    struct sfp_upstream_ops {
        int (*module_insert)(void *priv, const struct sfp_eeprom_id *id);
        void (*module_remove)(void *priv);
        void (*link_down)(void *priv);
        void (*link_up)(void *priv);
        int (*connect_phy)(void *priv, struct phy_device *);
        void (*disconnect_phy)(void *priv);
    }

.. _`sfp_upstream_ops.members`:

Members
-------

module_insert
    called after a module has been detected to determine
    whether the module is supported for the upstream device.

module_remove
    called after the module has been removed.

link_down
    called when the link is non-operational for whatever
    reason.

link_up
    called when the link is operational.

connect_phy
    called when an I2C accessible PHY has been detected
    on the module.

disconnect_phy
    called when a module with an I2C accessible PHY has
    been removed.

.. This file was automatic generated / don't edit.

