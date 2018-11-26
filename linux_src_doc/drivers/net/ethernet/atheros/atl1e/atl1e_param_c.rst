.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/atheros/atl1e/atl1e_param.c

.. _`atl1e_check_options`:

atl1e_check_options
===================

.. c:function:: void atl1e_check_options(struct atl1e_adapter *adapter)

    Range Checking for Command Line Parameters

    :param adapter:
        board private structure
    :type adapter: struct atl1e_adapter \*

.. _`atl1e_check_options.description`:

Description
-----------

This routine checks all command line parameters for valid user
input.  If an invalid value is given, or if no user specified
value exists, a default value is used.  The final value is stored
in a variable in the adapter structure.

.. This file was automatic generated / don't edit.

