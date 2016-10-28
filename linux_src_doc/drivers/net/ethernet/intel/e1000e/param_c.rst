.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/param.c

.. _`e1000e_check_options`:

e1000e_check_options
====================

.. c:function:: void e1000e_check_options(struct e1000_adapter *adapter)

    Range Checking for Command Line Parameters

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000e_check_options.description`:

Description
-----------

This routine checks all command line parameters for valid user
input.  If an invalid value is given, or if no user specified
value exists, a default value is used.  The final value is stored
in a variable in the adapter structure.

.. This file was automatic generated / don't edit.

