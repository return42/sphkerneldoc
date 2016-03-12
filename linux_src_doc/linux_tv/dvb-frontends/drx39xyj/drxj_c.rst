.. -*- coding: utf-8; mode: rst -*-

======
drxj.c
======



.. _xref_DRXJ_16TO8:

DRXJ_16TO8
==========

.. c:function:: DRXJ_16TO8 ( x)

    

    :param x:

        _undescribed_



Description
-----------

Block writes speed up I2C traffic between host and demod.
The macro takes care of the required byte order in a 16 bits word.
x -> lowbyte(x), highbyte(x)




.. _xref_DRXJ_8TO16:

DRXJ_8TO16
==========

.. c:function:: DRXJ_8TO16 ( x)

    

    :param x:

        _undescribed_



Description
-----------

Block read speed up I2C traffic between host and demod.
The macro takes care of the required byte order in a 16 bits word.




.. _xref_struct_drxu_code_block_hdr:

struct drxu_code_block_hdr
==========================

.. c:type:: struct drxu_code_block_hdr

    Structure of the microcode block headers



Definition
----------

.. code-block:: c

  struct drxu_code_block_hdr {
    u32 addr;
    u16 size;
    u16 CRC;
  };



Members
-------

:``u32 addr``:
    Destination address of the data in this block

:``u16 size``:
    Size of the block data following this header counted in
    		16 bits words

:``u16 CRC``:
    CRC value of the data block, only valid if CRC flag is
    		set.





.. _xref_init_hi:

init_hi
=======

.. c:function:: int init_hi (const struct drx_demod_instance * demod)

    

    :param const struct drx_demod_instance * demod:

        _undescribed_



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




.. _xref_get_vsb_post_rs_pck_err:

get_vsb_post_rs_pck_err
=======================

.. c:function:: int get_vsb_post_rs_pck_err (struct i2c_device_addr * dev_addr, u32 * pck_errs, u32 * pck_count)

    

    :param struct i2c_device_addr * dev_addr:

        _undescribed_

    :param u32 * pck_errs:

        _undescribed_

    :param u32 * pck_count:

        _undescribed_



Description
-----------

\brief Get the values of packet error in 8VSB mode
\return Error code




.. _xref_get_vs_bpost_viterbi_ber:

get_vs_bpost_viterbi_ber
========================

.. c:function:: int get_vs_bpost_viterbi_ber (struct i2c_device_addr * dev_addr, u32 * ber, u32 * cnt)

    

    :param struct i2c_device_addr * dev_addr:

        _undescribed_

    :param u32 * ber:

        _undescribed_

    :param u32 * cnt:

        _undescribed_



Description
-----------

\brief Get the values of ber in VSB mode
\return Error code




.. _xref_get_vs_bpre_viterbi_ber:

get_vs_bpre_viterbi_ber
=======================

.. c:function:: int get_vs_bpre_viterbi_ber (struct i2c_device_addr * dev_addr, u32 * ber, u32 * cnt)

    

    :param struct i2c_device_addr * dev_addr:

        _undescribed_

    :param u32 * ber:

        _undescribed_

    :param u32 * cnt:

        _undescribed_



Description
-----------

\brief Get the values of ber in VSB mode
\return Error code




.. _xref_get_vsbmer:

get_vsbmer
==========

.. c:function:: int get_vsbmer (struct i2c_device_addr * dev_addr, u16 * mer)

    

    :param struct i2c_device_addr * dev_addr:

        _undescribed_

    :param u16 * mer:

        _undescribed_



Description
-----------

\brief Get the values of MER
\return Error code




.. _xref_get_qamrs_err_count:

get_qamrs_err_count
===================

.. c:function:: int get_qamrs_err_count (struct i2c_device_addr * dev_addr, struct drxjrs_errors * rs_errors)

    

    :param struct i2c_device_addr * dev_addr:

        _undescribed_

    :param struct drxjrs_errors * rs_errors:

        _undescribed_



Description
-----------

\brief Get RS error count in QAM mode (used for post RS BER calculation)
\return Error code



precondition
------------

measurement period & measurement prescale must be set




.. _xref_drx_u_code_compute_crc:

drx_u_code_compute_crc
======================

.. c:function:: u16 drx_u_code_compute_crc (u8 * block_data, u16 nr_words)

    Compute CRC of block of microcode data.

    :param u8 * block_data:
        Pointer to microcode data.

    :param u16 nr_words:
        Size of microcode block (number of 16 bits words).



Description
-----------

returns The computed CRC residue.




.. _xref_drx_check_firmware:

drx_check_firmware
==================

.. c:function:: int drx_check_firmware (struct drx_demod_instance * demod, u8 * mc_data, unsigned size)

    checks if the loaded firmware is valid

    :param struct drx_demod_instance * demod:
        demod structure

    :param u8 * mc_data:
        pointer to the start of the firmware

    :param unsigned size:
        firmware size




.. _xref_drx_ctrl_u_code:

drx_ctrl_u_code
===============

.. c:function:: int drx_ctrl_u_code (struct drx_demod_instance * demod, struct drxu_code_info * mc_info, enum drxu_code_action action)

    Handle microcode upload or verify.

    :param struct drx_demod_instance * demod:

        _undescribed_

    :param struct drxu_code_info * mc_info:
        Pointer to information about microcode data.

    :param enum drxu_code_action action:
        Either UCODE_UPLOAD or UCODE_VERIFY



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


