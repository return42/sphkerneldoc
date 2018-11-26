.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/soc-ops.c

.. _`snd_soc_info_enum_double`:

snd_soc_info_enum_double
========================

.. c:function:: int snd_soc_info_enum_double(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    enumerated double mixer info callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        control element information
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_soc_info_enum_double.description`:

Description
-----------

Callback to provide information about a double enumerated
mixer control.

Returns 0 for success.

.. _`snd_soc_get_enum_double`:

snd_soc_get_enum_double
=======================

.. c:function:: int snd_soc_get_enum_double(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    enumerated double mixer get callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_get_enum_double.description`:

Description
-----------

Callback to get the value of a double enumerated mixer.

Returns 0 for success.

.. _`snd_soc_put_enum_double`:

snd_soc_put_enum_double
=======================

.. c:function:: int snd_soc_put_enum_double(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    enumerated double mixer put callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_put_enum_double.description`:

Description
-----------

Callback to set the value of a double enumerated mixer.

Returns 0 for success.

.. _`snd_soc_read_signed`:

snd_soc_read_signed
===================

.. c:function:: int snd_soc_read_signed(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int shift, unsigned int sign_bit, int *signed_val)

    Read a codec register and interpret as signed value

    :param component:
        component
    :type component: struct snd_soc_component \*

    :param reg:
        Register to read
    :type reg: unsigned int

    :param mask:
        Mask to use after shifting the register value
    :type mask: unsigned int

    :param shift:
        Right shift of register value
    :type shift: unsigned int

    :param sign_bit:
        Bit that describes if a number is negative or not.
    :type sign_bit: unsigned int

    :param signed_val:
        Pointer to where the read value should be stored
    :type signed_val: int \*

.. _`snd_soc_read_signed.description`:

Description
-----------

This functions reads a codec register. The register value is shifted right
by 'shift' bits and masked with the given 'mask'. Afterwards it translates
the given registervalue into a signed integer if sign_bit is non-zero.

Returns 0 on sucess, otherwise an error value

.. _`snd_soc_info_volsw`:

snd_soc_info_volsw
==================

.. c:function:: int snd_soc_info_volsw(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    single mixer info callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        control element information
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_soc_info_volsw.description`:

Description
-----------

Callback to provide information about a single mixer control, or a double
mixer control that spans 2 registers.

Returns 0 for success.

.. _`snd_soc_info_volsw_sx`:

snd_soc_info_volsw_sx
=====================

.. c:function:: int snd_soc_info_volsw_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Mixer info callback for SX TLV controls

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        control element information
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_soc_info_volsw_sx.description`:

Description
-----------

Callback to provide information about a single mixer control, or a double
mixer control that spans 2 registers of the SX TLV type. SX TLV controls
have a range that represents both positive and negative values either side
of zero but without a sign bit.

Returns 0 for success.

.. _`snd_soc_get_volsw`:

snd_soc_get_volsw
=================

.. c:function:: int snd_soc_get_volsw(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    single mixer get callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_get_volsw.description`:

Description
-----------

Callback to get the value of a single mixer control, or a double mixer
control that spans 2 registers.

Returns 0 for success.

.. _`snd_soc_put_volsw`:

snd_soc_put_volsw
=================

.. c:function:: int snd_soc_put_volsw(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    single mixer put callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_put_volsw.description`:

Description
-----------

Callback to set the value of a single mixer control, or a double mixer
control that spans 2 registers.

Returns 0 for success.

.. _`snd_soc_get_volsw_sx`:

snd_soc_get_volsw_sx
====================

.. c:function:: int snd_soc_get_volsw_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    single mixer get callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_get_volsw_sx.description`:

Description
-----------

Callback to get the value of a single mixer control, or a double mixer
control that spans 2 registers.

Returns 0 for success.

.. _`snd_soc_put_volsw_sx`:

snd_soc_put_volsw_sx
====================

.. c:function:: int snd_soc_put_volsw_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    double mixer set callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_put_volsw_sx.description`:

Description
-----------

Callback to set the value of a double mixer control that spans 2 registers.

Returns 0 for success.

.. _`snd_soc_info_volsw_range`:

snd_soc_info_volsw_range
========================

.. c:function:: int snd_soc_info_volsw_range(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    single mixer info callback with range.

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        control element information
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_soc_info_volsw_range.description`:

Description
-----------

Callback to provide information, within a range, about a single
mixer control.

returns 0 for success.

.. _`snd_soc_put_volsw_range`:

snd_soc_put_volsw_range
=======================

.. c:function:: int snd_soc_put_volsw_range(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    single mixer put value callback with range.

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_put_volsw_range.description`:

Description
-----------

Callback to set the value, within a range, for a single mixer control.

Returns 0 for success.

.. _`snd_soc_get_volsw_range`:

snd_soc_get_volsw_range
=======================

.. c:function:: int snd_soc_get_volsw_range(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    single mixer get callback with range

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_get_volsw_range.description`:

Description
-----------

Callback to get the value, within a range, of a single mixer control.

Returns 0 for success.

.. _`snd_soc_limit_volume`:

snd_soc_limit_volume
====================

.. c:function:: int snd_soc_limit_volume(struct snd_soc_card *card, const char *name, int max)

    Set new limit to an existing volume control.

    :param card:
        where to look for the control
    :type card: struct snd_soc_card \*

    :param name:
        Name of the control
    :type name: const char \*

    :param max:
        new maximum limit
    :type max: int

.. _`snd_soc_limit_volume.description`:

Description
-----------

Return 0 for success, else error.

.. _`snd_soc_info_xr_sx`:

snd_soc_info_xr_sx
==================

.. c:function:: int snd_soc_info_xr_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    signed multi register info callback

    :param kcontrol:
        mreg control
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        control element information
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_soc_info_xr_sx.description`:

Description
-----------

Callback to provide information of a control that can
span multiple codec registers which together
forms a single signed value in a MSB/LSB manner.

Returns 0 for success.

.. _`snd_soc_get_xr_sx`:

snd_soc_get_xr_sx
=================

.. c:function:: int snd_soc_get_xr_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    signed multi register get callback

    :param kcontrol:
        mreg control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_get_xr_sx.description`:

Description
-----------

Callback to get the value of a control that can span
multiple codec registers which together forms a single
signed value in a MSB/LSB manner. The control supports
specifying total no of bits used to allow for bitfields
across the multiple codec registers.

Returns 0 for success.

.. _`snd_soc_put_xr_sx`:

snd_soc_put_xr_sx
=================

.. c:function:: int snd_soc_put_xr_sx(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    signed multi register get callback

    :param kcontrol:
        mreg control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_put_xr_sx.description`:

Description
-----------

Callback to set the value of a control that can span
multiple codec registers which together forms a single
signed value in a MSB/LSB manner. The control supports
specifying total no of bits used to allow for bitfields
across the multiple codec registers.

Returns 0 for success.

.. _`snd_soc_get_strobe`:

snd_soc_get_strobe
==================

.. c:function:: int snd_soc_get_strobe(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    strobe get callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_get_strobe.description`:

Description
-----------

Callback get the value of a strobe mixer control.

Returns 0 for success.

.. _`snd_soc_put_strobe`:

snd_soc_put_strobe
==================

.. c:function:: int snd_soc_put_strobe(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    strobe put callback

    :param kcontrol:
        mixer control
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        control element information
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_soc_put_strobe.description`:

Description
-----------

Callback strobe a register bit to high then low (or the inverse)
in one pass of a single mixer enum control.

Returns 1 for success.

.. This file was automatic generated / don't edit.

