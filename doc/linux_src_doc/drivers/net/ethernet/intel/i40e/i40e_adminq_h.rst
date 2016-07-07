.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_adminq.h

.. _`i40e_aq_rc_to_posix`:

i40e_aq_rc_to_posix
===================

.. c:function:: int i40e_aq_rc_to_posix(int aq_ret, int aq_rc)

    convert errors to user-land codes

    :param int aq_ret:
        *undescribed*

    :param int aq_rc:
        *undescribed*

.. _`i40e_aq_rc_to_posix.aq_ret`:

aq_ret
------

AdminQ handler error code can override aq_rc

.. _`i40e_aq_rc_to_posix.aq_rc`:

aq_rc
-----

AdminQ firmware error code to convert

.. This file was automatic generated / don't edit.

