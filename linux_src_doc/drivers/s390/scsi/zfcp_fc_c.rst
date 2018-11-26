.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_fc.c

.. _`zfcp_fc_post_event`:

zfcp_fc_post_event
==================

.. c:function:: void zfcp_fc_post_event(struct work_struct *work)

    post event to userspace via fc_transport

    :param work:
        work struct with enqueued events
    :type work: struct work_struct \*

.. _`zfcp_fc_enqueue_event`:

zfcp_fc_enqueue_event
=====================

.. c:function:: void zfcp_fc_enqueue_event(struct zfcp_adapter *adapter, enum fc_host_event_code event_code, u32 event_data)

    safely enqueue FC HBA API event from irq context

    :param adapter:
        The adapter where to enqueue the event
    :type adapter: struct zfcp_adapter \*

    :param event_code:
        The event code (as defined in fc_host_event_code in
        scsi_transport_fc.h)
    :type event_code: enum fc_host_event_code

    :param event_data:
        The event data (e.g. n_port page in case of els)
    :type event_data: u32

.. _`zfcp_fc_incoming_els`:

zfcp_fc_incoming_els
====================

.. c:function:: void zfcp_fc_incoming_els(struct zfcp_fsf_req *fsf_req)

    handle incoming ELS \ ``fsf_req``\  - request which contains incoming ELS

    :param fsf_req:
        *undescribed*
    :type fsf_req: struct zfcp_fsf_req \*

.. _`zfcp_fc_ns_gid_pn`:

zfcp_fc_ns_gid_pn
=================

.. c:function:: int zfcp_fc_ns_gid_pn(struct zfcp_port *port)

    initiate GID_PN nameserver request

    :param port:
        port where GID_PN request is needed
    :type port: struct zfcp_port \*

.. _`zfcp_fc_ns_gid_pn.return`:

Return
------

-ENOMEM on error, 0 otherwise

.. _`zfcp_fc_trigger_did_lookup`:

zfcp_fc_trigger_did_lookup
==========================

.. c:function:: void zfcp_fc_trigger_did_lookup(struct zfcp_port *port)

    trigger the d_id lookup using a GID_PN request

    :param port:
        The zfcp_port to lookup the d_id for.
    :type port: struct zfcp_port \*

.. _`zfcp_fc_plogi_evaluate`:

zfcp_fc_plogi_evaluate
======================

.. c:function:: void zfcp_fc_plogi_evaluate(struct zfcp_port *port, struct fc_els_flogi *plogi)

    evaluate PLOGI playload

    :param port:
        zfcp_port structure
    :type port: struct zfcp_port \*

    :param plogi:
        plogi payload
    :type plogi: struct fc_els_flogi \*

.. _`zfcp_fc_plogi_evaluate.description`:

Description
-----------

Evaluate PLOGI playload and copy important fields into zfcp_port structure

.. _`zfcp_fc_test_link`:

zfcp_fc_test_link
=================

.. c:function:: void zfcp_fc_test_link(struct zfcp_port *port)

    lightweight link test procedure

    :param port:
        port to be tested
    :type port: struct zfcp_port \*

.. _`zfcp_fc_test_link.description`:

Description
-----------

Test status of a link to a remote port using the ELS command ADISC.
If there is a problem with the remote port, error recovery steps
will be triggered.

.. _`zfcp_fc_scan_ports`:

zfcp_fc_scan_ports
==================

.. c:function:: void zfcp_fc_scan_ports(struct work_struct *work)

    scan remote ports and attach new ports

    :param work:
        reference to scheduled work
    :type work: struct work_struct \*

.. _`zfcp_fc_sym_name_update`:

zfcp_fc_sym_name_update
=======================

.. c:function:: void zfcp_fc_sym_name_update(struct work_struct *work)

    Retrieve and update the symbolic port name

    :param work:
        ns_up_work of the adapter where to update the symbolic port name
    :type work: struct work_struct \*

.. _`zfcp_fc_sym_name_update.description`:

Description
-----------

Retrieve the current symbolic port name that may have been set by
the hardware using the GSPN request and update the fc_host
symbolic_name sysfs attribute. When running in NPIV mode (and hence
the port name is unique for this system), update the symbolic port
name to add Linux specific information and update the FC nameserver
using the RSPN request.

.. This file was automatic generated / don't edit.

