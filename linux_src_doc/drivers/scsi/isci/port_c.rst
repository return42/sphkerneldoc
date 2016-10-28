.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/port.c

.. _`sci_port_get_properties`:

sci_port_get_properties
=======================

.. c:function:: enum sci_status sci_port_get_properties(struct isci_port *iport, struct sci_port_properties *prop)

    This method simply returns the properties regarding the port, such as: physical index, protocols, sas address, etc.

    :param struct isci_port \*iport:
        *undescribed*

    :param struct sci_port_properties \*prop:
        *undescribed*

.. _`sci_port_get_properties.description`:

Description
-----------

Indicate if the user specified a valid port. SCI_SUCCESS This value is
returned if the specified port was valid. SCI_FAILURE_INVALID_PORT This
value is returned if the specified port is not valid.  When this value is
returned, no data is copied to the properties output parameter.

.. _`isci_port_link_down`:

isci_port_link_down
===================

.. c:function:: void isci_port_link_down(struct isci_host *isci_host, struct isci_phy *isci_phy, struct isci_port *isci_port)

    This function is called by the sci core when a link becomes inactive.

    :param struct isci_host \*isci_host:
        This parameter specifies the isci host object.

    :param struct isci_phy \*isci_phy:
        *undescribed*

    :param struct isci_port \*isci_port:
        *undescribed*

.. _`isci_port_hard_reset_complete`:

isci_port_hard_reset_complete
=============================

.. c:function:: void isci_port_hard_reset_complete(struct isci_port *isci_port, enum sci_status completion_status)

    This function is called by the sci core when the hard reset complete notification has been received.

    :param struct isci_port \*isci_port:
        *undescribed*

    :param enum sci_status completion_status:
        This parameter specifies the core status for the reset
        process.

.. _`sci_port_construct_dummy_rnc`:

sci_port_construct_dummy_rnc
============================

.. c:function:: void sci_port_construct_dummy_rnc(struct isci_port *iport, u16 rni)

    create dummy rnc for si workaround

    :param struct isci_port \*iport:
        *undescribed*

    :param u16 rni:
        remote node index for this remote node context.

.. _`sci_port_construct_dummy_rnc.description`:

Description
-----------

This routine will construct a dummy remote node context data structure
This structure will be posted to the hardware to work around a scheduler
error in the hardware.

.. _`sci_port_general_link_up_handler`:

sci_port_general_link_up_handler
================================

.. c:function:: void sci_port_general_link_up_handler(struct isci_port *iport, struct isci_phy *iphy, u8 flags)

    phy can be assigned to port?

    :param struct isci_port \*iport:
        *undescribed*

    :param struct isci_phy \*iphy:
        *undescribed*

    :param u8 flags:
        PF_RESUME, PF_NOTIFY to sci_port_activate_phy

.. _`sci_port_general_link_up_handler.description`:

Description
-----------

Determine if this phy can be assigned to this port . If the phy is
not a valid PHY for this port then the function will notify the user.
A PHY can only be part of a port if it's attached SAS ADDRESS is the
same as all other PHYs in the same port.

.. _`sci_port_is_wide`:

sci_port_is_wide
================

.. c:function:: bool sci_port_is_wide(struct isci_port *iport)

    If there are no phys or more than one phy then the method will return true.

    :param struct isci_port \*iport:
        *undescribed*

.. _`sci_port_is_wide.description`:

Description
-----------

bool true Is returned if this is a wide ported port. false Is returned if
this is a narrow port.

.. _`sci_port_link_detected`:

sci_port_link_detected
======================

.. c:function:: bool sci_port_link_detected(struct isci_port *iport, struct isci_phy *iphy)

    port wants the PHY to continue on to the link up state then the port layer must return true.  If the port object returns false the phy object must halt its attempt to go link up.

    :param struct isci_port \*iport:
        *undescribed*

    :param struct isci_phy \*iphy:
        *undescribed*

.. _`sci_port_link_detected.description`:

Description
-----------

true if the phy object can continue to the link up condition. true Is
returned if this phy can continue to the ready state. false Is returned if
can not continue on to the ready state. This notification is in place for
wide ports and direct attached phys.  Since there are no wide ported SATA
devices this could become an invalid port configuration.

.. _`sci_port_update_viit_entry`:

sci_port_update_viit_entry
==========================

.. c:function:: void sci_port_update_viit_entry(struct isci_port *iport)

    :param struct isci_port \*iport:
        *undescribed*

.. _`sci_port_update_viit_entry.description`:

Description
-----------



.. _`sci_port_post_dummy_request`:

sci_port_post_dummy_request
===========================

.. c:function:: void sci_port_post_dummy_request(struct isci_port *iport)

    post dummy/workaround request

    :param struct isci_port \*iport:
        *undescribed*

.. _`sci_port_post_dummy_request.description`:

Description
-----------

Prevent the hardware scheduler from posting new requests to the front
of the scheduler queue causing a starvation problem for currently
ongoing requests.

.. _`sci_port_abort_dummy_request`:

sci_port_abort_dummy_request
============================

.. c:function:: void sci_port_abort_dummy_request(struct isci_port *iport)

    power down parts of the silicon to save power.

    :param struct isci_port \*iport:
        *undescribed*

.. _`sci_port_add_phy`:

sci_port_add_phy
================

.. c:function:: enum sci_status sci_port_add_phy(struct isci_port *iport, struct isci_phy *iphy)

    :param struct isci_port \*iport:
        *undescribed*

    :param struct isci_phy \*iphy:
        *undescribed*

.. _`sci_port_add_phy.description`:

Description
-----------

This method will add a PHY to the selected port. This method returns an
enum sci_status. SCI_SUCCESS the phy has been added to the port. Any other
status is a failure to add the phy to the port.

.. _`sci_port_remove_phy`:

sci_port_remove_phy
===================

.. c:function:: enum sci_status sci_port_remove_phy(struct isci_port *iport, struct isci_phy *iphy)

    :param struct isci_port \*iport:
        *undescribed*

    :param struct isci_phy \*iphy:
        *undescribed*

.. _`sci_port_remove_phy.description`:

Description
-----------

This method will remove the PHY from the selected PORT. This method returns
an enum sci_status. SCI_SUCCESS the phy has been removed from the port. Any
other status is a failure to add the phy to the port.

.. This file was automatic generated / don't edit.

