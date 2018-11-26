.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/oss/pcm_oss.c

.. _`snd_pcm_hw_param_value_min`:

snd_pcm_hw_param_value_min
==========================

.. c:function:: unsigned int snd_pcm_hw_param_value_min(const struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir)

    :param params:
        the hw_params instance
    :type params: const struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param dir:
        pointer to the direction (-1,0,1) or NULL
    :type dir: int \*

.. _`snd_pcm_hw_param_value_min.description`:

Description
-----------

Return the minimum value for field PAR.

.. _`snd_pcm_hw_param_value_max`:

snd_pcm_hw_param_value_max
==========================

.. c:function:: unsigned int snd_pcm_hw_param_value_max(const struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir)

    :param params:
        the hw_params instance
    :type params: const struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param dir:
        pointer to the direction (-1,0,1) or NULL
    :type dir: int \*

.. _`snd_pcm_hw_param_value_max.description`:

Description
-----------

Return the maximum value for field PAR.

.. _`snd_pcm_hw_param_min`:

snd_pcm_hw_param_min
====================

.. c:function:: int snd_pcm_hw_param_min(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, unsigned int val, int *dir)

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param val:
        minimal value
    :type val: unsigned int

    :param dir:
        pointer to the direction (-1,0,1) or NULL
    :type dir: int \*

.. _`snd_pcm_hw_param_min.description`:

Description
-----------

Inside configuration space defined by PARAMS remove from PAR all
values < VAL. Reduce configuration space accordingly.
Return new minimum or -EINVAL if the configuration space is empty

.. _`snd_pcm_hw_param_max`:

snd_pcm_hw_param_max
====================

.. c:function:: int snd_pcm_hw_param_max(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, unsigned int val, int *dir)

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param val:
        maximal value
    :type val: unsigned int

    :param dir:
        pointer to the direction (-1,0,1) or NULL
    :type dir: int \*

.. _`snd_pcm_hw_param_max.description`:

Description
-----------

Inside configuration space defined by PARAMS remove from PAR all
values >= VAL + 1. Reduce configuration space accordingly.
Return new maximum or -EINVAL if the configuration space is empty

.. _`snd_pcm_hw_param_near`:

snd_pcm_hw_param_near
=====================

.. c:function:: int snd_pcm_hw_param_near(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, unsigned int best, int *dir)

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param best:
        value to set
    :type best: unsigned int

    :param dir:
        pointer to the direction (-1,0,1) or NULL
    :type dir: int \*

.. _`snd_pcm_hw_param_near.description`:

Description
-----------

Inside configuration space defined by PARAMS set PAR to the available value
nearest to VAL. Reduce configuration space accordingly.
This function cannot be called for SNDRV_PCM_HW_PARAM_ACCESS,
SNDRV_PCM_HW_PARAM_FORMAT, SNDRV_PCM_HW_PARAM_SUBFORMAT.
Return the value found.

.. _`snd_pcm_hw_param_set`:

snd_pcm_hw_param_set
====================

.. c:function:: int snd_pcm_hw_param_set(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, unsigned int val, int dir)

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param val:
        value to set
    :type val: unsigned int

    :param dir:
        pointer to the direction (-1,0,1) or NULL
    :type dir: int

.. _`snd_pcm_hw_param_set.description`:

Description
-----------

Inside configuration space defined by PARAMS remove from PAR all
values != VAL. Reduce configuration space accordingly.
Return VAL or -EINVAL if the configuration space is empty

.. This file was automatic generated / don't edit.

