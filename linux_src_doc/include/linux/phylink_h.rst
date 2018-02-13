.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/phylink.h

.. _`phylink_link_state`:

struct phylink_link_state
=========================

.. c:type:: struct phylink_link_state

    link state structure

.. _`phylink_link_state.definition`:

Definition
----------

.. code-block:: c

    struct phylink_link_state {
        __ETHTOOL_DECLARE_LINK_MODE_MASK(advertising);
        __ETHTOOL_DECLARE_LINK_MODE_MASK(lp_advertising);
        phy_interface_t interface;
        int speed;
        int duplex;
        int pause;
        unsigned int link:1;
        unsigned int an_enabled:1;
        unsigned int an_complete:1;
    }

.. _`phylink_link_state.members`:

Members
-------

__ETHTOOL_DECLARE_LINK_MODE_MASKadvertising
    *undescribed*

__ETHTOOL_DECLARE_LINK_MODE_MASKlp_advertising
    *undescribed*

interface
    link \ :c:type:`typedef phy_interface_t <phy_interface_t>`\  mode

speed
    link speed, one of the SPEED_* constants.

duplex
    link duplex mode, one of DUPLEX_* constants.

pause
    link pause state, described by MLO_PAUSE_* constants.

link
    true if the link is up.

an_enabled
    true if autonegotiation is enabled/desired.

an_complete
    true if autonegotiation has completed.

.. _`phylink_mac_ops`:

struct phylink_mac_ops
======================

.. c:type:: struct phylink_mac_ops

    MAC operations structure.

.. _`phylink_mac_ops.definition`:

Definition
----------

.. code-block:: c

    struct phylink_mac_ops {
        void (*validate)(struct net_device *ndev, unsigned long *supported, struct phylink_link_state *state);
        int (*mac_link_state)(struct net_device *ndev, struct phylink_link_state *state);
        void (*mac_config)(struct net_device *ndev, unsigned int mode, const struct phylink_link_state *state);
        void (*mac_an_restart)(struct net_device *ndev);
        void (*mac_link_down)(struct net_device *ndev, unsigned int mode);
        void (*mac_link_up)(struct net_device *ndev, unsigned int mode, struct phy_device *phy);
    }

.. _`phylink_mac_ops.members`:

Members
-------

validate
    Validate and update the link configuration.

mac_link_state
    Read the current link state from the hardware.

mac_config
    configure the MAC for the selected mode and state.

mac_an_restart
    restart 802.3z BaseX autonegotiation.

mac_link_down
    take the link down.

mac_link_up
    allow the link to come up.

.. _`phylink_mac_ops.description`:

Description
-----------

The individual methods are described more fully below.

.. _`validate`:

validate
========

.. c:function:: void validate(struct net_device *ndev, unsigned long *supported, struct phylink_link_state *state)

    Validate and update the link configuration

    :param struct net_device \*ndev:
        a pointer to a \ :c:type:`struct net_device <net_device>`\  for the MAC.

    :param unsigned long \*supported:
        ethtool bitmask for supported link modes.

    :param struct phylink_link_state \*state:
        a pointer to a \ :c:type:`struct phylink_link_state <phylink_link_state>`\ .

.. _`validate.description`:

Description
-----------

Clear bits in the \ ``supported``\  and \ ``state``\ ->advertising masks that
are not supportable by the MAC.

Note that the PHY may be able to transform from one connection
technology to another, so, eg, don't clear 1000BaseX just
because the MAC is unable to BaseX mode. This is more about
clearing unsupported speeds and duplex settings.

If the \ ``state``\ ->interface mode is \ ``PHY_INTERFACE_MODE_1000BASEX``\ 
or \ ``PHY_INTERFACE_MODE_2500BASEX``\ , select the appropriate mode
based on \ ``state``\ ->advertising and/or \ ``state``\ ->speed and update
\ ``state``\ ->interface accordingly.

.. _`mac_link_state`:

mac_link_state
==============

.. c:function:: int mac_link_state(struct net_device *ndev, struct phylink_link_state *state)

    Read the current link state from the hardware

    :param struct net_device \*ndev:
        a pointer to a \ :c:type:`struct net_device <net_device>`\  for the MAC.

    :param struct phylink_link_state \*state:
        a pointer to a \ :c:type:`struct phylink_link_state <phylink_link_state>`\ .

.. _`mac_link_state.description`:

Description
-----------

