.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_param.c

.. _`pch_gbe_validate_option`:

pch_gbe_validate_option
=======================

.. c:function:: int pch_gbe_validate_option(int *value, const struct pch_gbe_option *opt, struct pch_gbe_adapter *adapter)

    Validate option

    :param value:
        value
    :type value: int \*

    :param opt:
        option
    :type opt: const struct pch_gbe_option \*

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

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

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. _`pch_gbe_check_options`:

pch_gbe_check_options
=====================

.. c:function:: void pch_gbe_check_options(struct pch_gbe_adapter *adapter)

    Range Checking for Command Line Parameters

    :param adapter:
        Board private structure
    :type adapter: struct pch_gbe_adapter \*

.. This file was automatic generated / don't edit.

