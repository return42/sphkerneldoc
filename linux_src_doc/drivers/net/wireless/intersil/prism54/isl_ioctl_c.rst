.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intersil/prism54/isl_ioctl.c

.. _`prism54_mib_mode_helper`:

prism54_mib_mode_helper
=======================

.. c:function:: int prism54_mib_mode_helper(islpci_private *priv, u32 iw_mode)

    MIB change mode helper function

    :param islpci_private \*priv:
        *undescribed*

    :param u32 iw_mode:
        new mode (%IW_MODE\_\*)

.. _`prism54_mib_mode_helper.description`:

Description
-----------

This is a helper function, hence it does not lock. Make sure
caller deals with locking \*if\* necessary. This function sets the
mode-dependent mib values and does the mapping of the Linux
Wireless API modes to Device firmware modes. It also checks for
correct valid Linux wireless modes.

.. _`prism54_mib_init`:

prism54_mib_init
================

.. c:function:: void prism54_mib_init(islpci_private *priv)

    fill MIB cache with defaults

    :param islpci_private \*priv:
        *undescribed*

.. _`prism54_mib_init.description`:

Description
-----------

this function initializes the struct given as \ ``mib``\  with defaults,
of which many are retrieved from the global module parameter
variables.

.. This file was automatic generated / don't edit.

