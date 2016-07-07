.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_disc.c

.. _`fc_disc_stop_rports`:

fc_disc_stop_rports
===================

.. c:function:: void fc_disc_stop_rports(struct fc_disc *disc)

    Delete all the remote ports associated with the lport

    :param struct fc_disc \*disc:
        The discovery job to stop remote ports on

.. _`fc_disc_stop_rports.locking-note`:

Locking Note
------------

This function expects that the lport mutex is locked before
calling it.

.. _`fc_disc_recv_rscn_req`:

fc_disc_recv_rscn_req
=====================

.. c:function:: void fc_disc_recv_rscn_req(struct fc_disc *disc, struct fc_frame *fp)

    Handle Registered State Change Notification (RSCN)

    :param struct fc_disc \*disc:
        The discovery object to which the RSCN applies

    :param struct fc_frame \*fp:
        The RSCN frame

.. _`fc_disc_recv_rscn_req.locking-note`:

Locking Note
------------

This function expects that the disc_mutex is locked
before it is called.

.. _`fc_disc_recv_req`:

fc_disc_recv_req
================

.. c:function:: void fc_disc_recv_req(struct fc_lport *lport, struct fc_frame *fp)

    Handle incoming requests

    :param struct fc_lport \*lport:
        The local port receiving the request

    :param struct fc_frame \*fp:
        The request frame

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

    :param struct fc_disc \*disc:
        The discovery object to be restarted

.. _`fc_disc_restart.locking-note`:

Locking Note
------------

This function expects that the disc mutex
is already locked.

.. _`fc_disc_start`:

fc_disc_start
=============

.. c:function:: void fc_disc_start(void (*) disc_callback (struct fc_lport *, enum fc_disc_event, struct fc_lport *lport)

    Start discovery on a local port

    :param (void (\*) disc_callback (struct fc_lport \*, enum fc_disc_event):
        Callback function to be called when discovery is complete

    :param struct fc_lport \*lport:
        The local port to have discovery started on

.. _`fc_disc_done`:

fc_disc_done
============

.. c:function:: void fc_disc_done(struct fc_disc *disc, enum fc_disc_event event)

    Discovery has been completed

    :param struct fc_disc \*disc:
        The discovery context

    :param enum fc_disc_event event:
        The discovery completion status

.. _`fc_disc_done.locking-note`:

Locking Note
------------

This function expects that the disc mutex is locked before
it is called. The discovery callback is then made with the lock released,
and the lock is re-taken before returning from this function

.. _`fc_disc_error`:

fc_disc_error
=============

.. c:function:: void fc_disc_error(struct fc_disc *disc, struct fc_frame *fp)

    Handle error on dNS request

    :param struct fc_disc \*disc:
        The discovery context

    :param struct fc_frame \*fp:
        The error code encoded as a frame pointer

.. _`fc_disc_gpn_ft_req`:

fc_disc_gpn_ft_req
==================

.. c:function:: void fc_disc_gpn_ft_req(struct fc_disc *disc)

    Send Get Port Names by FC-4 type (GPN_FT) request

    :param struct fc_disc \*disc:
        *undescribed*

.. _`fc_disc_gpn_ft_req.locking-note`:

Locking Note
------------

This function expects that the disc_mutex is locked
before it is called.

.. _`fc_disc_gpn_ft_parse`:

fc_disc_gpn_ft_parse
====================

.. c:function:: int fc_disc_gpn_ft_parse(struct fc_disc *disc, void *buf, size_t len)

    Parse the body of the dNS GPN_FT response.

    :param struct fc_disc \*disc:
        *undescribed*

    :param void \*buf:
        The GPN_FT response buffer

    :param size_t len:
        The size of response buffer

.. _`fc_disc_gpn_ft_parse.description`:

Description
-----------

Goes through the list of IDs and names resulting from a request.

.. _`fc_disc_timeout`:

fc_disc_timeout
===============

.. c:function:: void fc_disc_timeout(struct work_struct *work)

    Handler for discovery timeouts

    :param struct work_struct \*work:
        Structure holding discovery context that needs to retry discovery

.. _`fc_disc_gpn_ft_resp`:

fc_disc_gpn_ft_resp
===================

.. c:function:: void fc_disc_gpn_ft_resp(struct fc_seq *sp, struct fc_frame *fp, void *disc_arg)

    Handle a response frame from Get Port Names (GPN_FT)

    :param struct fc_seq \*sp:
        The sequence that the GPN_FT response was received on

    :param struct fc_frame \*fp:
        The GPN_FT response frame

    :param void \*disc_arg:
        *undescribed*

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

    :param struct fc_seq \*sp:
        The sequence the GPN_ID is on

    :param struct fc_frame \*fp:
        The response frame

    :param void \*rdata_arg:
        The remote port that sent the GPN_ID response

.. _`fc_disc_gpn_id_resp.locking-note`:

Locking Note
------------

This function is called without disc mutex held.

.. _`fc_disc_gpn_id_req`:

fc_disc_gpn_id_req
==================

.. c:function:: int fc_disc_gpn_id_req(struct fc_lport *lport, struct fc_rport_priv *rdata)

    Send Get Port Names by ID (GPN_ID) request

    :param struct fc_lport \*lport:
        The local port to initiate discovery on

    :param struct fc_rport_priv \*rdata:
        remote port private data

.. _`fc_disc_gpn_id_req.locking-note`:

Locking Note
------------

This function expects that the disc_mutex is locked
before it is called.
On failure, an error code is returned.

.. _`fc_disc_single`:

fc_disc_single
==============

.. c:function:: int fc_disc_single(struct fc_lport *lport, struct fc_disc_port *dp)

    Discover the directory information for a single target

    :param struct fc_lport \*lport:
        The local port the remote port is associated with

    :param struct fc_disc_port \*dp:
        The port to rediscover

.. _`fc_disc_single.locking-note`:

Locking Note
------------

This function expects that the disc_mutex is locked
before it is called.

.. _`fc_disc_stop`:

fc_disc_stop
============

.. c:function:: void fc_disc_stop(struct fc_lport *lport)

    Stop discovery for a given lport

    :param struct fc_lport \*lport:
        The local port that discovery should stop on

.. _`fc_disc_stop_final`:

fc_disc_stop_final
==================

.. c:function:: void fc_disc_stop_final(struct fc_lport *lport)

    Stop discovery for a given lport

    :param struct fc_lport \*lport:
        The lport that discovery should stop on

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

    :param struct fc_lport \*lport:
        The local port that needs the discovery layer to be configured

    :param void \*priv:
        Private data structre for users of the discovery layer

.. _`fc_disc_init`:

fc_disc_init
============

.. c:function:: void fc_disc_init(struct fc_lport *lport)

    Initialize the discovery layer for a local port

    :param struct fc_lport \*lport:
        The local port that needs the discovery layer to be initialized

.. This file was automatic generated / don't edit.

