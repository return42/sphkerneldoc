.. -*- coding: utf-8; mode: rst -*-

======
mdio.h
======


.. _`mdio_if_info`:

struct mdio_if_info
===================

.. c:type:: mdio_if_info

    Ethernet controller MDIO interface


.. _`mdio_if_info.definition`:

Definition
----------

.. code-block:: c

  struct mdio_if_info {
    int prtad;
    u32 mmds;
    unsigned mode_support;
    struct net_device * dev;
    int (* mdio_read) (struct net_device *dev, int prtad, int devad,u16 addr);
    int (* mdio_write) (struct net_device *dev, int prtad, int devad,u16 addr, u16 val);
  };


.. _`mdio_if_info.members`:

Members
-------

:``prtad``:
    PRTAD of the PHY (\ ``MDIO_PRTAD_NONE`` if not present/unknown)

:``mmds``:
    Mask of MMDs expected to be present in the PHY.  This must be
    non-zero unless ``prtad`` = ``MDIO_PRTAD_NONE``\ .

:``mode_support``:
    MDIO modes supported.  If ``MDIO_SUPPORTS_C22`` is set then
    MII register access will be passed through with ``devad`` =
    ``MDIO_DEVAD_NONE``\ .  If ``MDIO_EMULATE_C22`` is set then access to
    commonly used clause 22 registers will be translated into
    clause 45 registers.

:``dev``:
    Net device structure

:``mdio_read``:
    Register read function; returns value or negative error code

:``mdio_write``:
    Register write function; returns 0 or negative error code




.. _`mdio45_ethtool_gset`:

mdio45_ethtool_gset
===================

.. c:function:: void mdio45_ethtool_gset (const struct mdio_if_info *mdio, struct ethtool_cmd *ecmd)

    get settings for ETHTOOL_GSET

    :param const struct mdio_if_info \*mdio:
        MDIO interface

    :param struct ethtool_cmd \*ecmd:
        Ethtool request structure



.. _`mdio45_ethtool_gset.description`:

Description
-----------

Since the CSRs for auto-negotiation using next pages are not fully
standardised, this function does not attempt to decode them.  Use
:c:func:`mdio45_ethtool_gset_npage` to specify advertisement bits from next
pages.



.. _`mmd_eee_cap_to_ethtool_sup_t`:

mmd_eee_cap_to_ethtool_sup_t
============================

.. c:function:: u32 mmd_eee_cap_to_ethtool_sup_t (u16 eee_cap)

    :param u16 eee_cap:
        value of the MMD EEE Capability register



.. _`mmd_eee_cap_to_ethtool_sup_t.description`:

Description
-----------

A small helper function that translates MMD EEE Capability (3.20) bits
to ethtool supported settings.



.. _`mmd_eee_adv_to_ethtool_adv_t`:

mmd_eee_adv_to_ethtool_adv_t
============================

.. c:function:: u32 mmd_eee_adv_to_ethtool_adv_t (u16 eee_adv)

    :param u16 eee_adv:
        value of the MMD EEE Advertisement/Link Partner Ability registers



.. _`mmd_eee_adv_to_ethtool_adv_t.description`:

Description
-----------

A small helper function that translates the MMD EEE Advertisment (7.60)
and MMD EEE Link Partner Ability (7.61) bits to ethtool advertisement
settings.



.. _`ethtool_adv_to_mmd_eee_adv_t`:

ethtool_adv_to_mmd_eee_adv_t
============================

.. c:function:: u16 ethtool_adv_to_mmd_eee_adv_t (u32 adv)

    :param u32 adv:
        the ethtool advertisement settings



.. _`ethtool_adv_to_mmd_eee_adv_t.description`:

Description
-----------

A small helper function that translates ethtool advertisement settings
to EEE advertisements for the MMD EEE Advertisement (7.60) and
MMD EEE Link Partner Ability (7.61) registers.



.. _`mdio_module_driver`:

mdio_module_driver
==================

.. c:function:: mdio_module_driver ( _mdio_driver)

    Helper macro for registering mdio drivers

    :param _mdio_driver:

        *undescribed*



.. _`mdio_module_driver.description`:

Description
-----------


Helper macro for MDIO drivers which do not do anything special in module
init/exit. Each module may only use this macro once, and calling it
replaces :c:func:`module_init` and :c:func:`module_exit`.

