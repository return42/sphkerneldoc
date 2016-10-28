.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/tcm_fc/tfc_sess.c

.. _`ft_prli`:

ft_prli
=======

.. c:function:: int ft_prli(struct fc_rport_priv *rdata, u32 spp_len, const struct fc_els_spp *rspp, struct fc_els_spp *spp)

    Handle incoming or outgoing PRLI for the FCP target

    :param struct fc_rport_priv \*rdata:
        remote port private

    :param u32 spp_len:
        service parameter page length

    :param const struct fc_els_spp \*rspp:
        received service parameter page (NULL for outgoing PRLI)

    :param struct fc_els_spp \*spp:
        response service parameter page

.. _`ft_prli.description`:

Description
-----------

Returns spp response code.

.. This file was automatic generated / don't edit.

