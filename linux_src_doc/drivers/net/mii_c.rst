.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/mii.c

.. _`mii_ethtool_gset`:

mii_ethtool_gset
================

.. c:function:: int mii_ethtool_gset(struct mii_if_info *mii, struct ethtool_cmd *ecmd)

    get settings that are specified in \ ``ecmd``\ 

    :param mii:
        MII interface
    :type mii: struct mii_if_info \*

    :param ecmd:
        requested ethtool_cmd
    :type ecmd: struct ethtool_cmd \*

.. _`mii_ethtool_gset.description`:

Description
-----------

The \ ``ecmd``\  parameter is expected to have been cleared before calling
\ :c:func:`mii_ethtool_gset`\ .

Returns 0 for success, negative on error.

.. _`mii_ethtool_get_link_ksettings`:

mii_ethtool_get_link_ksettings
==============================

.. c:function:: void mii_ethtool_get_link_ksettings(struct mii_if_info *mii, struct ethtool_link_ksettings *cmd)

    get settings that are specified in \ ``cmd``\ 

    :param mii:
        MII interface
    :type mii: struct mii_if_info \*

    :param cmd:
        requested ethtool_link_ksettings
    :type cmd: struct ethtool_link_ksettings \*

.. _`mii_ethtool_get_link_ksettings.description`:

Description
-----------

The \ ``cmd``\  parameter is expected to have been cleared before calling
\ :c:func:`mii_ethtool_get_link_ksettings`\ .

.. _`mii_ethtool_sset`:

mii_ethtool_sset
================

.. c:function:: int mii_ethtool_sset(struct mii_if_info *mii, struct ethtool_cmd *ecmd)

    set settings that are specified in \ ``ecmd``\ 

    :param mii:
        MII interface
    :type mii: struct mii_if_info \*

    :param ecmd:
        requested ethtool_cmd
    :type ecmd: struct ethtool_cmd \*

.. _`mii_ethtool_sset.description`:

Description
-----------

Returns 0 for success, negative on error.

.. _`mii_ethtool_set_link_ksettings`:

mii_ethtool_set_link_ksettings
==============================

.. c:function:: int mii_ethtool_set_link_ksettings(struct mii_if_info *mii, const struct ethtool_link_ksettings *cmd)

    set settings that are specified in \ ``cmd``\ 

    :param mii:
        MII interfaces
    :type mii: struct mii_if_info \*

    :param cmd:
        requested ethtool_link_ksettings
    :type cmd: const struct ethtool_link_ksettings \*

.. _`mii_ethtool_set_link_ksettings.description`:

Description
-----------

Returns 0 for success, negative on error.

.. _`mii_check_gmii_support`:

mii_check_gmii_support
======================

.. c:function:: int mii_check_gmii_support(struct mii_if_info *mii)

    check if the MII supports Gb interfaces

    :param mii:
        the MII interface
    :type mii: struct mii_if_info \*

.. _`mii_link_ok`:

mii_link_ok
===========

.. c:function:: int mii_link_ok(struct mii_if_info *mii)

    is link status up/ok

    :param mii:
        the MII interface
    :type mii: struct mii_if_info \*

.. _`mii_link_ok.description`:

Description
-----------

Returns 1 if the MII reports link status up/ok, 0 otherwise.

.. _`mii_nway_restart`:

mii_nway_restart
================

.. c:function:: int mii_nway_restart(struct mii_if_info *mii)

    restart NWay (autonegotiation) for this interface

    :param mii:
        the MII interface
    :type mii: struct mii_if_info \*

.. _`mii_nway_restart.description`:

Description
-----------

Returns 0 on success, negative on error.

.. _`mii_check_link`:

mii_check_link
==============

.. c:function:: void mii_check_link(struct mii_if_info *mii)

    check MII link status

    :param mii:
        MII interface
    :type mii: struct mii_if_info \*

.. _`mii_check_link.description`:

Description
-----------

If the link status changed (previous != current), call
\ :c:func:`netif_carrier_on`\  if current link status is Up or call
\ :c:func:`netif_carrier_off`\  if current link status is Down.

.. _`mii_check_media`:

mii_check_media
===============

.. c:function:: unsigned int mii_check_media(struct mii_if_info *mii, unsigned int ok_to_print, unsigned int init_media)

    check the MII interface for a carrier/speed/duplex change

    :param mii:
        the MII interface
    :type mii: struct mii_if_info \*

    :param ok_to_print:
        OK to print link up/down messages
    :type ok_to_print: unsigned int

    :param init_media:
        OK to save duplex mode in \ ``mii``\ 
    :type init_media: unsigned int

.. _`mii_check_media.description`:

Description
-----------

Returns 1 if the duplex mode changed, 0 if not.
If the media type is forced, always returns 0.

.. _`generic_mii_ioctl`:

generic_mii_ioctl
=================

.. c:function:: int generic_mii_ioctl(struct mii_if_info *mii_if, struct mii_ioctl_data *mii_data, int cmd, unsigned int *duplex_chg_out)

    main MII ioctl interface

    :param mii_if:
        the MII interface
    :type mii_if: struct mii_if_info \*

    :param mii_data:
        MII ioctl data structure
    :type mii_data: struct mii_ioctl_data \*

    :param cmd:
        MII ioctl command
    :type cmd: int

    :param duplex_chg_out:
        pointer to \ ``duplex_changed``\  status if there was no
        ioctl error
    :type duplex_chg_out: unsigned int \*

.. _`generic_mii_ioctl.description`:

Description
-----------

Returns 0 on success, negative on error.

.. This file was automatic generated / don't edit.

