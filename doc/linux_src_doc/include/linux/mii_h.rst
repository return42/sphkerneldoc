.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mii.h

.. _`mii_nway_result`:

mii_nway_result
===============

.. c:function:: unsigned int mii_nway_result(unsigned int negotiated)

    :param unsigned int negotiated:
        value of MII ANAR and'd with ANLPAR

.. _`mii_nway_result.description`:

Description
-----------

Given a set of MII abilities, check each bit and returns the
currently supported media, in the priority order defined by
IEEE 802.3u.  We use LPA_xxx constants but note this is not the
value of LPA solely, as described above.

The one exception to IEEE 802.3u is that 100baseT4 is placed
between 100T-full and 100T-half.  If your phy does not support
100T4 this is fine.  If your phy places 100T4 elsewhere in the
priority order, you will need to roll your own function.

.. _`mii_duplex`:

mii_duplex
==========

.. c:function:: unsigned int mii_duplex(unsigned int duplex_lock, unsigned int negotiated)

    :param unsigned int duplex_lock:
        Non-zero if duplex is locked at full

    :param unsigned int negotiated:
        value of MII ANAR and'd with ANLPAR

.. _`mii_duplex.description`:

Description
-----------

A small helper function for a common case.  Returns one
if the media is operating or locked at full duplex, and
returns zero otherwise.

.. _`ethtool_adv_to_mii_adv_t`:

ethtool_adv_to_mii_adv_t
========================

.. c:function:: u32 ethtool_adv_to_mii_adv_t(u32 ethadv)

    :param u32 ethadv:
        the ethtool advertisement settings

.. _`ethtool_adv_to_mii_adv_t.description`:

Description
-----------

A small helper function that translates ethtool advertisement
settings to phy autonegotiation advertisements for the
MII_ADVERTISE register.

.. _`mii_adv_to_ethtool_adv_t`:

mii_adv_to_ethtool_adv_t
========================

.. c:function:: u32 mii_adv_to_ethtool_adv_t(u32 adv)

    :param u32 adv:
        value of the MII_ADVERTISE register

.. _`mii_adv_to_ethtool_adv_t.description`:

Description
-----------

A small helper function that translates MII_ADVERTISE bits
to ethtool advertisement settings.

.. _`ethtool_adv_to_mii_ctrl1000_t`:

ethtool_adv_to_mii_ctrl1000_t
=============================

.. c:function:: u32 ethtool_adv_to_mii_ctrl1000_t(u32 ethadv)

    :param u32 ethadv:
        the ethtool advertisement settings

.. _`ethtool_adv_to_mii_ctrl1000_t.description`:

Description
-----------

A small helper function that translates ethtool advertisement
settings to phy autonegotiation advertisements for the
MII_CTRL1000 register when in 1000T mode.

.. _`mii_ctrl1000_to_ethtool_adv_t`:

mii_ctrl1000_to_ethtool_adv_t
=============================

.. c:function:: u32 mii_ctrl1000_to_ethtool_adv_t(u32 adv)

    :param u32 adv:
        value of the MII_CTRL1000 register

.. _`mii_ctrl1000_to_ethtool_adv_t.description`:

Description
-----------

A small helper function that translates MII_CTRL1000
bits, when in 1000Base-T mode, to ethtool
advertisement settings.

.. _`mii_lpa_to_ethtool_lpa_t`:

mii_lpa_to_ethtool_lpa_t
========================

.. c:function:: u32 mii_lpa_to_ethtool_lpa_t(u32 lpa)

    :param u32 lpa:
        *undescribed*

.. _`mii_lpa_to_ethtool_lpa_t.description`:

Description
-----------

A small helper function that translates MII_LPA
bits, when in 1000Base-T mode, to ethtool
LP advertisement settings.

.. _`mii_stat1000_to_ethtool_lpa_t`:

mii_stat1000_to_ethtool_lpa_t
=============================

.. c:function:: u32 mii_stat1000_to_ethtool_lpa_t(u32 lpa)

    :param u32 lpa:
        *undescribed*

.. _`mii_stat1000_to_ethtool_lpa_t.description`:

Description
-----------

A small helper function that translates MII_STAT1000
bits, when in 1000Base-T mode, to ethtool
advertisement settings.

.. _`ethtool_adv_to_mii_adv_x`:

ethtool_adv_to_mii_adv_x
========================

.. c:function:: u32 ethtool_adv_to_mii_adv_x(u32 ethadv)

    :param u32 ethadv:
        the ethtool advertisement settings

.. _`ethtool_adv_to_mii_adv_x.description`:

Description
-----------

A small helper function that translates ethtool advertisement
settings to phy autonegotiation advertisements for the
MII_CTRL1000 register when in 1000Base-X mode.

.. _`mii_adv_to_ethtool_adv_x`:

mii_adv_to_ethtool_adv_x
========================

.. c:function:: u32 mii_adv_to_ethtool_adv_x(u32 adv)

    :param u32 adv:
        value of the MII_CTRL1000 register

.. _`mii_adv_to_ethtool_adv_x.description`:

Description
-----------

A small helper function that translates MII_CTRL1000
bits, when in 1000Base-X mode, to ethtool
advertisement settings.

.. _`mii_lpa_to_ethtool_lpa_x`:

mii_lpa_to_ethtool_lpa_x
========================

.. c:function:: u32 mii_lpa_to_ethtool_lpa_x(u32 lpa)

    :param u32 lpa:
        *undescribed*

.. _`mii_lpa_to_ethtool_lpa_x.description`:

Description
-----------

A small helper function that translates MII_LPA
bits, when in 1000Base-X mode, to ethtool
LP advertisement settings.

.. _`mii_advertise_flowctrl`:

mii_advertise_flowctrl
======================

.. c:function:: u16 mii_advertise_flowctrl(int cap)

    get flow control advertisement flags

    :param int cap:
        Flow control capabilities (FLOW_CTRL_RX, FLOW_CTRL_TX or both)

.. _`mii_resolve_flowctrl_fdx`:

mii_resolve_flowctrl_fdx
========================

.. c:function:: u8 mii_resolve_flowctrl_fdx(u16 lcladv, u16 rmtadv)

    :param u16 lcladv:
        value of MII ADVERTISE register

    :param u16 rmtadv:
        value of MII LPA register

.. _`mii_resolve_flowctrl_fdx.description`:

Description
-----------

Resolve full duplex flow control as per IEEE 802.3-2005 table 28B-3

.. This file was automatic generated / don't edit.

