.. -*- coding: utf-8; mode: rst -*-

==========
omap_elm.c
==========


.. _`elm_config`:

elm_config
==========

.. c:function:: int elm_config (struct device *dev, enum bch_ecc bch_type, int ecc_steps, int ecc_step_size, int ecc_syndrome_size)

    Configure ELM module

    :param struct device \*dev:
        ELM device

    :param enum bch_ecc bch_type:
        Type of BCH ecc

    :param int ecc_steps:

        *undescribed*

    :param int ecc_step_size:

        *undescribed*

    :param int ecc_syndrome_size:

        *undescribed*



.. _`elm_configure_page_mode`:

elm_configure_page_mode
=======================

.. c:function:: void elm_configure_page_mode (struct elm_info *info, int index, bool enable)

    Enable/Disable page mode

    :param struct elm_info \*info:
        elm info

    :param int index:
        index number of syndrome fragment vector

    :param bool enable:
        enable/disable flag for page mode



.. _`elm_configure_page_mode.description`:

Description
-----------

Enable page mode for syndrome fragment index



.. _`elm_load_syndrome`:

elm_load_syndrome
=================

.. c:function:: void elm_load_syndrome (struct elm_info *info, struct elm_errorvec *err_vec, u8 *ecc)

    Load ELM syndrome reg

    :param struct elm_info \*info:
        elm info

    :param struct elm_errorvec \*err_vec:
        elm error vectors

    :param u8 \*ecc:
        buffer with calculated ecc



.. _`elm_load_syndrome.description`:

Description
-----------

Load syndrome fragment registers with calculated ecc in reverse order.



.. _`elm_start_processing`:

elm_start_processing
====================

.. c:function:: void elm_start_processing (struct elm_info *info, struct elm_errorvec *err_vec)

    start elm syndrome processing

    :param struct elm_info \*info:
        elm info

    :param struct elm_errorvec \*err_vec:
        elm error vectors



.. _`elm_start_processing.description`:

Description
-----------

Set syndrome valid bit for syndrome fragment registers for which
elm syndrome fragment registers are loaded. This enables elm module
to start processing syndrome vectors.



.. _`elm_error_correction`:

elm_error_correction
====================

.. c:function:: void elm_error_correction (struct elm_info *info, struct elm_errorvec *err_vec)

    locate correctable error position

    :param struct elm_info \*info:
        elm info

    :param struct elm_errorvec \*err_vec:
        elm error vectors



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

.. c:function:: void elm_decode_bch_error_page (struct device *dev, u8 *ecc_calc, struct elm_errorvec *err_vec)

    Locate error position

    :param struct device \*dev:
        device pointer

    :param u8 \*ecc_calc:
        calculated ECC bytes from GPMC

    :param struct elm_errorvec \*err_vec:
        elm error vectors



.. _`elm_decode_bch_error_page.description`:

Description
-----------

Called with one or more error reported vectors & vectors with
error reported is updated in err_vec[].error_reported



.. _`elm_context_save`:

elm_context_save
================

.. c:function:: int elm_context_save (struct elm_info *info)

    :param struct elm_info \*info:

        *undescribed*



.. _`elm_context_save.description`:

Description
-----------

saves ELM configurations to preserve them across Hardware powered-down



.. _`elm_context_restore`:

elm_context_restore
===================

.. c:function:: int elm_context_restore (struct elm_info *info)

    :param struct elm_info \*info:

        *undescribed*



.. _`elm_context_restore.description`:

Description
-----------

writes configurations saved duing power-down back into ELM registers

