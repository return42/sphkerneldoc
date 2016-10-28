.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_diag.c

.. _`i40e_diag_reg_pattern_test`:

i40e_diag_reg_pattern_test
==========================

.. c:function:: i40e_status i40e_diag_reg_pattern_test(struct i40e_hw *hw, u32 reg, u32 mask)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u32 reg:
        reg to be tested

    :param u32 mask:
        bits to be touched

.. _`i40e_diag_reg_test`:

i40e_diag_reg_test
==================

.. c:function:: i40e_status i40e_diag_reg_test(struct i40e_hw *hw)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

.. _`i40e_diag_reg_test.description`:

Description
-----------

Perform registers diagnostic test

.. _`i40e_diag_eeprom_test`:

i40e_diag_eeprom_test
=====================

.. c:function:: i40e_status i40e_diag_eeprom_test(struct i40e_hw *hw)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

.. _`i40e_diag_eeprom_test.description`:

Description
-----------

Perform EEPROM diagnostic test

.. This file was automatic generated / don't edit.

