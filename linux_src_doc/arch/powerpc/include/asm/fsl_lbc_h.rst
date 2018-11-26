.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/fsl_lbc.h

.. _`fsl_upm_start_pattern`:

fsl_upm_start_pattern
=====================

.. c:function:: void fsl_upm_start_pattern(struct fsl_upm *upm, u8 pat_offset)

    start UPM patterns execution

    :param upm:
        pointer to the fsl_upm structure obtained via fsl_upm_find
    :type upm: struct fsl_upm \*

    :param pat_offset:
        UPM pattern offset for the command to be executed
    :type pat_offset: u8

.. _`fsl_upm_start_pattern.description`:

Description
-----------

This routine programmes UPM so the next memory access that hits an UPM
will trigger pattern execution, starting at pat_offset.

.. _`fsl_upm_end_pattern`:

fsl_upm_end_pattern
===================

.. c:function:: void fsl_upm_end_pattern(struct fsl_upm *upm)

    end UPM patterns execution

    :param upm:
        pointer to the fsl_upm structure obtained via fsl_upm_find
    :type upm: struct fsl_upm \*

.. _`fsl_upm_end_pattern.description`:

Description
-----------

This routine reverts UPM to normal operation mode.

.. This file was automatic generated / don't edit.

