.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_disc.c

.. _`fc_disc_stop_rports`:

fc_disc_stop_rports
===================

.. c:function:: void fc_disc_stop_rports(struct fc_disc *disc)

    Delete all the remote ports associated with the lport

    :param disc:
        The discovery job to stop remote ports on
    :type disc: struct fc_disc \*

.. _`fc_disc_recv_rscn_req`:

fc_disc_recv_rscn_req
=====================

.. c:function:: void fc_disc_recv_rscn_req(struct fc_disc *disc, struct fc_frame *fp)

    Handle Registered State Change Notification (RSCN)

    :param disc:
        The discovery object to which the RSCN applies
    :type disc: struct fc_disc \*

    :param fp:
        The RSCN frame
    :type fp: struct fc_frame \*

.. _`fc_disc_recv_req`:

fc_disc_recv_req
================

.. c:function:: void fc_disc_recv_req(struct fc_lport *lport, struct fc_frame *fp)

    Handle incoming requests

    :param lport:
        The local port receiving the request
    :type lport: struct fc_lport \*

    :param fp:
        The request frame
    :type fp: struct fc_frame \*

.. _`fc_disc_recv_req.locking-note`:

Locking Note
------------

This function is called from the EM and will lock
the disc_mutex before calling the handler for the
request.

.. _`fc_disc_restart`:

fc_disc_restart
===============

.. c:function:: void fc_disc_restart(struct fc_disc *disc)

    Restart discovery

    :param disc:
        The discovery object to be restarted
    :type disc: struct fc_disc \*

.. _`fc_disc_start`:

fc_disc_start
=============

.. c:function:: void fc_disc_start(void (*disc_callback)(struct fc_lport *, enum fc_disc_event), struct fc_lport *lport)

    Start discovery on a local port

    :param void (\*disc_callback)(struct fc_lport \*, enum fc_disc_event):
        Callback function to be called when discovery is complete

    :param lport:
        The local port to have discovery started on
    :type lport: struct fc_lport \*

.. _`fc_disc_done`:

fc_disc_done
============

.. c:function:: void fc_disc_done(struct fc_disc *disc, enum fc_disc_event event)

    Discovery has been completed

    :param disc:
        The discovery context
    :type disc: struct fc_disc \*

    :param event:
        The discovery completion status
    :type event: enum fc_disc_event

.. _`fc_disc_error`:

fc_disc_error
=============

.. c:function:: void fc_disc_error(struct fc_disc *disc, struct fc_frame *fp)

    Handle error on dNS request

    :param disc:
        The discovery context
    :type disc: struct fc_disc \*

    :param fp:
        The error code encoded as a frame pointer
    :type fp: struct fc_frame \*

.. _`fc_disc_gpn_ft_req`:

fc_disc_gpn_ft_req
==================

.. c:function:: void fc_disc_gpn_ft_req(struct fc_disc *disc)

    Send Get Port Names by FC-4 type (GPN_FT) request

    :param disc:
        *undescribed*
    :type disc: struct fc_disc \*

.. _`fc_disc_gpn_ft_parse`:

fc_disc_gpn_ft_parse
====================

.. c:function:: int fc_disc_gpn_ft_parse(struct fc_disc *disc, void *buf, size_t len)

    Parse the body of the dNS GPN_FT response.

    :param disc:
        *undescribed*
    :type disc: struct fc_disc \*

    :param buf:
        The GPN_FT response buffer
    :type buf: void \*

    :param len:
        The size of response buffer
    :type len: size_t

.. _`fc_disc_gpn_ft_parse.description`:

Description
-----------

Goes through the list of IDs and names resulting from a request.

.. _`fc_disc_timeout`:

fc_disc_timeout
===============

.. c:function:: void fc_disc_timeout(struct work_struct *work)

    Handler for discovery timeouts

    :param work:
        Structure holding discovery context that needs to retry discovery
    :type work: struct work_struct \*

.. _`fc_disc_gpn_ft_resp`:

fc_disc_gpn_ft_resp
===================

.. c:function:: void fc_disc_gpn_ft_resp(struct fc_seq *sp, struct fc_frame *fp, void *disc_arg)

    Handle a response frame from Get Port Names (GPN_FT)

    :param sp:
        The sequence that the GPN_FT response was received on
    :type sp: struct fc_seq \*

    :param fp:
        The GPN_FT response frame
    :type fp: struct fc_frame \*

    :param disc_arg:
        *undescribed*
    :type disc_arg: void \*

.. _`fc_disc_gpn_ft_resp.locking-note`:

Locking Note
------------

This function is called without disc mutex held, and
should do all its processing with the mutex held

.. _`fc_disc_gpn_id_resp`:

fc_disc_gpn_id_resp
===================

.. c:function:: void fc_disc_gpn_id_resp(struct fc_seq *sp, struct fc_frame *fp, void *rdata_arg)

    Handle a response frame from Get Port Names (GPN_ID)

    :param sp:
        The sequence the GPN_ID is on
    :type sp: struct fc_seq \*

    :param fp:
        The response frame
    :type fp: struct fc_frame \*

    :param rdata_arg:
        The remote port that sent the GPN_ID response
    :type rdata_arg: void \*

.. _`fc_disc_gpn_id_resp.locking-note`:

Locking Note
------------

This function is called without disc mutex held.

.. _`fc_disc_gpn_id_req`:

fc_disc_gpn_id_req
==================

.. c:function:: int fc_disc_gpn_id_req(struct fc_lport *lport, struct fc_rport_priv *rdata)

    Send Get Port Names by ID (GPN_ID) request

    :param lport:
        The local port to initiate discovery on
    :type lport: struct fc_lport \*

    :param rdata:
        remote port private data
    :type rdata: struct fc_rport_priv \*

.. _`fc_disc_gpn_id_req.description`:

Description
-----------

On failure, an error code is returned.

.. _`fc_disc_single`:

fc_disc_single
==============

.. c:function:: int fc_disc_single(struct fc_lport *lport, struct fc_disc_port *dp)

    Discover the directory information for a single target

    :param lport:
        The local port the remote port is associated with
    :type lport: struct fc_lport \*

    :param dp:
        The port to rediscover
    :type dp: struct fc_disc_port \*

.. _`fc_disc_stop`:

fc_disc_stop
============

.. c:function:: void fc_disc_stop(struct fc_lport *lport)

    Stop discovery for a given lport

    :param lport:
        The local port that discovery should stop on
    :type lport: struct fc_lport \*

.. _`fc_disc_stop_final`:

fc_disc_stop_final
==================

.. c:function:: void fc_disc_stop_final(struct fc_lport *lport)

    Stop discovery for a given lport

    :param lport:
        The lport that discovery should stop on
    :type lport: struct fc_lport \*

.. _`fc_disc_stop_final.description`:

Description
-----------

This function will block until discovery has been
completely stopped and all rports have been deleted.

.. _`fc_disc_config`:

fc_disc_config
==============

.. c:function:: void fc_disc_config(struct fc_lport *lport, void *priv)

    Configure the discovery layer for a local port

    :param lport:
        The local port that needs the discovery layer to be configured
    :type lport: struct fc_lport \*

    :param priv:
        Private data structre for users of the discovery layer
    :type priv: void \*

.. _`fc_disc_init`:

fc_disc_init
============

.. c:function:: void fc_disc_init(struct fc_lport *lport)

    Initialize the discovery layer for a local port

    :param lport:
        The local port that needs the discovery layer to be initialized
    :type lport: struct fc_lport \*

.. This file was automatic generated / don't edit.

