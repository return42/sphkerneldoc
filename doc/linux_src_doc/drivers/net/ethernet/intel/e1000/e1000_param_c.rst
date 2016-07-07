.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000/e1000_param.c

.. _`e1000_check_options`:

e1000_check_options
===================

.. c:function:: void e1000_check_options(struct e1000_adapter *adapter)

    Range Checking for Command Line Parameters

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_check_options.description`:

Description
-----------

This routine checks all command line parameters for valid user
input.  If an invalid value is given, or if no user specified
value exists, a default value is used.  The final value is stored
in a variable in the adapter structure.

.. _`e1000_check_fiber_options`:

e1000_check_fiber_options
=========================

.. c:function:: void e1000_check_fiber_options(struct e1000_adapter *adapter)

    Range Checking for Link Options, Fiber Version

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_check_fiber_options.description`:

Description
-----------

Handles speed and duplex options on fiber adapters

.. _`e1000_check_copper_options`:

e1000_check_copper_options
==========================

.. c:function:: void e1000_check_copper_options(struct e1000_adapter *adapter)

    Range Checking for Link Options, Copper Version

    :param struct e1000_adapter \*adapter:
        board private structure

.. _`e1000_check_copper_options.description`:

Description
-----------

Handles speed and duplex options on copper adapters

.. This file was automatic generated / don't edit.

