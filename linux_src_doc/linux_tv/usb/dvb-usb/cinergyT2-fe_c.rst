.. -*- coding: utf-8; mode: rst -*-

==============
cinergyT2-fe.c
==============



.. _xref_compute_tps:

compute_tps
===========

.. c:function:: uint16_t compute_tps (struct dtv_frontend_properties * op)

    dvb frontend parameter set into TPS. See ETSI ETS-300744, section 4.6.2, table 9 for details.

    :param struct dtv_frontend_properties * op:

        _undescribed_



Description
-----------



 This function is probably reusable and may better get placed in a support
 library.


 We replace errornous fields by default TPS fields (the ones with value 0).


