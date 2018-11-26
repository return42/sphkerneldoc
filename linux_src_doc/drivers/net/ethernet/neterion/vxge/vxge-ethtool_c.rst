.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-ethtool.c

.. _`vxge_ethtool_set_link_ksettings`:

vxge_ethtool_set_link_ksettings
===============================

.. c:function:: int vxge_ethtool_set_link_ksettings(struct net_device *dev, const struct ethtool_link_ksettings *cmd)

    Sets different link parameters.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param cmd:
        pointer to the structure with parameters given by ethtool to set
        link information.
    :type cmd: const struct ethtool_link_ksettings \*

.. _`vxge_ethtool_set_link_ksettings.description`:

Description
-----------

The function sets different link parameters provided by the user onto
the NIC.

.. _`vxge_ethtool_set_link_ksettings.return-value`:

Return value
------------

0 on success.

.. _`vxge_ethtool_get_link_ksettings`:

vxge_ethtool_get_link_ksettings
===============================

.. c:function:: int vxge_ethtool_get_link_ksettings(struct net_device *dev, struct ethtool_link_ksettings *cmd)

    Return link specific information.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param cmd:
        pointer to the structure with parameters given by ethtool
        to return link information.
    :type cmd: struct ethtool_link_ksettings \*

.. _`vxge_ethtool_get_link_ksettings.description`:

Description
-----------

Returns link specific information like speed, duplex etc.. to ethtool.
Return value :
return 0 on success.

.. _`vxge_ethtool_gdrvinfo`:

vxge_ethtool_gdrvinfo
=====================

.. c:function:: void vxge_ethtool_gdrvinfo(struct net_device *dev, struct ethtool_drvinfo *info)

    Returns driver specific information.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param info:
        pointer to the structure with parameters given by ethtool to
        return driver information.
    :type info: struct ethtool_drvinfo \*

.. _`vxge_ethtool_gdrvinfo.description`:

Description
-----------

Returns driver specefic information like name, version etc.. to ethtool.

.. _`vxge_ethtool_gregs`:

vxge_ethtool_gregs
==================

.. c:function:: void vxge_ethtool_gregs(struct net_device *dev, struct ethtool_regs *regs, void *space)

    dumps the entire space of Titan into the buffer.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param regs:
        pointer to the structure with parameters given by ethtool for
        dumping the registers.
    :type regs: struct ethtool_regs \*

    :param space:
        *undescribed*
    :type space: void \*

.. _`vxge_ethtool_gregs.description`:

Description
-----------

Dumps the vpath register space of Titan NIC into the user given
buffer area.

.. _`vxge_ethtool_idnic`:

vxge_ethtool_idnic
==================

.. c:function:: int vxge_ethtool_idnic(struct net_device *dev, enum ethtool_phys_id_state state)

    To physically identify the nic on the system.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param state:
        requested LED state
    :type state: enum ethtool_phys_id_state

.. _`vxge_ethtool_idnic.description`:

Description
-----------

Used to physically identify the NIC on the system.
0 on success

.. _`vxge_ethtool_getpause_data`:

vxge_ethtool_getpause_data
==========================

.. c:function:: void vxge_ethtool_getpause_data(struct net_device *dev, struct ethtool_pauseparam *ep)

    Pause frame frame generation and reception.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param ep:
        pointer to the structure with pause parameters given by ethtool.
    :type ep: struct ethtool_pauseparam \*

.. _`vxge_ethtool_getpause_data.description`:

Description
-----------

Returns the Pause frame generation and reception capability of the NIC.

.. _`vxge_ethtool_getpause_data.return-value`:

Return value
------------

void

.. _`vxge_ethtool_setpause_data`:

vxge_ethtool_setpause_data
==========================

.. c:function:: int vxge_ethtool_setpause_data(struct net_device *dev, struct ethtool_pauseparam *ep)

    set/reset pause frame generation.

    :param dev:
        device pointer.
    :type dev: struct net_device \*

    :param ep:
        pointer to the structure with pause parameters given by ethtool.
    :type ep: struct ethtool_pauseparam \*

.. _`vxge_ethtool_setpause_data.description`:

Description
-----------

It can be used to set or reset Pause frame generation or reception
support of the NIC.

.. _`vxge_ethtool_setpause_data.return-value`:

Return value
------------

int, returns 0 on Success

.. This file was automatic generated / don't edit.

