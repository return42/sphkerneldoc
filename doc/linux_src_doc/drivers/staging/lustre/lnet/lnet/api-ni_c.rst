.. -*- coding: utf-8; mode: rst -*-

========
api-ni.c
========


.. _`lnet_lib_init`:

lnet_lib_init
=============

.. c:function:: int lnet_lib_init ( void)

    :param void:
        no arguments



.. _`lnet_lib_init.description`:

Description
-----------


Automatically called at module loading time. Caller has to call
:c:func:`lnet_lib_exit` after a call to :c:func:`lnet_lib_init`, if and only if the
latter returned 0. It must be called exactly once.

\retval 0 on success
\retval -ve on failures.



.. _`lnet_lib_exit`:

lnet_lib_exit
=============

.. c:function:: void lnet_lib_exit ( void)

    :param void:
        no arguments



.. _`lnet_lib_exit.description`:

Description
-----------


\pre :c:func:`lnet_lib_init` called with success.
\pre All LNet users called :c:func:`LNetNIFini` for matching :c:func:`LNetNIInit` calls.



.. _`lnetniinit`:

LNetNIInit
==========

.. c:function:: int LNetNIInit (lnet_pid_t requested_pid)

    :param lnet_pid_t requested_pid:

        *undescribed*



.. _`lnetniinit.description`:

Description
-----------


Users must call this function at least once before any other functions.
For each successful call there must be a corresponding call to
:c:func:`LNetNIFini`. For subsequent calls to :c:func:`LNetNIInit`, \a requested_pid is
ignored.

The PID used by LNet may be different from the one requested.
See :c:func:`LNetGetId`.

\param requested_pid PID requested by the caller.

\return >= 0 on success, and < 0 error code on failures.



.. _`lnetnifini`:

LNetNIFini
==========

.. c:function:: int LNetNIFini ( void)

    :param void:
        no arguments



.. _`lnetnifini.description`:

Description
-----------


Users must call this function once for each successful call to :c:func:`LNetNIInit`.
Once the :c:func:`LNetNIFini` operation has been started, the results of pending
API operations are undefined.

\return always 0 for current implementation.



.. _`lnet_fill_ni_info`:

lnet_fill_ni_info
=================

.. c:function:: void lnet_fill_ni_info (struct lnet_ni *ni, __u32 *cpt_count, __u64 *nid, int *peer_timeout, int *peer_tx_credits, int *peer_rtr_credits, int *max_tx_credits, struct lnet_ioctl_net_config *net_config)

    :param struct lnet_ni \*ni:

        *undescribed*

    :param __u32 \*cpt_count:

        *undescribed*

    :param __u64 \*nid:

        *undescribed*

    :param int \*peer_timeout:

        *undescribed*

    :param int \*peer_tx_credits:

        *undescribed*

    :param int \*peer_rtr_credits:

        *undescribed*

    :param int \*max_tx_credits:

        *undescribed*

    :param struct lnet_ioctl_net_config \*net_config:

        *undescribed*



.. _`lnet_fill_ni_info.description`:

Description
-----------

parameters

\param[in] ni network       interface structure
\param[out] cpt_count       the number of cpts the ni is on
\param[out] nid             Network Interface ID
\param[out] peer_timeout    NI peer timeout
\param[out] peer_tx_crdits  NI peer transmit credits
\param[out] peer_rtr_credits NI peer router credits
\param[out] max_tx_credits  NI max transmit credit
\param[out] net_config      Network configuration



.. _`lnetctl`:

LNetCtl
=======

.. c:function:: int LNetCtl (unsigned int cmd, void *arg)

    :param unsigned int cmd:

        *undescribed*

    :param void \*arg:

        *undescribed*



.. _`lnetgetid`:

LNetGetId
=========

.. c:function:: int LNetGetId (unsigned int index, lnet_process_id_t *id)

    :param unsigned int index:

        *undescribed*

    :param lnet_process_id_t \*id:

        *undescribed*



.. _`lnetgetid.description`:

Description
-----------


all interfaces share a same PID, as requested by :c:func:`LNetNIInit`.

\param index Index of the interface to look up.
\param id On successful return, this location will hold the
lnet_process_id_t ID of the interface.

\retval 0 If an interface exists at \a index.
\retval -ENOENT If no interface has been found.



.. _`lnetsnprinthandle`:

LNetSnprintHandle
=================

.. c:function:: void LNetSnprintHandle (char *str, int len, lnet_handle_any_t h)

    :param char \*str:

        *undescribed*

    :param int len:

        *undescribed*

    :param lnet_handle_any_t h:

        *undescribed*



.. _`lnetsnprinthandle.description`:

Description
-----------

\a len bytes.

