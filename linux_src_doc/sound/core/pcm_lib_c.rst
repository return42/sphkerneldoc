.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm_lib.c

.. _`snd_pcm_set_ops`:

snd_pcm_set_ops
===============

.. c:function:: void snd_pcm_set_ops(struct snd_pcm *pcm, int direction, const struct snd_pcm_ops *ops)

    set the PCM operators

    :param pcm:
        the pcm instance
    :type pcm: struct snd_pcm \*

    :param direction:
        stream direction, SNDRV_PCM_STREAM_XXX
    :type direction: int

    :param ops:
        the operator table
    :type ops: const struct snd_pcm_ops \*

.. _`snd_pcm_set_ops.description`:

Description
-----------

Sets the given PCM operators to the pcm instance.

.. _`snd_pcm_set_sync`:

snd_pcm_set_sync
================

.. c:function:: void snd_pcm_set_sync(struct snd_pcm_substream *substream)

    set the PCM sync id

    :param substream:
        the pcm substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_set_sync.description`:

Description
-----------

Sets the PCM sync identifier for the card.

.. _`snd_interval_refine`:

snd_interval_refine
===================

.. c:function:: int snd_interval_refine(struct snd_interval *i, const struct snd_interval *v)

    refine the interval value of configurator

    :param i:
        the interval value to refine
    :type i: struct snd_interval \*

    :param v:
        the interval value to refer to
    :type v: const struct snd_interval \*

.. _`snd_interval_refine.description`:

Description
-----------

Refines the interval value with the reference value.
The interval is changed to the range satisfying both intervals.
The interval status (min, max, integer, etc.) are evaluated.

.. _`snd_interval_refine.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_interval_div`:

snd_interval_div
================

.. c:function:: void snd_interval_div(const struct snd_interval *a, const struct snd_interval *b, struct snd_interval *c)

    refine the interval value with division

    :param a:
        dividend
    :type a: const struct snd_interval \*

    :param b:
        divisor
    :type b: const struct snd_interval \*

    :param c:
        quotient
    :type c: struct snd_interval \*

.. _`snd_interval_div.description`:

Description
-----------

c = a / b

Returns non-zero if the value is changed, zero if not changed.

.. _`snd_interval_muldivk`:

snd_interval_muldivk
====================

.. c:function:: void snd_interval_muldivk(const struct snd_interval *a, const struct snd_interval *b, unsigned int k, struct snd_interval *c)

    refine the interval value

    :param a:
        dividend 1
    :type a: const struct snd_interval \*

    :param b:
        dividend 2
    :type b: const struct snd_interval \*

    :param k:
        divisor (as integer)
    :type k: unsigned int

    :param c:
        result
    :type c: struct snd_interval \*

.. _`snd_interval_muldivk.description`:

Description
-----------

c = a * b / k

Returns non-zero if the value is changed, zero if not changed.

.. _`snd_interval_mulkdiv`:

snd_interval_mulkdiv
====================

.. c:function:: void snd_interval_mulkdiv(const struct snd_interval *a, unsigned int k, const struct snd_interval *b, struct snd_interval *c)

    refine the interval value

    :param a:
        dividend 1
    :type a: const struct snd_interval \*

    :param k:
        dividend 2 (as integer)
    :type k: unsigned int

    :param b:
        divisor
    :type b: const struct snd_interval \*

    :param c:
        result
    :type c: struct snd_interval \*

.. _`snd_interval_mulkdiv.description`:

Description
-----------

c = a * k / b

Returns non-zero if the value is changed, zero if not changed.

.. _`snd_interval_ratnum`:

snd_interval_ratnum
===================

.. c:function:: int snd_interval_ratnum(struct snd_interval *i, unsigned int rats_count, const struct snd_ratnum *rats, unsigned int *nump, unsigned int *denp)

    refine the interval value

    :param i:
        interval to refine
    :type i: struct snd_interval \*

    :param rats_count:
        number of ratnum_t
    :type rats_count: unsigned int

    :param rats:
        ratnum_t array
    :type rats: const struct snd_ratnum \*

    :param nump:
        pointer to store the resultant numerator
    :type nump: unsigned int \*

    :param denp:
        pointer to store the resultant denominator
    :type denp: unsigned int \*

.. _`snd_interval_ratnum.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_interval_ratden`:

snd_interval_ratden
===================

.. c:function:: int snd_interval_ratden(struct snd_interval *i, unsigned int rats_count, const struct snd_ratden *rats, unsigned int *nump, unsigned int *denp)

    refine the interval value

    :param i:
        interval to refine
    :type i: struct snd_interval \*

    :param rats_count:
        number of struct ratden
    :type rats_count: unsigned int

    :param rats:
        struct ratden array
    :type rats: const struct snd_ratden \*

    :param nump:
        pointer to store the resultant numerator
    :type nump: unsigned int \*

    :param denp:
        pointer to store the resultant denominator
    :type denp: unsigned int \*

.. _`snd_interval_ratden.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_interval_list`:

snd_interval_list
=================

.. c:function:: int snd_interval_list(struct snd_interval *i, unsigned int count, const unsigned int *list, unsigned int mask)

    refine the interval value from the list

    :param i:
        the interval value to refine
    :type i: struct snd_interval \*

    :param count:
        the number of elements in the list
    :type count: unsigned int

    :param list:
        the value list
    :type list: const unsigned int \*

    :param mask:
        the bit-mask to evaluate
    :type mask: unsigned int

.. _`snd_interval_list.description`:

Description
-----------

Refines the interval value from the list.
When mask is non-zero, only the elements corresponding to bit 1 are
evaluated.

.. _`snd_interval_list.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_interval_ranges`:

snd_interval_ranges
===================

.. c:function:: int snd_interval_ranges(struct snd_interval *i, unsigned int count, const struct snd_interval *ranges, unsigned int mask)

    refine the interval value from the list of ranges

    :param i:
        the interval value to refine
    :type i: struct snd_interval \*

    :param count:
        the number of elements in the list of ranges
    :type count: unsigned int

    :param ranges:
        the ranges list
    :type ranges: const struct snd_interval \*

    :param mask:
        the bit-mask to evaluate
    :type mask: unsigned int

.. _`snd_interval_ranges.description`:

Description
-----------

Refines the interval value from the list of ranges.
When mask is non-zero, only the elements corresponding to bit 1 are
evaluated.

.. _`snd_interval_ranges.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_pcm_hw_rule_add`:

snd_pcm_hw_rule_add
===================

.. c:function:: int snd_pcm_hw_rule_add(struct snd_pcm_runtime *runtime, unsigned int cond, int var, snd_pcm_hw_rule_func_t func, void *private, int dep,  ...)

    add the hw-constraint rule

    :param runtime:
        the pcm runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        the variable to evaluate
    :type var: int

    :param func:
        the evaluation function
    :type func: snd_pcm_hw_rule_func_t

    :param private:
        the private data pointer passed to function
    :type private: void \*

    :param dep:
        the dependent variables
    :type dep: int

    :param ellipsis ellipsis:
        variable arguments

.. _`snd_pcm_hw_rule_add.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_mask`:

snd_pcm_hw_constraint_mask
==========================

.. c:function:: int snd_pcm_hw_constraint_mask(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, u_int32_t mask)

    apply the given bitmap mask constraint

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param var:
        hw_params variable to apply the mask
    :type var: snd_pcm_hw_param_t

    :param mask:
        the bitmap mask
    :type mask: u_int32_t

.. _`snd_pcm_hw_constraint_mask.description`:

Description
-----------

Apply the constraint of the given bitmap mask to a 32-bit mask parameter.

.. _`snd_pcm_hw_constraint_mask.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_mask64`:

snd_pcm_hw_constraint_mask64
============================

.. c:function:: int snd_pcm_hw_constraint_mask64(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, u_int64_t mask)

    apply the given bitmap mask constraint

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param var:
        hw_params variable to apply the mask
    :type var: snd_pcm_hw_param_t

    :param mask:
        the 64bit bitmap mask
    :type mask: u_int64_t

.. _`snd_pcm_hw_constraint_mask64.description`:

Description
-----------

Apply the constraint of the given bitmap mask to a 64-bit mask parameter.

.. _`snd_pcm_hw_constraint_mask64.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_integer`:

snd_pcm_hw_constraint_integer
=============================

.. c:function:: int snd_pcm_hw_constraint_integer(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var)

    apply an integer constraint to an interval

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param var:
        hw_params variable to apply the integer constraint
    :type var: snd_pcm_hw_param_t

.. _`snd_pcm_hw_constraint_integer.description`:

Description
-----------

Apply the constraint of integer to an interval parameter.

.. _`snd_pcm_hw_constraint_integer.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_pcm_hw_constraint_minmax`:

snd_pcm_hw_constraint_minmax
============================

.. c:function:: int snd_pcm_hw_constraint_minmax(struct snd_pcm_runtime *runtime, snd_pcm_hw_param_t var, unsigned int min, unsigned int max)

    apply a min/max range constraint to an interval

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param var:
        hw_params variable to apply the range
    :type var: snd_pcm_hw_param_t

    :param min:
        the minimal value
    :type min: unsigned int

    :param max:
        the maximal value
    :type max: unsigned int

.. _`snd_pcm_hw_constraint_minmax.description`:

Description
-----------

Apply the min/max range constraint to an interval parameter.

.. _`snd_pcm_hw_constraint_minmax.return`:

Return
------

Positive if the value is changed, zero if it's not changed, or a
negative error code.

.. _`snd_pcm_hw_constraint_list`:

snd_pcm_hw_constraint_list
==========================

.. c:function:: int snd_pcm_hw_constraint_list(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_list *l)

    apply a list of constraints to a parameter

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        hw_params variable to apply the list constraint
    :type var: snd_pcm_hw_param_t

    :param l:
        list
    :type l: const struct snd_pcm_hw_constraint_list \*

.. _`snd_pcm_hw_constraint_list.description`:

Description
-----------

Apply the list of constraints to an interval parameter.

.. _`snd_pcm_hw_constraint_list.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_ranges`:

snd_pcm_hw_constraint_ranges
============================

.. c:function:: int snd_pcm_hw_constraint_ranges(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ranges *r)

    apply list of range constraints to a parameter

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        hw_params variable to apply the list of range constraints
    :type var: snd_pcm_hw_param_t

    :param r:
        ranges
    :type r: const struct snd_pcm_hw_constraint_ranges \*

.. _`snd_pcm_hw_constraint_ranges.description`:

Description
-----------

Apply the list of range constraints to an interval parameter.

.. _`snd_pcm_hw_constraint_ranges.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_ratnums`:

snd_pcm_hw_constraint_ratnums
=============================

.. c:function:: int snd_pcm_hw_constraint_ratnums(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ratnums *r)

    apply ratnums constraint to a parameter

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        hw_params variable to apply the ratnums constraint
    :type var: snd_pcm_hw_param_t

    :param r:
        struct snd_ratnums constriants
    :type r: const struct snd_pcm_hw_constraint_ratnums \*

.. _`snd_pcm_hw_constraint_ratnums.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_ratdens`:

snd_pcm_hw_constraint_ratdens
=============================

.. c:function:: int snd_pcm_hw_constraint_ratdens(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ratdens *r)

    apply ratdens constraint to a parameter

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        hw_params variable to apply the ratdens constraint
    :type var: snd_pcm_hw_param_t

    :param r:
        struct snd_ratdens constriants
    :type r: const struct snd_pcm_hw_constraint_ratdens \*

.. _`snd_pcm_hw_constraint_ratdens.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_msbits`:

snd_pcm_hw_constraint_msbits
============================

.. c:function:: int snd_pcm_hw_constraint_msbits(struct snd_pcm_runtime *runtime, unsigned int cond, unsigned int width, unsigned int msbits)

    add a hw constraint msbits rule

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param width:
        sample bits width
    :type width: unsigned int

    :param msbits:
        msbits width
    :type msbits: unsigned int

.. _`snd_pcm_hw_constraint_msbits.description`:

Description
-----------

This constraint will set the number of most significant bits (msbits) if a
sample format with the specified width has been select. If width is set to 0
the msbits will be set for any sample format with a width larger than the
specified msbits.

.. _`snd_pcm_hw_constraint_msbits.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_step`:

snd_pcm_hw_constraint_step
==========================

.. c:function:: int snd_pcm_hw_constraint_step(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var, unsigned long step)

    add a hw constraint step rule

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        hw_params variable to apply the step constraint
    :type var: snd_pcm_hw_param_t

    :param step:
        step size
    :type step: unsigned long

.. _`snd_pcm_hw_constraint_step.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_constraint_pow2`:

snd_pcm_hw_constraint_pow2
==========================

.. c:function:: int snd_pcm_hw_constraint_pow2(struct snd_pcm_runtime *runtime, unsigned int cond, snd_pcm_hw_param_t var)

    add a hw constraint power-of-2 rule

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param cond:
        condition bits
    :type cond: unsigned int

    :param var:
        hw_params variable to apply the power-of-2 constraint
    :type var: snd_pcm_hw_param_t

.. _`snd_pcm_hw_constraint_pow2.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_rule_noresample`:

snd_pcm_hw_rule_noresample
==========================

.. c:function:: int snd_pcm_hw_rule_noresample(struct snd_pcm_runtime *runtime, unsigned int base_rate)

    add a rule to allow disabling hw resampling

    :param runtime:
        PCM runtime instance
    :type runtime: struct snd_pcm_runtime \*

    :param base_rate:
        the rate at which the hardware does not resample
    :type base_rate: unsigned int

.. _`snd_pcm_hw_rule_noresample.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_hw_param_value`:

snd_pcm_hw_param_value
======================

.. c:function:: int snd_pcm_hw_param_value(const struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir)

    return \ ``params``\  field \ ``var``\  value

    :param params:
        the hw_params instance
    :type params: const struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param dir:
        pointer to the direction (-1,0,1) or \ ``NULL``\ 
    :type dir: int \*

.. _`snd_pcm_hw_param_value.return`:

Return
------

The value for field \ ``var``\  if it's fixed in configuration space
defined by \ ``params``\ . -%EINVAL otherwise.

.. _`snd_pcm_hw_param_first`:

snd_pcm_hw_param_first
======================

.. c:function:: int snd_pcm_hw_param_first(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir)

    refine config space and return minimum value

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param dir:
        pointer to the direction (-1,0,1) or \ ``NULL``\ 
    :type dir: int \*

.. _`snd_pcm_hw_param_first.description`:

Description
-----------

Inside configuration space defined by \ ``params``\  remove from \ ``var``\  all
values > minimum. Reduce configuration space accordingly.

.. _`snd_pcm_hw_param_first.return`:

Return
------

The minimum, or a negative error code on failure.

.. _`snd_pcm_hw_param_last`:

snd_pcm_hw_param_last
=====================

.. c:function:: int snd_pcm_hw_param_last(struct snd_pcm_substream *pcm, struct snd_pcm_hw_params *params, snd_pcm_hw_param_t var, int *dir)

    refine config space and return maximum value

    :param pcm:
        PCM instance
    :type pcm: struct snd_pcm_substream \*

    :param params:
        the hw_params instance
    :type params: struct snd_pcm_hw_params \*

    :param var:
        parameter to retrieve
    :type var: snd_pcm_hw_param_t

    :param dir:
        pointer to the direction (-1,0,1) or \ ``NULL``\ 
    :type dir: int \*

.. _`snd_pcm_hw_param_last.description`:

Description
-----------

Inside configuration space defined by \ ``params``\  remove from \ ``var``\  all
values < maximum. Reduce configuration space accordingly.

.. _`snd_pcm_hw_param_last.return`:

Return
------

The maximum, or a negative error code on failure.

.. _`snd_pcm_lib_ioctl`:

snd_pcm_lib_ioctl
=================

.. c:function:: int snd_pcm_lib_ioctl(struct snd_pcm_substream *substream, unsigned int cmd, void *arg)

    a generic PCM ioctl callback

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

    :param cmd:
        ioctl command
    :type cmd: unsigned int

    :param arg:
        ioctl argument
    :type arg: void \*

.. _`snd_pcm_lib_ioctl.description`:

Description
-----------

Processes the generic ioctl commands for PCM.
Can be passed as the ioctl callback for PCM ops.

.. _`snd_pcm_lib_ioctl.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_period_elapsed`:

snd_pcm_period_elapsed
======================

.. c:function:: void snd_pcm_period_elapsed(struct snd_pcm_substream *substream)

    update the pcm status for the next period

    :param substream:
        the pcm substream instance
    :type substream: struct snd_pcm_substream \*

.. _`snd_pcm_period_elapsed.description`:

Description
-----------

This function is called from the interrupt handler when the
PCM has processed the period size.  It will update the current
pointer, wake up sleepers, etc.

Even if more than one periods have elapsed since the last call, you
have to call this only once.

.. _`snd_pcm_add_chmap_ctls`:

snd_pcm_add_chmap_ctls
======================

.. c:function:: int snd_pcm_add_chmap_ctls(struct snd_pcm *pcm, int stream, const struct snd_pcm_chmap_elem *chmap, int max_channels, unsigned long private_value, struct snd_pcm_chmap **info_ret)

    create channel-mapping control elements

    :param pcm:
        the assigned PCM instance
    :type pcm: struct snd_pcm \*

    :param stream:
        stream direction
    :type stream: int

    :param chmap:
        channel map elements (for query)
    :type chmap: const struct snd_pcm_chmap_elem \*

    :param max_channels:
        the max number of channels for the stream
    :type max_channels: int

    :param private_value:
        the value passed to each kcontrol's private_value field
    :type private_value: unsigned long

    :param info_ret:
        store struct snd_pcm_chmap instance if non-NULL
    :type info_ret: struct snd_pcm_chmap \*\*

.. _`snd_pcm_add_chmap_ctls.description`:

Description
-----------

Create channel-mapping control elements assigned to the given PCM stream(s).

.. _`snd_pcm_add_chmap_ctls.return`:

Return
------

Zero if successful, or a negative error value.

.. This file was automatic generated / don't edit.

