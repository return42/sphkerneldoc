.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/port_config.c

.. _`sci_apc_agent_link_up`:

sci_apc_agent_link_up
=====================

.. c:function:: void sci_apc_agent_link_up(struct isci_host *ihost, struct sci_port_configuration_agent *port_agent, struct isci_port *iport, struct isci_phy *iphy)

    handle apc link up events

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param port_agent:
        *undescribed*
    :type port_agent: struct sci_port_configuration_agent \*

    :param iport:
        *undescribed*
    :type iport: struct isci_port \*

    :param iphy:
        *undescribed*
    :type iphy: struct isci_phy \*

.. _`sci_apc_agent_link_up.description`:

Description
-----------

This method handles the automatic port configuration for link up
notifications. Is it possible to get a link down notification from a phy
that has no assocoated port?

.. This file was automatic generated / don't edit.

