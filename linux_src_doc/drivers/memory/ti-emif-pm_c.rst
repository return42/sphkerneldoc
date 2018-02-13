.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/ti-emif-pm.c

.. _`ti_emif_copy_pm_function_table`:

ti_emif_copy_pm_function_table
==============================

.. c:function:: int ti_emif_copy_pm_function_table(struct gen_pool *sram_pool, void *dst)

    copy mapping of pm funcs in sram

    :param struct gen_pool \*sram_pool:
        pointer to struct gen_pool where dst resides

    :param void \*dst:
        void \* to address that table should be copied

.. _`ti_emif_copy_pm_function_table.description`:

Description
-----------

Returns 0 if success other error code if table is not available

.. _`ti_emif_get_mem_type`:

ti_emif_get_mem_type
====================

.. c:function:: int ti_emif_get_mem_type( void)

    return type for memory type in use

    :param  void:
        no arguments

.. _`ti_emif_get_mem_type.description`:

Description
-----------

Returns memory type value read from EMIF or error code if fails

.. This file was automatic generated / don't edit.

