.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_npiv.c

.. _`libfc_vport_create`:

libfc_vport_create
==================

.. c:function:: struct fc_lport *libfc_vport_create(struct fc_vport *vport, int privsize)

    Create a new NPIV vport instance

    :param vport:
        fc_vport structure from scsi_transport_fc
    :type vport: struct fc_vport \*

    :param privsize:
        driver private data size to allocate along with the Scsi_Host
    :type privsize: int

.. _`fc_vport_id_lookup`:

fc_vport_id_lookup
==================

.. c:function:: struct fc_lport *fc_vport_id_lookup(struct fc_lport *n_port, u32 port_id)

    find NPIV lport that matches a given fabric ID

    :param n_port:
        Top level N_Port which may have multiple NPIV VN_Ports
    :type n_port: struct fc_lport \*

    :param port_id:
        Fabric ID to find a match for
    :type port_id: u32

.. _`fc_vport_id_lookup.return`:

Return
------

matching lport pointer or NULL if there is no match

.. _`__fc_vport_setlink`:

\__fc_vport_setlink
===================

.. c:function:: void __fc_vport_setlink(struct fc_lport *n_port, struct fc_lport *vn_port)

    update link and status on a VN_Port

    :param n_port:
        parent N_Port
    :type n_port: struct fc_lport \*

    :param vn_port:
        VN_Port to update
    :type vn_port: struct fc_lport \*

.. _`__fc_vport_setlink.locking`:

Locking
-------

must be called with both the N_Port and VN_Port lp_mutex held

.. _`fc_vport_setlink`:

fc_vport_setlink
================

.. c:function:: void fc_vport_setlink(struct fc_lport *vn_port)

    update link and status on a VN_Port

    :param vn_port:
        virtual port to update
    :type vn_port: struct fc_lport \*

.. _`fc_vports_linkchange`:

fc_vports_linkchange
====================

.. c:function:: void fc_vports_linkchange(struct fc_lport *n_port)

    change the link state of all vports

    :param n_port:
        Parent N_Port that has changed state
    :type n_port: struct fc_lport \*

.. _`fc_vports_linkchange.locking`:

Locking
-------

called with the n_port lp_mutex held

.. This file was automatic generated / don't edit.

