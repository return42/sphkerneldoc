.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-ethtool.c

.. _`vxge_ethtool_sset`:

vxge_ethtool_sset
=================

.. c:function:: int vxge_ethtool_sset(struct net_device *dev, struct ethtool_cmd *info)

    Sets different link parameters.

    :param struct net_device \*dev:
        device pointer.

    :param struct ethtool_cmd \*info:
        pointer to the structure with parameters given by ethtool to set
        link information.

.. _`vxge_ethtool_sset.description`:

Description
-----------

The function sets different link parameters provided by the user onto
the NIC.

.. _`vxge_ethtool_sset.return-value`:

Return value
------------

0 on success.

.. _`vxge_ethtool_gset`:

vxge_ethtool_gset
=================

.. c:function:: int vxge_ethtool_gset(struct net_device *dev, struct ethtool_cmd *info)

    Return link specific information.

    :param struct net_device \*dev:
        device pointer.

    :param struct ethtool_cmd \*info:
        pointer to the structure with parameters given by ethtool
        to return link information.

.. _`vxge_ethtool_gset.description`:

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

    :param struct net_device \*dev:
        device pointer.

    :param struct ethtool_drvinfo \*info:
        pointer to the structure with parameters given by ethtool to
        return driver information.

.. _`vxge_ethtool_gdrvinfo.description`:

Description
-----------

Returns driver specefic information like name, version etc.. to ethtool.

.. _`vxge_ethtool_gregs`:

vxge_ethtool_gregs
==================

.. c:function:: void vxge_ethtool_gregs(struct net_device *dev, struct ethtool_regs *regs, void *space)

    dumps the entire space of Titan into the buffer.

    :param struct net_device \*dev:
        device pointer.

    :param struct ethtool_regs \*regs:
        pointer to the structure with parameters given by ethtool for
        dumping the registers.

    :param void \*space:
        *undescribed*

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

    :param struct net_device \*dev:
        device pointer.

    :param enum ethtool_phys_id_state state:
        requested LED state

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

    :param struct net_device \*dev:
        device pointer.

    :param struct ethtool_pauseparam \*ep:
        pointer to the structure with pause parameters given by ethtool.

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

    :param struct net_device \*dev:
        device pointer.

    :param struct ethtool_pauseparam \*ep:
        pointer to the structure with pause parameters given by ethtool.

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

