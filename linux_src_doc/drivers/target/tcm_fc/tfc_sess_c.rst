.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/tcm_fc/tfc_sess.c

.. _`ft_prli`:

ft_prli
=======

.. c:function:: int ft_prli(struct fc_rport_priv *rdata, u32 spp_len, const struct fc_els_spp *rspp, struct fc_els_spp *spp)

    Handle incoming or outgoing PRLI for the FCP target

    :param rdata:
        remote port private
    :type rdata: struct fc_rport_priv \*

    :param spp_len:
        service parameter page length
    :type spp_len: u32

    :param rspp:
        received service parameter page (NULL for outgoing PRLI)
    :type rspp: const struct fc_els_spp \*

    :param spp:
        response service parameter page
    :type spp: struct fc_els_spp \*

.. _`ft_prli.description`:

Description
-----------

Returns spp response code.

.. This file was automatic generated / don't edit.

