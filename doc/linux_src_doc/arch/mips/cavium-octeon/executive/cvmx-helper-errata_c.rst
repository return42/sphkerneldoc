.. -*- coding: utf-8; mode: rst -*-

====================
cvmx-helper-errata.c
====================


.. _`__cvmx_helper_errata_qlm_disable_2nd_order_cdr`:

__cvmx_helper_errata_qlm_disable_2nd_order_cdr
==============================================

.. c:function:: void __cvmx_helper_errata_qlm_disable_2nd_order_cdr (int qlm)

    720, the 2nd order CDR circuit on CN52XX pass 1 doesn't work properly. The following code disables 2nd order CDR for the specified QLM.

    :param int qlm:
        QLM to disable 2nd order CDR for.

