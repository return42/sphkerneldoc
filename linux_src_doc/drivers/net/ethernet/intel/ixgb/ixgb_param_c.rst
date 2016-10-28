.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgb/ixgb_param.c

.. _`ixgb_check_options`:

ixgb_check_options
==================

.. c:function:: void ixgb_check_options(struct ixgb_adapter *adapter)

    Range Checking for Command Line Parameters

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_check_options.description`:

Description
-----------

This routine checks all command line parameters for valid user
input.  If an invalid value is given, or if no user specified
value exists, a default value is used.  The final value is stored
in a variable in the adapter structure.

.. This file was automatic generated / don't edit.

