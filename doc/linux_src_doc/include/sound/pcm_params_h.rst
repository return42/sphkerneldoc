.. -*- coding: utf-8; mode: rst -*-

============
pcm_params.h
============


.. _`params_access`:

params_access
=============

.. c:function:: snd_pcm_access_t params_access (const struct snd_pcm_hw_params *p)

    get the access type from the hw params

    :param const struct snd_pcm_hw_params \*p:
        hw params



.. _`params_format`:

params_format
=============

.. c:function:: snd_pcm_format_t params_format (const struct snd_pcm_hw_params *p)

    get the sample format from the hw params

    :param const struct snd_pcm_hw_params \*p:
        hw params



.. _`params_subformat`:

params_subformat
================

.. c:function:: snd_pcm_subformat_t params_subformat (const struct snd_pcm_hw_params *p)

    get the sample subformat from the hw params

    :param const struct snd_pcm_hw_params \*p:
        hw params



.. _`params_period_bytes`:

params_period_bytes
===================

.. c:function:: unsigned int params_period_bytes (const struct snd_pcm_hw_params *p)

    get the period size (in bytes) from the hw params

    :param const struct snd_pcm_hw_params \*p:
        hw params



.. _`params_width`:

params_width
============

.. c:function:: int params_width (const struct snd_pcm_hw_params *p)

    get the number of bits of the sample format from the hw params

    :param const struct snd_pcm_hw_params \*p:
        hw params



.. _`params_width.description`:

Description
-----------

This function returns the number of bits per sample that the selected sample
format of the hw params has.

