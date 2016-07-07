.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/dvb-usb/cinergyT2-fe.c

.. _`compute_tps`:

compute_tps
===========

.. c:function:: uint16_t compute_tps(struct dtv_frontend_properties *op)

    dvb frontend parameter set into TPS. See ETSI ETS-300744, section 4.6.2, table 9 for details.

    :param struct dtv_frontend_properties \*op:
        *undescribed*

.. _`compute_tps.description`:

Description
-----------

This function is probably reusable and may better get placed in a support
library.

We replace errornous fields by default TPS fields (the ones with value 0).

.. This file was automatic generated / don't edit.