Read the current link state from the MAC, reporting the current
speed in \ ``state``\ ->speed, duplex mode in \ ``state``\ ->duplex, pause mode
in \ ``state``\ ->pause using the \ ``MLO_PAUSE_RX``\  and \ ``MLO_PAUSE_TX``\  bits,
negotiation completion state in \ ``state``\ ->an_complete, and link
up state in \ ``state``\ ->link.

.. _`mac_config`:

mac_config
==========

.. c:function:: void mac_config(struct net_device *ndev, unsigned int mode, const struct phylink_link_state *state)

    configure the MAC for the selected mode and state

    :param struct net_device \*ndev:
        a pointer to a \ :c:type:`struct net_device <net_device>`\  for the MAC.

    :param unsigned int mode:
        one of \ ``MLO_AN_FIXED``\ , \ ``MLO_AN_PHY``\ , \ ``MLO_AN_INBAND``\ .

    :param const struct phylink_link_state \*state:
        a pointer to a \ :c:type:`struct phylink_link_state <phylink_link_state>`\ .

.. _`mac_config.the-action-performed-depends-on-the-currently-selected-mode`:

The action performed depends on the currently selected mode
-----------------------------------------------------------


\ ``MLO_AN_FIXED``\ , \ ``MLO_AN_PHY``\ :
  Configure the specified \ ``state``\ ->speed, \ ``state``\ ->duplex and
  \ ``state``\ ->pause (%MLO_PAUSE_TX / \ ``MLO_PAUSE_RX``\ ) mode.

\ ``MLO_AN_INBAND``\ :
  place the link in an inband negotiation mode (such as 802.3z
  1000base-X or Cisco SGMII mode depending on the \ ``state``\ ->interface
  mode). In both cases, link state management (whether the link
  is up or not) is performed by the MAC, and reported via the
  \ :c:func:`mac_link_state`\  callback. Changes in link state must be made
  by calling \ :c:func:`phylink_mac_change`\ .

  If in 802.3z mode, the link speed is fixed, dependent on the
  \ ``state``\ ->interface. Duplex is negotiated, and pause is advertised
  according to \ ``state``\ ->an_enabled, \ ``state``\ ->pause and
  \ ``state``\ ->advertising flags. Beware of MACs which only support full
  duplex at gigabit and higher speeds.

  If in Cisco SGMII mode, the link speed and duplex mode are passed
  in the serial bitstream 16-bit configuration word, and the MAC
  should be configured to read these bits and acknowledge the
  configuration word. Nothing is advertised by the MAC. The MAC is
  responsible for reading the configuration word and configuring
  itself accordingly.

.. _`mac_an_restart`:

mac_an_restart
==============

.. c:function:: void mac_an_restart(struct net_device *ndev)

    restart 802.3z BaseX autonegotiation

    :param struct net_device \*ndev:
        a pointer to a \ :c:type:`struct net_device <net_device>`\  for the MAC.

.. _`mac_link_down`:

mac_link_down
=============

.. c:function:: void mac_link_down(struct net_device *ndev, unsigned int mode)

    take the link down

    :param struct net_device \*ndev:
        a pointer to a \ :c:type:`struct net_device <net_device>`\  for the MAC.

    :param unsigned int mode:
        link autonegotiation mode

.. _`mac_link_down.description`:

Description
-----------

If \ ``mode``\  is not an in-band negotiation mode (as defined by
\ :c:func:`phylink_autoneg_inband`\ ), force the link down and disable any
Energy Efficient Ethernet MAC configuration.

.. _`mac_link_up`:

mac_link_up
===========

.. c:function:: void mac_link_up(struct net_device *ndev, unsigned int mode, struct phy_device *phy)

    allow the link to come up

    :param struct net_device \*ndev:
        a pointer to a \ :c:type:`struct net_device <net_device>`\  for the MAC.

    :param unsigned int mode:
        link autonegotiation mode

    :param struct phy_device \*phy:
        any attached phy

.. _`mac_link_up.description`:

Description
-----------

If \ ``mode``\  is not an in-band negotiation mode (as defined by
\ :c:func:`phylink_autoneg_inband`\ ), allow the link to come up. If \ ``phy``\ 
is non-%NULL, configure Energy Efficient Ethernet by calling
\ :c:func:`phy_init_eee`\  and perform appropriate MAC configuration for EEE.

.. This file was automatic generated / don't edit.

