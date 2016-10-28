.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_param.c

.. _`pch_gbe_validate_option`:

pch_gbe_validate_option
=======================

.. c:function:: int pch_gbe_validate_option(int *value, const struct pch_gbe_option *opt, struct pch_gbe_adapter *adapter)

    Validate option

    :param int \*value:
        value

    :param const struct pch_gbe_option \*opt:
        option

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_validate_option.return`:

Return
------

0:                      Successful.

.. _`pch_gbe_validate_option.negative-value`:

Negative value
--------------

Failed.

.. _`pch_gbe_check_copper_options`:

pch_gbe_check_copper_options
============================

.. c:function:: void pch_gbe_check_copper_options(struct pch_gbe_adapter *adapter)

    Range Checking for Link Options, Copper Version

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. _`pch_gbe_check_options`:

pch_gbe_check_options
=====================

.. c:function:: void pch_gbe_check_options(struct pch_gbe_adapter *adapter)

    Range Checking for Command Line Parameters

    :param struct pch_gbe_adapter \*adapter:
        Board private structure

.. This file was automatic generated / don't edit.

