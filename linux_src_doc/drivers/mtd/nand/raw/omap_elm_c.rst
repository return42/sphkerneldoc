.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/omap_elm.c

.. _`elm_config`:

elm_config
==========

.. c:function:: int elm_config(struct device *dev, enum bch_ecc bch_type, int ecc_steps, int ecc_step_size, int ecc_syndrome_size)

    Configure ELM module

    :param dev:
        ELM device
    :type dev: struct device \*

    :param bch_type:
        Type of BCH ecc
    :type bch_type: enum bch_ecc

    :param ecc_steps:
        *undescribed*
    :type ecc_steps: int

    :param ecc_step_size:
        *undescribed*
    :type ecc_step_size: int

    :param ecc_syndrome_size:
        *undescribed*
    :type ecc_syndrome_size: int

.. _`elm_configure_page_mode`:

elm_configure_page_mode
=======================

.. c:function:: void elm_configure_page_mode(struct elm_info *info, int index, bool enable)

    Enable/Disable page mode

    :param info:
        elm info
    :type info: struct elm_info \*

    :param index:
        index number of syndrome fragment vector
    :type index: int

    :param enable:
        enable/disable flag for page mode
    :type enable: bool

.. _`elm_configure_page_mode.description`:

Description
-----------

Enable page mode for syndrome fragment index

.. _`elm_load_syndrome`:

elm_load_syndrome
=================

.. c:function:: void elm_load_syndrome(struct elm_info *info, struct elm_errorvec *err_vec, u8 *ecc)

    Load ELM syndrome reg

    :param info:
        elm info
    :type info: struct elm_info \*

    :param err_vec:
        elm error vectors
    :type err_vec: struct elm_errorvec \*

    :param ecc:
        buffer with calculated ecc
    :type ecc: u8 \*

.. _`elm_load_syndrome.description`:

Description
-----------

Load syndrome fragment registers with calculated ecc in reverse order.

.. _`elm_start_processing`:

elm_start_processing
====================

.. c:function:: void elm_start_processing(struct elm_info *info, struct elm_errorvec *err_vec)

    start elm syndrome processing

    :param info:
        elm info
    :type info: struct elm_info \*

    :param err_vec:
        elm error vectors
    :type err_vec: struct elm_errorvec \*

.. _`elm_start_processing.description`:

Description
-----------

Set syndrome valid bit for syndrome fragment registers for which
elm syndrome fragment registers are loaded. This enables elm module
to start processing syndrome vectors.

.. _`elm_error_correction`:

elm_error_correction
====================

.. c:function:: void elm_error_correction(struct elm_info *info, struct elm_errorvec *err_vec)

    locate correctable error position

    :param info:
        elm info
    :type info: struct elm_info \*

    :param err_vec:
        elm error vectors
    :type err_vec: struct elm_errorvec \*

.. _`elm_error_correction.description`:

Description
-----------

On completion of processing by elm module, error location status
register updated with correctable/uncorrectable error information.
In case of correctable errors, number of errors located from
elm location status register & read the positions from
elm error location register.

.. _`elm_decode_bch_error_page`:

elm_decode_bch_error_page
=========================

.. c:function:: void elm_decode_bch_error_page(struct device *dev, u8 *ecc_calc, struct elm_errorvec *err_vec)

    Locate error position

    :param dev:
        device pointer
    :type dev: struct device \*

    :param ecc_calc:
        calculated ECC bytes from GPMC
    :type ecc_calc: u8 \*

    :param err_vec:
        elm error vectors
    :type err_vec: struct elm_errorvec \*

.. _`elm_decode_bch_error_page.description`:

Description
-----------

Called with one or more error reported vectors & vectors with
error reported is updated in err_vec[].error_reported

.. _`elm_context_save`:

elm_context_save
================

.. c:function:: int elm_context_save(struct elm_info *info)

    saves ELM configurations to preserve them across Hardware powered-down

    :param info:
        *undescribed*
    :type info: struct elm_info \*

.. _`elm_context_restore`:

elm_context_restore
===================

.. c:function:: int elm_context_restore(struct elm_info *info)

    writes configurations saved duing power-down back into ELM registers

    :param info:
        *undescribed*
    :type info: struct elm_info \*

.. This file was automatic generated / don't edit.

