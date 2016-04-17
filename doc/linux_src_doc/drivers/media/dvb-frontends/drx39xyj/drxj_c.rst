.. -*- coding: utf-8; mode: rst -*-

======
drxj.c
======


.. _`drxj_16to8`:

DRXJ_16TO8
==========

.. c:function:: DRXJ_16TO8 ( x)

    :param x:

        *undescribed*



.. _`drxj_16to8.description`:

Description
-----------

Block writes speed up I2C traffic between host and demod.
The macro takes care of the required byte order in a 16 bits word.
x -> lowbyte(x), highbyte(x)



.. _`drxj_8to16`:

DRXJ_8TO16
==========

.. c:function:: DRXJ_8TO16 ( x)

    :param x:

        *undescribed*



.. _`drxj_8to16.description`:

Description
-----------

Block read speed up I2C traffic between host and demod.
The macro takes care of the required byte order in a 16 bits word.



.. _`drxu_code_block_hdr`:

struct drxu_code_block_hdr
==========================

.. c:type:: drxu_code_block_hdr

    Structure of the microcode block headers


.. _`drxu_code_block_hdr.definition`:

Definition
----------

.. code-block:: c

  struct drxu_code_block_hdr {
    u32 addr;
    u16 size;
    u16 CRC;
  };


.. _`drxu_code_block_hdr.members`:

Members
-------

:``addr``:
    Destination address of the data in this block

:``size``:
    Size of the block data following this header counted in

                    16 bits words

:``CRC``:
    CRC value of the data block, only valid if CRC flag is
    set.




.. _`init_hi`:

init_hi
=======

.. c:function:: int init_hi (const struct drx_demod_instance *demod)

    :param const struct drx_demod_instance \*demod:

        *undescribed*



.. _`init_hi.description`:

Description
-----------

\brief Initialise and configurate HI.
\param demod pointer to demod data.
\return int Return status.
\retval 0 Success.
\retval -EIO Failure.

Needs to know Psys (System Clock period) and Posc (Osc Clock period)
Need to store configuration in driver because of the way I2C
bridging is controlled.



.. _`get_vsb_post_rs_pck_err`:

get_vsb_post_rs_pck_err
=======================

.. c:function:: int get_vsb_post_rs_pck_err (struct i2c_device_addr *dev_addr, u32 *pck_errs, u32 *pck_count)

    :param struct i2c_device_addr \*dev_addr:

        *undescribed*

    :param u32 \*pck_errs:

        *undescribed*

    :param u32 \*pck_count:

        *undescribed*



.. _`get_vsb_post_rs_pck_err.description`:

Description
-----------

\brief Get the values of packet error in 8VSB mode
\return Error code



.. _`get_vs_bpost_viterbi_ber`:

get_vs_bpost_viterbi_ber
========================

.. c:function:: int get_vs_bpost_viterbi_ber (struct i2c_device_addr *dev_addr, u32 *ber, u32 *cnt)

    :param struct i2c_device_addr \*dev_addr:

        *undescribed*

    :param u32 \*ber:

        *undescribed*

    :param u32 \*cnt:

        *undescribed*



.. _`get_vs_bpost_viterbi_ber.description`:

Description
-----------

\brief Get the values of ber in VSB mode
\return Error code



.. _`get_vs_bpre_viterbi_ber`:

get_vs_bpre_viterbi_ber
=======================

.. c:function:: int get_vs_bpre_viterbi_ber (struct i2c_device_addr *dev_addr, u32 *ber, u32 *cnt)

    :param struct i2c_device_addr \*dev_addr:

        *undescribed*

    :param u32 \*ber:

        *undescribed*

    :param u32 \*cnt:

        *undescribed*



.. _`get_vs_bpre_viterbi_ber.description`:

Description
-----------

\brief Get the values of ber in VSB mode
\return Error code



.. _`get_vsbmer`:

get_vsbmer
==========

.. c:function:: int get_vsbmer (struct i2c_device_addr *dev_addr, u16 *mer)

    :param struct i2c_device_addr \*dev_addr:

        *undescribed*

    :param u16 \*mer:

        *undescribed*



.. _`get_vsbmer.description`:

Description
-----------

\brief Get the values of MER
\return Error code



.. _`get_qamrs_err_count`:

get_qamrs_err_count
===================

.. c:function:: int get_qamrs_err_count (struct i2c_device_addr *dev_addr, struct drxjrs_errors *rs_errors)

    :param struct i2c_device_addr \*dev_addr:

        *undescribed*

    :param struct drxjrs_errors \*rs_errors:

        *undescribed*



.. _`get_qamrs_err_count.description`:

Description
-----------

\brief Get RS error count in QAM mode (used for post RS BER calculation)
\return Error code



.. _`get_qamrs_err_count.precondition`:

precondition
------------

measurement period & measurement prescale must be set



.. _`drx_u_code_compute_crc`:

drx_u_code_compute_crc
======================

.. c:function:: u16 drx_u_code_compute_crc (u8 *block_data, u16 nr_words)

    Compute CRC of block of microcode data.

    :param u8 \*block_data:
        Pointer to microcode data.

    :param u16 nr_words:
        Size of microcode block (number of 16 bits words).



.. _`drx_u_code_compute_crc.description`:

Description
-----------

returns The computed CRC residue.



.. _`drx_check_firmware`:

drx_check_firmware
==================

.. c:function:: int drx_check_firmware (struct drx_demod_instance *demod, u8 *mc_data, unsigned size)

    checks if the loaded firmware is valid

    :param struct drx_demod_instance \*demod:
        demod structure

    :param u8 \*mc_data:
        pointer to the start of the firmware

    :param unsigned size:
        firmware size



.. _`drx_ctrl_u_code`:

drx_ctrl_u_code
===============

.. c:function:: int drx_ctrl_u_code (struct drx_demod_instance *demod, struct drxu_code_info *mc_info, enum drxu_code_action action)

    Handle microcode upload or verify.

    :param struct drx_demod_instance \*demod:

        *undescribed*

    :param struct drxu_code_info \*mc_info:
        Pointer to information about microcode data.

    :param enum drxu_code_action action:
        Either UCODE_UPLOAD or UCODE_VERIFY



.. _`drx_ctrl_u_code.0`:

0
-

- In case of UCODE_UPLOAD: code is successfully uploaded.

              - In case of UCODE_VERIFY: image on device is equal to
  image provided to this control function.
        -EIO:

- In case of UCODE_UPLOAD: I2C error.
- In case of UCODE_VERIFY: I2C error or image on device

  is not equal to image provided to this control function.
        -EINVAL:

- Invalid arguments.
- Provided image is corrupt

