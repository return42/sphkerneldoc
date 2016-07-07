.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libsas/sas_port.c

.. _`sas_form_port`:

sas_form_port
=============

.. c:function:: void sas_form_port(struct asd_sas_phy *phy)

    - add this phy to a port

    :param struct asd_sas_phy \*phy:
        the phy of interest

.. _`sas_form_port.description`:

Description
-----------

This function adds this phy to an existing port, thus creating a wide
port, or it creates a port and adds the phy to the port.

.. _`sas_deform_port`:

sas_deform_port
===============

.. c:function:: void sas_deform_port(struct asd_sas_phy *phy, int gone)

    - remove this phy from the port it belongs to

    :param struct asd_sas_phy \*phy:
        the phy of interest

    :param int gone:
        *undescribed*

.. _`sas_deform_port.description`:

Description
-----------

This is called when the physical link to the other phy has been
lost (on this phy), in Event thread context. We cannot delay here.

.. This file was automatic generated / don't edit.

