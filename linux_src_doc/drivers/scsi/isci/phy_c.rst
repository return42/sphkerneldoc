.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/phy.c

.. _`phy_get_non_dummy_port`:

phy_get_non_dummy_port
======================

.. c:function:: struct isci_port *phy_get_non_dummy_port(struct isci_phy *iphy)

    currently contained by the dummy port, then the phy is considered to not be part of a port.

    :param iphy:
        *undescribed*
    :type iphy: struct isci_phy \*

.. _`phy_get_non_dummy_port.description`:

Description
-----------

This method returns a handle to a port that contains the supplied phy.
NULL This value is returned if the phy is not part of a real
port (i.e. it's contained in the dummy port). !NULL All other
values indicate a handle/pointer to the port containing the phy.

.. _`sci_phy_set_port`:

sci_phy_set_port
================

.. c:function:: void sci_phy_set_port(struct isci_phy *iphy, struct isci_port *iport)

    :param iphy:
        *undescribed*
    :type iphy: struct isci_phy \*

    :param iport:
        *undescribed*
    :type iport: struct isci_port \*

.. _`sci_phy_set_port.description`:

Description
-----------



.. _`sci_phy_setup_transport`:

sci_phy_setup_transport
=======================

.. c:function:: void sci_phy_setup_transport(struct isci_phy *iphy, u32 device_id)

    :param iphy:
        *undescribed*
    :type iphy: struct isci_phy \*

    :param device_id:
        *undescribed*
    :type device_id: u32

.. _`sci_phy_setup_transport.description`:

Description
-----------

\ ``iphy``\  The phy for which the direct attached device id is to
be assigned.
\ ``device_id``\  The direct attached device ID to assign to the phy.
This will either be the RNi for the device or an invalid RNi if there
is no current device assigned to the phy.

.. _`sci_phy_complete_link_training`:

sci_phy_complete_link_training
==============================

.. c:function:: void sci_phy_complete_link_training(struct isci_phy *iphy, enum sas_linkrate max_link_rate, u32 next_state)

    perform processing common to all protocols upon completion of link training.

    :param iphy:
        *undescribed*
    :type iphy: struct isci_phy \*

    :param max_link_rate:
        This parameter specifies the maximum link rate to be
        associated with this phy.
    :type max_link_rate: enum sas_linkrate

    :param next_state:
        This parameter specifies the next state for the phy's starting
        sub-state machine.
    :type next_state: u32

.. _`isci_phy_control`:

isci_phy_control
================

.. c:function:: int isci_phy_control(struct asd_sas_phy *sas_phy, enum phy_func func, void *buf)

    This function is one of the SAS Domain Template functions. This is a phy management function.

    :param sas_phy:
        *undescribed*
    :type sas_phy: struct asd_sas_phy \*

    :param func:
        This parameter specifies the phy control function being invoked.
    :type func: enum phy_func

    :param buf:
        This parameter is specific to the phy function being invoked.
    :type buf: void \*

.. _`isci_phy_control.description`:

Description
-----------

status, zero indicates success.

.. This file was automatic generated / don't edit.

